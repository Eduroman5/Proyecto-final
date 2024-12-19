import api

lista_preguntas = api.obtener_preguntas()

api.bienvenida()


for info_pregunta in lista_preguntas:
     correcta = info_pregunta['correct_answer']
     incorrectas = info_pregunta['incorrect_answers']
     todas = info_pregunta['incorrect_answers']
     todas.append(correcta)
     api.mostrar_menu_preguntas(info_pregunta['question'], todas)



api.introduce_respuesta(['correct_answer'])

