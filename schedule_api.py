import requests

def init(fields):
	json = {"bldgcode": fields.bldg, "classdays": fields.days, "classname": fields.classname,"classnum": fields.code, "classtype": fields.classtype, "endtime": fields.end, "professor": fields.professor, "roomcode": fields.room, "seats": fields.seats, "starttime": fields.start}
	r = requests.post("http://127.0.0.1:5000/api/class", headers={'content-type':'application/json'}, json=json)
