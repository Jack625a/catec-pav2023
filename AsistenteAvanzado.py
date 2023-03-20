import speech_recognition as sr
import webbrowser
import requests

#funcion para reconocer la voz nuevo
def recognize_speech():
    r=sr.Recognizer()
    with sr.Microphone(device_index=2) as source:
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

#Funcion para Realizar la busqueda avanzada en Youtube
def buscar_yotube(busqueda):
    url="https://www.youtube.com/results?search_query=" +busqueda.replace('','+')
    response=requests.get(url)
    video_ids=response.text.split('"videoId":"')[1:]
    video_id=video_ids[0].split('"')[0]
    url="https://www.youtube.com/watch?v="+video_id+"?autoplay=1"
    webbrowser.open(url)
#Funcion para Realizar la busqueda en Google
def buscar_google(busqueda):
    url="https://www.google.com/search?q=" +busqueda.replace(' ','+')
    webbrowser.open(url)

#Funcion Principal
def main():
    while True:
        texto=recognize_speech()
        if "cerrar" in texto:
            print("Apagando...")
            break
        elif "youtube" in texto:
            print("¿Que musica quieres escuchar?")
            music_query=recognize_speech()
            if music_query:
                print("Busqueda en YouTube...")
                buscar_yotube(music_query)
        elif "google" in texto:
            print("Busqueda en Google...")
            buscar_google(texto)

#Funcion para ejecutar todo
if __name__=="__main__":
    main()
            

    
#print("Hola bienvenido ¿que musica deseas escuchar?")
#busqueda=recognize_speech()

#if busqueda:
 #   print("Buscando "+ busqueda + "en Youtube...")
  #  buscar_yotube(busqueda)
#else:
 #   print("No se ha entendido lo que dijo, Intentelo de nuevo")