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

## Inventario con categorías

inventario = {
    "tecnologia": ["Laptop", "Mouse", "Teclado"],
    "hogar": ["Silla", "Mesa", "Lampara"],
    "ropa": ["Camisa", "Pantalon", "Zapatos"]
}


for k in inventario:
    mensaje = k + "\n"
    for p in inventario[k]:
        mensaje += f"- {p} \n"
    print(mensaje)

## Contar productos por categoría

inventario = {
    "tecnologia": ["Laptop", "Mouse", "Teclado"],
    "hogar": ["Silla", "Mesa", "Lampara"],
    "ropa": ["Camisa", "Pantalon", "Zapatos"]
}

for k in inventario:
    print(f"{k}: {len(inventario[k])}")

## Buscar producto en inventario

producto_buscado = "Mouse"

for k in inventario :
    if producto_buscado in inventario[k]:
        print(f"{producto_buscado} esta en la categoria {k}")
        break
else:
    print("Producto no encontrado")

## Diccionario de usuarios con roles

usuarios = [
    {"username": "mario", "rol": "admin", "activo": True},
    {"username": "ana", "rol": "user", "activo": True},
    {"username": "luis", "rol": "user", "activo": False},
    {"username": "sofia", "rol": "moderator", "activo": True}
]

for u in usuarios:
    if u["activo"] :
        print(u)

## Contar usuarios por rol

conteo_roles = {}

for u in usuarios:
    if u["rol"] not in conteo_roles:
        conteo_roles[u["rol"]] = 0
    conteo_roles[u["rol"]] += 1

print(conteo_roles)

## Pedidos de una tienda

pedidos = [
    {
        "id": 1,
        "cliente": "Mario",
        "productos": [
            {"nombre": "Laptop", "precio": 2500000},
            {"nombre": "Mouse", "precio": 80000}
        ]
    },
    {
        "id": 2,
        "cliente": "Ana",
        "productos": [
            {"nombre": "Teclado", "precio": 120000},
            {"nombre": "Monitor", "precio": 900000}
        ]
    }
]


for p in pedidos:
    print(p["cliente"])


## Total por pedido

for p in pedidos:
    total = 0
    for b in p["productos"]:
        total += b["precio"]
    print(f"Pedido {p['id']} - Cliente: {p['cliente']} - Total: {total}")

## Pedido más costoso

mayor = pedidos[0]

for p in pedidos:
    total = 0
    for b in p["productos"]:
        total += b["precio"]
    p["total"] = total
    if p["total"] > mayor["total"]:
        mayor = p

print(f"El pedido mas costoso {mayor['id']} - Cliente {mayor['cliente']} - Total {mayor['total']}")

## Mini sistema de cursos

cursos = [
    {
        "nombre": "Python Basics",
        "estudiantes": ["Mario", "Ana", "Luis"]
    },
    {
        "nombre": "SQL Fundamentals",
        "estudiantes": ["Sofia", "Carlos"]
    },
    {
        "nombre": "FastAPI Intro",
        "estudiantes": []
    }
]

conteo = {}

for c in cursos:
    conteo[c["nombre"]] = len(c["estudiantes"])

print(conteo)

## Agregar estudiante a un curso

cursos = [
    {
        "nombre": "Python Basics",
        "estudiantes": ["Mario", "Ana", "Luis"]
    },
    {
        "nombre": "SQL Fundamentals",
        "estudiantes": ["Sofia", "Carlos"]
    },
    {
        "nombre": "FastAPI Intro",
        "estudiantes": []
    }
]

curso_buscado = "FastAPI Intro"
nuevo_estudiante = "Mario"

for c in cursos:
    if c["nombre"] == curso_buscado:
        c["estudiantes"].append(nuevo_estudiante)
        break
else:
    print("Curso no encontrado")

print(cursos)





