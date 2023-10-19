def getProduct(**datos):  # al  usar ** podemos ingresar cuantos parametros querramos
    print(datos["id"], datos["name"])


getProduct(id = "001", 
           name = "iphone", 
           desc = "esto es un iphone")  # es fundamental ingresar tanto parametro como argumento ya que creara un diccionario