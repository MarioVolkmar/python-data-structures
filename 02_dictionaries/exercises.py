## Crear e imprimir un diccionario

persona = {
    "nombre" : "Mario",
    "edad" : 32,
    "ciudad" : "Medellín"
}

print(persona)

## Acceder a valores

producto = {
    "nombre": "Laptop",
    "precio": 2500000,
    "stock": 5
}

print(f"Nombre: {producto['nombre']} \nPrecio: {producto['precio']} \nStock: {producto['stock']}")

## Modificar un valor

usuario = {
    "nombre": "Mario",
    "edad": 31,
    "activo": True
}

usuario["edad"] = 32

print(usuario)

## Agregar una nueva clave

libro = {
    "titulo": "Clean Code",
    "autor": "Robert C. Martin"
}

libro["paginas"] = 464

print(libro)

## Eliminar una clave

carro = {
    "marca": "Renault",
    "modelo": "Stepway",
    "año": 2021,
    "color": "gris"
}

carro.pop("color")

print(carro)

## Verificar si existe una clave

estudiante = {
    "nombre": "Ana",
    "curso": "Python",
    "nota": 4.5
}

print("La nota existe") if "nota" in estudiante.keys() else print("La nota no existe")

## Usar .get()

config = {
    "host": "localhost",
    "port": 8000
}


print(config.get("debug" , False))

## Recorrer claves

persona = {
    "nombre": "Mario",
    "edad": 32,
    "ciudad": "Medellín"
}

for k in persona.keys() :
    print(k)

## Recorrer valores

persona = {
    "nombre": "Mario",
    "edad": 32,
    "ciudad": "Medellín"
}

for v in persona.values() :
    print(v)

## Recorrer claves y valores

for k, v in persona.items():
    print(f"{k} : {v}")

## Contar productos en stock

producto = {
    "nombre": "Mouse",
    "precio": 80000,
    "stock": 0
}

print("Stock disponible") if producto["stock"] > 0 else print("Stock acabado")

## Actualizar stock

producto = {
    "nombre": "Teclado",
    "precio": 120000,
    "stock": 10
}

cantidad_vendida = 3

producto["stock"] -= cantidad_vendida

print(f"Stock acual: {producto['stock']}")

## Calcular valor total de inventario

producto = {
    "nombre": "Monitor",
    "precio": 900000,
    "stock": 4
}

producto["valor_total"] = producto["precio"] * producto["stock"]

print(f"El total de invetario es: {producto['valor_total']}")

## Diccionario dentro de lista

productos = [
    {"nombre": "Laptop", "precio": 2500000, "stock": 3},
    {"nombre": "Mouse", "precio": 80000, "stock": 10},
    {"nombre": "Teclado", "precio": 120000, "stock": 5}
]

for p in productos :
    print(p["nombre"])

## Sumar precios de productos

productos = [
    {"nombre": "Laptop", "precio": 2500000, "stock": 3},
    {"nombre": "Mouse", "precio": 80000, "stock": 10},
    {"nombre": "Teclado", "precio": 120000, "stock": 5}
]

suma = 0

suma = 0

for p in productos:
    suma += p["precio"]

print(f"Suma de precios: {suma}")

## Filtrar productos con stock

productos = [
    {"nombre": "Laptop", "precio": 2500000, "stock": 0},
    {"nombre": "Mouse", "precio": 80000, "stock": 10},
    {"nombre": "Teclado", "precio": 120000, "stock": 5},
    {"nombre": "Monitor", "precio": 900000, "stock": 0}
]

disponibles = []

for p in productos:
    if p["stock"] > 0:
        disponibles.append(p)

print(disponibles)

## Buscar producto por nombre

productos = [
    {"nombre": "Laptop", "precio": 2500000, "stock": 0},
    {"nombre": "Mouse", "precio": 80000, "stock": 10},
    {"nombre": "Teclado", "precio": 120000, "stock": 5},
    {"nombre": "Monitor", "precio": 900000, "stock": 0}
]


producto_buscado = "Mouse"

for p in productos:
    if p["nombre"] == producto_buscado:
        print(f"Producto encontrado: {p['nombre']} \nPrecio: {p['precio']} \nStock: {p['stock']}")
        break
else: 
    print("Producto no encontrado")

## Actualizar precio de un producto

productos = [
    {"nombre": "Laptop", "precio": 2500000, "stock": 3},
    {"nombre": "Mouse", "precio": 80000, "stock": 10},
    {"nombre": "Teclado", "precio": 120000, "stock": 5}
]

for p in productos:
    if p["nombre"] == "Mouse":
        p["precio"] = 95000
        break

print(productos)

## Mini sistema de usuario

usuario = {}

nombre = input("Ingresa tu nombre ")
edad = input("Ingresa tu edad ")
email = input("Ingresa tu email ")

usuario["nombre"] = nombre
usuario["edad"] = edad
usuario["email"] = email

print(usuario)

## Mini inventario con menú

inventario = []

while True:
    solicitud  =  input("1. Agregar producto 2. Ver productos  3. Buscar producto 4. Actualizar stock 5. Salir ")
    if solicitud == "1":
        nombre = input("Ingresa el nombre del producto ")
        precio = input("Ingresa el precio del producto ")
        stock = input("Ingresa el stock del producto ")
        producto = {
            "nombre" : nombre ,
            "precio" : precio ,
            "stock" : int(stock)
        }
        inventario.append(producto)
    elif solicitud == "2":
        print(inventario)
    elif solicitud == "3":
        producto_busqueda = input("Ingrese el nombre del producto ")
        for p in inventario :
            if p["nombre"] == producto_busqueda:
                print(f"Producto encontrado - {p}")
                break
        else:
            print("Producto no encontrado")
    elif solicitud == "4":
        producto_busqueda = input("Ingrese el nombre del producto ")
        stock_nuevo = int(input("Ingresa el nuevo stock "))
        for p in inventario :
            if p["nombre"] == producto_busqueda:
                p["stock"] = stock_nuevo 
                break
        else:
            print("Producto no encontrado")
    elif solicitud == "5":
        break
    else:
        print("Ingrese un dato valido")
