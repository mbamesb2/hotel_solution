from tornado import gen, ioloop, web, escape
from tornado.httpclient import AsyncHTTPClient
from operator import itemgetter
from fetchResults import hotelFetcher
import json

class MainHandler(web.RequestHandler):
		
	@gen.coroutine
	def get(self):
		hf = hotelFetcher()
		results = yield hf.fetch_data()
		results = hf.sort_data(results)

		self.write({ 
			'results': results})
	
def make_app():
	return web.Application([
		(r"/hotels/search", MainHandler),
	])

def run():
	app = make_app()
	app.listen(8000)
	print "Server started. Listening on port 8000..."
	ioloop.IOLoop.current().start()

if __name__ == "__main__":
	run()