#Este es un juego simple de preguntas y respuestas utilizando la biblioteca Tkinter de Python para crear la interfaz gráfica. El juego muestra una pregunta con cuatro opciones de respuesta. El usuario debe seleccionar una opción y se le dará una respuesta de si es correcta o incorrecta. El juego lleva un registro del puntaje actual del usuario y muestra el puntaje final al finalizar el juego#

import tkinter as tk
import random

#Definir una pregunta y respuesta

pregunta = [
    {
        'pregunta':'¿Qué características fundamentales definen a un agente de cambio social?',
        'opciones':['Un fuerte compromiso social y disposición para desarrollar soluciones.','Alta capacidad económica y poder político.','Interés en la política y habilidades tecnológicas.','Pasividad ante los problemas sociales.'],
        'respuesta_correcta':'Un fuerte compromiso social y disposición para desarrollar soluciones.'
    },
    {
        'pregunta': '¿Cuál es una estrategia esencial para convertirse en un agente de cambio?',
        'opciones': ['Identificar un problema social que te apasione y desarrollar un plan de acción.', 'Evitar involucrarse en conflictos sociales.','Delegar responsabilidades a otras personas.','Centrarse únicamente en problemas globales y no locales.'],
        'respuesta_correcta': 'Identificar un problema social que te apasione y desarrollar un plan de acción.'
    },
    {
        'pregunta': '¿Qué valores caracterizan a un agente de cambio social?',
        'opciones': ['Empatía, educación y liderazgo.','Autoritarismo, individualismo y desprecio por la educación.','Neutralidad, indiferencia y conformismo.','Exclusividad, elitismo y desdén por la comunidad.'],
        'respuesta_correcta': 'Empatía, educación y liderazgo.'
    },
    {
        'pregunta': '¿Cuál es una forma efectiva de buscar soluciones para problemas sociales?',
        'opciones': ['Definir objetivos y desarrollar un plan basado en la experiencia y necesidades de la comunidad.','Ignorar las necesidades de la comunidad y centrarse en soluciones teóricas.','Evitar definir objetivos claros y actuar espontáneamente.','Limitarse a criticar sin proponer soluciones.'],
        'respuesta_correcta':'Definir objetivos y desarrollar un plan basado en la experiencia y necesidades de la comunidad.'
    },
    {
        'pregunta': '¿Qué acciones pueden ayudar a generar un cambio positivo en tu entorno más cercano?',
        'opciones': ['Pequeñas acciones dentro de tus círculos más cercanos.','Evitar cualquier tipo de acción o iniciativa.','Esperar a que otros tomen la iniciativa.','Enfocarse exclusivamente en problemas internacionales'],
        'respuesta_correcta': 'Pequeñas acciones dentro de tus círculos más cercanos.'
    },
    {
        'pregunta':'¿Qué puede lograr la participación activa en iniciativas sociales y voluntariado?',
        'opciones': ['Poco o ningún impacto en la sociedad.','Aislamiento y desconexión con la comunidad.','Un efecto profundo en la sociedad, mejorando la calidad de vida.','Exclusivo beneficio personal sin contribuir al bienestar común.'],
        'respuesta_correcta' : 'Un efecto profundo en la sociedad, mejorando la calidad de vida. '
    },
    {
        'pregunta':'¿Cómo puedes redoblar tus esfuerzos como agente de cambio social?',
        'opciones': ['Actuando de manera aislada y sin colaboración.', 'Formando alianzas con organizaciones sin fines de lucro o grupos comunitarios.', 'Evitando la participación en movimientos colectivos.','Manteniendo tus acciones en secreto y sin difusión.'],
        'respuesta_correcta' : 'Formando alianzas con organizaciones sin fines de lucro o grupos comunitarios.'
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