var ctx = document.getElementById("myChart1").getContext("2d");
var ctx2 = document.getElementById("myChart").getContext("2d");
var ctx3 = document.getElementById("myChart3").getContext("2d");
var ctx4 = document.getElementById("myChart4").getContext("2d");

let fechas = $(".fecha")
let horas = $(".tiempo")
/*******************************para las fechas*********************************************/
let fechas01 = [];
let fechas02 = [];
let fechas03 = [];
let fechas04 = [];
let fechas05 = [];
let fechas06 = [];
let fechas07 = [];
let fechas08 = [];
let fechas09 = [];
let fechas10 = [];
let fechas11 = [];
let fechas12 = [];

let fechas012 = [];
let fechas022 = [];
let fechas032 = [];
let fechas042 = [];
let fechas052 = [];
let fechas062 = [];
let fechas072 = [];
let fechas082 = [];
let fechas092 = [];
let fechas102 = [];
let fechas112 = [];
let fechas122 = [];

let lengthEN =0;
let lengthFE=0;
let lengthMAR=0;
let lengthA=0;
let lengthMAY=0;
let lengthJ=0;
let lengthJUL=0;
let lengthAG=0;
let lengthSE=0;
let lengthOC=0;
let lengthNOV=0;
let lengtDIC=0;

let lengthEN2 =0;
let lengthFE2=0;
let lengthMAR2=0;
let lengthA2=0;
let lengthMAY2=0;
let lengthJ2=0;
let lengthJUL2=0;
let lengthAG2=0;
let lengthSE2=0;
let lengthOC2=0;
let lengthNOV2=0;
let lengtDIC2=0;

let año2022 = 0;
let año2021 = 0;

let arr_22=[];
let arr_result=[];

let arr_year22=[];
let arr_year21=[];
let arr_year=[];



let año=""; 
let valor_year ="2021";
let valor_year2 ="2022";

fechas.map((id, fecha) =>{
   //console.log($(fecha).attr("fecha"))
    let mes = $(fecha).attr("fecha").split("-")[1];
    let año =$(fecha).attr("fecha").split("-")[0];
    arr_year.push(año);

     if (año == valor_year) {
        arr_year21.push(año);
    } 
       
    if (año == valor_year2) {
        arr_year22.push(año);
    } 


    //console.log(año+" "+mes)
    if (año == valor_year && mes == '01') {
        fechas01.push(mes)
        lengthEN  = fechas01.length;
    } 

    if (año == valor_year && mes == '02') {
        fechas02.push(mes)
        lengthFE  = fechas02.length;
    }    
     if (año == valor_year && mes == '03') {
        fechas03.push(mes)
        lengthMAR  = fechas03.length;
    }

    if (año == valor_year && mes == '04') {
        fechas04.push(mes)
        lengthA = fechas04.length;
    }
    
    if (año == valor_year && mes == '05') {
        fechas06.push(mes)
        lengthMAY = fechas05.length;
    }

    if (año == valor_year && mes == '06') {
        fechas06.push(mes)
        lengthJ = fechas06.length;
    }

    if (año == valor_year && mes == '07') {
        fechas07.push(mes)
        lengthJUL = fechas07.length;
    }
    if (año == valor_year && mes == '08') {
        fechas08.push(mes)
        lengthAG = fechas08.length;
    }
    if (año == valor_year && mes == '09') {
        fechas09.push(mes)
        lengthSE = fechas09.length;
    }

    if (año == valor_year && mes == '10') {
        fechas10.push(mes)
        lengthOC = fechas10.length;
    }

    if (año == valor_year && mes == '11') {
        fechas11.push(mes)
        lengthNOV = fechas11.length;
    }

    if (año == valor_year && mes == '12') {
        fechas12.push(mes)
        lengthDIC= fechas12.length;
    }

//******************************************************** */
    if (año == valor_year && mes == '01') {
        fechas012.push(mes)
        lengthEN2  = fechas012.length;
    } 

    if (año == valor_year && mes == '02') {
        fechas022.push(mes)
        lengthFE2  = fechas022.length;
    }    
     if (año == valor_year && mes == '03') {
        fechas032.push(mes)
        lengthMAR2  = fechas032.length;
    }

    if (año == valor_year && mes == '04') {
        fechas042.push(mes)
        lengthA2 = fechas042.length;
    }
    
    if (año == valor_year && mes == '05') {
        fechas052.push(mes)
        lengthMAY2 = fechas052.length;
    }

    if (año == valor_year && mes == '06') {
        fechas062.push(mes)
        lengthJ2 = fechas062.length;
    }

    if (año == valor_year && mes == '07') {
        fechas072.push(mes)
        lengthJUL2 = fechas072.length;
    }
    if (año == valor_year && mes == '08') {
        fechas082.push(mes)
        lengthAG2 = fechas082.length;
    }
    if (año == valor_year && mes == '09') {
        fechas092.push(mes)
        lengthSE = fechas092.length;
    }

    if (año == valor_year && mes == '10') {
        fechas102.push(mes)
        lengthOC2 = fechas102.length;
    }

    if (año == valor_year && mes == '11') {
        fechas112.push(mes)
        lengthNOV2 = fechas112.length;
    }

    if (año == valor_year && mes == '12') {
        fechas122.push(mes)
        lengthDIC2 = fechas122.length;
    }


});

