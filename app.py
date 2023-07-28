
##############################################################################
# sigle page flask "reactivo" interactuando con el Dom sin renderizar de nuevo
##############################################################################

import jyserver.Flask as js
from flask import Flask, render_template, request
import time
import os
import json
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
   
        
        
    def cambiar(self,valor):
         self.js.dom.info1.innerHTML = valor
    def preguntar(self,pregunta):
        
        user_input=pregunta.lower()
        self.respuesta=bot.reply("localuser",user_input)
        self.js.respuesta=str(self.respuesta)
        self.js.larespuesta(str(self.respuesta))
        
    @js.task
    def main(self):
                # nuestro bucle hace las veces de "event listener of javascript"
                while True:
                  self.js.respuesta=str(self.respuesta)
        
          
@app.route('/')
def single_page():
    """ App.main() """
    return App.render(render_template('chat.html'))

