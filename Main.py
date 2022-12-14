from static.Py.Functions import *

import sys, os 
from flask import Flask, render_template
from distutils.log import debug

#Instanciamos la clase Flask y le enviamos como parámetro el nombre del módulo actual

app = Flask(__name__)

url = 'https://api.todoist.com/sync/v9/sync'
token = '778bc7bcc3a75d5837be9ba427447bbe59bbcce4'

@app.route("/")
def Dashboard():
    data = getProjects(url,token)
    return render_template('Dashboard.html',data = data)
if __name__ == "__main__":
    app.run(debug=True)