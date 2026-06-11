## Crear e imprimir una lista

nombres = ["Mario", "Ana", "Luis", "Sofia", "Carlos"]

print (nombres)

for n in nombres:
    print(n)

## Acceder a elementos

frutas = ["manzana", "pera", "uva", "mango", "piña"]


print(f"La primera fruta es: {frutas[0]} y la ultima es: {frutas[-1]}")


## Modificar un elemento

colores = ["rojo", "azul", "verde"]

colores[colores.index("azul")] = "amarillo"

print(colores)

## Agregar elementos

numeros = [1, 2, 3]

numeros.extend([4,5])

print(numeros)


## Eliminar el último elemento

tareas = ["estudiar", "entrenar", "leer", "descansar"]

print(f"La tarea eliminada fue: {tareas.pop()} y la lista de tareas actual quedo como: {tareas}")


## Eliminar un elemento específico

lenguajes = ["Python", "Java", "C++", "JavaScript"]

lenguajes.remove("Java")

print(lenguajes)


## Verificar si un elemento existe

usuarios = ["mario", "ana", "luis"]
usuario_buscado = "mariO"

print("Usuario encontrado") if usuario_buscado in usuarios else print("Usuario no encontrado")

for u in usuarios:
    if u.lower() == usuario_buscado.lower():
        print("Usuario encontrado")
        break
else:
    print("Usuario no encontrado")


## Recorrer una lista

productos = ["pan", "leche", "huevos", "arroz"]

mensaje = ""

for p in productos:
    if  p == productos[-1]:
        mensaje += p 
    else:
        mensaje += p + ", "

print(f"La lista de productos es {mensaje}")


## Contar elementos manualmente

animales = ["perro", "gato", "conejo", "perro", "loro"]
longitud = 0

for a in animales:
    longitud += 1

print(f"La cantidad de animales es de {longitud}")


## Contar cuántas veces aparece un elemento

animales = ["perro", "gato", "conejo", "perro", "loro", "perro"]

n = 0

for a in animales:
    if a.lower() == "perro":
        n += 1

print(f"La cantidad de veces que aparace perro es de {n} veces")

## Sumar números de una lista

numeros = [10, 20, 30, 40, 50]

suma = sum(numeros)

suma2 = 0

for n in numeros:
    suma2 += n

print(suma,suma2)

## Promedio de una lista

notas = [4.0, 3.5, 5.0, 2.8, 4.2]

prom = sum(notas) / len(notas)

suma = 0

for n in notas:
    suma += n

promedio = suma / len(notas)

print(prom, promedio)

## Encontrar el mayor número 

numeros = [15, 8, 22, 3, 19]

maxi = max(numeros)

maximo = numeros[0]

for n in numeros:
    if n > maximo:
        maximo = n

print(maximo, maxi)

## Encontrar el menor número

numeros = [15, 8, 22, 3, 19]

meno = min(numeros)

menor = numeros[0]

for n in numeros:
    if n < menor:
        menor = n

print(menor, meno)


## Separar números pares

numeros = [1, 2, 3, 4, 5, 6, 7, 8]
pares = []

for n in numeros:
    if n % 2 == 0:
        pares.append(n)

print(pares)

## Separar positivos, negativos y ceros

numeros = [3, -1, 0, 7, -5, 0, 9, -2]
positivos = []
negativos = []
ceros = []

for n in numeros:
    if n == 0:
        ceros.append(n)
    if n > 0:
        positivos.append(n)
    else:
        negativos.append(n)

print(positivos, negativos, ceros)

## Crear una nueva lista con valores duplicados

numeros = [1, 2, 3, 4, 5]

dobles = []

for n in numeros:
    dobles.append(n*2)

print(dobles)

## Filtrar palabras largas

palabras = ["sol", "computador", "python", "backend", "ia"]

palabras_largas = []

for p in palabras:
    if len(p) > 5:
        palabras_largas.append(p)

print (palabras_largas)

## Lista de compras con menú

compras = []

while True:
    solicitud = input("'1' Agregar producto - '2' Ver producto - '3' Eliminar producto - '4' Salir ")
    if solicitud == "1":
        compra = input("Nombre producto")
        compras.append(compra)
    elif solicitud == "2":
        print(compras)
    elif solicitud == "3":
        if len(compras) > 0:
            compras.pop()
    elif solicitud == "4":
        break
    else:
        print("Ingreso invalido")

## Sistema simple de notas

notas = []

while True:
    nota = input("Ingrese una nota de 0 a 5 o salir")
    if nota.lower() == "salir":
        break
    elif 0 <= float(nota) <= 5:
        notas.append(float(nota))
    else:
        print("Nota Invalida")

print(f"Notas : {notas} \nMayor: {max(notas)} \nMenor: {min(notas)} \nPromedio: {sum(notas) / len(notas)}")