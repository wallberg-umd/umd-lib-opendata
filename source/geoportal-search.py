import urllib.request
import json

# Search BTAA Geoportal using JSON OpenSearch

ENDPOINT = 'https://geo.btaa.org/catalog.json'


''' Search BTAA Geoportal using JSON OpenSearch, using named parameters '''

# Build the URL

# Contributing institution is University of Maryland
params = {'f[dct_provenance_s][]': "Maryland"}

search_url = ENDPOINT + '?' + urllib.parse.urlencode(params)

print('\n========================')
print(f'Search URL: {search_url}')

# Get search results as parsed XML
with urllib.request.urlopen(search_url) as request:
    response = json.loads(request.read())

    # Iterate over the returned items
    for item in response['data']:
        link = item['links']['self']

        if 'attributes' in item:
            title = item['attributes']['dc_description_s']['attributes']['value']
        else:
            title = "??"

        print('----')
        print(f'Title: {title}')
        print(f'Link:  {link}')

