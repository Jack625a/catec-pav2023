import openai
import time
openai.api_key="sk-rdgfhghgd"
modelo="text-davinci-003"

print("Hola bienvenido mi nombres PAV estoy aqui para resolver cualquier pregunta que tengas ¿En que puedo ayudarte? ")

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