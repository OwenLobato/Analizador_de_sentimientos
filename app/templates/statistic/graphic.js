let posts;
posts=$('#posts').val();

let cadena="2021-04-22";
function cuantasVecesAparece(cadena, posts){
    var indices = [];
    for(var i = 0; i < cadena.length; i++) {
      if (cadena[i].toLowerCase() === posts) indices.push(i);
    }
      return console.log(indices.length);
  }


var ctx = document.getElementById("myChart1").getContext("2d");
var ctx2 = document.getElementById("myChart").getContext("2d");
var ctx3 = document.getElementById("myChart3").getContext("2d");
var ctx4 = document.getElementById("myChart4").getContext("2d");


var myChart2= new Chart(ctx2,{
    type:"line",
    data:{
        labels:['col1','col2','col3',"col4"],
        datasets:[{
            label:'Num datos',
            label:'Num datos',
            data:[posts],
            backgroundColor:[
                'rgba(66, 134, 244,0.1)',
                'rgba(66, 13, 244,0.1)',
            ]
        }]
    },
    options:{
        scales:{
            yAxes:[{
                ticks:{
                    beginAtZero:true
                }
            }]
        }
    }
});

var myChart= new Chart(ctx,{
    type:"pie",
    data:{
        labels:['col1','col2','col3','tf'],
        datasets:[{
            label:'Num datos',
            data:[1,9,15,33],
            backgroundColor:[
                'rgb(66, 134, 244,0.5)',
                'rgb(74, 135, 72,0.5)',
                'rgb(229, 89, 50,0.5)'
            ]
        }]
    },
    optionss:{
        scales:{
            yAxes:[{
                ticks:{
                    beginAtZero:true
                }
            }]
        }
    }
});

const DATA_COUNT = 7;
const NUMBER_CFG = {count: DATA_COUNT, min: -100, max: 100};
const data = {
labels: ["enero","febrero","Marzo","abril","mayo"],
datasets: [{
    label: 'Dataset 1',
    data: [1,50,3,3,15] ,
    fill: false,
    borderColor:['rgb(74, 145, 72,0.5)'],
    backgroundColor:['rgb(74, 135, 72,0.5)'],
}]
};

var myChart3= new Chart(ctx3,{ 
    type: 'line',
    data: data,
    options: {
        plugins: {
            title: {
                display: true,
                text: 'Chart Title',
            },
            subtitle: {
                display: true,
                text: 'Chart Subtitle',
                color: 'blue',
                font: {
                    size: 12,
                    family: 'tahoma',
                    weight: 'normal',
                    style: 'italic'
                },
                padding: {
                    bottom: 10
                }
            }
        }
    }
});

const totalDuration = 10000;
const delayBetweenPoints = totalDuration / data.length;
const previousY = (ctx4) => ctx4.index === 0 ? ctx4.chart.scales.y.getPixelForValue(100) : ctx4.chart.getDatasetMeta(ctx4.datasetIndex).data[ctx4.index - 1].getProps(['y'], true).y;
const animation = {
x: {
    type: 'number',
    easing: 'linear',
    duration: delayBetweenPoints,
    from: NaN, // the point is initially skipped
    delay(ctx4) {
    if (ctx4.type !== 'data' || ctx4.xStarted) {
        return 0;
    }
    ctx4.xStarted = true;
    return ctx4.index * delayBetweenPoints;
    }
},
y: {
    type: 'number',
    easing: 'linear',
    duration: delayBetweenPoints,
    from: previousY,
    delay(ctx4) {
    if (ctx4.type !== 'data' || ctx4.yStarted) {
        return 0;
    }
    ctx4.yStarted = true;
    return ctx4.index * delayBetweenPoints;
    }
}
};

const data4 = [21,43,5,76,7];
const data2 = [50,4,3,76,7];
let prev = 100;
let prev2 = 80;

var myChart4= new Chart(ctx4,{
    type: 'line',
    data: {
        datasets: [{
            borderColor: '#cf041f',
            borderWidth: 1,
            radius: 0,
            data: data4,
        },{
            borderColor: '#2c6c97',
            borderWidth: 1,
            radius: 0,
            data: data2,
        }]
    },
    options: {
        animation,
        interaction: {
            intersect: false
        },
        plugins: {
            legend: false
        },
        scales: {
            x: {type: 'linear'}
        }
    }
});

