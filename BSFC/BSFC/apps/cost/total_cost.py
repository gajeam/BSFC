from BSFC.apps.item.models import Item

def total_cost():

	A = Item.objects.all()

	total = 0

	for thing in A:
		total += thing.cost.item_cost*thing.count

	return total

