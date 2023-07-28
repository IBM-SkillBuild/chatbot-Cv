
##############################################################################
# sigle page flask "reactivo" interactuando con el Dom sin renderizar de nuevo
##############################################################################

import jyserver.Flask as js
from flask import Flask, render_template, request
import time
import os
import json
from fuzzywuzzy import fuzz
from rivescript import RiveScript
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
#load the JSON file
with open('myjson.json', 'r', encoding='utf-8') as f:
    chatbot_data = json.load(f)
bot=RiveScript()    
bot.load_file('eduardo.rivescript')
bot.sort_replies()

@js.use(app)
class App():
    # esta función se puede llamar desde js or html 
    def cambiar(self,valor):
         self.js.dom.info1.innerHTML = valor
    def preguntar(self,pregunta):
        
        user_input=pregunta.lower()
        mejor_coincidencia=chatbot_data['datos'][0]['pregunta']
        mejor_respuesta=chatbot_data['datos'][0]['respuesta']  
        mejor_accion=chatbot_data['datos'][0]['accion'] 
        mejor_ejecucion=chatbot_data['datos'][0]['path'] 
        mejor_url=chatbot_data['datos'][0]['url'] 
         
       
        
        porcentaje_obtenido=0
                                                  
        for question in chatbot_data['datos']:
            porcentaje_iterado=fuzz.token_sort_ratio(user_input,question['pregunta'].lower())+\
            fuzz.partial_ratio(user_input,question['respuesta'].lower() ) 
                
           
            if porcentaje_iterado>porcentaje_obtenido:
               
                mejor_coincidencia=question['pregunta'].lower()
                mejor_respuesta=question['respuesta'].lower()
                mejor_accion=question['accion'].lower()
                mejor_ejecucion=question['path'].lower()
                mejor_url=question['url'].lower()
                mejor_seguridad=question['seguridad'].lower()
                porcentaje_obtenido=porcentaje_iterado
                if porcentaje_obtenido>100:
                 #self.js.dom.mensaje2.innerHTML="La mejor coincidencia....:  "+str(mejor_coincidencia)
                 self.js.respuesta = str(mejor_respuesta) + ". Se ha elegido esta respuesta con una puntuación de "+str(porcentaje_obtenido)
                 self.js.larespuesta(str(mejor_respuesta)+ ". Se ha elegido esta respuesta con una puntuación de "+str(porcentaje_obtenido))
                else:
                   #self.js.dom.mensaje2.innerHTML="Consulta no coincidente"
                   #self.js.respuesta ="Ninguna respuesta obtiene un porcentaje de similitud permitido"
                   #self.js.larespuesta("Ninguna respuesta obtiene un porcentaje de similitud permitido")  
                   self.respuesta=bot.reply("localuser",user_input)
                   self.js.larespuesta(str(self.respuesta))
         
                   
   
          
                 
                 
           
 

@app.route('/')
def single_page():
   
    return App.render(render_template('chat.html'))

