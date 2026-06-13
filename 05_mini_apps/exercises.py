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

## Sistema de usuarios

usuarios = []

while True:
    s = input("1. Registrar usuario 2. Login 3. Desconectar  4. Ver usuarios 5. Desactivar usuario 6. Salir ")
    if s == "1":
        usuario = input("Usuario: ")
        password = input("Clave: ")
        estado = True
        login = False
        u = {
            "usuario" : usuario.strip() ,
            "password" : password.strip(),
            "estado" : estado ,
            "login" : login
        }
        for cl in usuarios:
            if cl["usuario"] == usuario:
                print("Usuario ya en uso")
                break
        else:
            usuarios.append(u)
    elif s == "2":
        busq = input("Usuario: ")
        clave = input("Contraseña: ")
        for u in usuarios:
            if (u["usuario"] == busq.strip() and u["password"] == clave.strip()) and u["estado"]:
                print("Ingreso concedido")
                u["login"] = True
                break
        else:
            print("Clave o usuario errados")
    elif s == "3":
        busq = input("Usuario: ")
        for u in usuarios:
            if u["usuario"] == busq and u["login"]:
                print("Desconexion exitosa")
                u["login"] = False
                break
        else:
            print("Error")
    elif s == "4":
        print(usuarios)
    elif s == "5":
        busq = input("Usuario: ")
        for u in usuarios:
            if u["usuario"] == busq.strip() and u["login"]:
                print("Cambio de estado generado")
                u["estado"] = False
                u["login"] = False
                break
        else:
            print("Error Login")
    elif s == "6":
        break
    else:
        print("Error")


## Biblioteca básica

libros = []

while True:
    s = input("1. Agregar libro 2. Ver libros 3. Buscar libro 4. Prestar libro 5. Devolver libro 6. Salir ")
    if s == "1":
        titulo = input("Titulo: ")
        autor = input("Autor: ")
        libro = {
            "titulo" : titulo ,
            "autor" : autor ,
            "disponible" : True
        }
        libros.append(libro)
    elif s == "2":
        print(libros)
    elif s == "3":
        busq = input("Titulo: ")
        for l in libros:
            if l["titulo"] == busq:
                print(f"Encontrado {l}")
                break
        else:
            print("No existe")
    elif s == "4":
        busq = input("Titulo: ")
        for l in libros:
            if l["titulo"] == busq and l["disponible"]:
                l["disponible"] = False
                print(f"Prestamo ejecutado {l}")
                break
        else:
            print("Error")
    elif s == "5":
        busq = input("Titulo: ")
        for l in libros:
            if l["titulo"] == busq and not l["disponible"]:
                l["disponible"] = True
                print(f"Devolucion ejecutada {l}")
                break
        else:
            print("Error")
    elif s == "6":
        break
    else:
        print("Error input")


## Control de gastos

gastos = []

while True:
    s = input("1. Agregar gasto 2. Ver gastos 3. Total gastado 4. Total por categoría 5. Salir ")
    if s == "1":
        descripcion = input("Gasto: ")
        categoria = input("Categoria: ")
        valor = float(input("Valor: "))
        gasto = {
            "descripcion" : descripcion ,
            "categoria" : categoria ,
            "valor" : valor
        }
        gastos.append(gasto)
    elif s == "2":
        print(gastos)
    elif s == "3":
        total = 0
        for g in gastos:
            total += g["valor"]
        print(f"Total {total}")
    elif s == "4":
        categorias = {}
        for g in gastos:
            if g["categoria"] not in categorias:
                categorias[g["categoria"]] = 0
            categorias[g["categoria"]] += g["valor"]
        print(categorias)
    elif s == "5":
        break
    else:
        print("Error input")

## Registro de ventas

ventas = []

