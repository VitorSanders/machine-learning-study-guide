import sys
import time
import requests

GDELT_API_URL = 'https://api.gdeltproject.org/api/v2/doc/doc'
# GDELT requires OR clauses to be wrapped in parentheses
DEFAULT_QUERY = '(shipping OR logistics OR maritime)'
DEFAULT_MAX_RECORDS = 5


def build_gdelt_query_parameters(query=DEFAULT_QUERY, max_records=DEFAULT_MAX_RECORDS):
    """Return API parameters for a shipping-market doclist GDELT query."""
    return {
        'query': query,
        'mode': 'artlist',
        'maxrecords': max_records,
        'format': 'json',
        'sort': 'DateDesc'
    }


def fetch_gdelt_articles_with_retries(api_url, params, max_attempts=5, initial_backoff=1):
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
    """Extract article list from GDELT API response or return an empty list."""
    if not isinstance(data, dict):
        return []
    return data.get('articles') or []


def print_news_articles(articles):
    """Print up to 5 articles in a human-readable format."""
    if not articles:
        print('No articles found for query.')
        return

    print('Latest 5 news articles from GDELT:')
    for i, article in enumerate(articles[:5], start=1):
        title = article.get('title', 'No title')
        url = article.get('url', 'No URL')
        date = article.get('seendate', article.get('date', 'Unknown date'))
        print(f"{i}. [{date}] {title}\n   {url}")
    print('\nDone.')


def main():
    params = build_gdelt_query_parameters()
    try:
        data = fetch_gdelt_articles_with_retries(GDELT_API_URL, params)
    except RuntimeError as e:
        print('Error:', e, file=sys.stderr)
        sys.exit(1)

    articles = extract_articles_from_gdelt_response(data)
    print_news_articles(articles)


if __name__ == '__main__':
    main()