#import speech_recognition as sr
#for index, name in enumerate(sr.Microphone.list_microphone_names()):
    #print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))

import speech_recognition as sr

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



