#Este es un juego simple de preguntas y respuestas utilizando la biblioteca Tkinter de Python para crear la interfaz gráfica. El juego muestra una pregunta con cuatro opciones de respuesta. El usuario debe seleccionar una opción y se le dará una respuesta de si es correcta o incorrecta. El juego lleva un registro del puntaje actual del usuario y muestra el puntaje final al finalizar el juego#

import tkinter as tk
import random

#Definir una pregunta y respuesta

pregunta = [
    {
        'pregunta':'¿Cuál es el objetivo principal del proceso productivo?',
    'opciones':['Incrementar la producción sin importar la calidad.','Cubrir la demanda de los clientes satisfaciendo sus necesidades de consumo.','Reducir el costo de los productos a cualquier costo','Utilizar únicamente maquinaria avanzada sin considerar otros recursos'],
        'respuesta_correcta':'Cubrir la demanda de los clientes satisfaciendo sus necesidades de consumo.'
    },
    {
        'pregunta': '¿Qué elementos son necesarios en todo proceso productivo?',
'opciones': ['Solo maquinaria avanzada.', 'Recursos económicos y tecnológicos, además de recursos humanos adecuados.','Solo recursos humanos.','Recursos económicos únicamente.' ],
        'respuesta_correcta': 'Recursos económicos y tecnológicos, además de recursos humanos adecuados.'
    },
    {
        'pregunta': '¿Qué puede ocurrir si no se planifica e implementa correctamente un proceso productivo?',
        'opciones': ['Se maximiza la eficiencia y se alcanza el desarrollo equitativo.','Se logra satisfacer las necesidades de consumo de manera óptima.','Se puede provocar un impacto negativo en la biodiversidad y desigualdad social.','Se optimiza el uso de recursos tecnológicos y económicos.'],
        'respuesta_correcta': 'Se puede provocar un impacto negativo en la biodiversidad y desigualdad social.'
    },
    {
        'pregunta': '¿Cómo influye la distribución espacial de las desigualdades en los procesos productivos?',
        'opciones': ['Aumenta la igualdad y el acceso a bienes y servicios.','Promueve el desarrollo equitativo de todas las regiones.','Genera disparidades en la riqueza, condiciones de vida y acceso a servicios.','No tiene ningún efecto significativo en las sociedades.'],
        'respuesta_correcta':'Genera disparidades en la riqueza, condiciones de vida y acceso a servicios.'
    },
    {
        'pregunta': '¿Qué ocurre con los bienes sociales como bosques y sistemas hidrológicos en procesos productivos irresponsables?',
        'opciones': ['Se preservan y se usan sosteniblemente.','Se protegen adecuadamente para el bienestar común.','Se sobreexplotan, causando desequilibrios ecológicos y pobreza en comunidades.','Se distribuyen equitativamente entre la población.'],
        'respuesta_correcta': 'Se sobreexplotan, causando desequilibrios ecológicos y pobreza en comunidades.'
    },
    {
        'pregunta':'¿Cómo se pueden mitigar las desigualdades y contradicciones en los procesos productivos?',
        'opciones': ['Ignorando las comunidades marginadas.','Fomentando únicamente el desarrollo urbano.','Mediante programas de inclusión social y económica que apoyen a las comunidades marginadas.','Concentrando la inversión en las grandes ciudades.'],
        'respuesta_correcta' : 'Mediante programas de inclusión social y económica que apoyen a las comunidades marginadas.'
    },
    {
        'pregunta':'¿Qué factores se deben considerar minuciosamente para lograr un desarrollo equitativo y eficiente en los procesos productivos?',
        'opciones': ['Solo los beneficios económicos a corto plazo.', 'Únicamente la maximización de la producción.', 'Todos los factores, incluyendo los recursos, la planeación, y el impacto social y ambiental.','Solo la reducción de costos operativos.'],
        'respuesta_correcta' : 'Todos los factores, incluyendo los recursos, la planeación, y el impacto social y ambiental.'
    }
]

def mostrar_pregunta():
    #Función para mostrar una nueva pregunta y opciones de respuesta
    global pregunta_actual, puntaje_actual, preguntas_disponibles
    resultado_texto.set('')
    if not preguntas_disponibles:
        #Si no hay más preguntas disponibles, mostrar mensaje y finalizar el juego.
        pregunta_texto.set('No hay más preguntas disponibles.')
        siguiente_boton.config(state=tk.DISABLED)
        terminar_juego()
        return
    pregunta_actual = random.choice(preguntas_disponibles)
    pregunta_texto.set(pregunta_actual['pregunta'])
    for i, opcion in enumerate(pregunta_actual['opciones']):
        botones_opciones[i].config(text=opcion)
    siguiente_boton.config(state=tk.DISABLED)
    puntaje_label.config(text=f"Puntaje actual: {puntaje_actual}")

def verificar_respuesta(respuesta):
    #Función para verificar la respuesta seleccionada por el usuario
    global pregunta_actual, puntaje_actual, preguntas_disponibles
    if pregunta_actual['respuesta_correcta'] == respuesta:
        resultado_texto.set('¡Respuesta Correcta!')
        puntaje_actual += 10
    else:
        resultado_texto.set('Respuesta Incorrecta')
    siguiente_boton.config(state=tk.NORMAL)
    #Eliminar la pregunta actual de la lsita de preguntas disponibles
    preguntas_disponibles.remove(pregunta_actual)
    
def terminar_juego():
    #Funcion para finalizar el juego y mostrar el puntaje final
    global puntaje_actual
    pregunta_texto.set('Juego Terminado')
    for boton in botones_opciones:
        boton.config(state=tk.DISABLED)
    resultado_texto.set(f'Puntaje final:{puntaje_actual}')
    
#Configuar la ventana principal
ventana= tk.Tk()
ventana.title('Juego de Preguntas y Respuestas')

#Crear una copia de la lista de preguntas disponibles al inicio del juego
preguntas_disponibles = pregunta.copy()

#Variable para llevar un registro de la pregunta actual
pregunta_actual = None

#Variable para mostrar la pregunta actual
pregunta_texto = tk.StringVar()
pregunta_label = tk.Label(ventana, textvariable=pregunta_texto, font=('Arial',14))
pregunta_label.pack(pady=10)

#Botones para opciones de respuesta
botones_opciones = []
for i in range(4):
    boton = tk.Button(ventana, text='', font=('Arial',12), command=lambda i=i:verificar_respuesta(pregunta_actual['opciones'][i]))
    botones_opciones.append(boton)
    boton.pack(pady=5)
    
#Variable para mostrar si la respuesta fue correcta o incorrecta
resultado_texto = tk.StringVar()
resultado_label = tk.Label(ventana, textvariable=resultado_texto,font=('Arial',12))
resultado_label.pack(pady=10)

#Botón "Siguiente"
siguiente_boton = tk.Button(ventana, text='Siguiente', font=('Arial',12),command=mostrar_pregunta)
siguiente_boton.pack(pady=10)
siguiente_boton.config(state=tk.DISABLED)

#Puntaje Actual
puntaje_actual = 0
puntaje_label = tk.Label(ventana, text=f"Puntaje actual: {puntaje_actual}",font=('Arial',12))
puntaje_label.pack(pady=10)

#Botón "Terminar Juego"
terminar_boton = tk.Button(ventana, text='Terminar Juego', font=('Arial',12), command=terminar_juego)
terminar_boton.pack(pady=10)

#Iniciar el juego
mostrar_pregunta()

#Iniciar el bucle principal de la aplicación
ventana.mainloop()

#Saluds :) 