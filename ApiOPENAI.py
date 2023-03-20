import time
openai.api_key="Sus Apis"

print("Hola mi nombres PAV estoy aqui para resolver cualquier pregunta que tengas ¿En que puedo ayudarte? ")

def obtener_respuesta(pregunta):
    respuesta=openai.Completion.create(
        engine="text-davinci-003",
        prompt=pregunta,
        temperature=0.5,
        max_tokens=100,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return respuesta.choices[0].text.strip()

while True:
    pregunta=input("Ingrese su pregunta: ")
    respuesta=obtener_respuesta(pregunta)
    print(respuesta)