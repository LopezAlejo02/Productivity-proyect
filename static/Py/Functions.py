from todoist_api_python.api import TodoistAPI
from todoist_api_python.models import Task
api = TodoistAPI("778bc7bcc3a75d5837be9ba427447bbe59bbcce4")

def getProjects():
    try:
        projects = api.get_projects()
    except Exception as error:
        print(error)
    return projects

def getTasks():
    try:
        tasks = api.get_tasks()
    except Exception as error:
        print(error)
    return tasks

def getSections(id_project):
    try:
        sections = api.get_sections(project_id=id_project)
    except Exception as error:
        print(error)
    return sections


#Task of a project
def get_Project_Tasks(project_name):
    projects = getProjects()

    for project in projects:
        if project.name == project_name:
            id = project.id

    tasks = getTasks()
    tasks_ret = tasks[:0]
    #tasks = [task for task in tasks if not (task.project_id != id)]
    for task in tasks:
        if task.project_id == id:
            tasks_ret.append(task)
            
    return tasks_ret

#Task of the project "Sprint" in section "Diario"
def get_Section_tasks(project_name, section_name):
    projects = getProjects()

    tasks = get_Project_Tasks(project_name)

    for project in projects:
        if project.name == project_name:
            project_id = project.id

    sections = getSections(project_id)

    for section in sections:
        if section.name == section_name:
            section_id = section.id    

    tasks_ret = tasks[:0]
    for task in tasks:
        if task.section_id == section_id:
            tasks_ret.append(task)

    return tasks_ret