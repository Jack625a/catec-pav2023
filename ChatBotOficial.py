import pyttsx3 #Conversor d texto a voz
import openai #Api para red neuronal
import webbrowser #Servicio de acceso a internet
import speech_recognition as sr #Reconocimiento de Voz
import pyaudio #Control de Audio y Salida
import time #Control del tiempo
import math #funciones matematica
import requests #Respuesta a la url

#creacion de funciones

#primera opciob del menu
def chatbot():
    print("chatbot")
#segunda opcion del menu
def chatbot_voz():
    print("Chatbot mediante voZ")
def calculadora():
    print("Calculadora Avanzada")
def musica():
    print("musica")
def asistente():
    print("asistente que navega por internet")

#funciones especiales
#reconocimiento de voz 
def recognize_speech():
    r=sr.Recognizer()
    with sr.Microphone(device_index=2) as source:
        r.adjust_for_ambient_noise(source)
        print("Puede hablar ahora...")
        audio=r.listen(source)
    try:
        texto=r.recognize_google(audio, language="es-ES")
        print("El mensaje escuchado es:", texto)
        return texto.lower()
    except sr.UnknownValueError:
        print("No se pudo entender el audio")
        return ""
    except sr.RequestError as e:
        print("Error al conectar con el servicio del reconocimiento de voz")
        return ""
#Funcion para Realizar la busqueda avanzada en Youtube
def buscar_yotube(busqueda):
    url="https://www.youtube.com/results?search_query=" +busqueda.replace('','+')
    response=requests.get(url)
    video_ids=response.text.split('"videoId":"')[1:]
    video_id=video_ids[0].split('"')[0]
    url="https://www.youtube.com/watch?v="+video_id+"?autoplay=1"
    webbrowser.open(url)
#funcion de webbroser - navegacion en internet
def open_website(texto):
    if 'youtube' in texto:
        webbrowser.open("https://www.youtube.com/")
    elif 'netflix' in texto:
        webbrowser.open("https://www.netflix.com/")
    elif 'facebook' in texto:
        webbrowser.open("https://www.facebook.com/")
    elif 'google' in texto:
        webbrowser.open("https://www.google.com/search?q=$texto")
    else:
        print("No tengo registro de esa busqueda")
#Funcion para Realizar la busqueda en Googlee
def buscar_google(busqueda):
    url="https://www.google.com/search?q=" +busqueda.replace(' ','+')
    webbrowser.open(url)
#funcion api del neuronal
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

engine = pyttsx3.init()
engine.setProperty('rate', 110)
engine.setProperty('voce','spanish-mexico')

def hablar(texto):
    engine.say(texto)
    engine.runAndWait()

mensaje_bienvenida="¡Bienvenido al chatbot avanzado!. Mi nombre es PAV, Estamos encantados de ofrecerte una experiencia única con nuestras cinco opciones de servicio. Nuestro chatbot con OpenAI te brinda respuestas inteligentes y precisas a tus preguntas, mientras que la opción de reconocimiento de voz hace que la conversación sea aún más fluida y natural. Si necesitas resolver cálculos complejos, nuestra calculadora avanzada está a tu disposición. Si te gusta disfrutar de la música, nuestro chatbot te permite escuchar tus canciones favoritas con solo hablar. Finalmente, nuestra asistencia virtual te ayuda a solucionar problemas y realizar tareas cotidianas con facilidad. Estamos seguros de que encontrarás nuestra herramienta de chatbot avanzado convincente y útil. ¡Adelante, inténtalo!"
hablar(mensaje_bienvenida)

