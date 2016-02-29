# File name: main.py
# Author: Benjamin Corn
# Date created: 2/20/2016
# Date last modified: 2/25/2016
# Python Version: 3.0

import scraper

# data collection variables
college = "ENG"
dept = "EK"
coursentry = list()
new_course = ''

while new_course != 'quit':
	new_course = input('Enter class: ')

	coursentry.append(new_course)
for n in coursentry:
	# calling main scraping function
	scraper.table(college, dept, n)



