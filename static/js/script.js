

let map = L.map("mapid").setView([-23.531127, -46.635932], 13);
let osmUrl='https://cartodb-basemaps-{s}.global.ssl.fastly.net/light_all/{z}/{x}/{y}.png';

L.tileLayer(osmUrl).addTo(map);


function color_idade_serie(d){
    if (d>20){
        return "red"
    }
    if (d<20 && d>10){
        return "orange"
    }
    if (d<10 && d>5){
        return "green"
    }
    if (d<5){
        return "blue"
    }
}

function onCircleClick(e){

    document.getElementById("overlay").style.display = "block"

    let info = `<ul class="info-escola">
                <li> Nome da Escola: ${e.target.options.nome_escola}</li>
                <li> Código INEP: ${e.target.options.cod_inep}</li>
                <hr>
                <li class="subinfo-escola">Nota IDEB 2017 Fundamental 1
                <p class="indicador">${e.target.options.ideb_f1_2017}</p></li>
                <li class="subinfo-escola">Nota IDEB 2017 Fundamental 2
                <p class="indicador">${e.target.options.ideb_f2_2017}</p></li>
                <li class="subinfo-escola">Distorção Idade-Série do Ensino Fundamental
                <p class="indicador">${e.target.options.dist_idade_serie}</p></li>
                <li><p class="indicador-secund">${e.target.options.pior_desempenho}</p></li>
                </ul>`

    let overlay = document.getElementById("overlay")
    overlay.innerHTML = ""
    overlay.innerHTML = info
}

function getSchools(){
    $.getJSON("http://localhost:5000/escolas", function(data){
        let escolas = data["escolas"]
        
        escolas.forEach(function(d){
            let circle = L.circleMarker([d.LATITUDE, d.LONGITUDE], {
                stroke: true,
                color: "#fefeff",
                weight: 3,
                fill:true,
                fillColor:color_idade_serie(d.Total_EF),
                fillOpacity: 1,
                radius:7,
                nome_escola: d.NOMESC,
                cod_inep: d.CODINEP,
                ideb_f1_2017: d.IDEB_2017_EF1,
                ideb_f2_2017: d.IDEB_2017_EF2,
                dist_idade_serie: d.Total_EF,
                pior_desempenho: d.PIOR_DESEMP === 1 ? "Essa escola está entre as 100 piores do munícipio de São Paulo" : "",
            })
            circle.on("click", onCircleClick)
            circle.addTo(map)
        })
    })
}



function getDistricts(){
    
    function drawDistrict(data){
        let distritos = data["distritos"]
        distritos.forEach(function(d){
            let polygonCoordinates = d["geometry"]["coordinates"][0]
            L.polygon(polygonCoordinates).addTo(map)
        })
    }

    dataPromise = new Promise ((resolve, reject) =>{
        const response =  fetch("http://localhost:5000/distritos")
        dataResponse = response.then(res => res.json())
                                .then(data => resolve(data))
                                .catch(err => reject(err))       
                            
    });
    dataPromise.then(d => drawDistrict(d))
    console.log(map)
}

function get_selected_UDHs(valor_indicador){

    let var_quartiles = {
        "t_analf18m":[1.5, 3.3, 5.9],
        "t_fbbas": [98.6, 103.72, 109.88],
        "t_fbfund": [106.24, 110.82, 116.22],
        "t_fbmed": [68.09, 83.33, 98.43],
        "idhme":[0.62,0.70, 0.79]
    };


    function color_quartile(d, quartile_array){

        if (d<quartile_array[0]){
            return "#05A849"
        } else if (quartile_array[0]<d && d<quartile_array[1]){
            return "#FFEE01"
        }else if (quartile_array[1]<d && d<quartile_array[2]){
            return "#FF6207"
        } else if (quartile_array[2]<d){
            return "#FF0117"
        };
    };

    let quartiles = var_quartiles[valor_indicador];

    function draw_legend(){

        legend_element = document.getElementById("info-legend");
        legend_element.style.display = "block";
        legend_element.innerHTML = "";

        // var labels = [ `Menor que ${quartiles[0]}`,`Entre ${quartiles[0]} e ${quartiles[1]}`, `Entre ${quartiles[1]} e ${quartiles[2]}`, `Maior que ${quartiles[2]}`];
        for(var i=0; i <quartiles.length; i++){
                let color = color_quartile(quartiles[i]+0.001, quartiles)
                legend_element.innerHTML += `<div style="float:left"><svg witdh="40" height="40" style="float:left"> 
                                            <rect width='20' height='20' rx='5' ry='5' x='5' y='5' style="fill: ${color};float:left"/>
                                            </svg><p style=font-size:11px; float:left">Entre ${quartiles[i]} e ${quartiles[i+1]}</p>
                                             </div>` 
        }   
    }

    draw_legend();
    function drawUDH(data){

        map.eachLayer(function(layer){
            if ((layer._leaflet_id !== 26) || layer.hasOwnProperty("_bounds")){
                map.removeLayer(layer)
            }
        })

        let udh_group = new L.featureGroup();
        
        let udhs = data["udhs"]
        udhs.forEach(function(d){
            let polygonCoordinates = d["geometry"]["coordinates"][0]
            L.polygon(polygonCoordinates, {color:color_quartile(d[valor_indicador], quartiles), weight: .5}).addTo(udh_group)
        });
        map.addLayer(udh_group);
    }

    dataPromise = new Promise ((resolve, reject) =>{
        const response =  fetch("http://localhost:5000/udhs")
        dataResponse = response.then(res => res.json())
                                .then(data => resolve(data))
                                .catch(err => reject(err))                      
    });
    dataPromise.then(d => drawUDH(d));
    
}


function getUDHS(){

    document.getElementById("div-lista-indicadores").style.display = "block";

    document.addEventListener('DOMContentLoaded', function() {
        var elems = document.querySelectorAll('select');
        var instances = M.FormSelect.init(elems);
      });


      let lista = document.getElementById("lista-indicadores")
      lista.addEventListener("change", function(){
            let valor = lista.value
            get_selected_UDHs(valor)
      } )

}


function clearMap(){
    document.location.reload()
}



document.getElementById("escolas").addEventListener("click", getSchools)
document.getElementById("distritos").addEventListener("click", getDistricts)
document.getElementById("udhs").addEventListener("click", getUDHS)
document.getElementById("clear").addEventListener("click", clearMap)













