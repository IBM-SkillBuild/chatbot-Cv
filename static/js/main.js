let mensajePython=""

function hacer(botonPulsado){
    mensajePython=" se ha pulsado el boton "+ botonPulsado
    if (botonPulsado=="boton1"){
        document.getElementById('info2').style.color="red"
    }else{
        document.getElementById('info2').style.color="blue"
    }
}



function onclickhandler(e) {
    server.cambiar(e.value)
  }