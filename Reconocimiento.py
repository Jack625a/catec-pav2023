import speech_recognition as sr

r=sr.Recognizer()
with sr.Microphone(device_index=2) as source:
    r.adjust_for_ambient_noise(source)
    print("Puede hablar ahora...")
    audio=r.listen(source)
    try:
        texto=r.recognize_google(audio, language="es-ES")
        print("El mensaje escuchado es:", texto)
    except sr.UnknownValueError:
        print("No se pudo entender el audio")
    except sr.RequestError as e:
        print("Error al conectar con el servicio del reconocimiento de voz")