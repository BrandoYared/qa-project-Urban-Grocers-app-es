import configuration
import data
import requests

def post_new_user():
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,  # inserta la dirección URL completa
                         json=data.user_body,  # inserta el cuerpo de solicitud
                         headers=data.headers)  # inserta los encabezados
def post_new_kits(body):
    token = post_new_user().json()
    print(token)
    headers = data.headers.copy() #crea una copia de los headers adicionales
    headers["Authorization"] = "Bearer " + token["authToken"]
    print(headers)
    return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,  # inserta la dirección URL completa
                         json=data.kit_body,  # inserta el cuerpo de solicitud
                         headers=headers)  # inserta los encabezados