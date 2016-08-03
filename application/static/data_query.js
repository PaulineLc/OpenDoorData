//When the page loads we want to automatically query the DB and plot
//plot the information on the chart

var room_selection;
function displayDate(){
	var date = new Date(document.getElementById("datething").value);
	getPredictedInfo(date.getDate(), date.getMonth() + 1, date.getFullYear())
}

function getPredictedInfo(date, month, year){
	var xmlhttp = new XMLHttpRequest();
	
	var url = "/predicted/" + room_selection + "/" + date + "/" + month + "/" + year;
	console.log(url)

	xmlhttp.onreadystatechange = function() {
	    if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {
	        var predictedValues = JSON.parse(xmlhttp.responseText);
	        //Once we've got the data from our database in JSON format we then
	        //proceed to draw the chart
	        console.log(predictedValues);
	        drawPredictedValueCharts(predictedValues);
	    }
	};
	xmlhttp.open("GET", url, true);
	xmlhttp.send();
}
//Using XMLHttpRequest() to query flask application
function getRoomInfo(){
	//get the room selected by the user
	var selector = document.getElementById("room_select");
	room_selection = selector.options[selector.selectedIndex].value;


	//Then do a AJAX request for data about this room
	sendJSONRequest(room_selection);
	
}

function sendJSONRequest(room){
	var xmlhttp = new XMLHttpRequest();
	var url = "/dailyavg/" + room;
	

	xmlhttp.onreadystatechange = function() {
	    if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {
	        var general_hourly_average = JSON.parse(xmlhttp.responseText);
	        //Once we've got the data from our database in JSON format we then
	        //proceed to draw the chart
	        // TODO: If a chart has already been drawn 
	        // then it needs to be refreshed rather than drawn again

	        var occupancy_data_points = setOccupancyPercentage(general_hourly_average[0].Daily);
	        getFrequencyPercentage(general_hourly_average[0].Frequency)
	        createHourlyAverageChart(general_hourly_average[0].Daily);
	        createFrequencyOfUseChart(general_hourly_average[0].Frequency);
	        createOccupancyChart(occupancy_data_points);
	    }
	};
	xmlhttp.open("GET", url, true);
	xmlhttp.send();
}
