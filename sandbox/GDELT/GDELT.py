import sys
import time
import requests

GDELT_API_URL = 'https://api.gdeltproject.org/api/v2/doc/doc'
# GDELT requires OR clauses to be wrapped in parentheses
DEFAULT_QUERY = '(shipping OR logistics OR maritime)'
DEFAULT_MAX_RECORDS = 250
DEFAULT_DAYS = 30
# Use YYYYMMDDHHMMSS format for API filtering, e.g. 20260213000000
DEFAULT_START_DATETIME = None  # set e.g. '20260310000000' for fixed range
DEFAULT_END_DATETIME = None  # set e.g. '20260315000000' for fixed range


def build_gdelt_query_parameters(query=DEFAULT_QUERY, max_records=DEFAULT_MAX_RECORDS, startdatetime=None, enddatetime=None):
    """Return API parameters for a shipping-market doclist GDELT query."""
    params = {
        'query': query,
        'mode': 'artlist',
        'maxrecords': max_records,
        'format': 'json',
        'sort': 'DateDesc'
    }

    if startdatetime is not None:
        params['startdatetime'] = startdatetime
    if enddatetime is not None:
        params['enddatetime'] = enddatetime

    return params


def build_last_n_day_windows(days=DEFAULT_DAYS, window_size=1):
    """Generate (startdatetime,enddatetime) windows for the last N days."""
    from datetime import datetime, timedelta

    now = datetime.utcnow().replace(hour=0, minute=0, second=0, microsecond=0)
    windows = []
    for i in range(days):
        end = now - timedelta(days=i)
        start = end - timedelta(days=window_size)
        windows.append((start.strftime('%Y%m%d%H%M%S'), end.strftime('%Y%m%d%H%M%S')))

    return list(reversed(windows))  # oldest first


def fetch_gdelt_articles_with_retries(api_url, params, max_attempts=20, initial_backoff=1):
    """Fetch GDELT JSON data with retries and exponential backoff on 429 rate limits."""
    backoff = initial_backoff
    for attempt in range(1, max_attempts + 1):
        try:
            response = requests.get(api_url, params=params, timeout=15)
            response.raise_for_status()

            if not response.text:
                raise RuntimeError('GDELT response body is empty')

            try:
                return response.json()
            except ValueError as e:
                snippet = response.text[:500].replace('\n', ' ') if isinstance(response.text, str) else ''
                raise RuntimeError(f'Invalid JSON from GDELT API (status {response.status_code}): {snippet}') from e

        except requests.exceptions.HTTPError as e:
            status = getattr(response, 'status_code', None)
            if status == 429 and attempt < max_attempts:
                print(f'Rate limited (429); retrying in {backoff} second(s) (attempt {attempt}/{max_attempts})')
                time.sleep(backoff)
                backoff *= 2
                continue
            raise RuntimeError(f'GDELT API error: {e} (status {status})') from e
        except requests.RequestException as e:
            raise RuntimeError(f'Network error querying GDELT API: {e}') from e
    raise RuntimeError('Max retry attempts reached for GDELT API call.')


def extract_articles_from_gdelt_response(data):
    """Extract article list from GDELT API response and return only English articles."""
    if not isinstance(data, dict):
        return []

    articles = data.get('articles') or []
    english_articles = [a for a in articles if (a.get('language') or '').strip().lower() == 'english']
    return english_articles


def print_news_articles(articles):
    """Print all returned articles in a human-readable format."""
    if not articles:
        print('No articles found for query.')
        return

    print(f'Latest {len(articles)} news articles from GDELT:')
    for i, article in enumerate(articles, start=1):
        title = article.get('title', 'No title')
        url = article.get('url', 'No URL')
        date = article.get('seendate', article.get('date', 'Unknown date'))
        print(f"{i}. [{date}] {title}\n   {url}")
    print('\nDone.')


def main():
    if DEFAULT_START_DATETIME and DEFAULT_END_DATETIME:
        windows = [(DEFAULT_START_DATETIME, DEFAULT_END_DATETIME)]
    else:
        windows = build_last_n_day_windows(days=DEFAULT_DAYS)

    collected = []
    seen_urls = set()

    for startdatetime, enddatetime in windows:
        params = build_gdelt_query_parameters(startdatetime=startdatetime, enddatetime=enddatetime)
        try:
            data = fetch_gdelt_articles_with_retries(GDELT_API_URL, params)
        except RuntimeError as e:
            print(f'Warning: window {startdatetime}-{enddatetime} failed: {e}', file=sys.stderr)
            continue

        articles = extract_articles_from_gdelt_response(data)

        for article in articles:
            url = article.get('url')
            if not url or url in seen_urls:
                continue
            seen_urls.add(url)
            collected.append(article)

    if DEFAULT_START_DATETIME and DEFAULT_END_DATETIME:
        print(f'Retrieved {len(collected)} unique English articles from {DEFAULT_START_DATETIME} to {DEFAULT_END_DATETIME}.')
    else:
        print(f'Retrieved {len(collected)} unique English articles in the last {DEFAULT_DAYS} days.')
    print_news_articles(collected)


if __name__ == '__main__':
    main()