import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 110)
engine.setProperty('voce','spanish-mexico')

def hablar(texto):
   #texto=input("Ingrese el mensaje: ")
    engine.say(texto)
    engine.runAndWait()

hablar(texto=input("Ingrese su mensaje: "))

