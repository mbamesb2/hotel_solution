from tornado import gen, ioloop, web
from tornado.httpclient import AsyncHTTPClient
from operator import itemgetter
import json


	
class hotelFetcher(object):
	def __init__(self):
		self.providers = ['http://localhost:9000/scrapers/expedia',
	        	'http://localhost:9000/scrapers/orbitz',
				'http://localhost:9000/scrapers/priceline',
				'http://localhost:9000/scrapers/travelocity',
				'http://localhost:9000/scrapers/hilton'
				]

	@gen.coroutine
	def fetch_data(self):
		http_client = AsyncHTTPClient()
		response = yield [http_client.fetch(provider) for provider in self.providers]
		raise gen.Return(response)

	def sort_data(self, results):
		hotels = []
		results = [json.loads(result.body) for result in results]
		results = [result["results"] for result in results]
		for provider in results:
			for item in provider:
				hotels.append(item)
		hotels.sort(key=itemgetter('ecstasy'), reverse = True)
		return hotels
