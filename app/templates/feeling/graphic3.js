var ctx = document.getElementById("myChart1").getContext("2d");
var ctx2 = document.getElementById("myChart2").getContext("2d");
var ctx3 = document.getElementById("myChart3").getContext("2d");
var ctx4 = document.getElementById("myChart4").getContext("2d");
var ctx5 = document.getElementById("myChart5").getContext("2d");
var ctx6 = document.getElementById("myChart6").getContext("2d");
var ctx7 = document.getElementById("myChart7").getContext("2d");
var ctx8 = document.getElementById("myChart8").getContext("2d");
var ctx9 = document.getElementById("myChart9").getContext("2d");
var ctx10 = document.getElementById("myChart10").getContext("2d");
var ctx11 = document.getElementById("myChart11").getContext("2d");
var ctx12 = document.getElementById("myChart12").getContext("2d");
var ctx13 = document.getElementById("myChart13").getContext("2d");


let sentimientos01 = [];
let sentimientos02 = [];
let sentimientos03 = [];
let sentimientos04 = [];
let sentimientos05 = [];
let sentimientos06 = [];
let sentimientos07 = [];
let sentimientos08 = [];
let sentimientos09 = [];
let sentimientos10 = [];
let sentimientos11 = [];
let sentimientos12 = [];


let genero_h=[];
let genero_m=[];
let genero_e=[];

let res=[];
let res2=[];
let res3=[];


var repetidos={};
var repetidos2={};
var repetidos3={};


let feeling = [];
let meses= [];

positivo="Positivo";
negativo="Negativo";
neutro="Neutro";

num_positivo=0;
num_negativo=0;
num_neutro=0;


var year="";
let valida_mes="0";
let clase_sentimiento = $(".sentimiento");
let gen = $(".genero");

gen.map((id,genero) =>{

    let tipo_genero=$(genero).attr("hym")
    
    if(tipo_genero=="H"){
        genero_h.push(tipo_genero);
    }else if(tipo_genero=="M"){
        genero_m.push(tipo_genero);
    }else if(tipo_genero=="E"){
        genero_e.push(tipo_genero);
    }
});

 genero_h.forEach(function(numero){
    repetidos[numero] = (repetidos[numero] || 0) + 1;
});

genero_m.forEach(function(numero){
    repetidos2[numero] = (repetidos2[numero] || 0) + 1;
});

genero_e.forEach(function(numero){
    repetidos3[numero] = (repetidos3[numero] || 0) + 1;
});

 res1=Object.values(repetidos) //array que recibe objeto con horas y las veces que se repiten
 res2=Object.values(repetidos2)
 res3=Object.values(repetidos3)


clase_sentimiento.map((id,sentimiento) =>{
    let valor=$(sentimiento).attr("valor")
    let mes = $(sentimiento).attr("fecha").split("-")[1];

   if(valor!=""){
        feeling.push(valor.trim())
        meses.push(mes)
   }
});


for(i=0;i< feeling.length;i++){
    switch(meses[i]) {
        case "01":
            sentimientos01.push(feeling[i])
          break;
         case "02":
                sentimientos02.push(feeling[i])
            break;
          case "03":
                sentimientos03.push(feeling[i])
                break;
            case "04":
                sentimientos04.push(feeling[i])
                break;
            case "05":
                sentimientos05.push(feeling[i])
                break; 
            case "06":
                sentimientos06.push(feeling[i])
                break;
            case "07":
               sentimientos07.push(feeling[i])
            break;
            case "08":
                sentimientos08.push(feeling[i])
            break;
            case "09":
                 sentimientos09.push(feeling[i])
            break;
            case "10":
                  sentimientos10.push(feeling[i])
            break;
            case "11":
                  sentimientos11.push(feeling[i])
            break;
            case "12":
                   sentimientos12.push(feeling[i]);
            break;
        default:
      }
}


console.log(sentimientos04)

/*******************************para las sentimientos*********************************************/

