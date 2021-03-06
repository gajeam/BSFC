from BSFC.apps.item.models import Item
from BSFC.apps.cost.models import Cost
from BSFC.apps.revenue.models import Revenue
import requests


def get_api_data(endpoint, filterItems=None, expandItems=None):
    url = 'https://api.clover.com/v3/merchants/RCM4Z558RGRJ8/' + endpoint
    parameters = {"limit": 1000}
    if filterItems is not None:
        parameters["filter"] = filterItems
    if expandItems is not None:
        parameters["expand"] = expandItems
    headers = {"Authorization": "Bearer 8661cfda-4d67-fe8b-61fd-939901219070"}
    response = requests.get(url, headers=headers, params=parameters)
    if response.status_code == 200:
        # this gives a list of objects (dicts) of endpoint, expanded by params
        resp_json = response.json()
        if 'elements' in resp_json:
            return resp_json['elements']
        return resp_json
    return []
