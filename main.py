import requests
import time


def obtener_preguntas(cantidad=15):
    url = f"https://opentdb.com/api.php?amount={cantidad}&type=multiple"
    respuesta = requests.get(url)
    if respuesta.status_code == 200:
        return respuesta.json().get('results', [])
    else:
        print("Error al obtener preguntas. Inténtalo de nuevo más tarde.")
        return []