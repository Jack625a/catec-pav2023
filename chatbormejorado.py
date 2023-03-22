import openai
import time
openai.api_key="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"

modelo="text-davinci-003"

print("hola bienvenido mi nombre es siri y estare aqui para resolver cualquier duda que tengas: ")

def obtener_respuesta(pregunta):
    respuesta=openai.Completion.create(
        engine=modelo,
        prompt=pregunta,
        temperature=0.6,
        max_tokens=100,
        top_p=1,
        frequentcy_penalty=0,
        presence_penalty=0
    )
    return respuesta.choices[0].text.strip()

while True:
    pregunta=input("ingrese su pregunta?: ")
    respuesta=obtener_respuesta(pregunta)
    print("la respuesta a tu pregunta:", pregunta, "es: ", respuesta)
    time.sleep(1)








