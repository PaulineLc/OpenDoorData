
//  google.charts.load('current', {
//             packages: ['corechart']
//         });
// function checkInput(){
//     var xmlhttp = new XMLHttpRequest();
//     var url = "/getjson/2/Monday";

//     xmlhttp.onreadystatechange = function() {
//     if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {
//         var data = JSON.parse(xmlhttp.responseText);        
//         console.log(data.length);
//         insertData(data);


//     }
// };
// xmlhttp.open("GET", url, true);
// xmlhttp.send();
// }

// function insertData(data){
   
//     drawChart(data);
// }
// function drawChart(dailydata) {
//     var data = new google.visualization.DataTable();
//     data.addColumn('string', 'Time');
//     data.addColumn('number', 'Average Occupancy');
//     data.addRow(["08:00", parseInt(dailydata[0])]);
//     data.addRow(["09:00", parseInt(dailydata[1])]);
//     data.addRow(["10:00", parseInt(dailydata[2])]);
//     data.addRow(["11:00", parseInt(dailydata[3])]);
//     data.addRow(["12:00", parseInt(dailydata[4])]);
//     data.addRow(["13:00", parseInt(dailydata[5])]);
//     data.addRow(["14:00", parseInt(dailydata[6])]);
//     data.addRow(["15:00", parseInt(dailydata[7])]);
//     data.addRow(["16:00", parseInt(dailydata[8])]);
//     data.addRow(["17:00", parseInt(dailydata[9])]);
//     data.addRow(["18:00", parseInt(dailydata[10])]);
//     data.addRow(["19:00", parseInt(dailydata[11])]);
//     data.addRow(["20:00", parseInt(dailydata[12])]);
//     data.addRow(["21:00", parseInt(dailydata[13])]);
//     data.addRow(["22:00", parseInt(dailydata[14])]);
//     data.addRow(["23:00", parseInt(dailydata[15])]);

//     var options = {
//                 backgroundColor: { fill: 'white' },
//                 animation: {"startup": false,
//                            duration: 1000,
//                             easing: 'out'},
//                 title : 'Average Hourlyddd Occupancy for B002',
//                 legend: {
//                     position: 'none'
//                 },
//                 width: '100%',
//                 chartArea:{left:20,top:10,right:10,width:'100%',height: '80%'},
//                 curveType: 'function',
//                 colors: ['#084C55'],
//                 bar: {
//                     gap: 10
//                 },
//                 gridlines: {
//                     color: 'black'
//                 },
//                 vAxis: {
//                     gridlines: {
//                         color: 'white'
//                     },
//                     title: 'Average Occupancy',
//                     textPosition: 'none'
//                 },
//                 hAxis: {
//                     textStyle : {
//                         fontSize: 10
//                     },
//                     slantedText: true,
//                     slantedTextAngle: 45
//                 }
//             };

//     function resize(){
//         var chart = new google.visualization.ColumnChart(document.getElementById("hourlyChart"));
//             chart.draw(data, options);
//     }
//      window.onload = resize();
//        window.onresize = resize;
// }

// google.charts.setOnLoadCallback(checkInput);

function createChart(){
var ctx = document.getElementById("myChart");
var myChart = new Chart(ctx, {
    type: 'line',
    lineTension: 0.1,
    bezierCurve: false,
    data: {
        labels: ["Red", "Blue", "Yellow", "Green", "Purple", "Orange"],
        datasets: [{
            fill: false,
            label: '# of Votes',
            data: [12, 19, 3, 5, 2, 3],
            backgroundColor:
                'rgba(255, 99, 132, 0.2)'
            ,
            borderColor: [
                'rgba(255,99,132,1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(255, 159, 64, 1)'
            ],
            borderWidth: 1
        }]
    },
    options: {
        title: {
            display: true,
            text: hi
        },
        legend: {
            display: false
        }
        
    }
});


}
var hi="hithere";

createChart();