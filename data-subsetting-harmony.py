# https://nasa-openscapes.github.io/2021-Cloud-Hackathon/tutorials/07_Harmony_Subsetting.html

import requests
from pprint import pprint
import datetime as dt
import xarray as xr

url = 'https://cmr.earthdata.nasa.gov/search'

collection_url = f'{url}/collections'

short_name = "MODIS_A-JPL-L2P-v2019.0"
concept_id = "C1940473819-POCLOUD"

response = requests.get(
    collection_url,
    params = {'concept_id': concept_id},
    headers = {'Accept': 'application/json'}
)
pprint(response.json())
