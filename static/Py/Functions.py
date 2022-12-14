import requests
#Función que retorna los proyectos
def getProjects(url, token):
    #La variable url almacena la dirección de la API que vamos consumir
    #url = 'https://api.todoist.com/sync/v9/sync'

    #Este es el token proveido por la API para autorizar el consumo
    #token = '778bc7bcc3a75d5837be9ba427447bbe59bbcce4'

    #Este diccionario contiene el token para la autenticación
    headers = {'Authorization': 'Bearer ' + token}
    #Este diccionario contiene los parámetros del tipo de sincronización que queremos (completa) y el tipo de datos que queremos (proyectos)
    params = {'sync_toke' : '*',
            'resource_types' : '["projects"]'
            }

    #La variable data es donde se almacena los datos recibidos de la API mediante el método get y le enviamos la petición autorización (headers) y los parametros que queremos de retorno (params)
    data = requests.get(url,headers=headers,params=params)

    projects = []

    #Con este condicional se verifica que el codigo devuelto por el servidor es 200 que indica que la petición se realizó con éxito
    if data.status_code == 200:
        #Convertimos los datos recibidos en formato JSON
        data = data.json()
        projects = data['projects']
        print(projects[0])
    return projects