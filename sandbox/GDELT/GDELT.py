import sys
import time
import requests

# GDELT 2.0 doc API for recent news
# The query below searches for Brazil-related articles. We request JSON and limit to 5.
GDELT_API_URL = 'https://api.gdeltproject.org/api/v2/doc/doc'

params = {
    'query': 'brazil',
    'mode': 'artlist',
    'maxrecords': 5,
    'format': 'json',
    'sort': 'DateDesc'
}

max_attempts = 5
sleep_seconds = 1

for attempt in range(1, max_attempts + 1):
    try:
        response = requests.get(GDELT_API_URL, params=params, timeout=15)
        response.raise_for_status()
        data = response.json()
        break
    except requests.exceptions.HTTPError as e:
        if response.status_code == 429 and attempt < max_attempts:
            print(f'Rate limited (429), retrying in {sleep_seconds} seconds ({attempt}/{max_attempts})')
            time.sleep(sleep_seconds)
            sleep_seconds *= 2
            continue
        print('Error querying GDELT API:', e, file=sys.stderr)
        sys.exit(1)
    except requests.RequestException as e:
        print('Network error querying GDELT API:', e, file=sys.stderr)
        sys.exit(1)
else:
    print('Max retry attempts reached, aborting.', file=sys.stderr)
    sys.exit(1)

articles = data.get('articles') or data.get('articles', [])

if not articles:
    print('No articles found for Brazil.')
    sys.exit(0)

print('Latest 5 Brazilian news articles from GDELT:')
for i, article in enumerate(articles[:5], start=1):
    title = article.get('title', 'No title')
    url = article.get('url', 'No URL')
    date = article.get('seendate', article.get('date', 'Unknown date'))
    print(f"{i}. [{date}] {title}\n   {url}")

print('\nDone.')