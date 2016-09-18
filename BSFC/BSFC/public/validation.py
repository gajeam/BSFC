import logging
log = logging.getLogger('django')

def validate_item(item_dict):
	if 'cost' not in item_dict or item_dict['cost'] == 0:
		log.error(item_dict['name'] + ' does not have a cost entered or cost is zero.')
		item_dict['cost'] = 0
	if 'unitName' not in item_dict:
		item_dict['unitName'] = None
	if not item_dict['categories']['elements']:
		log.error(item_dict['name'] + ' does not an associated category.')
		item_dict['categories']['elements'][0]['name'] = None

