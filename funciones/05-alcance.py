saludo = "hola global"

def saludar():
    saludo = ("hola mundo")
    print(saludo)

def saludaChanchito():
    saludo = ("hola chanchito")
    print(saludo)



saludar()
saludaChanchito()
print(saludo)


def potencia(base,expo):
    if expo == 0:
        return 1
    resultado = base * potencia(base,expo-1)
    return resultado

print(potencia(2,10))
