var ctx1 = document.getElementById("myChart1").getContext("2d");
var ctx2 = document.getElementById("myChart2").getContext("2d");
var ctx3 = document.getElementById("myChart3").getContext("2d");
var ctx4 = document.getElementById("myChart4").getContext("2d");
var ctx5 = document.getElementById("myChart5").getContext("2d");
var ctx6 = document.getElementById("myChart6").getContext("2d");

/* --------------- KPIS VALUES ---------------  */
let growth_rate = $(".growth_rate").text();
let post_reach = $(".post_reach").text();
let applause_rate = $(".applause_rate").text();
let avg_engagement_rate = $(".avg_engagement_rate").text();
let amplification_rate = $(".amplification_rate").text();
let comment_conversation_rate = $(".comment_conversation_rate").text();

console.log(growth_rate);
console.log(post_reach);
console.log(applause_rate);
console.log(avg_engagement_rate);
console.log(amplification_rate);
console.log(comment_conversation_rate);

/*******************************para las fechas*********************************************/

/*******************************Grafica 1*********************************************************************** */
var myChart= new Chart(ctx1,{
    type: "pie",
    data:{
        labels:['Porcentaje'],
        datasets:[{
            label:'Num datos',
            data:[growth_rate,(100-growth_rate)],
            backgroundColor:[
                'rgb(66, 134, 244,0.5)'
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
        labels:['Porcentaje'],
        datasets:[{
            label:'Num datos',
            data:[post_reach,(100-post_reach)],
            backgroundColor:[
                'rgb(66, 134, 244,0.5)'
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
        labels:['Porcentaje'],
        datasets:[{
            label:'Num datos',
            data:[applause_rate,(100-applause_rate)],
            backgroundColor:[
                'rgb(66, 134, 244,0.5)'
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
        labels:['Porcentaje'],
        datasets:[{
            label:'Num datos',
            data:[avg_engagement_rate,(100-avg_engagement_rate)],
            backgroundColor:[
                'rgb(66, 134, 244,0.5)'
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
        labels:['Porcentaje'],
        datasets:[{
            label:'Num datos',
            data:[amplification_rate,(100-amplification_rate)],
            backgroundColor:[
                'rgb(66, 134, 244,0.5)'
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
        labels:['Porcentaje'],
        datasets:[{
            label:'Num datos',
            data:[comment_conversation_rate,(100-comment_conversation_rate)],
            backgroundColor:[
                'rgb(66, 134, 244,0.5)'
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
