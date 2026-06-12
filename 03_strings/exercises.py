## Imprimir caracteres

texto = "Python"

for l in texto:
    print(l)

## Contar caracteres manualmente

texto = "backend"

longitud = 0

for l in texto:
    longitud += 1

print(f"Tiene un total de {longitud} letras")

## Convertir texto

nombre = "mario volkmar"

print(f"{nombre.upper()} \n{nombre.lower()} \n{nombre.title()}")

## Limpiar espacios

texto = "   Python Backend   "

print(f"Texto original = {texto} \nTexto limpio = {texto.strip()}")

## Contar vocales

texto = "programacion"

vocales = "aeiou"
contador = 0

for l in texto:
    if l in vocales:
        contador += 1
    
print(f"Vocales: {contador}")

## Contar consonantes

texto = "backend python" 

vocales = "aeiou"
abecedario = "qwertyuiopasdfghjklñzxcvbnm"

consonantes = 0

for i in texto:
    if i in abecedario and i not in vocales:
        consonantes += 1
    
print(f"Consonates = {consonantes}")

## Contar vocales, consonantes y espacios

texto = "FastAPI framework"

vocales = "aeiou"
abecedario = "qwertyuiopasdfghjklñzxcvbnm"

vocal = 0
letras = 0
espacios = 0

for i in texto:
    if i.lower() in vocales:
        vocal += 1
    elif i.lower() in abecedario and i not in vocales:
        letras += 1
    elif i == " ":
        espacios += 1

print(vocal , letras, espacios)

## Reemplazar palabras

texto = "Estoy aprendiendo Java"

texto_modificado = texto.replace("Java", "Python")

print(texto_modificado)

## Verificar palabra dentro de frase

frase = "Python es excelente para backend"
palabra = "backend"

print("Palabra encontrada") if palabra in frase else print("Palabra no encontrada")

## Separar frase en palabras

frase = "Estoy aprendiendo estructuras de datos"

lista_frase = frase.split()

print(lista_frase)

## Contar palabras

frase = "Python es un lenguaje muy usado en backend"

palabras = frase.split()

cantidad_palabras = len(palabras)

print(cantidad_palabras)

## Unir palabras

palabras = ["Python", "es", "genial"]

frase = " ".join(palabras)

print(frase)

## Invertir texto manualmente

texto = "python"
invertido = ""

for i in range(len(texto) - 1, -1 , -1):
    invertido += texto[i]

print(invertido)

invertido2 = texto[::-1]

print(invertido2)

## Detectar palíndromo

palabra = "radar"

if palabra == palabra[::-1]:
    print("Es palindromo")
else: 
    print("No es palindromo")

## Palíndromo ignorando espacios

frase = "anita lava la tina"

lista_palabras = frase.split()

frase_no_espacios = "".join(lista_palabras)

print("Es palindromo ") if frase_no_espacios == frase_no_espacios[::-1] else print("No es palindromo")

## Contar una letra específica

texto = "banana"
letra = "a"
contar = 0

for t in texto :
    if t.lower() == letra:
        contar += 1

print(f"a = {contar}")

## Limpiar texto con símbolos

texto = "Hola!!! Estoy, aprendiendo... Python???"

abecedario = "qwertyuiopasdfghjklñzxcvbnm"

texto_sin = ""

for i in texto:
    if i.lower() in abecedario or i == " ":
        texto_sin += i

print(texto_sin)

## Crear slug

titulo = "      Curso de Python Backend           "

titulo_mod = titulo.strip().lower().replace(" " , "-")

print(titulo_mod)

## Validar email simple

email = "mario@example.com"

contiene_arroba = False
contiene_punto = False
no_inicia_arroba = False
no_finaliza_arroba = False

if "@" in email:
    contiene_arroba = True
if "." in email:
    contiene_punto = True
if email[0] != "@" :
    no_inicia_arroba = True
if email[-1] != "@" :
    no_finaliza_arroba = True

print("Email Valido") if contiene_arroba and contiene_punto and no_inicia_arroba and no_finaliza_arroba else print("Email invalido")

## Normalizador de nombres

nombre = "   mArIo   vOLkMaR   "

nombre = nombre.strip().title().split()

nombre_normalizado = " ".join(nombre)

print(nombre_normalizado)




