//When the page loads we want to automatically query the DB and plot
//plot the information on the chart

//Using XMLHttpRequest() to query flask application
var xmlhttp = new XMLHttpRequest();
var url = "/dailyavg/2";

xmlhttp.onreadystatechange = function() {
    if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {
        var dailyAvg = JSON.parse(xmlhttp.responseText);
        //Once we've got the data from our database in JSON format we then
        //proceed to draw the chart
        createDailyAverageChart(dailyAvg[0].Daily);
        doSomething(dailyAvg[0].Frequency);
    }
};
xmlhttp.open("GET", url, true);
xmlhttp.send();

var xmlhttp2 = new XMLHttpRequest();
var url2 = "/prediction/";

xmlhttp2.onreadystatechange = function() {
    if (xmlhttp2.readyState == 4 && xmlhttp2.status == 200) {
        var prediction = JSON.parse(xmlhttp2.responseText);
        console.log("gothere");
        //Once we've got the data from our database in JSON format we then
        //proceed to draw the chart
        console.log(prediction);
        
    }
};
xmlhttp2.open("GET", url2, true);
xmlhttp2.send();


