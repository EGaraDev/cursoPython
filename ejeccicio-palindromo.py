def noSpaceToLower(texto):
    return texto.replace(" ","").lower()

def esPalindromo(texto):
    texto = noSpaceToLower(texto)
    cont = -1
    for char in texto:
        if char != texto[cont]:
            return False
        cont -= 1
    return True


print("casa", esPalindromo("casa"))
print("neuquen", esPalindromo("neuquen"))
print("amo la paloma", esPalindromo("amo la paloma"))

## version curso

def no_space(texto):
    nuevoTexto = ""
    for char in texto:
        if char != " ":
            nuevoTexto += char
    return nuevoTexto

def reverse(texto):
    textoReves = ""
    for char in texto:
        textoReves = char + textoReves
    return textoReves

def es_palindromo(texto):
    texto = no_space(texto)
    textoReves = reverse(texto)
    return texto.lower() == textoReves.lower()

print("casa", es_palindromo("casa"))
print("neuquen", es_palindromo("neuquen"))
print("amo la paloma", es_palindromo("amo la paloma"))