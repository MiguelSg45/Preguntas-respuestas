#Este es un juego simple de preguntas y respuestas utilizando la biblioteca Tkinter de Python para crear la interfaz gráfica. El juego muestra una pregunta con cuatro opciones de respuesta. El usuario debe seleccionar una opción y se le dará una respuesta de si es correcta o incorrecta. El juego lleva un registro del puntaje actual del usuario y muestra el puntaje final al finalizar el juego#

import tkinter as tk
import random

#Definir una pregunta y respuesta

pregunta = [
    {
        'pregunta':'¿Cuál es la velocidad aproximada a la que se desplazan las ondas sísmicas generadas por las placas tectónicas en México?',
        'opciones':['12,000 km/h','24,000 km/h','36,000 km/h'],
        'respuesta_correcta':'24,000 km/h'
    },
    {
        'pregunta': '¿Cuántos sismos se han registrado en México entre 1900 y 2023?',
        'opciones': ['257,240', '150,000','300,000'],
        'respuesta_correcta': '257,240'
    },
    {
        'pregunta': '¿Cuál fue la magnitud del sismo del 19 de septiembre de 1985?',
        'opciones': ['7.1','8.1','6.9'],
        'respuesta_correcta': '8.1'
    },
    {
        'pregunta': '¿Qué porcentaje de los sismos registrados en México entre 1900 y 2023 han sido menores a 5.9 en la escala de Richter?',
        'opciones': ['95.432%','97.543%','99.876%'],
        'respuesta_correcta':'99.876%'
    },
    {
        'pregunta': '¿Qué fue una de las causas principales de los graves daños causados por el sismo del 19 de septiembre de 1985 en la Ciudad de México?',
        'opciones': ['La falta de un sistema de alerta sísmica','La magnitud del sismo fue demasiado baja','La ciudad estaba bien preparada'],
        'respuesta_correcta': 'La falta de un sistema de alerta sísmica'
    },
    {
        'pregunta':'¿Cuántos edificios resultaron dañados durante el sismo del 19 de septiembre de 1985?',
        'opciones': ['5,000','1,200','3,300'],
        'respuesta_correcta' : '3,300'
    },
    {
        'pregunta':'¿Cuáles fueron los costos directos e indirectos estimados de los sismos de 1985 en México?',
        'opciones': ['2,500 millones de dólares', '4,100 millones de dólares', '6,000 millones de dólares,'],
        'respuesta_correcta' : '4,100 millones de dólares'
    },
    {
        'pregunta': '¿Cuál fue la reacción de la población civil tras el sismo del 19 de septiembre de 1985?',
        'opciones': ['Se evacuaron inmediatamente','No reaccionaron debido al miedo','Se organizaron rápidamente para rescatar a los sobrevivientes'],
        'respuesta_correcta': 'Se organizaron rápidamente para rescatar a los sobrevivientes'
    },
    {
        'pregunta':'¿Qué evento significativo ocurrió exactamente 32 años después del sismo de 1985?',
        'opciones': ['Otro sismo devastador el 19 de septiembre de 2017','Una erupción volcánica','Una gran inundación'],
        'respuesta_correcta' : 'Otro sismo devastador el 19 de septiembre de 2017'
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
for i in range(3):
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