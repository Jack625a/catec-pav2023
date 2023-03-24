import pyttsx3 #Conversor d texto a voz

engine=pyttsx3.init()
voices=engine.getProperty('voices')
for voice in voices:
    print(voice.id)