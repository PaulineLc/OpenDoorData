
//Lists of strings used for yAxis labels
var timeList = ["08:00", "09:00", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00", "17:00", "18:00", "19:00"];
var dayList = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"];


function createDailyAverageChart(dailyAvg){
    console.log(dailyAvg);
    var ctx = document.getElementById("myChart");
    var myChart = new Chart(ctx, {
        type: 'bar',
        lineTension: 0.1,
        bezierCurve: false,
        data: {
            labels: dayList,
            datasets: [{
                fill: true,
                label: '# of Devices',
                data: dailyAvg,
                backgroundColor:
                'rgba(255, 99, 132, 0.2)'
                ,
                borderColor:'rgba(255,99,132,1)',
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                yAxes: [{
                    scaleLabel:{
                        //used for y axis title
                    },
                    ticks: {
                        beginAtZero:true
                    }
                }]
            },
            maintainAspectRatio: false,
            responsive: true,
            title: {
                fontSize: 15,
                fontFamily: "'Helvetica Neue', 'Helvetica', 'Arial', sans-serif",
                display: true,
                text: "Daily Average Associated Devices"
            },
            legend: {
                display: false
            }

        }
    });
}

function doSomething(stuff){
    var ctz = document.getElementById("pChart");
    var data = {
    labels: [
        "In Use",
        "Unused"
    ],
    datasets: [
        {
            data: stuff,
            backgroundColor: ["#00ff99","rgba(255,99,132,1)"],
            hoverBackgroundColor: [
                "#FF6384",
                "#36A2EB"
            ]
        }]
};

    var myDoughnutChart = new Chart(ctz, {
    type: 'pie',
    data: data,
    options:{
        title: {
            fontSize: 15,
            fontFamily: "'Helvetica Neue', 'Helvetica', 'Arial', sans-serif",
            display: true,
            text: "Frequency of Use"
        },
        rotation: 45,
        maintainAspectRatio: false,
        responsive: true,
        legend:{
            display: true,
            position: "bottom",
            labels:{
                padding: 5,
                boxWidth: 20

            }
        }
    }
});


}