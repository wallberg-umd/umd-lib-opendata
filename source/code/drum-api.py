#!/usr/bin/env python3

import urllib.request
import json

# Get a list of items from DRUM using the REST API

ENDPOINT = 'https://api.drum.lib.umd.edu/server/api'

items_url = ENDPOINT + '/discover/browses/title/items'

# Get JSON results
with urllib.request.urlopen(items_url) as request:
    response = json.loads(request.read())

    # Iterate over the returned items
    for item in response['_embedded']['items']:
        md = item['metadata']
        link = ", ".join(entry['value'] for entry in md['dc.identifier.uri'])
        title = "; ".join(entry['value'] for entry in md['dc.title'])

        print('----')
        print(f'Title: {title}')
        print(f'Link:  {link}')
