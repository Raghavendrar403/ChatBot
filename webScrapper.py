from bs4 import BeautifulSoup as bs
from urllib.request import urlopen as uReq
from urllib.request import Request
import os

urlStart = "https://www.holidify.com/places/" 
urlEnd = "/sightseeing-and-things-to-do.html"


headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}

with open('cities.txt') as cities:
	citiesList = cities.read().split('\n')
	citiesList.remove(citiesList[-1])

places = citiesList

dirName = "FamousPlaces"

try:
	os.mkdir(dirName)
	print(f"Directory {dirName} created")
except:
	print(f"Directory {dirName} already exists")

htmlDirName = "HTMLFiles"

try:
	os.mkdir(htmlDirName)
	print(f"Directory {htmlDirName} created")
except:
	print(f"Directory {htmlDirName} already exists")


# Start retrieving html files
os.chdir(htmlDirName)
for p in places:
	# Complete URL to parse
	myUrl = urlStart + p + urlEnd
	print("================Started parsing "+p+"======================")
	print("getting html for "+p)
	try:
		req = Request(myUrl, headers=headers)
		htmlObject = uReq(req)
		htmlFile = htmlObject.read()
		text = htmlFile.decode('utf-8')
		print("saving the html file")
		with open(p+'.html', 'w+') as myHTML:
			myHTML.write(text)		
		print('file '+p+'.html saved');

	except:
		print('The HTML page is not available for '+p)
	
# Go back to previous directory
os.chdir('..')


