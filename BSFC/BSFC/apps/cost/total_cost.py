from BSFC.apps.item.models import Item

A = Items.objects.all()

total = 0

for thing in A
	total += thing.cost.item_cost*thing.count

return total

