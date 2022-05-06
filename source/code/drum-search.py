import urllib.request
from xml.etree import ElementTree

# Search DRUM using OpenSearch

ENDPOINT = 'https://drum.lib.umd.edu/open-search/discover'

def search(**params):
    ''' Search DRUM using OpenSearch, using named parameters '''

    # Build the URL
    params['rpp'] = 5  # get first 5 results
    search_url = ENDPOINT + '?' + urllib.parse.urlencode(params)

    print('\n========================')
    print(f'Search URL: {search_url}')

    # Get search results as parsed XML
    with urllib.request.urlopen(search_url) as request:
        atom = ElementTree.parse(request).getroot()

        # Iterate over the returned items
        for element in atom.findall('{http://www.w3.org/2005/Atom}entry'):

            # Extract Item information
            title = element.find('{http://www.w3.org/2005/Atom}title').text
            handle_url = element.find('{http://www.w3.org/2005/Atom}link').get('href')
            author = element.find('{http://www.w3.org/2005/Atom}author/{http://www.w3.org/2005/Atom}name').text

            print('----')
            print(f'Title:      {title}')
            print(f'Author:     {author}')
            print(f'Handle URL: {handle_url}')

# phrase is "Black Lives Matter"
search(query='"Black Lives Matter"')

# advisor is smela
# collection is 1903/2795 (Mechanical Engineering ETDs)
search(query='advisor:smela', scope='1903/2795')

# community is 1903/2278 (Library Staff Research Works)
search(query='*:*', scope='1903/2278')

