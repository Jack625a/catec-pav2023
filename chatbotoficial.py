import pyttsx3  #convierte de texto a voz
import openai   #api para red neuronal
import webbrowser  #servicio de acceso a internet
import speech_recognition as sr #reconocimiento de voz
import pyaudio   #control de audio y salida

#creacion de funciones
teclado
#primera opcion del menu
def chatbot():
    print("chatbot")

#segunda opcion del menu
def chatbot_voz():
    print("chatbot mediante voz")
def calculadora():
    print("calculadora avanzada")
def musica():
    print("musica")
def asistente():
    print("asistente que navega por internet")

#funciones especiales
def reconocimiento_voz():
    r=sr.Recognizer()
    
    engine = pyttsx3.init()
    engine.setProperty('rate',120)
    engine.setProperty('voce','spanish-bolivia')
