numeros = [1,2,3]

##feo
# primero = numeros[0]
# segundo = numeros[1]
# tercero = numeros[2]

primero, segundo, tercero = numeros # asigna variable a cada elemento de la lista

print(primero) # imprime 1

prim, *otros = numeros # asignamos el primero valor a la variable prim y el resto de elementos a la variable otros

print(prim, otros)

num = [1,2,3,4,5,6,7,8,9]

pri, seg, *otros, penul,ult = num # guarda en pri el primer elem en seg el segundo , en penul el penultimo en ult el ultimo y en otros el resto

print(pri,seg,otros, penul,ult)

