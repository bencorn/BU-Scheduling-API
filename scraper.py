from collections import namedtuple
import textcleaners
from bs4 import BeautifulSoup
import urllib.request
import schedule_api


def table(college, dept, course):
	soup = BeautifulSoup(urllib.request.urlopen(
		'https://www.bu.edu/link/bin/uiscgi_studentlink.pl/1454031983?ModuleName=univschr.pl&SearchOptionDesc=Class+Number&SearchOptionCd=S&KeySem=20164&ViewSem=Spring+2016&College=%s&Dept=%s&Course=%s&Section=' % (
			college, dept, course)).read())
	class_nums = len(soup('table')[5].findAll('tr'))

	for row_id in range(1, class_nums - 4):

		colspan = str((soup('table')[5].find_all('tr')[row_id].find_all('td')))
		if 'colspan="1"' in colspan:
			# Class num
			classnum = soup('table')[5].findAll('tr')[row_id].findAll('td')[1].a.string
			if course in classnum:
				# Class name + professor
				name = soup('table')[5].findAll('tr')[row_id].findAll('td')[2].font.text

				professor = textcleaners.cprofessor(name)  # Retrieves last list item
				name = textcleaners.cclassname(name,professor)
				print(professor)

				code = dept + course
				# Class type
				classtype = soup('table')[5].findAll('tr')[row_id].findAll('td')[5].font.text
				classtype = classtype.strip()

				# Open seats
				seats = soup('table')[5].findAll('tr')[row_id].findAll('td')[6].font.text
				seats = seats.strip()
				seats = int(seats)

				# Building code
				bldg = soup('table')[5].findAll('tr')[row_id].findAll('td')[7].a.text
				bldg = textcleaners.cbldg(bldg)

				# Room code
				room = soup('table')[5].findAll('tr')[row_id].findAll('td')[8].font.text
				room = textcleaners.croom(room)

				# Class days
				days = soup('table')[5].findAll('tr')[row_id].findAll('td')[9].font.text
				days = textcleaners.cdays(days)

				# Start time
				start = soup('table')[5].findAll('tr')[row_id].findAll('td')[10].font.text
				start = textcleaners.cstart(start)

				# End time
				end = soup('table')[5].findAll('tr')[row_id].findAll('td')[11].font.text
				end = textcleaners.cend(end)

				Fields = namedtuple('Fields',
									['code', 'classname', 'professor', 'classtype', 'seats', 'bldg', 'room', 'days'
										, 'start', 'end'])
				fields = Fields(code, name, professor, classtype, seats, bldg, room, days, start, end)

				# print(fields)
				# print("\n")

				# Initializing api POST request to database
				schedule_api.init(fields)
