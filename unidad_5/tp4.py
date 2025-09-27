#1) Crear una lista con las notas de 10 estudiantes.
#• Mostrar la lista completa.
#• Calcular y mostrar el promedio.
#• Indicar la nota más alta y la más baja.
# creoamos una lista de notas.
notas=[5,7,6,8,9,10,7,2,3,5]
print("notas:")
for i in notas:
    print(i,end=" ")
print()    
#calculamos el promedio
promedio = sum(notas)/len(notas)
print("promedio: ",promedio)
#calculamos la notas mas alta y la mas minima
print("nota mas alta: ",max(notas))
print("nota mas vaja: ",min(notas))

#-------------------------------------------------------------------------------
#EJERCICIO 2
#-------------------------------------------------------------------------------
#2) Pedir al usuario que cargue 5 productos en una lista.
#• Mostrar la lista ordenada alfabéticamente. Investigue el uso del método sorted().
#• Preguntar al usuario qué producto desea eliminar y actualizar la lista.
# Pedir al usuario que ingrese 5 productos
productos = []

for i in range(5):
    producto = input(f"Ingrese el producto {i+1}: ")
    productos.append(producto)

# Mostrar la lista ordenada alfabéticamente usando sorted()
print("\nLista de productos ordenada alfabéticamente:")
productos_ordenados = sorted(productos)
print(productos_ordenados)

# Preguntar qué producto eliminar
eliminar = input("\n¿Qué producto desea eliminar?: ")

# Verificar si el producto está en la lista
if eliminar in productos_ordenados:
    productos_ordenados.remove(eliminar)
    print("\nLista actualizada después de eliminar el producto:")
    print(productos_ordenados)
else:
    print("\nEl producto no se encuentra en la lista.")

#-------------------------------------------------------------------------------
#EJERCICIO 3
#-------------------------------------------------------------------------------
#3) Generar una lista con 15 números enteros al azar entre 1 y 100.
#• Crear una lista con los pares y otra con los impares.
#• Mostrar cuántos números tiene cada lista.
#3) Generar una lista con 15 números enteros al azar entre 1 y 100.
#• Crear una lista con los pares y otra con los impares.
#• Mostrar cuántos números tiene cada lista.
import random
numeros=[]
# Generar lista con 15 números aleatorios entre 1 y 100
for i in range(15):
    numero_aleatorio= random.randint(1,100)
    numeros.append(numero_aleatorio)

# Crear listas para pares e impares
pares = []
impares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

# Mostrar resultados
print("Lista original de números:", numeros)
print("Números pares:", pares)
print("Cantidad de números pares:", len(pares))
print("Números impares:", impares)
print("Cantidad de números impares:", len(impares))

#-------------------------------------------------------------------------------
#EJERCICIO 4
#-------------------------------------------------------------------------------
#4) Dada una lista con valores repetidos:
#• Crear una nueva lista sin elementos repetidos.
#• Mostrar el resultado.
datos=[1,2,5,6,3,6,9,4,10]
sin_duplicados=[]

for i in datos:
    if i not in sin_duplicados:
        sin_duplicados.append(i)

print("lista original: ")
for d in datos:
    print(i, end=" ")
print ()

print ("lista sin duplicados")
for i in sin_duplicados:
    print(i,end=" ")
print()
#-------------------------------------------------------------------------------
#EJERCICIO 5
#-------------------------------------------------------------------------------
#Crear una Lista con los nombres de 8 estudiantes presentes en clase.

#Preguntar al usuario si quiere agregar un nuevo estudiante o eliminar uno existente.

#Mostrar la Lista final actualizada.

asistencia = ["Santiago", "Julian", "Morena", "Lucía", "Martina", "luis", "Karen", "Martín"]



print("Asistencia actual:")
for a in asistencia:
    print(a)


opcion = input("¿Desea agregar (A) o eliminar (E) un estudiante?").upper()

if opcion == "A":

    nuevo = input("ingrese el nombre a agregar:")

    asistencia.append(nuevo)

