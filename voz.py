import speech_recognition as sr
import webbrowser
def recognize_speech():
    r=sr.Recognizer()
    with sr.Microphone(device_index=1) as source:
        r.adjust_for_ambient_noise(source)
        print("Puede hablar ahora.......: ")
        audio=r.listen(source)
    try:
        texto=r.recognize_google(audio, language="es-ES")
        print("El mensaje escuchando es: "+texto)
    except sr.UnknownValueError:
        print("No se pudo entender el audio: ")
    except sr.RequestError as e:
        print("Erro no tiene conexion a internet: ")

def abrir_sitioweb(texto):
    if 'youtube' in texto:
        url="https://www.youtube.com/"
    elif 'netflix' in texto:
        url="https://www.netflix.com/"
    elif 'facebook' in texto:
        url="https://www.facebook.com/"
    elif 'google' in texto:
        url="https://www.google.com/search?q=$texto"
    else:
        print("No tengo registro de esa busqueda: ")
        return webbrowser.open(url, new=2)
while True:
    texto=recognize_speech()
    if 'salir' in texto:
        break
    if any(word in texto for word in ['youtube','netflix','facebook','google']):
        abrir_sitioweb(texto)


