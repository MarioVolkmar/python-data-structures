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

## 




