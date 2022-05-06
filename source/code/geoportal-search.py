import urllib.request
import json

# Search BTAA Geoportal using JSON OpenSearch

ENDPOINT = 'https://geo.btaa.org/catalog.json'

# Keyword query on 'Maryland'
params = {
    "search_field": "all_fields",
    "q": "maryland",
}

search_url = ENDPOINT + '?' + urllib.parse.urlencode(params)

# Get search results as parsed XML
with urllib.request.urlopen(search_url) as request:
    response = json.loads(request.read())

    # Iterate over the returned items
    for item in response['data']:
        link = item['links']['self']

        if 'attributes' in item:
            title = item['attributes']['dct_description_sm']['attributes']['value']
        else:
            title = "??"

        print('----')
        print(f'Title: {title}')
        print(f'Link:  {link}')
