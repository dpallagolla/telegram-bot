from uber_rides.session import Session
from uber_rides.client import UberRidesClient
from uber_cab import uber_cab
import json
from pprint import pprint



class get_products:

	def __init__(self):
		session = Session(server_token='')

		client = UberRidesClient(session)

		response = client.get_products(37.77, -122.41)

		products = response.json.get('products')


		#ubers variable contains all available products in json format
		ubers = json.loads(json.dumps(products))

		cab_list = []

		for uber in ubers:
			ucab = uber_cab(uber['display_name'],uber['shared'],uber['description'],uber['capacity'])
			print ucab.getDetails()
			cab_list.append(ucab)

		return cab_list



