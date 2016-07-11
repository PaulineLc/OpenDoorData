
 google.charts.load('current', {
            packages: ['corechart']
        });
function checkInput(){
	var xmlhttp = new XMLHttpRequest();
	var url = "/getjson/2/Monday";

	xmlhttp.onreadystatechange = function() {
    if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {
        var data = JSON.parse(xmlhttp.responseText);        
        console.log(data.length);
        insertData(data);


    }
};
xmlhttp.open("GET", url, true);
xmlhttp.send();
}

function insertData(data){
	var imageDiv = document.getElementById("roompic");
	imageDiv.style.display = "block";
	imageDiv.src = "static/images/b002.jpg";
	drawChart(data);
}
function drawChart(dailydata) {
    var data = new google.visualization.DataTable();
    data.addColumn('string', 'Time');
    data.addColumn('number', 'Average Occupancy');
    data.addRow(["08:00", parseInt(dailydata[0])]);
    data.addRow(["09:00", parseInt(dailydata[1])]);
    data.addRow(["10:00", parseInt(dailydata[2])]);
    data.addRow(["11:00", parseInt(dailydata[3])]);
    data.addRow(["12:00", parseInt(dailydata[4])]);
    data.addRow(["13:00", parseInt(dailydata[5])]);
    data.addRow(["14:00", parseInt(dailydata[6])]);
    data.addRow(["15:00", parseInt(dailydata[7])]);
    data.addRow(["16:00", parseInt(dailydata[8])]);
    data.addRow(["17:00", parseInt(dailydata[9])]);
    data.addRow(["18:00", parseInt(dailydata[10])]);
    data.addRow(["19:00", parseInt(dailydata[11])]);
    data.addRow(["20:00", parseInt(dailydata[12])]);
    data.addRow(["21:00", parseInt(dailydata[13])]);
    data.addRow(["22:00", parseInt(dailydata[14])]);
    data.addRow(["23:00", parseInt(dailydata[15])]);

	var options = {
                backgroundColor: { fill: "transparent" },
                animation: {"startup": true,
                           duration: 1000,
                            easing: 'out'},
                title : 'Average Hourly Occupancy for B002',
                height : 200,
                width : 700,
                legend: {
                    position: 'none'
                },
                curveType: 'function',
                colors: ['#084C55'],
                bar: {
                    gap: 10
                },
                gridlines: {
                    color: 'none'
                },
                vAxis: {
                    gridlines: {
                        color: 'transparent'
                    },
                    title: '\n\n\n\nAverage Occupancy',
                    textPosition: 'out'
                },
                hAxis: {
                	textStyle : {
                		fontSize: 10
                	},
                    slantedText: true,
                    slantedTextAngle: 45
                }
            };

    var chart = new google.visualization.ColumnChart(document.getElementById("hourlyChart"));
            chart.draw(data, options);
}