let msg = ""
let msg2=""
let empezar="no"
let respuesta=""
var $messages = $('.messages-content'),
    d, h, m,
    i = 0;

$(window).load(function() {
  $messages.mCustomScrollbar();
  setTimeout(function() {
    /*  fakeMessage(); */
    respuesta = "Hola soy Eduardo.  Si no sabes que preguntarme, escribe ayuda"
    escribir()
    
  }, 100);
});

function updateScrollbar() {
  $messages.mCustomScrollbar("update").mCustomScrollbar('scrollTo', 'bottom', {
    scrollInertia: 10,
    timeout: 0
  });
  $('.message-input').focus();
}

function setDate(){
  d = new Date()
  if (m != d.getMinutes()) {
    m = d.getMinutes();
    $('<div class="timestamp">' + d.getHours() + ':' + m + '</div>').appendTo($('.message:last'));
  }
}

function insertMessage() {
  msg = $('.message-input').val();
  if ($.trim(msg) == '') {
    return false;
  }
  $('<div class="message message-personal">' + msg + '</div>').appendTo($('.mCSB_container')).addClass('new');
  setDate();
  $('.message-input').val(null);
  updateScrollbar();
  setTimeout(function() {
    fakeMessage();
  }, 100 + (Math.random() * 20) * 100);
  $('.message-input').focus();
}

$('.message-submit').click(function() {
  insertMessage();
});

$(window).on('keydown', function(e) {
  if (e.which == 13) {
    insertMessage();
    return false;
  }
})


function fakeMessage() {
  if ($('.message-input').val() != '') {
    return false;
  }
  if (msg != "") {
    msg2=msg
    empezar="si"
    cargando();
    escribir();
     
  }
  
  
 
}
function escribir(){
 
 
  setTimeout(function () {
   
    $('.message.loading').remove();
     if (respuesta == '') {
       respuesta = 'error timeout de servidor.wait a moment';
       server.preguntar()
       
     }
    $('<div class="message new"><figure class="avatar"><img src="../static/images/foto-chatbot-edu.png" /></figure>' + respuesta + '</div>').appendTo($('.mCSB_container')).addClass('new');
    setDate();
    updateScrollbar();
     
   
    
    
  }, 1000 + (Math.random() * 20) * 100);
  if (respuesta == 'error timeout de servidor.wait a moment') {
       respuesta = 'error timeout de servidor.wait a moment';
       server.preguntar();
       escribir()
     }
    respuesta=""
}
function cargando() {
   $('<div class="message loading new"><figure class="avatar"><img src="../static/images/foto-chatbot-edu.png" /></figure><span></span></div>').appendTo($('.mCSB_container'));
   updateScrollbar();
}

function larespuesta(mirespuesta){
  respuesta=mirespuesta
}


function resolver(asunto) {
  $('.message-input').val(asunto)
  msg=asunto
  insertMessage();
}