from bs4 import BeautifulSoup as bs

from os import listdir
from os.path import join, isfile
import os

# First get all the HTML files from HTMLFiles folders
htmlPath = os.getcwd()+'/HTMLFiles'
htmlFiles = [join(htmlPath,f) for f in listdir(htmlPath) if isfile(join(htmlPath,f))]

# Loop over every single one of them and create a json file for each city
for singleFile in htmlFiles:
	# Parse the name of different locations and their
	# description. Save them as JSON file.

