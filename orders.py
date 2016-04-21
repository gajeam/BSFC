headers = {"Authorization": "Bearer 8661cfda-4d67-fe8b-61fd-939901219070"}
url = 'https://api.clover.com/v3/merchants/RCM4Z558RGRJ8/orders?expand=lineItems'
import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds']

credentials = ServiceAccountCredentials.from_json_keyfile_name('BSFC-e1ba6e23904b.json', scope)

gc = gspread.authorize(credentials)

wks = gc.open_by_url("https://docs.google.com/spreadsheets/d/12sv4lmEC3OhesEd0yPHy1c_Yu3wtOEBVLxie3TxYIMo/edit#gid=0").get_worksheet(1)
import requests
from urllib.parse import quote

import sys
unixtime = str(sys.argv)[1]
url += '&createdTime' + quote('>') + unixtime
req = requests.get(url, headers=headers)
data = req.json()['elements']
#print(data)
