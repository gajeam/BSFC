headers = {"Authorization": "Bearer 8661cfda-4d67-fe8b-61fd-939901219070"}
url = 'https://api.clover.com/v3/merchants/RCM4Z558RGRJ8/items?expand=lineItems'
import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds']

credentials = ServiceAccountCredentials.from_json_keyfile_name('BSFC-e1ba6e23904b.json', scope)

gc = gspread.authorize(credentials)

wks = gc.open_by_url("https://docs.google.com/spreadsheets/d/12sv4lmEC3OhesEd0yPHy1c_Yu3wtOEBVLxie3TxYIMo/edit#gid=0").sheet1
import requests
req = requests.get(url, headers=headers)
data = req.json()['elements']
nameCell = wks.find('NAME')
priceCell = wks.find('PRICE')
costCell = wks.find('COST')
stockcountCell = wks.find('STOCKCOUNT')
count = int(nameCell.row) + 1
for item in data:
	if 'stockCount' not in item:
		item['stockCount'] = 'NULL'
	if 'cost' not in item:
		item['cost'] = 'NULL'
	if 'price' not in item:
		item['price'] = 'NULL'
	wks.update_cell(count, nameCell.col, item['name'])
	wks.update_cell(count, priceCell.col, item['price'])
	wks.update_cell(count, costCell.col, item['cost'])
	wks.update_cell(count, stockcountCell.col, item['stockCount'])
	count += 1
### TODO

# ORDERS