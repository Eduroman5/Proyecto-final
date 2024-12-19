import api

lista_preguntas = api.obtener_preguntas()

api.bienvenida()

puntuacion = 0
for info_pregunta in lista_preguntas:
    correcta = info_pregunta['correct_answer']
    incorrectas = info_pregunta['incorrect_answers']
    todas = info_pregunta['incorrect_answers']
    todas.append(correcta)
    api.mostrar_menu_preguntas(info_pregunta['question'], todas)
    respuesta_usuario = input("Introduce la respuesta: ")

    if respuesta_usuario == correcta:
        puntuacion += 1
        print(f"¡Correcto! Puntuación actual: {puntuacion}")
    else:
        print(f"Respuesta incorrecta. Has perdido. Puntuación final: {puntuacion}")
        break





