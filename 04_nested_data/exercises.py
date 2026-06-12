## Lista de listas

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for f in matriz:
    print(f)

## Recorrer todos los elementos de una matriz

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for f in matriz:
    for c in f:
        print(c)

##  Sumar todos los elementos de una matriz

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

suma = 0

for f in matriz:
    for c in f:
        suma += c

print(suma)

## Contar pares e impares en una matriz

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

pares = 0
impares = 0

for f in matriz:
    for c in f:
        if c % 2 == 0:
            pares += 1
        else:
            impares += 1

print(pares, impares)

## Lista de estudiantes

estudiantes = [
    {"nombre": "Ana", "nota": 4.5},
    {"nombre": "Luis", "nota": 3.2},
    {"nombre": "Carlos", "nota": 2.8},
    {"nombre": "Sofia", "nota": 5.0}
]

for e in estudiantes :
    print(e["nombre"])

## Mostrar estudiantes aprobados

estudiantes = [
    {"nombre": "Ana", "nota": 4.5},
    {"nombre": "Luis", "nota": 3.2},
    {"nombre": "Carlos", "nota": 2.8},
    {"nombre": "Sofia", "nota": 5.0}
]

for e in estudiantes:
    if e["nota"] >= 3:
        print(f"Pasa {e['nombre']}")


## Promedio de notas

suma = 0

for e in estudiantes:
    suma += e["nota"]

promedio = suma / len(estudiantes)

print(promedio)

## Mejor estudiante

mejor = estudiantes[0]

for e in estudiantes:
    if e["nota"] > mejor["nota"]:
        mejor = e

print(mejor)

## Agregar estado a cada estudiante

for e in estudiantes:
    if e["nota"] >= 3:
        e["estado"] = "Aprobado"
    else:
        e["estado"] = "Reprobado"

print(estudiantes)