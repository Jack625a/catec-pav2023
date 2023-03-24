import pyttsx3

engine = pyttsx3.init()

# Establecer la voz en español de México
voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-ES_HELENA_11.0"

# Establecer la voz seleccionada
engine.setProperty('voice', voice_id)

engine.say("Hola, soy una voz en español de México")
engine.runAndWait()
