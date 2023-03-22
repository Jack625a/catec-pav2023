import pyttsx3
engine = pyttsx3.init()
engine.setProperty('rate',120)
engine.setProperty('voce','spanish-bolivia')

def hablar(texto):
    #texto=input("ingrese el mensaje: ")
    engine.say(texto)
    engine.runAndWait()

hablar(texto=input("ingrese su mensaje: "))

