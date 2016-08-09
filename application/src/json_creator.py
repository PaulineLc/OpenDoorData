import json
import collections

def return_json(data):

	j = json.dumps(data)

	return j

def createGeneralDataJson(hourly_average, frequency_of_use):
	#print(frequency_of_use)

	output_list = []


	d = collections.OrderedDict()
	d['Daily'] = hourly_average
	d['Frequency'] = frequency_of_use
	output_list.append(d)

	j = json.dumps(output_list)
	print(j)
	return j

def createBuildingInfoJson(building_info, room_info):
	output_list = []

	# building_dict = collections.OrderedDict()
	# building_dict['name'] = building_info[2]
	# building_dict['phone'] = building_info[3]
	# building_dict['email'] = building_info[4]
	# building_dict['weekday_opening'] = building_info[5]
	# building_dict['weekday_closing'] = building_info[6]
	# building_dict['weekend_opening'] = building_info[7]
	# building_dict['weekend_closing'] = building_info[8]

	# romm_dict = collection.OrderedDict()
	# room_dict['']
	d = collections.OrderedDict()
	d['building_info'] = building_info
	d['room_list'] = room_info

	output_list.append(d)

	j = json.dumps(d)
	print(j)
	return j