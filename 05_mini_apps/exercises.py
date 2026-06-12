## Lista de compras simple

compras = []

while True:
    solicitud = input("1. Agregar producto 2. Ver lista 3. Eliminar último producto 4. Salir ")
    if solicitud == "1":
        producto = input("Ingresa el nombre del producto ")
        precio = input("Ingresa el precio del producto ")
        cantidad = input("Ingresa la cantidad del producto ")
        compras.append([producto, float(precio), int(cantidad)])
    elif solicitud == "2":
        print(compras)
    elif solicitud == "3":
        if len(compras) > 0:
            compras.pop()
    elif solicitud == "4":
        break
    else:
        print("Ingreso errado")

## Lista de tareas

tareas = []

while True:
    solicitud = input("1. Agregar tarea 2. Ver tareas 3. Marcar tarea como completada 4. Salir ")
    if solicitud == "1":
        titulo = input("Nombre Tarea ")
        estado = "pendiente"
        tareas.append({
            "titulo" : titulo ,
            "estado" : estado
        })
    elif solicitud == "2":
        print(tareas)
    elif solicitud == "3":
        tarea = input("Ingrese el titulo de la tarea ")
        for t in tareas:
            if t["titulo"] == tarea:
                t["estado"] = "completada"
                break
        else:
            print("Tarea no encontrada")
    elif solicitud == "4":
        break
    else:
        print("Opcion no valida")

## Agenda de contactos

contactos = []

while True:
    solicitud = input("1. Agregar contacto 2. Ver contactos 3. Buscar contacto por nombre 4. Salir ")
    if solicitud == "1":
        nombre = input("Ingrese el nombre del contacto ")
        telefono = input("Ingrese el telefono ")
        email = input("Ingrese el email ")
        contacto = {
            "nombre" : nombre ,
            "telefono" : telefono ,
            "email" : email
        }
        contactos.append(contacto)
    elif solicitud == "2":
        print(contactos)
    elif solicitud == "3":
        busqueda = input("Ingrese el contacto a buscar")
        for c in contactos:
            if c["nombre"].lower() == busqueda.lower() :
                print(f"Contacto encontrado {c}")
                break
        else:
            print("El contacto no existe")
    elif solicitud == "4":
        break
    else:
        print("Ingreso invalido")

## Inventario básico

inventario = []

while True:
    solicitud = input("1. Agregar producto 2. Ver inventario 3. Buscar producto 4. Actualizar stock 5. Salir ")
    if solicitud == "1":
        nombre = input("Ingresa el nombre del producto ")
        precio = input("Ingrese el precio del producto ")
        stock = input ("Ingrese el stock del producto ")
        producto = {
            "nombre" : nombre ,
            "precio" : precio ,
            "stock" : stock
        }
        inventario.append(producto)
    elif solicitud == "2":
        print(inventario)
    elif solicitud == "3":
        busqueda = input("Ingrese el nombre del producto ")
        for p in inventario:
            if p["nombre"] == busqueda:
                print(f"Producto encontrado {p}")
                break
        else:
            print("Producto inexistente")  
    elif solicitud == "4":
        busqueda = input("Ingrese el nombre del producto ")
        nuevo_stock = input("Ingrese el nuevo stock ")
        for p in inventario:
            if p["nombre"] == busqueda:
                p["stock"] = nuevo_stock
                break
        else:
            print("Producto inexistente")
    elif solicitud == "5":
        break
    else:
        print("Opcion invalida")

## Sistema de notas

notas = []

while True:
    solicitud = input("1. Agregar nota 2. Ver notas 3. Calcular promedio 4. Ver nota mayor 5. Ver nota menor 6. Salir ")
    if solicitud == "1":
        while True:
            n = float(input("Ingrese una nota de 0 a 5 "))
            if 0 <= n <= 5:
                print(f"Nota {n} agregada")
                notas.append(n)
                break
            else:
                print("Ingrese una nota valida")
    elif solicitud == "2":
        print(notas)
    elif solicitud == "3":
        sum = 0
        for n in notas:
            sum += n
        prom = sum / len(notas)
        print (f"El promedio es de: {prom}")
    elif solicitud == "4":
        print(f"La nota mayor es: {max(notas)}")
    elif solicitud == "5":
        print(f"La nota menor es: {min(notas)} ")
    elif solicitud == "6":
        break
    else:
        print("Ingreso invalido")

