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
    projects_names = [project.name for project in getProjects()]
    projects_names.pop(0)
    project_tasks = [len(get_Project_Tasks(project)) for project in projects_names]
    tasks = getTasks()
    unAsigned = len(get_Project_Tasks("Inbox"))
    day_tasks = len(get_Section_tasks("Sprint","Diario"))
    return render_template('Dashboard.html',active_tasks = len(tasks), unasigned_tasks = unAsigned , day_tasks = day_tasks, projects_names = projects_names, project_tasks = project_tasks)
if __name__ == "__main__":
    app.run(debug=True)