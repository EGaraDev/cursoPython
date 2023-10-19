mascotas = ["pelusa","pulga","felipe","pulga","chanchito feliz","obi"] 

mascotas.insert(1,"melvin") # agregas un elemento en la posicion indicada los demas elementos se desplazan
print(mascotas)

mascotas.append("chanchito triste") # agrega un elemento al final de la lista
print(mascotas)

mascotas.remove("pulga") # busca el elemento y lo borra, si hay repetidos borra el primero que aparece
print(mascotas)

mascotas.pop(1) # por default borra el ultimo elemento si se agrega  el indice por parameto borrara ese elemento
print(mascotas)

del mascotas[0] #  borra el elemento indicado por parametro
print(mascotas)

mascotas.clear() # elimina todos los elementos
print(mascotas)