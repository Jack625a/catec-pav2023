import openai
openai.api_key="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"

print(" HOLA MI NOMBRE ES BRANDON ESTOY AQUI PARA CUALQUIER DUDA QUE TENGAS: ")

def obtener_respuesta(pregunta):
    respuesta=openai.completion.create(
        engine="text-davinci-003",
        prompt=pregunta,
        temperature=0.5,
        max_tokens=100,
        top_p=1,
        frequentcy_penalty=0,
        presence_penalty=0
    )
    return respuesta.choices[0],text.strip()

while True:
    pregunta=input("ingrese su pregunta")
    respuesta=obtener_respuesta(pregunta)
    print(respuesta)
