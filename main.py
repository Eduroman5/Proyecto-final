import api

lista_preguntas = api.obtener_preguntas()

api.bienvenida()

comodin_usado = False
puntuacion = 0
for info_pregunta in lista_preguntas:
    correcta = info_pregunta['correct_answer']
    incorrectas = info_pregunta['incorrect_answers']
    todas = info_pregunta['incorrect_answers']
    todas.append(correcta)
    api.mostrar_menu_preguntas(info_pregunta['question'], todas)




    comodin = input("Quieres usae el comodin")
    if comodin_usado:
        print("Ya has usado el comodin")
    elif comodin == "s":
        print("Comodin usado")
        comodin_usado = True
        continue
    else:
        print("Sigamos")




    respuesta_usuario = input("Introduce la respuesta: ")

    if respuesta_usuario == correcta:
        puntuacion += 1
        print(f"¡Correcto! Puntuación actual: {puntuacion}")
    else:
        print(f"Respuesta incorrecta. Has perdido. Puntuación final: {puntuacion}")
        break





