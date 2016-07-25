import json
import collections

def return_json(data):

	j = json.dumps(data)

	return j

def createRoomJson(daily_average, frequency_of_use):
        
        
    
    output_list = []
    

    d = collections.OrderedDict()
    d['Daily'] = daily_average
    d['Frequency'] = frequency_of_use

        
        
        

    output_list.append(d) 
    
    j = json.dumps(output_list)
    return j