#Trabajo practico N°1 
#Materia: programación 1 
#Nombre: Santiago ronanduano 

#ejercicio 1 
print("Hola", nombre) 

#ejercicio 2
nombre= input("ingrese su nombre:") 
print(f"hola {nombre}") 

#ejercicio 3  
nombre = input("ingrese su nombre:") 
apellido = input("ingrese su apellido:") 
edad = input("ingrese su edad:") 
lugarDeResidencia = input("ingre su lugar de residencia:") 
print(f"hola soy {nombre} {apellido}, tengo {edad} años y soy de {lugarDeResidencia}") 

#ejercicio 4 
import math 
# Pedir al usuario el radio del círculo 
radio = float(input("Introduce el radio del círculo: ")) 
# Calcular el área y el perímetro 
area = 3.1416 * radio ** 2 
perimetro = 2 * 3.1416 * radio 
# Mostrar los resultados 
print(f"Área del círculo: {area:.2f}") 
print(f"Perímetro del círculo: {perimetro:.2f}") 

#ejercicio 5 
# Pedir al usuario una cantidad de segundos 
segundos = int(input("Introduce una cantidad de segundos: ")) 
# Calcular cuántas horas hay en esos segundos 
horas = segundos / 3600  # 1 hora = 3600 segundos 
# Mostrar el resultado 
print(f"{segundos} segundos equivalen a {horas:.f} horas.") 

#ejercicio 6 
# Pedir al usuario un número 
numero = int(input("Introduce un número: ")) 
# Imprimir la tabla de multiplicar del 1 al 10 
print(f"Tabla de multiplicar del {numero}:") 
for i in range(1, 11): 
resultado = numero * i 
print(f"{numero} x {i} = {resultado}") 

#ejercicio 7 
num1 = int(input("Introduce el primer número (distinto de 0): ")) 
num2 = int(input("Introduce el segundo número (distinto de 0): ")) 
if num1 != 0 and num2 != 0: 
suma = num1 + num2 
resta = num1 - num2 
multiplicacion = num1 * num2 
division = num1 / num2 
print(f"Suma: {num1} + {num2} = {suma}") 
print(f"Resta: {num1} - {num2} = {resta}") 
print(f"Multiplicación: {num1} * {num2} = {multiplicacion}") 
print(f"División: {num1} / {num2} = {division:.2f}") 
else: 
print("Error: ambos números deben ser distintos de 0.") 

#ejercicio 8 
peso = float(input("Introduce tu peso en kilogramos: ")) 
altura = float(input("Introduce tu altura en metros: ")) 
imc = peso / (altura * altura) 
#resulatado 
print("Tu Índice de Masa Corporal (IMC) es:", round(imc, 2)) 

#ejercicio 9 
celsius = float(input("Introduce la temperatura en grados Celsius: ")) 
fahrenheit = (9 / 5) * celsius + 32 
#imprime el resultado 
print("La temperatura en grados Fahrenheit es:", round(fahrenheit, 2)) 

#ejercicio 10 
num1 = float(input("Introduce el primer número: ")) 
num2 = float(input("Introduce el segundo número: ")) 
num3 = float(input("Introduce el tercer número: ")) 
promedio = (num1 + num2 + num3) / 3 
print("El promedio de los tres números es:", round(promedio, 2)) 