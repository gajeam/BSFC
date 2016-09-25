from BSFC.apps.item.models import Item
from generic_items import custom_item
from generic_items import unknown_item
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
        item_dict['categories']['elements'].append({'name' : None})
    return item_dict
    
def validate_line_item(line_item_dict):
	if 'item' not in line_item_dict:
		if line_item_dict['name'] == 'Custom Item':
			log.error('Custom Item logged')
			return custom_item
		else:
			log.error(line_item_dict['name'] + ' does not have an order id in Clover. Recorded as Unknown Item.')
			return unknown_item
	else:
		return None
