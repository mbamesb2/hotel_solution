==============================
Hipmunk Hotel Search Solution
Michael Bamesberger
==============================

This program returns a JSON list of hotel search results. The search results are pulled from five APIs and sorted by 'ecstasy'.

The program runs in conjunction with Hipmunk's hotel_search scraper program, which must be started first. Navigate to the hotel_search folder and enter the following into the command line: 

	python scraperapi.py

Then, run the setup.py script in the hotel_solution folder. Once finished, enter the following:

	python scraperUpdate.py

Then, navigate to http://localhost:8000/hotels/search to view the sorted
hotel list.

To test the solution program, keep the scraperapi program and the scraperupdate program running, and enter the following:
	
	python hotel_search.scraperapi_test
	

Layout
=========

The solution contains two files:

*scraperUpdate.py, which contains the web application
*fetchResults.py, which contains the API calls and sort logic

