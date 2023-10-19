mascotas = ["wolfgang", "pelusa", "pulga", "copito", "obi", "dona"]
print(mascotas[0])
mascotas[0] = "bicho"
print(mascotas[0])

print(mascotas)
print(mascotas[1:3])  # accede desde el elemento 1 hasta el 3
print(mascotas[-1])  # accede al ultimo elemento
print(mascotas[::2]) # accede cada 2 elementos
print(mascotas[1::2])  # accede desde el elemento 1  cada 2 elementos
print(mascotas[0:3:2])  # accede desde el elemento 0  cada 2 elementos hasta el elemento 3

numeros = list(range(21))
print(numeros[::2])  #imprime los numero pares
print(numeros[1::2])  #imprime los numero impares