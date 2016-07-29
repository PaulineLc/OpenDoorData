function convertToPercentage(data, capacity){
	//This function takes in a set of data points and returns them as a percentage
	//of a rooms capacity

	for (var i = 0; i <  data.length; i++){
		data[i] = Math.round(data[i]/capacity * 100) / 100;
	}
	return data
}