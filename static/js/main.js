let factor = '';
let accion = '';
window.addEventListener('DOMContentLoaded', (event) => {
  console.log('DOM fully loaded and parsed');
  history.pushState(null, null, location.href);
  history.back();
  history.forward();
  window.onpopstate = function () {
    history.go(1);
  };

  $('.panel-primero').on('show.bs.collapse', function () {
    $('#todo').show();
    $('#search').val('');
    $('#mensaje').text('Que quieres saber ?');
    var mipregunta = document.getElementById('search');
    setTimeout(function () {
      mipregunta.focus();
    }, 200);
  });

  
});

$('#collapseTwo').on('show.bs.collapse', function (e) {
  if ($('#mensaje2').text() == 'Te cuento como funciona esta app') {
    setTimeout(function () {
      var maq = document.getElementById('leer');
      var typewriter = new Typewriter(maq, {
        loop: false,
      });
      typewriter
        .typeString(
          'Se produce una iteración sobre un archivo Json. Hay una libreria que determina la respuesta más acertada basandose en un algoritmo que ofrece porcentajes de similitud basados en NLP. Procesamiento del lenguaje natural.',
        )
        .start();
    }, 1);
  }
});

$('#search').on('change keydown keyup paste input', function (e) {
  if ($('#search').val() == '') {
    $('#mensaje').text('Que quieres saber ?');
  } else {
    $('#mensaje').text('Ya te estoy escuchando');
  }

  if (e.which == 13) {
   
    if ($('#search').val() == '') {
      $('#mensaje').text('Debes rellenar una pregunta ?');
    } else {
      $('#botonbuscar').click();
    }

    
  }
});

$('#headingTwo').click(function () {
  $('#botonbuscar').click();
  setTimeout(function () {
    $('#search').val('');
  }, 1000);
 
});
  

$('#botonbuscar').click(function () {
  if ($('#search').val() != '') {
    server.hola();
    $('#collapseOne').collapse('hide');
    setTimeout(function () {
      $('#collapseTwo').collapse('show');
    }, 1000);

    setTimeout(function () {
      var maq = document.getElementById('leer');
      var respuesta = document.getElementById('datos');
      var typewriter = new Typewriter(maq, {
        loop: false,
        delay: 125,
      });
      typewriter.typeString(factor).start();
    }, 1000);
  }
   setTimeout(function () {
     if (accion.includes('ver boton cv')) {
       $('#micv').show();
     } else {
       $('#micv').hide();
     }
   }, 1000);
   setTimeout(function () {
     if (accion.includes('ver video')) {
       $('#vervideo').show();
     } else {
       $('#vervideo').hide();
     }
   }, 1000);
   setTimeout(function () {
     if (accion.includes('ver github')) {
       $('#github').show();
     } else {
       $('#github').hide();
     }
   }, 1000);
  
   setTimeout(function () {
     if (accion.includes('pdf')) {
       $('#micvpdf').show();
     } else {
       $('#micvpdf').hide();
     }
   }, 1000);
  setTimeout(function () {
    if (accion.includes('linkedin')) {
      $('#linkedin').show();
    } else {
      $('#linkedin').hide();
    }
  }, 1000);
   setTimeout(function () {
     if (accion.includes('flask')) {
       $('#verflask').show();
     } else {
       $('#verflask').hide();
     }
   }, 1000);
 
});

/*******************************
 * ACCORDION WITH TOGGLE ICONS
 *******************************/
function toggleIcon(e) {
  $(e.target)
    .prev('.panel-heading')
    .find('.more-less')
    .toggleClass('glyphicon-plus glyphicon-minus');
}
$('.panel-group').on('hidden.bs.collapse', toggleIcon);
$('.panel-group').on('shown.bs.collapse', toggleIcon);


$('#todaslaspreguntas').on('change', function () {
  $('#search').val(this.value)
  myModal.close();
   $('#botonbuscar').click();
});

function iralcv() {
  window.open('https://cv-eduardo.github.io/', '_blank');
}
function iralcvpdf() {
  window.open('https://cv-eduardo.github.io/docs/Eduardo%20Cabrera%20Bl%C3%A1zquez-cv-2023.pdf', '_blank');
}

function github() {
  window.open('https://github.com/Api-Nasa/React-Web', '_blank');
}
function vervideo() {
  window.open('https://mega.nz/file/droGRYiZ#d9t6EW_p2BrXfYGHmxwmeonKKxBX_82JqaF7p9yarbM','_blank');
}

function verlinkedin() {
  window.open('https://www.linkedin.com/in/e-cabrera-blazquez/', '_blank');
}

function verflask() {
  window.open('https://github.com/IBM-SkillBuild/flask-chatbot', '_blank');
}

$('#todo').click(function () {
 $('#collapseTwo').collapse('hide');
})