elif opcion == "E":

    eliminar=input ("Ingrese el nombre a eliminar: ")
    if eliminar in asistencia:


        asistencia.remove(eliminar)

    else:

        print("Ese estudiante no estaba en la lista")

print ("Lista final:")

for a in asistencia:
    print(a)

#-------------------------------------------------------------------------------
#EJERCICIO 6
#-------------------------------------------------------------------------------
#6) Dada una lista con 7 números, rotar todos los elementos una posición hacia la derecha (el último pasa a ser el primero).
numeros = [1,2,3,4,5,6,7]

ultimo = numeros[-1]
resto = numeros[:-1]
lista_rotada= [ultimo] + resto
print(lista_rotada)

lista_rotadaV2= numeros[-1:]+numeros[:-1]
print(lista_rotadaV2)

#-------------------------------------------------------------------------------
#EJERCICIO 7
#-------------------------------------------------------------------------------
#7) Crear una matriz (lista anidada) de 7x2 con las temperaturas mínimas y máximas de una semana.
#• Calcular el promedio de las mínimas y el de las máximas.
#• Mostrar en qué día se registró la mayor amplitud térmica.
temperaturas = [
    [12, 22],  
    [10, 24],  
    [14, 20],  
    [11, 25],  
    [9,  23],  
    [13, 21],  
    [10, 26]
]
minimas = [fila[0] for fila in temperaturas]
maximas = [fila[1] for fila in temperaturas]

prom_min = sum(minimas/len(minimas))
prom_max = sum(maximas/len(maximas))

amplitudes = [ fila[1]- fila [0]for fila in temperaturas]
dia_mayor_amplitud = amplitudes.index(max(amplitudes))+1
print("el dia con mayor amplitud es: ",dia_mayor_amplitud)
#-------------------------------------------------------------------------------
#EJERCICIO 8
#-------------------------------------------------------------------------------
notas = [
    [7, 8, 9],   # Estudiante 1
    [6, 5, 7],   # Estudiante 2
    [9, 8, 10],  # Estudiante 3
    [5, 6, 6],   # Estudiante 4
    [8, 7, 9]    # Estudiante 5
]
print("promedio de cada estudiante")

for fila in notas:
    for nota in fila:
        print (nota, end=" ")
    print()

print("Promedio de cada estudiante:")
for i in range(5):
    suma = 0
    for  j in range(3):
        suma += notas[i][j]
    promedio = suma / 3
    print (f"estudiante {i+1}: {promedio}")



# Promedio de cada materia
for j in range(3):
    suma = 0
    for i in range(5):
        suma += notas [i][j]
    promedio= suma / 5
    print(f"promedio materia {j+1}: {promedio:.2f}")

#-------------------------------------------------------------------------------
#EJERCICIO 9
#-------------------------------------------------------------------------------
#9) Representar un tablero de Ta-Te-Ti como una lista de listas (3x3).
#• Inicializarlo con guiones "-" representando casillas vacías.
#• Permitir que dos jugadores ingresen posiciones (fila, columna) para colocar "X" o "O".
#• Mostrar el tablero después de cada jugada
tablero = []
for i in range (3):
    fila = []
    for j in range (3):
        fila.append(fila)
    tablero.append(fila)

for fila in tablero:
    for celda in fila:
        print(celda, end= " ")
    print()
jugador ="x"
jugadas = 0
while jugadas < 9:
    print(f"\nturno del jugador {jugador}")

    fila = int(input("ingrese la fila (0-2)"))
    columna = int(input("ingrese la columna (0-2)"))
    
    if fila<0 or fila>2 or columna<0 or columna>2:
        print("posicion fuera de rango. intentar de nuevo")
        continue 

    if tablero[fila][columna] == "-":
        tablero[fila][columna]= jugador
        jugadas +=1
    else:
        print("casilla ocupada,inteta de nuevo")
        continue

    for fila in tablero:
        for celda in fila:
            print(celda, end= " ")
        print()
    if jugador== "x":
        jugador ="o"
    else:
        jugador = "x"
    