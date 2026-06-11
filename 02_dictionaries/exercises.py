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
