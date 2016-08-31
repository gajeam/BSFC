from BSFC.apps.tips.models import Tips

def get_tips(start_date, end_date):
	"""add up and return all donations ("tips") made in range (inclusive) specified in input params."""
	todays_payments = #call to REST API to get list of all payments, expanding by 'order,' 'refunds,' and 'tender' and filtering by day
	total = 0
	for payment_dict in todays_payments:
		if 'tipAmount' in payment_dict:
			total += payment_dict['tipAmount']
	return total
