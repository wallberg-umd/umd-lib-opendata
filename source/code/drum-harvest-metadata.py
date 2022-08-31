#!/usr/bin/env python3

# Use the DRUM OpenSearch API to harvest a list of
# all items in DRUM

import logging
from xml.etree import ElementTree
from http.client import HTTPConnection
import sys

import requests
import yaml


# Search DRUM using OpenSearch

ENDPOINT = 'https://drum.lib.umd.edu/open-search/discover'
RPP = 100  # Maximum records per page allowed by DRUM

ATOM = '{http://www.w3.org/2005/Atom}'
OPENSEARCH = '{http://a9.com/-/spec/opensearch/1.1/}'


def search(**params):
    ''' Search DRUM using OpenSearch, using named parameters '''

    params['rpp'] = RPP
    start = 1

    # Get paged results
    while True:

        # Submit the request for the next page of items
        params['start'] = start
        response = requests.get(ENDPOINT, params=params)

        if not response.ok:
            print(f'Error reading response: {response}')
            return

        # Get search results as parsed XML
        atom = ElementTree.fromstring(response.text)

        total_results = int(atom.find(f'{OPENSEARCH}totalResults').text)

        # Iterate over the returned items
        for element in atom.findall(f'{ATOM}entry'):

            item = {}

            # Extract Item information
            item['title'] = element.find(f'{ATOM}title').text
            item['handle_url'] = element.find(f'{ATOM}link').get('href')
            item['updated'] = element.find(f'{ATOM}updated').text

            if (e := element.find(f'{ATOM}published')) is not None:
                item['published'] = e.text

            item['author'] = []
            for author in element.findall(f'{ATOM}author/{ATOM}name'):
                item['author'].append(author.text)

            item['summary'] = []
            for summary in element.findall(f'{ATOM}summary'):
                item['summary'].append(summary.text)

            # Write the record as a single YAML document to stdout
            yaml.dump(item, sys.stdout, explicit_start=True)

        # Check if we received all of the results
        if start + RPP > total_results:
            return
        else:
            start += RPP


if __name__ == "__main__":
    search(query='*:*')
