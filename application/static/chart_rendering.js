
//Lists of strings used for yAxis labels
var timeList_short = ["09:00", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00"];
var timeList_long = ["09:00", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00, 17:00"];
var dayList = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"];

//Declaring the charts as variables before creation for the sake of destroying them
//Updating the content might be a better option
var AverageHourlyChart = null;
var fiveCategoryChart = null;
var threeCategoryChart = null;
var frequencyOfUseChart = null;

function createHourlyAverageChart(hourly_averages){
    //Get our data
    hourly_data = []
    for (var i = 0; i < hourly_averages.length; i++){
        hourly_data.push(hourly_averages[i].occupancy_category_5);
    }

    var ctx = document.getElementById("dailyAverageChart");
    averageHourlyChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: timeList_long,
            datasets: [{
                fill: true,
                label: '# of Devices',
                data: hourly_data,
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
                        min: 0,
                        max: 1
                    }
                }]
            },
            maintainAspectRatio: false,
            responsive: true,
            title: {
                fontSize: 10,
                fontFamily: "'Helvetica Neue', 'Helvetica', 'Arial', sans-serif",
                display: false,
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

    frequencyOfUseChart = new Chart(ctz, {
        type: 'pie',
        data: data,
        options:{
            title: {
                fontSize: 15,
                fontFamily: "'Helvetica Neue', 'Helvetica', 'Arial', sans-serif",
                display: false,
                text: "Frequency of Use"
            },
            rotation: 45,
            maintainAspectRatio: false,
            responsive: true,
            legend:{
                display: true,
                position: "top",
                labels:{
                    padding: 5,
                    boxWidth: 20

                }
            }
        }
    });
}


function drawPredictedValueCharts(predictedValues){
    var dataLength = Object.keys(predictedValues).length;
    var occupancy_data = [];
    var predicted_data_5_cat = [];
    var associated_devices = [];
    var predicted_data_3_cat = [];

    for (i = 0; i < dataLength; i++){
        occupancy_data.push(predictedValues[i].occupancy);
        predicted_data_5_cat.push(predictedValues[i].occupancy_category_5);
        associated_devices.push(predictedValues[i].assoc_devices);
        predicted_data_3_cat.push(predictedValues[i].occupancy_category_3);
    }
    associated_devices = convertToPercentage(associated_devices, predictedValues[0].capacity);
    drawFiveCateogryChart(occupancy_data, predicted_data_5_cat, associated_devices);
    drawThreeCategoryChart(predicted_data_3_cat);
}

function drawFiveCateogryChart(occupancy_data, predicted_data, associated_devices){
    var ctx = document.getElementById("predictedHourly-5-cat");    
    console.log(associated_devices);

    if(window.fiveCategoryChart !== null){
        window.fiveCategoryChart.destroy();
        console.log("destroyed");
    }

    fiveCategoryChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: timeList_short,
            datasets: [{
                fill: true,
                label: 'Actual Occupancy',
                data: occupancy_data,
                backgroundColor: 
                'rgba(255, 99, 132, 0.2)',
                borderColor:'rgba(255,99,132,1)',
                borderWidth: 1
            },
            {
                fill: true,
                label: 'Predicted Devices',
                data: predicted_data,
                backgroundColor:
                'rgba(100, 230, 184, 0.2)',
                borderColor:"rgba(100, 230, 184, 0.2)",
                borderWidth: 1
            },

            {
                fill: false,
                label: 'Associated Devices',
                data: associated_devices,
                backgroundColor:
                "rgba(51, 133, 255, 0.2)",
                borderColor:"#3385ff",
                borderWidth: 1}]
            },
            options: {

                scales: {
                    yAxes: [{
                        scaleLabel:{
                        //used for y axis title
                    },
                    ticks: {
                        min: 0
                    }
                }]
            },
            elements:{
                line:{
                    tension: 0
                }
            },
            
            maintainAspectRatio: false,
            responsive: true,
            title: {
                fontSize: 15,
                fontFamily: "'Helvetica Neue', 'Helvetica', 'Arial', sans-serif",
                display: false,
                text: "5-Category Occupancy Stastics"
            },
            legend: {
                display: true
            }

        }
    });
    
}

function drawThreeCategoryChart(predicted_data_3_cat){

    var options = {
        maintainAspectRatio: false,
        responsive: true,
        elements:{
            line:{
                tension: 0
            }
        },
        scales: {
            yAxes: [
            {
              ticks: {
               callback: function(label, index, labels) {
                if (label == 1){
                    return "Full";
                }
                else if (label == 0.5){
                    return "Occupied";
                }
                else{
                 return "Empty";
                }
                },
                min: "0",
                max: "1",
                fixedStepSize: 0.5
         },
    }]
}
}
var ctx = document.getElementById("predictedHourly-3-cat");
if(window.threeCategoryChart !== null){
    window.threeCategoryChart.destroy();
    console.log("got to three");
}

threeCategoryChart = new Chart(ctx, {
    type: 'line',
    data: {
        labels: timeList_short,
        datasets: [{
            fill: true,
            label: 'Actual Occupancy',
            data: predicted_data_3_cat,
            backgroundColor:
            'rgba(255, 99, 132, 0.2)',
            borderColor:'rgba(255,99,132,1)',
            borderWidth: 1}]
        },

        options
    });


}

function destroyCharts(){
    if(window.fiveCategoryChart !== null){
        window.fiveCategoryChart.destroy();
    }
    if(window.threeCategoryChart !== null){
        window.threeCategoryChart.destroy()
    }
    if(window.dailyAverageChart !== null){
        window.dailyAverageChart.destroy()
    }
    if(window.frequencyOfUseChart !== null){
        window.frequencyOfUseChart.destroy()
    }
}   