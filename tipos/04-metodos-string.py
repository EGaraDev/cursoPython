animal = "    chanCHito feliz    "
print(animal.upper())  # metodo para llevar todas las letras a mayuscula
print(animal.lower())  # metodo para llevar todas las letras a minuscula
print(animal.strip().capitalize())  # metodo para llevar la primer letra a mayus y demas a minus
print(animal.title())  # metodo para llevar la primer letra de cada palabra a mayuscula y demas a minuscula
print(animal.strip()) # metodo que elimina los espacios al comienzo y final del string
print(animal.lstrip())  # quita los espacios a la izquierda
print(animal.rstrip())  # quita los espacios a la derecha
print(animal.find("CH"))  # busca cadena de caracteres dentro del string y devuelve la posicion de inicio
print(animal.find("cH"))  # si no lo encuentra devuelve -1
print(animal.replace("nCH","j"))  # busca cadena de caracteres y la reemplaza por el parametro indicado
print("nCH" in animal)  # retorna buleano 
print("nCH" not in animal)