while True:
    s = input("1. Registrar venta 2. Ver ventas 3. Calcular ingresos totales 4. Producto más vendido 5. Salir ")
    if s == "1":
        producto = input("Producto: ")
        cantidad = int(input("Cantidad: "))
        precio = float(input("Precio: "))
        v = {
            "producto" : producto ,
            "cantidad" : cantidad ,
            "precio" : precio
        }
        ventas.append(v)
    elif s == "2":
        print(ventas)
    elif s == "3":
        total = 0
        for v in ventas:
            total += (v["precio"] * v["cantidad"])
        print(f"El total fue: {total}")
    elif s == "4":
        max = ventas[0]
        for v in ventas:
            if v["cantidad"] > max["cantidad"]:
                max = v
        print(f"El producto mas vendido es: {max}")
    elif s == "5":
        break
    else:
        input("Error input")

## Encuesta simple

respuestas = []

while True:
    s = input("1. Agregar respuesta 2. Ver respuestas 3. Contar sí 4. Contar no 5. Salir ")
    if s == "1":
        pregunta = input("Pregunta: ")
        respuesta = input("Si o No: ")
        if respuesta.lower() == "si":
            r = True
        else:
            r = False
        ingreso = {
            "pregunta" : pregunta,
            "respuesta" : r
        }
        respuestas.append(ingreso)
    elif s == "2":
        print(respuestas)
    elif s == "3":
        sis = 0
        for r in respuestas:
            if r["respuesta"]:
                sis += 1
        print(f"Afirmativas: {sis}")
    elif s == "4":
        nos = 0
        for r in respuestas:
            if not r["respuesta"]:
                nos += 1
        print(f"Negativas: {nos}")
    elif s == "5":
        break
    else:
        print("Error input")

## Sistema de cursos

cursos = []

while True:
    s = input("1. Crear curso 2. Ver cursos 3. Agregar estudiante a curso 4. Ver estudiantes de un curso 5. Salir ")
    if s == "1":
        nombre = input("Nombre Curso: ")
        for curso in cursos:
            if curso["nombre"] == nombre:
                print("El curso ya exite")
                break
        else:
            c = {
                    "nombre" : nombre ,
                    "estudiantes" : []
                }
            cursos.append(c)
    elif s == "2":
        print(cursos)
    elif s == "3":
        busq = input("Curso ")
        for c in cursos:
            if c["nombre"].lower() == busq.lower():
                while True:
                    est = input("Ingrese el estudiante / 0 para Salir")
                    if est == "0":
                        break
                    c["estudiantes"].append(est)
                break
        else: 
            print("El curso no existe")
    elif s == "4":
        busq = input("Curso ")
        for c in cursos:
            if c["nombre"].lower() == busq.lower():
                print(f"Curso: {c}")
    elif s== "5":
        break
    else:
        print("Error input")

## Gestor de proyectos

proyectos = []

while True:
    s = input("1. Crear proyecto 2. Agregar tarea a proyecto 3. Ver proyectos 4. Marcar tarea como completada 5. Salir ")
    if s == "1":
        nombre = input("Nombre proyecto: ")
        for p in proyectos:
            if p["nombre"] == nombre:
                print("Ese proyecto ya existe")
                break
        else:
            proy = {
                "nombre" : nombre ,
                "tareas" : []
            }
            proyectos.append(proy)
    elif s == "2":
        busq = input("Nombre proyecto: ")
        for p in proyectos:
            if p["nombre"] == busq:
                while True:
                    titulo = input("Ingresa tarea // Marca 0 para salir ")
                    if titulo == "0":
                        break
                    tarea ={
                        "titulado" : titulo,
                        "estado" : False
                    }
                    p["tareas"].append(tarea)
                break
        else:
            print("No existe ese proyecto")
    elif s == "3":
        print(proyectos)
    elif s == "4":
        busq = input("Nombre proyecto: ")
        for p in proyectos:
            if p["nombre"] == busq:
                busq_tarea = input("Nombre tarea: ")
                for t in p["tareas"]:
                    if t["titulado"] == busq_tarea:
                        t["estado"] = True
                        print(f"Estado de {t} actualizado")
                        break
                else:
                    print("No existe esa tarea")
                break
        else:
            print("No existe ese proyecto")
    elif s  == "5":
        break
    else:
        print("Error input")

## Sistema de soporte básico

tickets = []

