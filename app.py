from http import server
from flask import Flask
import json
import os
import jyserver.Flask as jsf
from flask import render_template,request
import time
from fuzzywuzzy import fuzz

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
#load the JSON file
with open('myjson.json', 'r', encoding='utf-8') as f:
    chatbot_data = json.load(f)
   

@jsf.use(app)
class App:
   
    def __init__(self):
        pass

    def prueba(self):
      pass    
    def hola(self):
        self.js.dom.mensaje2.innerHTML="Consulta no coincidente"
        self.js.factor ="Ninguna respuesta obtiene un porcentaje de similitud permitido"
        pregunta=str(self.js.mipreguntavalor)
        user_input=pregunta.lower()
        mejor_coincidencia=chatbot_data['datos'][0]['pregunta']
        mejor_respuesta=chatbot_data['datos'][0]['respuesta']  
        mejor_accion=chatbot_data['datos'][0]['accion'] 
        mejor_ejecucion=chatbot_data['datos'][0]['path'] 
        mejor_url=chatbot_data['datos'][0]['url'] 
         
       
        
        porcentaje_obtenido=0
                                                  
        for question in chatbot_data['datos']:
            porcentaje_iterado=fuzz.token_set_ratio(user_input,question['pregunta'].lower())+\
            fuzz.token_set_ratio(user_input,question['respuesta'].lower() ) 
                
           
            if porcentaje_iterado>porcentaje_obtenido:
               
                mejor_coincidencia=question['pregunta'].lower()
                mejor_respuesta=question['respuesta'].lower()
                mejor_accion=question['accion'].lower()
                mejor_ejecucion=question['path'].lower()
                mejor_url=question['url'].lower()
                mejor_seguridad=question['seguridad'].lower()
                porcentaje_obtenido=porcentaje_iterado
                if porcentaje_obtenido>80:
                 self.js.dom.mensaje2.innerHTML="La mejor coincidencia....:  "+str(mejor_coincidencia)
                 self.js.factor = str(mejor_respuesta) + ". Se ha elegido esta respuesta con una puntuación de "+str(porcentaje_obtenido)
                 self.js.accion = str(mejor_accion)
                
          
                
      
      
          


@app.route('/')
def hello_world():
  mispreguntas=[]
  return App.render(render_template('index.html', data=mispreguntas,)) 
    
    
if __name__ == '__main__':
    app.run('127.0.0.1', 8000, debug=True)    
