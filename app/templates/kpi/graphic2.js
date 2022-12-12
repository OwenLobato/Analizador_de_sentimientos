var ctx1 = document.getElementById("myChart1").getContext("2d");
var ctx2 = document.getElementById("myChart2").getContext("2d");

var ctx3 = document.getElementById("myChart3").getContext("2d");
var ctx4 = document.getElementById("myChart4").getContext("2d");
var ctx5 = document.getElementById("myChart5").getContext("2d");
var ctx6 = document.getElementById("myChart6").getContext("2d");

/*******************************para las fechas*********************************************/

/*******************************Grafica 1*********************************************************************** */
var myChart= new Chart(ctx1,{
    type: "pie",
    data:{
        labels:['Volumen total año 2021','Volumen total año 2022'],
        datasets:[{
            label:'Num datos',
            data:[1,23,4],
            backgroundColor:[
                'rgb(66, 134, 244,0.5)',
                'rgb(74, 135, 72,0.5)',
    
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

/*******************************Grafica 1*********************************************************************** */
var myChart2= new Chart(ctx2,{
    type: "pie",
    data:{
        labels:['Volumen total año 2021','Volumen total año 2022'],
        datasets:[{
            label:'Num datos',
            data:[1,23,4],
            backgroundColor:[
                'rgb(66, 134, 244,0.5)',
                'rgb(74, 135, 72,0.5)',
    
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

/*******************************Grafica 1*********************************************************************** */
var myChart3= new Chart(ctx3,{
    type: "pie",
    data:{
        labels:['Volumen total año 2021','Volumen total año 2022'],
        datasets:[{
            label:'Num datos',
            data:[1,23,4],
            backgroundColor:[
                'rgb(66, 134, 244,0.5)',
                'rgb(74, 135, 72,0.5)',
    
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

/*******************************Grafica 1*********************************************************************** */
var myChart4= new Chart(ctx4,{
    type: "pie",
    data:{
        labels:['Volumen total año 2021','Volumen total año 2022'],
        datasets:[{
            label:'Num datos',
            data:[1,23,4],
            backgroundColor:[
                'rgb(66, 134, 244,0.5)',
                'rgb(74, 135, 72,0.5)',
    
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

/*******************************Grafica 1*********************************************************************** */
var myChart5= new Chart(ctx5,{
    type: "pie",
    data:{
        labels:['Volumen total año 2021','Volumen total año 2022'],
        datasets:[{
            label:'Num datos',
            data:[1,23,4],
            backgroundColor:[
                'rgb(66, 134, 244,0.5)',
                'rgb(74, 135, 72,0.5)',
    
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

/*******************************Grafica 1*********************************************************************** */
var myChart6= new Chart(ctx6,{
    type: "pie",
    data:{
        labels:['Volumen total año 2021','Volumen total año 2022'],
        datasets:[{
            label:'Num datos',
            data:[1,23,4],
            backgroundColor:[
                'rgb(66, 134, 244,0.5)',
                'rgb(74, 135, 72,0.5)',
    
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