año2021+=lengthEN+lengthFE+lengthMAR+lengthA+lengthMAY+lengthJ+lengthJUL+lengthAG+lengthSE+lengthOC+lengthNOV+lengtDIC;
año2022+=lengthEN2+lengthFE2+lengthMAR2+lengthA2+lengthMAY2+lengthJ2+lengthJUL2+lengthAG2+lengthSE2+lengthOC2+lengthNOV2+lengtDIC2;

/*******************************para las horas******************************************* */
let horasrep = [];
let res = []
let res2 = []
let sortable = [];
//posibles horas de publicacion
let horario = ["00","01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","21","22","23","24"]
let horas_usadas=[];
var repetidos = {};
var numero; 
//par asacar la hora
horas.map((id, tiempo) =>{
    hora = $(tiempo).attr("hora").split(":")[0];
    horasrep.push(hora);
});


//sca las horas repetidas 
horasrep.forEach(function(numero){
    repetidos[numero] = (repetidos[numero] || 0) + 1;
});

console.log(repetidos)
for (var hora in repetidos) {
    sortable.push([hora, repetidos[hora]]);
}
//ordena + a -
sortable.sort(function(a, b) {
    return a[1] - b[1];
});

sortable.reverse();
for(i=0;i<=10;i++){//se obtiene las primeras 10 publicadas de cada publicacion guardadas en res
horas_usadas.push(sortable[i][0]);
}

 //const resul = horasrep.reduce((prev, cur) => ((prev[cur] = prev[cur] + 1 || 1), prev), {})
 res=Object.values(repetidos) //array que recibe objeto con horas y las veces que se repiten

 //se ordena de + a -
function comparar(a,b){return a - b}
 res.sort(comparar);

 res.reverse();
 //se obtiene las primeras 10 horas repetidas de cada publicacion guardadas en res
 for(i=0;i<=10;i++){
    res2.push(res[i]);
 }

/*******************************CODIGO PARA LOS SHARES*********************************************/
let compartido = $(".compartido")

let compartidas=[]
let share_fecha21=[]
let share_fecha22=[]
let sum1=0;
let sum2=0;

compartido.map((id, compartido) =>{
    shares = $(compartido).attr("compartido");
    compartidas.push(shares);
});


//extrae los compartidos en 2021
for(i=0;i < arr_year.length;i++){

    if(arr_year[i] == "2021"){
        const parsed = Number.parseInt(compartidas[i], 10);
        share_fecha21.push(parsed);
        sum1+=parsed;
    }

    if(arr_year[i] == "2022"){
        const parsed = Number.parseInt(compartidas[i], 10);
        share_fecha22.push(parsed);
        sum2+=parsed;
    }
}
/*******************************Grafica 1*********************************************************************** */

var myChart2= new Chart(ctx2,{
    type:"line",
    data:{
        labels:['Enero','Febrero','Marzo',"abril","Mayo","Jun","Jul","Agosto","Sept","Oct","Nov","Dic"],
        datasets:[{
            label:'Volumen de Publicaciones del año 2021',
            data:[lengthEN,lengthFE,lengthMAR,lengthA,lengthMAY,lengthJ,lengthJUL,lengthAG,lengthSE,lengthOC,lengthNOV,lengtDIC],
            backgroundColor:[
                'rgba(66, 134, 244,0.3)',
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
/*******************************Grafica 2*********************************************************************** */
var myChart= new Chart(ctx,{
    type: "pie",
    data:{
        labels:['Volumen total año 2021','Volumen total año 2022'],
        datasets:[{
            label:'Num datos',
            data:[año2021,año2022],
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
/*******************************Grafica 3*********************************************************************** */
var myChart3= new Chart(ctx3,{ 
    type: "pie",
    data:{
        labels:horas_usadas,
        datasets:[{
            label:"",
            data:res2,
            backgroundColor:[
                 'rgb(78, 151, 44)',
                 'rgb(151, 83, 44)',
                 'rgb(151, 131, 44)',
                 'rgb(122, 151, 44)',
                 'rgb(78, 151, 44)',
                 'rgb(44, 151, 58)',
                 'rgb(44, 151, 97)',
                 'rgb(44, 151, 137)',
                 'rgb(44, 130, 151)',
                 'rgb(44, 94, 151)',
                 'rgb(55, 44, 151)',
                 'rgb(99, 44, 151)',
                 'rgb(138, 44, 151)',
                 'rgb(151, 44, 133)',
                 'rgb(151, 44, 89)',
                 'rgb(151, 44, 44)',
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
var xValues = ["Post Compartidos 2021","Post Compartidos 2022"]
var yValues = [sum1,sum2]
var barColors = ["green","blue"]

var myChart4= new Chart(ctx4,{ 
    type: "bar",
    data: {
      labels: xValues,
      datasets: [{
        backgroundColor: barColors,
        data: yValues
      }]
    },
    options: {
      legend: {display: false},
      title: {
        display: true,
        text: "AÑO MÁS VIRAL"
      }
    }
       

});