while True:
    s = input("1. Crear ticket 2. Ver tickets 3. Buscar ticket por id 4. Cerrar ticket 5. Salir ")
    if s == "1":
        id = str(len(tickets) + 1)
        cliente = input("Nombre cliente: ")
        problema = input("Queja: ")
        estado = True
        t = {
            "id" : id ,
            "cliente" : cliente ,
            "problema" : problema ,
            "estado" : estado
        }
        tickets.append(t)
    elif s == "2":
        print(tickets)
    elif s == "3":
        busq = input("Id: ")
        for t in tickets:
            if t["id"] == busq:
                print(f"Ticket encotrado: {t}")
                break
        else:
            print("No existe ese ticket")
    elif s == "4":
        busq = input("Id: ")
        for t in tickets:
            if t["id"] == busq:
                t["estado"] = False
                print(f"Ticket cerrado - {t}")
                break
        else:
            print("No existe ese ticket") 
    elif s == "5":
        break
    else:
        print("Error input")  


## Procesador de texto simple

texto = input("Ingresa texto: ")

texto_aux = texto.strip().lower().split()
texto = " ".join(texto_aux).capitalize()

c_palabras = len(texto_aux)
max_palabra = max(texto_aux, key = len)

c_py = 0
for p in texto_aux:
    if p.lower() == "python":
        c_py += 1

slug = []
for p in texto_aux:
    if len(p) >= 3 and p not in slug:
            slug.append(p)
slug = "-".join(slug)

print(texto, c_palabras , max_palabra, c_py, slug)

## Mini CRM de clientes

clientes = []

while True:
    s = input("1. Agregar cliente 2. Ver clientes 3. Buscar cliente por email 4. Cambiar estado 5. Filtrar por estado 6. Salir ")
    if s == "1":
        id = str(len(clientes) + 1)
        nombre = input("Nombre cliente: ")
        email = input("Email cliente ")
        for c in clientes:
            if c["email"] == email:
                print("Error, email ya usado")
                break
        else:
            while True:
                estado = input("1. Prospecto 2. Contactado 3. Cliente 4. Inactivo ")
                if estado == "1":
                    estado = "Prospecto"
                    break
                elif estado == "2":
                    estado = "Contactado"
                    break
                elif estado == "3":
                    estado = "Cliente"
                    break
                elif estado == "4":
                    estado = "Inactivo"
                    break
                else: 
                    print("Error input")
            cliente = {
                "id" : id ,
                "nombre" : nombre ,
                "email" : email ,
                "estado" : estado
            }
            clientes.append(cliente)
    elif s == "2":
        print(clientes)
    elif s == "3":
        busq = input("Email cliente: ")
        for c in clientes:
            if c["email"] == busq:
                print(f"Cliente encontrado - {c}")
                break
        else:
            print("Correo no existe")
    elif s == "4":
        busq = input("Id cliente: ")
        for c in clientes:
            if c["id"] == busq:
                while True:
                    estado = input("Nuevo Estado - MARCA // 1. Prospecto 2. Contactado 3. Cliente 4. Inactivo ")
                    if estado == "1":
                        c["estado"] = "Prospecto"
                        break
                    elif estado == "2":
                        c["estado"] = "Contactado"
                        break
                    elif estado == "3":
                        c["estado"] = "Cliente"
                        break
                    elif estado == "4":
                        c["estado"] = "Inactivo"
                        break
                    else: 
                        print("Error input")
                print(f"Estado actualizado - {c}")
                break
        else:
            print("No existe ese ID")
    elif s == "5":
        res = []
        while True:
                estado = input("Busqueda Estado - MARCA // 1. Prospecto 2. Contactado 3. Cliente 4. Inactivo ")
                if estado == "1":
                    estado = "Prospecto"
                    break
                elif estado == "2":
                    estado = "Contactado"
                    break
                elif estado == "3":
                    estado = "Cliente"
                    break
                elif estado == "4":
                    estado = "Inactivo"
                    break
                else: 
                    print("Error input")
        for c in clientes:
            if c["estado"] == estado:
                res.append(c)
        print(f"Clientes con estado {estado} son: {res}")
    elif s == "6":
        break
    else:
        print("Error input")
