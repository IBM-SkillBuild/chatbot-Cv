
##############################################################################
# sigle page flask "reactivo" interactuando con el Dom sin renderizar de nuevo
##############################################################################

import jyserver.Flask as js
from flask import Flask, render_template, request
import time
import os
import json
from rivescript import RiveScript
from fuzzywuzzy import fuzz
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
    pregunta=""
    empezar="no"
        
        
    def cambiar(self,valor):
         self.js.dom.info1.innerHTML = valor
    def preguntar(self):
        self.js.empezar="si"
        
        
        
    @js.task
    def main(self):
                # nuestro bucle hace las veces de "event listener of javascript"
                while True:
                   
                  if str(self.js.empezar)=="si":  
                    self.js.empezar="no"
                    user_input=str(self.js.msg)
                    mejor_coincidencia=chatbot_data['datos'][0]['pregunta']
                    mejor_respuesta=chatbot_data['datos'][0]['respuesta']  
                    mejor_accion=chatbot_data['datos'][0]['accion'] 
                    mejor_ejecucion=chatbot_data['datos'][0]['path'] 
                    mejor_url=chatbot_data['datos'][0]['url'] 
                    
                  
                    
                    porcentaje_obtenido=0
                                                              
                    for question in chatbot_data['datos']:
                        porcentaje_iterado=fuzz.token_sort_ratio(user_input,question['pregunta'])+\
                        fuzz.partial_ratio(user_input,question['respuesta'] ) 
                            
                      
                        if porcentaje_iterado>porcentaje_obtenido:
                          
                            mejor_coincidencia=question['pregunta']
                            mejor_respuesta=question['respuesta']
                            mejor_accion=question['accion']
                            mejor_ejecucion=question['path']
                            mejor_url=question['url']
                            mejor_seguridad=question['seguridad']
                            porcentaje_obtenido=porcentaje_iterado
                            if porcentaje_obtenido>85:
                              #self.js.dom.mensaje2.innerHTML="La mejor coincidencia....:  "+str(mejor_coincidencia)
                              self.js.respuesta = str(mejor_respuesta) 
                              self.js.larespuesta(str(mejor_respuesta))
                            else:
                              #self.js.dom.mensaje2.innerHTML="Consulta no coincidente"
                              #self.js.respuesta ="Ninguna respuesta obtiene un porcentaje de similitud permitido"
                              #self.js.larespuesta("Ninguna respuesta obtiene un porcentaje de similitud permitido") 
                              self.respuesta=bot.reply("localuser",user_input)
                              self.js.respuesta=str(self.respuesta)
                              self.js.larespuesta(str(self.respuesta)) 
                    time.sleep(1)
                    
                    
                    
                    
                    
        
          
@app.route('/')
def single_page():
    App.main() 
    return App.render(render_template('chat.html'))