## Registro de estudiantes

estudiantes = []

while True:
    s = input("1. Agregar estudiante 2. Ver estudiantes 3. Ver aprobados 4. Ver reprobados 5. Salir ")
    if s == "1":
        nombre = input("Nombre: ")
        edad = input("Edad: ")
        notas = []
        sum = 0
        while True:
            nota = float(input("Ingrese las notas de 0 a 5 // Marque -1 para finalizar ingreso de notas "))
            if nota == -1:
                break
            elif 0 <= nota <= 5:
                print(f"Nota {nota} ingresada")
                sum += nota
                notas.append(nota)
            else:
                print("Error")
        prom = sum / len(notas)
        if prom >= 3:
            aprobado = True
        else:
            aprobado = False
        estudiante ={
            "nombre" : nombre ,
            "edad" : edad ,
            "notas" : notas ,
            "aprobado" : aprobado
        }
        estudiantes.append(estudiante)
    elif s == "2":
        print(estudiantes)
    elif s == "3":
        for n in estudiantes:
            if n["aprobado"] :
                print(f"Aprobado {n}")
    elif s == "4":
        for n in estudiantes:
            if not n["aprobado"] :
                print(f"Reprobado {n}")
    elif s == "5":
        break
    else:
        print("Error")

## Carrito de compras

carrito = []

while True:
    s = input("1. Agregar producto al carrito 2. Ver carrito 3. Calcular total 4. Eliminar último producto 5. Salir ")
    if s == "1":
        nombre = input("Producto: ")
        precio = float(input("Precio: "))
        cantidad = int(input("Cantidad: "))
        p = {
            "producto" : nombre,
            "precio" : precio, 
            "cantidad" : cantidad
        }
        carrito.append(p)
    elif s == "2":
        print(carrito)
    elif s == "3":
        total = 0
        for c in carrito :
            sub_total = c["precio"] * c["cantidad"]
            c["subtotal"] = sub_total
            total += sub_total
        print(f"El total del carrito es de {total}")
    elif s == "4":
        if len(carrito) > 0:
            carrito.pop()
    elif s == "5":
        break
    else:
        print("Error")

## Buscador de palabras

frases = []

while True:
    s = input("1. Agregar frase 2. Ver frases 3. Buscar palabra 4. Salir ")
    if s == "1":
        frase = input("Frase: ")
        frases.append(frase.lower())
    elif s == "2":
        print(frases)
    elif s == "3":
        busqueda = input("Palabra busqueda: ")
        for f in frases:
            aux = f.split()
            if busqueda in aux:
                print(f"{busqueda} - Frase: {f}")
                break
        else:
            print("Palabra no encontrada")
    elif s == "4" :
        break
    else:
        print("Error")

## Contador de palabras

frase = input("Ingresa una frase: ")
frase = frase.strip()

vocales = "aeiou"
letras = "qwertyuiopasdfghjklñzxcvbnm"

c_palabras = len(frase.split())
c_caracteres = len(frase)
c_vocal = 0
c_consonante = 0
c_espacios = 0
c_simbolos = 0

for f in frase :
    if f.lower() in vocales:
        c_vocal += 1
    elif f.lower() in letras and f.lower() not in vocales:
        c_consonante += 1
    elif f == " ":
        c_espacios += 1
    else:
        c_simbolos += 1

print(f"Palabras: {c_palabras} - Caracteres: {c_caracteres} - Vocales: {c_vocal} - Consonantes: - {c_consonante} - Espacios: {c_espacios} - Simbolos: {c_simbolos}")


## Normalizador de nombres

nombres = []

while True:
    s = input("1. Agregar nombre 2. Ver nombres normalizados 3. Salir ")
    if s == "1":
        nombre = input("Nombre: ")
        nombre = nombre.strip().title().split()
        nombre = " ".join(nombre)
        nombres.append(nombre)
    elif s == "2":
        print(nombres)
    elif s == "3":
        break
    else:
        print("Error")

## 

