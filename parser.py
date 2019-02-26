from bs4 import BeautifulSoup as bs

from os import listdir
from os.path import join, isfile
import os
import json

# First get all the HTML files from HTMLFiles folders
htmlPath = os.getcwd()+'/HTMLFiles'
htmlFiles = [join(htmlPath,f) for f in listdir(htmlPath) if isfile(join(htmlPath,f))]

# Create a folder to store the json files.
jsonDir = 'JSONFiles'
try:
	os.mkdir(jsonDir)
	print(f'Directory {jsonDir} created successfully')
except:
	print(f'Directory {jsonDir} alredy exists')

jsonData = {}


# Loop over every single one of them and create a json file for each city
for city in htmlFiles:
	# Parse the name of different locations and their
	# description. Save them as JSON file.

	# All the famous places in a city are store in a div tag with
	# class='col-md-6 col-xs-12 col-sm-6 ptvColumn nopaddingMobile nopaddingLeftTablet'

	# First split will take out the absolute address and split it
	# the last in the split list is the file name
	# for indexing in the dictionary we take out the .html part
	# we store it in lower case
	cityName = city.split('/')[-1].split('.')[0].lower()
	print(cityName)
	jsonData[cityName] = []
	with open(city, 'r') as singleFile:
		# parse the html file
		htmlFile = bs(singleFile.read(),'html.parser')
		# retrieve all the div containers	
		divContainers = htmlFile.findAll('div',{'class':'col-md-6 col-xs-12 col-sm-6 ptvColumn nopaddingMobile nopaddingLeftTablet'})
		
		for eachPlace in divContainers:
			try:
				# First retrieve the place name
				placeName = eachPlace.find('h2',{'class':'ptvObjective'}).text
				# Retrieve its description. strip() function is used to remove extra whietspaces
				placeDescription = eachPlace.find('p',{'class':'ptvText'}).text.strip()

				# Save the placeName and in the jsonData dictionary for the city
				jsonData[cityName].append({
					placeName:placeDescription,
				})

			except:
				pass

	# Now save the jsonData in the json file for that city
	with open('JSONFiles/'+cityName+'.json','w+') as jsonFile:
		json.dump(jsonData, jsonFile)
			
	# Delete that jsonData key value pair	
	del jsonData[cityName]
		
