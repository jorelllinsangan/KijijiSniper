from bs4 import BeautifulSoup as bs
from ProductAd import ProductAd
import requests, sched, time, webbrowser, random



url = raw_input("Please enter kijiji url: ")
tags = []
userInput = ""
while userInput != "q":
	userInput = raw_input("Enter a string to watch out for (press q when done): ")
	userInput.lower()
	if userInput != "q":
		tags.append(userInput)

s = sched.scheduler(time.time, time.sleep)
entryId = set()

def snipeThatLens(count):
	print "Checking for 10-18mm Canon Lens: %d" % count
	
	req = requests.get(url=url)
	soup = bs(req.text, 'html.parser')
	tables = soup.find_all('table')

	for entry in tables:
		for tag in tags:
			if entry.a != None and entry.a.string != None and tag in entry.a.string:
				adId = entry.div['data-adid'] 
				if adId not in entryId:
					entryId.add(adId)
					webbrowser.open(url)

	s.enter(random.randint(100,600), 1, snipeThatLens, (count+1,))

snipeThatLens(1)

# s.run()