/*******************************Grafica 1*********************************************************************** */
for(i=0;i<sentimientos01.length;i++){
    if(sentimientos01[i]==positivo){
        num_negativo=num_negativo+1;
    }else if(sentimientos01[i]==negativo){
        num_positivo=num_positivo+1;
    }else if(sentimientos01[i]==neutro){
        num_neutro=num_neutro+1;
    } 
    
}
console.log(num_positivo)
var myChart= new Chart(ctx,{
    type: "pie",
    data:{
        labels:["Negativo","Positivo","Neutro"],
        datasets:[{
            label:'Num datos',
            data:[num_negativo,num_positivo,num_neutro],
            backgroundColor:[
                'rgb(122, 151, 44)',
                'rgb(78, 151, 44)',
                'rgb(44, 151, 58)',
    
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

/*******************************Grafica 2*********************************************************************** */
num_positivo=0;
num_negativo=0;
num_neutro=0;

for(i=0;i<sentimientos02.length;i++){
    if(sentimientos02[i]==positivo){
        num_negativo=num_negativo+1;
    }else if(sentimientos02[i]==negativo){
        num_positivo=num_positivo+1;
    }else if(sentimientos02[i]==neutro){
        num_neutro=num_neutro+1;
    } 
    
}
var myChart2= new Chart(ctx2,{
    type: "pie",
    data:{
        labels:["Negativo","Positivo","Neutro"],
        datasets:[{
            label:'Num datos',
            data:[num_negativo,num_positivo,num_neutro],
            backgroundColor:[
                'rgb(44, 151, 97)',
                'rgb(44, 151, 137)',
                'rgb(44, 130, 151)',
    
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


/*******************************Grafica 3*********************************************************************** */
num_positivo=0;
num_negativo=0;
num_neutro=0;
for(i=0;i<sentimientos03.length;i++){
    if(sentimientos03[i]==positivo){
        num_negativo=num_negativo+1;
    }else if(sentimientos03[i]==negativo){
        num_positivo=num_positivo+1;
    }else if(sentimientos03[i]==neutro){
        num_neutro=num_neutro+1;
    } 
    
}
var myChart3 = new Chart(ctx3,{
    type: "pie",
    data:{
        labels:["Negativo","Positivo","Neutro"],
        datasets:[{
            label:'Num datos',
            data:[num_negativo,num_positivo,num_neutro],
            backgroundColor:[
                'rgb(151, 51, 44)',
                'rgb(151, 83, 44)',
                'rgb(151, 131, 44)',
    
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

/*******************************Grafica 4*********************************************************************** */
num_positivo=0;
num_negativo=0;
num_neutro=0;
for(i=0;i<sentimientos04.length;i++){
    if(sentimientos04[i]==positivo){
        num_negativo=num_negativo+1;
    }else if(sentimientos04[i]==negativo){
        num_positivo=num_positivo+1;
    }else if(sentimientos04[i]==neutro){
        num_neutro=num_neutro+1;
    } 
    
}

var myChart4= new Chart(ctx4,{
    type: "pie",
    data:{
        labels:["Negativo","Positivo","Neutro"],
        datasets:[{
            label:'Num datos',
            data:[num_positivo,num_negativo,num_neutro],
            backgroundColor:[
                'rgb(44, 94, 151)',
                 'rgb(55, 44, 151)',
                 'rgb(99, 44, 151)',
    
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

/*******************************Grafica 5*********************************************************************** */
num_positivo=0;
num_negativo=0;
num_neutro=0;
for(i=0;i<sentimientos05.length;i++){
    if(sentimientos05[i]==positivo){
        num_negativo=num_negativo+1;
    }else if(sentimientos05[i]==negativo){
        num_positivo=num_positivo+1;
    }else if(sentimientos05[i]==neutro){
        num_neutro=num_neutro+1;
    } 
    
}
var myChart5= new Chart(ctx5,{
    type: "pie",
    data:{
        labels:["Negativo","Positivo","Neutro"],
        datasets:[{
            label:'Num datos',
            data:[num_negativo,num_positivo,num_neutro],
            backgroundColor:[
                'rgb(138, 44, 151)',
                'rgb(151, 44, 133)',
                'rgb(151, 44, 89)',
    
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

/*******************************Grafica 6*********************************************************************** */
num_positivo=0;
num_negativo=0;
num_neutro=0;
for(i=0;i<sentimientos06.length;i++){
    if(sentimientos06[i]==positivo){
        num_negativo=num_negativo+1;
    }else if(sentimientos06[i]==negativo){
        num_positivo=num_positivo+1;
    }else if(sentimientos06[i]==neutro){
        num_neutro=num_neutro+1;
    } 
    
}
var myChart6= new Chart(ctx6,{
    type: "pie",
    data:{
        labels:["Negativo","Positivo","Neutro"],
        datasets:[{
            label:'Num datos',
            data:[num_negativo,num_positivo,num_neutro],
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


/*******************************Grafica 7*********************************************************************** */
for(i=0;i<sentimientos07.length;i++){
    if(sentimientos07[i]==positivo){
        num_negativo=num_negativo+1;
    }else if(sentimientos07[i]==negativo){
        num_positivo=num_positivo+1;
    }else if(sentimientos07[i]==neutro){
        num_neutro=num_neutro+1;
    } 
    
}
var myChart7= new Chart(ctx7,{
    type: "pie",
    data:{
        labels:["Negativo","Positivo","Neutro"],
        datasets:[{
            label:'Num datos',
            data:[num_negativo,num_positivo,num_neutro],
            backgroundColor:[
                'rgb(44, 151, 97)',
                'rgb(44, 151, 137)',
                'rgb(44, 130, 151)',
    
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

/*******************************Grafica 8*********************************************************************** */
for(i=0;i<sentimientos08.length;i++){
    if(sentimientos08[i]==positivo){
        num_negativo=num_negativo+1;
    }else if(sentimientos08[i]==negativo){
        num_positivo=num_positivo+1;
    }else if(sentimientos08[i]==neutro){
        num_neutro=num_neutro+1;
    } 
    
}
var myChart8= new Chart(ctx8,{
    type: "pie",
    data:{
        labels:["Negativo","Positivo","Neutro"],
        datasets:[{
            label:'Num datos',
            data:[num_negativo,num_positivo,num_neutro],
            backgroundColor:[
                'rgb(44, 151, 58)',
                'rgb(44, 151, 97)',
                'rgb(44, 151, 137)',
    
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

/*******************************Grafica 9*********************************************************************** */
for(i=0;i<sentimientos09.length;i++){
    if(sentimientos09[i]==positivo){
        num_negativo=num_negativo+1;
    }else if(sentimientos09[i]==negativo){
        num_positivo=num_positivo+1;
    }else if(sentimientos09[i]==neutro){
        num_neutro=num_neutro+1;
    } 
    
}
var myChart9 = new Chart(ctx9,{
    type: "pie",
    data:{
        labels:["Negativo","Positivo","Neutro"],
        datasets:[{
            label:'Num datos',
            data:[num_negativo,num_positivo,num_neutro],
            backgroundColor:[
                'rgb(44, 94, 151)',
                'rgb(99, 44, 151)',
                'rgb(151, 83, 44)',
    
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

/*******************************Grafica 10*********************************************************************** */
for(i=0;i<sentimientos10.length;i++){
    if(sentimientos10[i]==positivo){
        num_negativo=num_negativo+1;
    }else if(sentimientos10[i]==negativo){
        num_positivo=num_positivo+1;
    }else if(sentimientos10[i]==neutro){
        num_neutro=num_neutro+1;
    } 
    
}
var myChart10= new Chart(ctx10,{
    type: "pie",
    data:{
        labels:["Negativo","Positivo","Neutro"],
        datasets:[{
            label:'Num datos',
            data:[num_negativo,num_positivo,num_neutro],
            backgroundColor:[

                'rgb(78, 151, 44)',
                'rgb(151, 44, 44)',
                'rgb(99, 44, 151)',

    
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

/*******************************Grafica 11*********************************************************************** */
for(i=0;i<sentimientos11.length;i++){
    if(sentimientos11[i]==positivo){
        num_negativo=num_negativo+1;
    }else if(sentimientos11[i]==negativo){
        num_positivo=num_positivo+1;
    }else if(sentimientos11[i]==neutro){
        num_neutro=num_neutro+1;
    } 
    
}
var myChart11 = new Chart(ctx11,{
    type: "pie",
    data:{
        labels:["Negativo","Positivo","Neutro"],
        datasets:[{
            label:'Num datos',
            data:[num_negativo,num_positivo,num_neutro],
            backgroundColor:[
                'rgb(78, 151, 44)',
                'rgb(138, 44, 151)',
                'rgb(151, 44, 133)',

    
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

/*******************************Grafica 12*********************************************************************** */
for(i=0;i<sentimientos12.length;i++){
    if(sentimientos12[i]==positivo){
        num_negativo=num_negativo+1;
    }else if(sentimientos12[i]==negativo){
        num_positivo=num_positivo+1;
    }else if(sentimientos12[i]==neutro){
        num_neutro=num_neutro+1;
    } 
    
}
var myChart12= new Chart(ctx12,{
    type: "pie",
    data:{
        labels:["Negativo","Positivo","Neutro"],
        datasets:[{
            label:'Num datos',
            data:[num_negativo,num_positivo,num_neutro],
            backgroundColor:[
                'rgb(78, 151, 44)',
                'rgb(151, 44, 89)',
                'rgb(44, 94, 151)',
    
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


/*******************************Grafica 13*********************************************************************** */


var myChart13= new Chart(ctx13,{
    type: "pie",
    data:{
        labels:["Hombres","Mujeres","Empresas"],
        datasets:[{
            label:'Num datos',
            data:[res1,res2,res3],
            backgroundColor:[
                'rgb(78, 151, 44)',
                'rgb(151, 44, 89)',
                'rgb(44, 94, 151)',
    
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