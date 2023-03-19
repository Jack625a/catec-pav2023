import openai
import time

openai.api_key="sus Apis"
modelo="text-davinci-003"

print("Hola bienvenido mi nombre es PAV y estare aqui para resolver cualquier duda que tengas. ")

def obtener_respuesta(pregunta):
    respuesta=openai.Completion.create(
        engine=modelo,
        prompt=pregunta,
        temperature=0.8,
        max_tokens=200,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return respuesta.choices[0].text.strip()

while True:
    pregunta=input("Cual es tu consulta que deseas resolver? : ")
    respuesta=obtener_respuesta(pregunta)
    print("La respuesta a la pregunta: ",pregunta, "es: ", respuesta)
    time.sleep(1)
