import json
import collections

#TODO: These functions are highly repetitive, can they be made more modular

def createGeneralDataJson(hourly_average, frequency_of_use, occupancy_rating):
	'''Function that takes in the hourly average data created from occupancy_prediction.py and the frequency of use data
	for a room and returns the two parameters merged into one JSON file'''

	output_list = []

	d = collections.OrderedDict()
	d['Daily'] = hourly_average
	d['Frequency'] = frequency_of_use
	d['Occupancy_Rating'] = occupancy_rating

	output_list.append(d)
	j = json.dumps(output_list)
	return j

def createBuildingInfoJson(building_info, room_info):
	'''Function that takes in a queried building's information and a list of all rooms with the rooms capacity
	and returns the two parameters merged into one JSON file'''
	output_list = []

	d = collections.OrderedDict()
	d['building_info'] = building_info
	d['room_list'] = room_info
	output_list.append(d)

	j = json.dumps(d)
	print(j)
	return j

def returnModuleJSON(m_data, reg_stu):
	'''Function that takes in a queried module's information and the registered students for that module
	and returns the two parameters merged into one JSON file'''
	output_list = []

	d = collections.OrderedDict()
	d['module_info'] = m_data
	d['registered_students'] = reg_stu
	
	output_list.append(d)
	j = json.dumps(d)
	return j

