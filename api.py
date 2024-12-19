
import requests

def bienvenida():
    print(" Bienvenido a ¿Quién quiere ser millonario?\n")
    nombre = input("Por favor, ingresa tu nombre: ")
    print(f"\n¡Bienvenido, {nombre}! Comencemos el juego.\n")


def obtener_preguntas():
        respuesta = requests.get(f"https://opentdb.com/api.php?amount=15&category=21&difficulty=easy&type=multiple")
        respuesta_formateada = respuesta.json()

        error = respuesta_formateada['response_code'] != 0
        if error:
                print("LIMITE DE PETICIONES EXCEDIDO")
                return[]
        lista_preguntas = respuesta_formateada['results']

        return lista_preguntas

def mostrar_menu_preguntas(pregunta, lista_respuesta):
        print("*"*70)
        print(pregunta)
        for respuesta in lista_respuesta:
                print("\t" + respuesta)
        print("*" * 70)









