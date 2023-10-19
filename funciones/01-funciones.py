def hola(nombre, apellido = "feliz"):  # se puedeagregar valor por default de parametro en caso que no se ingrese posteriormente
    print("hola mundo")
    print(f"Hola {nombre} {apellido}")


hola("eduardo", "garayalde")
hola("chanchito")  # el segundo argumento tomara por default "feliz" ya que no se ingreso uno nuevo



hola(apellido = "gara", nombre = "edu")  # se puede ingresar los parametros en orden distinto, siempre y cuando se declares a todos

