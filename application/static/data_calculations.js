function convertToPercentage(data, capacity){
	//This function takes in a set of data points and returns them as a percentage
	//of a rooms capacity

	for (var i = 0; i <  data.length; i++){
		data[i] = Math.round(data[i]/capacity * 100) / 100;
	}
	return data
}

function getFrequencyPercentage(freq){
	console.log(freq[1]);
	var sum = parseInt(freq[0]) + parseInt(freq[1]);
	console.log(sum);
	var frequency_percentage = Math.round(freq[0] / sum * 100);
	console.log(frequency_percentage);
	document.getElementById("general_fou_percent").innerHTML = frequency_percentage.toString() + "%";
}

function setOccupancyPercentage(occu){
	var sum = 0;
	console.log(occu[0].occupancy_category_5);
	for (var i  = 0; i < occu.length; i++){
		sum += occu[i].occupancy_category_5;
	}
	var occupancy_percentage = Math.round((sum / occu.length) * 100);
	var occupancy_data_points = []
	occupancy_data_points.push(occupancy_percentage);
	document.getElementById("general_occupancy_percent").innerHTML = occupancy_percentage.toString() + "%";
	occupancy_data_points.push(100 - occupancy_percentage);
	console.log(occupancy_data_points);
	return occupancy_data_points;
}