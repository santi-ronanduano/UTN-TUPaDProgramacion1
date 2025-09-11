#TRABAJO PRACTICO N°2
#"ESTRUCTURA CONDICIONALES"

#--------------------------------------------------------
#Ejercicio 1
#--------------------------------------------------------

# le pide la edad al usuario
edad = int(input("Ingrese su edad: "))

# Verifica si es mayor de edad
if edad >= 18:
    print("Es mayor de edad")
else:
    print("No es mayor de edad")

#--------------------------------------------------------
#ejercicio 2
#--------------------------------------------------------

nota=int(input("ingrese su nota: "))
#verefica si aprobo o no aprobo
if nota >=6:
    input("usted aprobo")
else:
    input("usted desaprobo")

#--------------------------------------------------------
#ejercicio 3
#--------------------------------------------------------

#le pide un numero al usuario
numero=int(input("ingrese un numero"))
#verifica si el numero es par o impar
if numero %2 == 0:
    input("el numero es par")
else:
    input("el numero es impar")

#--------------------------------------------------------
#ejercicio 4
#--------------------------------------------------------

edad= int(input("ingrese su edad: "))
if edad <=12:
    input("Niño/a")
elif edad >=12 and edad <18:
    input("Adolescente")
elif edad >=18 and edad <30:
    input("Adulto/a joven")
else:
    edad>=30
    input("Adulto/a")

#--------------------------------------------------------
#ejercicio 5   
#--------------------------------------------------------

# le pedimos al usuario que ingrese un acontraseña
contraceña = input ("ingrese contraceña: ")
#verifica si la contraseña cumple con los caracteres necesarios
if len (contraceña) < 8 :
    input("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")
elif len (contraceña) > 14:
    input ("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")
else:
    input ("Ha ingresado una contraseña correcta")

#--------------------------------------------------------
#ejercicio 6
#--------------------------------------------------------

import random
from statistics import mode, median, mean
mi_lista = [random.randint(1, 100) for i in range(50)]
#calcula  la moda, la mediana y la media
moda = mode(mi_lista)
mediana = median(mi_lista)
media = mean(mi_lista)
#muestra el resultado de la moda, la mediana y la media
print("Números aleatorios:",)

print(f"Media: {media}")

print(f"Mediana: {mediana}")

print(f"Moda: {moda}")
# Determinar si el sesgo es positivo o negativo
if media > mediana > moda:
    print("Sesgo positivo (a la derecha)")
elif media < mediana < moda:
    print("Sesgo negativo (a la izquierda)")
else:
    print("Sin sesgo (aproximadamente simétrica)")

#--------------------------------------------------------
#ejercicio 7
#-------------------------------------------------------- 

# le Pide una palabra al usuario
palabra = input("Ingresa una frase o palabra: ")

# Compruba si la palabra ingresada termina en vocal
if palabra[-1] in "aeiou":
    palabra += "!"
    
# Imprime el resultado de la palabra
print(palabra)

#--------------------------------------------------------
#ejecicio 8
#--------------------------------------------------------

#le pide al usuario que ingrese un nombre
nombre=input("ingrese su nombre: ") 
#le pide al usuario que ingrese un numero, segun la opcion que el desee
print("Elige una un numero:")
print("1. Nombre en MAYÚSCULAS")
print("2. Nombre en minúsculas")
print("3. Nombre con primera letra mayúscula")
numero=int(input(" ingrese un numero: "))
#modifica el nombre ingrasado por el usurio segun el numero elegido
if numero == 1:
     print(nombre.upper())
elif numero == 2:
     print(nombre.lower())
elif numero==3:
     print(nombre.title())
else:
    print("Opción no válida", nombre)

#--------------------------------------------------------
#ejecicio 9
#--------------------------------------------------------

# le Pide al usuario la magnitud del terremoto
magnitud = float(input("Ingresa la magnitud del terremoto: "))

# Clasifica según la escala de Richter
if magnitud < 3:
    categoria = "Muy leve (imperceptible)"
elif 3 <= magnitud < 4:
    categoria = "Leve (ligeramente perceptible)"
elif 4 <= magnitud < 5:
    categoria = "Moderado (sentido por personas, pero generalmente no causa daños)"
elif 5 <= magnitud < 6:
    categoria = "Fuerte (puede causar daños en estructuras débiles)"
elif 6 <= magnitud < 7:
    categoria = "Muy Fuerte (puede causar daños significativos)"
else:  
    categoria = "Extremo (puede causar graves daños a gran escala)"

# Imprime cual es la categoria del terremoto
print("Clasificación:", categoria)

#--------------------------------------------------------
#ejercicio 10
#--------------------------------------------------------

# Pide información al usuario
hemisferio = input("¿En qué hemisferio te encuentras? (N/S): ").upper()
mes = int(input("Ingresa el mes (1-12): "))
dia = int(input("Ingresa el día (1-31): "))

# Determina la estación según el hemisferio y la fecha
if hemisferio == "N":
    if (mes == 12 and dia >= 21) or (mes in [1,2]) or (mes == 3 and dia <= 20):
        estacion = "Invierno"
    elif (mes == 3 and dia >= 21) or (mes in [4,5]) or (mes == 6 and dia <= 20):
        estacion = "Primavera"
    elif (mes == 6 and dia >= 21) or (mes in [7,8]) or (mes == 9 and dia <= 20):
        estacion = "Verano"
    elif (mes == 9 and dia >= 21) or (mes in [10,11]) or (mes == 12 and dia <= 20):
        estacion = "Otoño"
    else:
        estacion = "Fecha inválida"
elif hemisferio == "S":
    if (mes == 12 and dia >= 21) or (mes in [1,2]) or (mes == 3 and dia <= 20):
        estacion = "Verano"
    elif (mes == 3 and dia >= 21) or (mes in [4,5]) or (mes == 6 and dia <= 20):
        estacion = "Otoño"
    elif (mes == 6 and dia >= 21) or (mes in [7,8]) or (mes == 9 and dia <= 20):
        estacion = "Invierno"
    elif (mes == 9 and dia >= 21) or (mes in [10,11]) or (mes == 12 and dia <= 20):
        estacion = "Primavera"
    else:
        estacion = "Fecha inválida"
else:
    estacion = "Hemisferio no válido"

# Muestra el resultado
print("La estación actual es:", estacion)

