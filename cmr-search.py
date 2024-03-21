# API documentation: https://cmr.earthdata.nasa.gov/search/site/docs/search/api.html

import requests
import datetime as dt
from pprint import pprint

cmr_base = 'https://cmr.earthdata.nasa.gov/search'

# Search all collections
all_collections = requests.get(
    f'{cmr_base}/collections',
    # params = {'page_size': 20},  # <-- How to search results
    headers = {'Accept': 'application/json'}
).json()

# Print down to a certain depth
pprint(all_collections, depth=3)

# Print IDs and titles for the results
def print_products(result):
    i = 0
    for item in result['feed']['entry']:
        i += 1
        print(f"{i}: [{item['id']}] {item['title']}")

print_products(all_collections)

# Inspect an individual entry
all_collections['feed']['entry'][0]

# Search for MODIS projects
modis_collections = requests.get(
    f'{cmr_base}/collections.json',
    params = {'instrument': 'MODIS',
              'short_name': 'reflect',
              'processing_level_id': '3',
              'page_size': 30}
).json()

print_products(modis_collections)
