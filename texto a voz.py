import pyttsx3

engine = pyttsx3.init()
engine.setProperty("rate", 110)
engine.setProperty("voce","spanish-mexico")

def hablar(texto):
    #
    engine.say(texto)
    enigme.runAndWait()

hablar(texto=input("ingrese su mensaje: "))