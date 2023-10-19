def suma(*numeros): #  colocando el * delante del parametro este se vuelve un iterable
    resultado = 0
    for numero in numeros:
        resultado += numero
    print (resultado)


suma(2,5)
suma(2,4,7)
suma(2,10,20,30)