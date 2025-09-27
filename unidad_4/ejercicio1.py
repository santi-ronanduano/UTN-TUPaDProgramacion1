#----------------------------------------------------------------
#EJERCICIO 1
#----------------------------------------------------------------
#1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
#(incluyendo ambos extremos), en orden creciente, mostrando un número por línea. for i in range(0, 101):  # desde 0 hasta 100
for i in range(0,101):
    print(i)


#---------------------------------------------------------------
#EJERCICIO 2
#---------------------------------------------------------------
#2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
#dígitos que contiene.
# Pedir el número al usuario
numero = int(input("Ingresa un número entero: "))

# Contador de dígitos
contador = 0

# Caso especial: si el número es 0
if numero == 0:
    contador = 1
else:
    # Mientras el número sea mayor que 0
    while numero > 0:
        numero = numero // 10    # Quita el último dígito
        contador = contador + 1  # Suma 1 al contador

# Mostrar el resultado
print("El número tiene", contador, "dígito(s).")

#---------------------------------------------------------------------------
#EJERCICIO 3
#---------------------------------------------------------------------------
#3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
#dados por el usuario, excluyendo esos dos valores.
# a este ejercicio no lo pude lograar comprender muy bien 
inicio=int(input("introduce el valor de inicio"))
fin=int (input("introduce el valor de fin"))
if inicio > fin:
    inicio, fin = fin, inicio  

# Empezamos desde el número siguiente al inicio
numero = inicio + 1

# Variable para la suma
suma = 0

# Bucle while para sumar los números entre los dos valores
while numero < fin:
    suma = suma + numero
    numero = numero + 1

# Mostrar el resultado
print("La suma de los números entre", inicio, "y", fin, "es:", suma)


#---------------------------------------------------------------------------
#EJERCICIO 4
#---------------------------------------------------------------------------
#4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
#secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0.
# Programa que suma números enteros hasta que el usuario ingrese 0

# Variable para guardar la suma acumulada
suma = 0

print("Ingresa números enteros para sumar. Escribe 0 para terminar.")

# Bucle repetitivo
numero = int(input("Ingresa un número: "))

while numero != 0:
    suma = suma + numero        # Agrega el número a la suma
    numero = int(input("Ingresa otro número (0 para terminar): "))

# Cuando el usuario ingresa 0, termina el bucle
print("La suma total de los números ingresados es:", suma)

#---------------------------------------------------------------------------
#EJERCICIO 5
#---------------------------------------------------------------------------
#5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
#programa debe mostrar cuántos intentos fueron necesarios para acertar el número.
import random  
# Generar un número aleatorio entre 0 y 9
numero_secreto = random.randint(0, 9)

# Contador de intentos
intentos = 0

print("Adivina el número secreto (entre 0 y 9)")

# Bucle hasta que el usuario acierte
# Inicializamos con un valor distinto del número secreto
adivinanza = -1  
while adivinanza != numero_secreto:
    adivinanza = int(input("Ingresa tu intento: "))
    # Contamos cada intento
    intentos = intentos + 1  

    if adivinanza < numero_secreto:
        print("Muy bajo, intenta otra vez.")
    elif adivinanza > numero_secreto:
        print("Muy alto, intenta otra vez.")

# Cuando acierta
print(f"¡Correcto! El número era {numero_secreto}.")
print(f"Lo adivinaste en {intentos} intento(s).")

#---------------------------------------------------------------------------
#EJERCICIO 6
#---------------------------------------------------------------------------
#6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
#entre 0 y 100, en orden decreciente.
# Imprimir los números pares entre 0 y 100 en orden decreciente usando if
# Desde 100 hasta 0, de uno en uno
for numero in range(100,-1,-1 ):  
    # Verifica si el número es par
    if numero % 2 == 0:            
        print(numero)


#---------------------------------------------------------------------------
#EJERCICIO 7
#---------------------------------------------------------------------------

# Programa que suma los números desde 0 hasta un número positivo indicado por el usuario

# Pedir el número al usuario
n = int(input("Ingresa un número entero positivo: "))

# Inicializar variables
suma = 0
numero = 0

# Bucle para sumar todos los números de 0 a n
while numero <= n:
    suma = suma + numero
    numero = numero + 1

# Mostrar el resultado
print("La suma de los números desde 0 hasta", n, "es:", suma)

#---------------------------------------------------------------------------
#EJERCICIO 8
#---------------------------------------------------------------------------
# Cantidad de números a ingresar
cantidad_numeros = 100  # Se puede cambiar fácilmente para probar con menos números

# Contadores
pares = 0
impares = 0
positivos = 0
negativos = 0

# Bucle para pedir los números al usuario
for i in range(cantidad_numeros):
    numero = int(input(f"Ingrese el número {i+1}: "))

    # Contar pares e impares
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

    # Contar positivos y negativos
    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1
    # El 0 no se cuenta ni como positivo ni como negativo

# Mostrar resultados
print("Cantidad de números pares:", pares)
print("Cantidad de números impares:", impares)
print("Cantidad de números positivos:", positivos)
print("Cantidad de números negativos:", negativos)

#---------------------------------------------------------------------------
#EJERCICIO 9
#---------------------------------------------------------------------------
cantidad_numeros = 100  # Cambiá este valor para probar con menos números

# Variable para acumular la suma
suma = 0

# Bucle para pedir los números
for i in range(cantidad_numeros):
    numero = int(input(f"Ingrese el número {i+1}: "))
    suma += numero

# Calcular la media
media = suma / cantidad_numeros

# Mostrar el resultado
print("La media de los números ingresados es:", media)

#-------------------------------------------------------------------------------
#EJERCICIO 10 
#-------------------------------------------------------------------------------

# Pedimos el número al usuario
numero = int(input("Ingresa un número entero: "))

# Guardar el número original para saber si era negativo
numero_original = numero

# Si el número es negativo, lo hacemos positivo para invertir
if numero < 0:
    numero = -numero

# Variable para el número invertido
numero_invertido = 0

# Mientras queden dígitos
while numero > 0:
    # Tomamos el último dígito
    digito = numero % 10               
    # Lo agregamos al invertido
    numero_invertido = numero_invertido * 10 + digito  
    # Quitamos el último dígito
    numero = numero // 10               

# Si el número original era negativo, lo devolvemos a negativo
if numero_original < 0:
    numero_invertido = -numero_invertido

# Mostrar el resultado
print("El número invertido es:", numero_invertido)
