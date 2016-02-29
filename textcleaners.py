import re


def cprofessor(name):
	prof = re.findall('[A-Z][^A-Z]*', name)[-1]
	return prof


def cclassname(name, prof):
	#name = re.findall('[A-Z][^A-Z]*', name)[:-1]
	#name = [name.replace(u'\xa0', u' ') for name in name]
	name = name.replace(prof, '') #for name in name]
	name = "".join(name)
	return name


def cbldg(bldg):
	bldg = re.sub('ARR', '', bldg)
	bldg = bldg.strip()
	return bldg


def croom(room):
	room = re.sub('ARR', '', room)
	room = room.strip()
	return room


def cdays(days):
	days = days.strip()
	if len(days) > 7:
		days = days[:-(len(days)-7)]
		return days
	else:
		return days


def cstart(start):
	start = start.strip()
	start = start.split(" ")[0]
	return start


def cend(end):
	end = end.strip()
	end = end.split(" ")[0]
	return end