while True:
    #mostrar el menu disponible
    print("Seleccione una Opción")
    texto_Inicial="Seleccione una Opción"
    hablar(texto_Inicial)
    activarVoz="Desea continuar con la guia por voz? 1.Para Continuar, 2. Para Desactivar"
    opcion_Voz=int(input("Seleccione la opción: "))
    if opcion_Voz==1:
        print("Seleccione una Opción")
        print("1. ChatBot")
        print("2. ChatBot mediante reconocimiento de voz")
        print("3. Calculadora Avanzada")
        print("4. Selector de musica")
        print("5. Asistente Virtual")
        mensaje_voz="Seleccione una Opción: Opción 1. ChatBot, Opción 2. ChatBot mediante reconocimiento de voz, Opción 3. Calculadora Avanzada, Opción 4. Selector de musica, Opción 5. Asistente Virtual"
        hablar(mensaje_voz)
        opcion=int(input(">: "))

        if opcion==1:
            openai.api_key="sus Apis"
            modelo="text-davinci-003"

            print("Hola bienvenido mi nombre es PAV y estare aqui para resolver cualquier duda que tengas. ")
            mensaje_chatbot="Hola bienvenido mi nombre es PAV y estare aqui para resolver cualquier duda que tengas. "
            hablar(mensaje_chatbot)
            while True:
                pregunta=input("Cual es tu consulta que deseas resolver? : ")
                respuesta=obtener_respuesta(pregunta)
                print(">: ", respuesta)
                time.sleep(1)
        elif opcion==2:
            mensaje_chatbotvoz="Para poder utilizar el chatbot se realizara mediante el reconomiento de voz"
            hablar(mensaje_chatbotvoz)
            print("Para poder utilizar el chatbot se realizara mediante el reconomiento de voz")
            openai.api_key="sus Apis"
            modelo="text-davinci-003"
            while True:
                texto=recognize_speech()
                respuesta=obtener_respuesta(texto)
                hablar(respuesta)
                if 'apagar' in texto:
                    break
        elif opcion ==3:
            #Funciones lambda para operaciones aritemeticas
            suma=lambda x,y:x+y
            resta=lambda x,y:x-y
            multiplicacion=lambda x,y:x*y
            division=lambda x,y:x/y
            #Funciones lambda para operaciones trigonometricas
            seno=lambda x:math.sin(x)
            conseno=lambda x:math.cos(x)
            tangente=lambda x:math.tan(x)
            #Funciones lambda para operaciones geometricas
            area_circulo= lambda r:math.pi*r**2
            area_triangulo=lambda b,a:b*a*0.5
            area_rectangulo=lambda b,a:b*a
            #Funciones lambda para operaciones logaritmicas
            logaritmoN=lambda x:math.log(x)
            logaritmo10=lambda x:math.log10(x)
            logaritmo2=lambda x:math.log2(x)

            print("Calculadora con funsion Lambda   PAV-2023")
            print("Seleccione las operaciones que desea realiZAr")
            print("Operaciones Ariteticas= OA")
            print("Operaciones Trigonometricas= OT")
            print("Operaciones Geometricas= OG")
            print("Logaritmos= LO")
            mensaje_calculadora="Seleccione las operaciones que desea realiZAr,Operaciones Ariteticas= OA, Operaciones Trigonometricas= OT, Operaciones Geometricas= OG, Logaritmos= LO "
            hablar(mensaje_calculadora)
            opcion=input("Ingrese la operacion que desea realiZar")
            if opcion == "OA":
                print("Seleccione una operacion aritmetica")
                print("SUMA= S")
                print("RESTA= R")
                print("MULTIPLICACION= M")
                print("DIVISION= D")
                operacion=input("Ingrese una opción: ")
                num1=float(input("Ingrese un primer numero: "))
                num2=float(input("Ingrese un segundo numero: "))
                if operacion == "S":
                    resultado=suma(num1,num2)
                    print("El resultado de la suma es: ",resultado)
                elif operacion == "R":
                    resultado=resta(num1,num2)
                    print("El resultado de la resta es: ",resultado)
                elif operacion == "M":
                    resultado=multiplicacion(num1,num2)
                    print("El resultado de la multiplicación es: ",resultado)
                elif operacion == "D":
                    resultado=division(num1,num2)
                    print("El resultado de la division es: ",resultado)
                else:
                    print("Seleccione una opción valida")
            elif opcion == "OT":
                print("Seleccione una operación trigonometrica")
                print("Seno= SE")
                print("Coseno= CS")
                print("Tangente= TA")
                operacion=input("Ingrese la operacion que desea realiZar: ")

                num3=float(input("Ingrese un numero: "))
                if operacion == "SE":
                    resultado=seno(num3)
                    print("El seno de ", num3, "es: ",resultado)
                elif operacion == "CS":
                    resultado=conseno(num3)
                    print("El coseno de ", num3, "es: ",resultado)
                elif operacion == "TA":
                    resultado=tangente(num3)
                    print("La tangente de ", num3, "es: ",resultado)
                else:
                    print ("Error seleccione una opción habilitada")
            elif opcion == "OG":
                print("Seleccione la operación geometrica que dese realiZar")
                print("Area del circulo= AC")
                print("Area del triangulo= AT")
                print("Area del rectangulo= AR")
                operacion=input("Ingrese una opcion para la operacion geometrica que desea realiZar")
                if operacion == "AC":
                    radio=float(input("Ingrese el radio del circulo"))
                    resultado=area_circulo(radio)
                    print("El area del circulo del radio ingresado ",radio, " es: ", resultado)
                elif operacion == "AT":
                    base=float(input("Ingrese la base del triangulo"))
                    altura=float(input("Ingrese la altura del triangulo"))
                    resultado=area_triangulo(base,altura)
                    print("El area del triangulo es: ", resultado)
                elif operacion == "AR":
                    base=float(input("Ingrese la base del rectangulo: "))
                    altura=float(input("Ingrese la altura del rectangulo: "))
                    resultado=area_rectangulo(base,altura)
                    print("El area del rectangulo es: ", resultado)
                else:
                    print("Error seleccione una opción valida")
            elif opcion == "LO":
                print("Seleccione una operacion de logaritmos que desea calcular")
                print("Logaritmo Natural= LN")
                print("Logaritmo en base 10= L10")
                print("Logaritmo en base 2= L2")
                operacion=input("Ingrese la operacion logaritmica que desea realiZar: ")
                num=float(input("Ingrese un numero: "))

                if operacion == "LN":
                    resultado=logaritmoN(num)
                    print("El logaritmo natural de ", num, " es: ", resultado)
                elif operacion == "L10":
                    resultado=logaritmo10(num)
                    print("El logaritmo en base 10 de ", num, " es: ", resultado)
                elif operacion == "L2":
                    resultado=logaritmo2(num)
                    print("El logaritmo en base 2 de ", num, " es: ", resultado)
                else:
                    print("Error debe selccionar una opción valida")
            else:
                print("Error debe selccionar una opción valida")
        elif opcion==4:
            while True:
                texto=recognize_speech()
                if "cerrar" in texto:
                    print("Apagando...")
                    break
                elif "youtube" in texto:
                    print("¿Que musica quieres escuchar?")
                    mensaje_youtube="¿Que musica quieres escuchar?"
                    hablar(mensaje_youtube)
                    music_query=recognize_speech()
                    if music_query:
                        print("Busqueda en YouTube...")
                        buscar_yotube(music_query)
        elif opcion==5:
             print("Hola soy tu asistente virtual, solamente dime que deseas buscar y yo te lo mostrare")
             mensaje_asistente="Hola soy tu asistente virtual, solamente dime que deseas buscar y yo te lo mostrare, inicia con la palabra clave buscar antes de tu busqueda que desees encontrar"
             hablar(mensaje_asistente)
             while True:
                texto=recognize_speech()
                if "cerrar" in texto:
                    print("Apagando...")
                    break
                elif "buscar" in texto:
                    print("Busqueda en Google...")
                    buscar_google(texto)            
        
    else:
        print("Seleccione una Opción")
        print("1. ChatBot")
        print("2. ChatBot mediante reconocimiento de voz")
        print("3. Calculadora Avanzada")
        print("4. Selector de musica")
        print("5. Asistente Virtual")
        opcion=int(input(">: "))

        if opcion==1:
            openai.api_key="sus Apis"
            modelo="text-davinci-003"

            print("Hola bienvenido mi nombre es PAV y estare aqui para resolver cualquier duda que tengas. ")
            while True:
                pregunta=input("Cual es tu consulta que deseas resolver? : ")
                respuesta=obtener_respuesta(pregunta)
                print(">: ", respuesta)
                time.sleep(1)
        elif opcion==2:
            print("Para poder utilizar el chatbot se realizara mediante el reconomiento de voz")
            openai.api_key="sus Apis"
            modelo="text-davinci-003"
            while True:
                texto=recognize_speech()
                respuesta=obtener_respuesta(texto)
                hablar(respuesta)
                if 'apagar' in texto:
                    break
        elif opcion ==3:
            #Funciones lambda para operaciones aritemeticas
            suma=lambda x,y:x+y
            resta=lambda x,y:x-y
            multiplicacion=lambda x,y:x*y
            division=lambda x,y:x/y
            #Funciones lambda para operaciones trigonometricas
            seno=lambda x:math.sin(x)
            conseno=lambda x:math.cos(x)
            tangente=lambda x:math.tan(x)
            #Funciones lambda para operaciones geometricas
            area_circulo= lambda r:math.pi*r**2
            area_triangulo=lambda b,a:b*a*0.5
            area_rectangulo=lambda b,a:b*a
            #Funciones lambda para operaciones logaritmicas
            logaritmoN=lambda x:math.log(x)
            logaritmo10=lambda x:math.log10(x)
            logaritmo2=lambda x:math.log2(x)

            print("Calculadora con funsion Lambda   PAV-2023")
            print("Seleccione las operaciones que desea realiZAr")
            print("Operaciones Ariteticas= OA")
            print("Operaciones Trigonometricas= OT")
            print("Operaciones Geometricas= OG")
            print("Logaritmos= LO")

            opcion=input("Ingrese la operacion que desea realiZar")
            if opcion == "OA":
                print("Seleccione una operacion aritmetica")
                print("SUMA= S")
                print("RESTA= R")
                print("MULTIPLICACION= M")
                print("DIVISION= D")
                operacion=input("Ingrese una opción: ")
                num1=float(input("Ingrese un primer numero: "))
                num2=float(input("Ingrese un segundo numero: "))
                if operacion == "S":
                    resultado=suma(num1,num2)
                    print("El resultado de la suma es: ",resultado)
                elif operacion == "R":
                    resultado=resta(num1,num2)
                    print("El resultado de la resta es: ",resultado)
                elif operacion == "M":
                    resultado=multiplicacion(num1,num2)
                    print("El resultado de la multiplicación es: ",resultado)
                elif operacion == "D":
                    resultado=division(num1,num2)
                    print("El resultado de la division es: ",resultado)
                else:
                    print("Seleccione una opción valida")
            elif opcion == "OT":
                print("Seleccione una operación trigonometrica")
                print("Seno= SE")
                print("Coseno= CS")
                print("Tangente= TA")
                operacion=input("Ingrese la operacion que desea realiZar: ")

                num3=float(input("Ingrese un numero: "))
                if operacion == "SE":
                    resultado=seno(num3)
                    print("El seno de ", num3, "es: ",resultado)
                elif operacion == "CS":
                    resultado=conseno(num3)
                    print("El coseno de ", num3, "es: ",resultado)
                elif operacion == "TA":
                    resultado=tangente(num3)
                    print("La tangente de ", num3, "es: ",resultado)
                else:
                    print ("Error seleccione una opción habilitada")
            elif opcion == "OG":
                print("Seleccione la operación geometrica que dese realiZar")
                print("Area del circulo= AC")
                print("Area del triangulo= AT")
                print("Area del rectangulo= AR")
                operacion=input("Ingrese una opcion para la operacion geometrica que desea realiZar")
                if operacion == "AC":
                    radio=float(input("Ingrese el radio del circulo"))
                    resultado=area_circulo(radio)
                    print("El area del circulo del radio ingresado ",radio, " es: ", resultado)
                elif operacion == "AT":
                    base=float(input("Ingrese la base del triangulo"))
                    altura=float(input("Ingrese la altura del triangulo"))
                    resultado=area_triangulo(base,altura)
                    print("El area del triangulo es: ", resultado)
                elif operacion == "AR":
                    base=float(input("Ingrese la base del rectangulo: "))
                    altura=float(input("Ingrese la altura del rectangulo: "))
                    resultado=area_rectangulo(base,altura)
                    print("El area del rectangulo es: ", resultado)
                else:
                    print("Error seleccione una opción valida")
            elif opcion == "LO":
                print("Seleccione una operacion de logaritmos que desea calcular")
                print("Logaritmo Natural= LN")
                print("Logaritmo en base 10= L10")
                print("Logaritmo en base 2= L2")
                operacion=input("Ingrese la operacion logaritmica que desea realiZar: ")
                num=float(input("Ingrese un numero: "))

                if operacion == "LN":
                    resultado=logaritmoN(num)
                    print("El logaritmo natural de ", num, " es: ", resultado)
                elif operacion == "L10":
                    resultado=logaritmo10(num)
                    print("El logaritmo en base 10 de ", num, " es: ", resultado)
                elif operacion == "L2":
                    resultado=logaritmo2(num)
                    print("El logaritmo en base 2 de ", num, " es: ", resultado)
                else:
                    print("Error debe selccionar una opción valida")
            else:
                print("Error debe selccionar una opción valida")
        elif opcion==4:
            while True:
                texto=recognize_speech()
                if "cerrar" in texto:
                    print("Apagando...")
                    break
                elif "youtube" in texto:
                    print("¿Que musica quieres escuchar?")
                    mensaje_youtube="¿Que musica quieres escuchar?"
                    hablar(mensaje_youtube)
                    music_query=recognize_speech()
                    if music_query:
                        print("Busqueda en YouTube...")
                        buscar_yotube(music_query)
        elif opcion==5:
             print("Hola soy tu asistente virtual, solamente dime que deseas buscar y yo te lo mostrare")
             mensaje_asistente="Hola soy tu asistente virtual, solamente dime que deseas buscar y yo te lo mostrare, inicia con la palabra clave buscar antes de tu busqueda que desees encontrar"
             hablar(mensaje_asistente)
             while True:
                texto=recognize_speech()
                if "cerrar" in texto:
                    print("Apagando...")
                    break
                elif "buscar" in texto:
                    print("Busqueda en Google...")
                    buscar_google(texto)            