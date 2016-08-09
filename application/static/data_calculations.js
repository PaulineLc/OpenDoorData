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

function calculateYaxisLabels(minfo){
	//initiate labels to an empty array
	var labels = [];

	//loop through each class that has been recorded and create a yaxis label string consisting of the date format = 'day' of 'month' 'yea' @ 'TIME'
	for (var i = 0; i < minfo.length; i++){
		var dateStr = minfo[i].event_day + " " + getMonth(minfo[i].event_month) + " " + minfo[i].event_year + " @ " + minfo[i].event_hour;
		labels.push(dateStr);
	}

	return labels;
}

function getMonth(m_int){
	var month = new Array();
	month[1] = "January";
	month[2] = "February";
	month[3] = "March";
	month[4] = "April";
	month[5] = "May";
	month[6] = "June";
	month[7] = "July";
	month[8] = "August";
	month[9] = "September";
	month[10] = "October";
	month[11] = "November";
	month[12] = "December";

	return month[m_int];
}