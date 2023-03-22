import openai
import time
openai.api_key="sk-"
modelo="text-davinci-003"

print("Hola bienvenido mi nombres PAV estoy aqui para resolver cualquier pregunta que tengas ¿En que puedo ayudarte? ")

def obtener_respuesta(pregunta):
    respuesta=openai.Completion.create(
        engine=modelo,
        prompt=pregunta,
        temperature=0.5,
        max_tokens=100,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return respuesta.choices[0].text.strip()

while True:
    pregunta=input("cual es tu consulta que deseas resolver? : ")
    repuesta=obtener_respuesta(pregunta)
    print("la respuesta a la pregunta: ",pregunta,"es: ",repuesta)
    time.sleep(1)