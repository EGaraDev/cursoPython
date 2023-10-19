print("Bienvenido a la calculadora \n Para salir escribe Salir")
print("operaciones: sum, rest, mult, div")

numero = ""

while True:
    
    if numero == "": # se puede colocar if not resultado
        numero = input("Ingrese un numero: ")
        if numero.lower() == "salir":
            break
        numero = float(numero)
    op = input("Ingresa operacion: ")
    if op.lower() == "salir":
            break
    num2 = input("ingresa siguiente numero: ")
    if num2.lower() == "salir":
            break
    num2 = float(num2)

    if op.lower() == "sum":
        numero += num2
    elif op.lower() == "rest":
        numero -= num2
    elif op.lower() == "mult":
        numero *= num2
    elif op.lower() == "div":
        numero /= num2
    else:
        print(f"{op} no es una operacion valida")
        
    print(f"El resultado es: {numero}")

print("Hasta luego")