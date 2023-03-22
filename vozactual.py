import speech_recognition as sr
import webbrowser
#funcion para reconocer la voz nuevo
def recognize_speech():
    r=sr.Recognizer()
    with sr.Microphone(device_index=1) as source:
        r.adjust_for_ambient_noise(source)
        print("Puede hablar ahora...")
        audio=r.listen(source)
    try:
        texto=r.recognize_google(audio, language="es-ES")
        print("El mensaje escuchado es:", texto)
        return texto.lower()
    except sr.UnknownValueError:
        print("No se pudo entender el audio")
        return ""
    except sr.RequestError as e:
        print("Error al conectar con el servicio del reconocimiento de voz")
        return ""

#funcion para ingresar a internet 
def open_website(texto):
    if 'youtube' in texto:
        webbrowser.open("https://www.youtube.com/")
    elif 'netflix' in texto:
        webbrowser.open("https://www.netflix.com/")
    elif 'facebook' in texto:
        webbrowser.open("https://www.facebook.com/")
    elif 'google' in texto:
        webbrowser.open("https://www.google.com/search?q=$texto")
    else:
        print("No tengo registro de esa busqueda")

    
while True:
    texto=recognize_speech()
    if 'apagar' in texto:
        break
    if any(word in texto for word in ['youtube','netflix','facebook','google']):
        open_website(texto)