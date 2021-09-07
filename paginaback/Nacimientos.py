class nacimiento:

 def __init__(self,nombre,precio,tamanio,cantidad,tipo):

    self.nombre =nombre
    self.precio = precio
    self.tamanio =tamanio
    self.cantidad =cantidad
    self.tipo = tipo

 def setNombre(self,nombre):
     self.nombre = nombre
 def setPrecio(self,precio):
     self.precio = precio
 def setTamanio(self,tamanio):
     self.tamanio = tamanio
 def setCantidad(self,cantidad):
         self.cantidad = cantidad
 def setTipo(self,tipo):
         self.tipo = tipo

 

 def getNombre(self):
        return  self.nombre

 def getPrecio(self):
        return  self.precio

 def getTamanio(self):
    return  self.tamanio
 def getCantidad(self):
        return  self.cantidad
 def getTipo(self):
        return  self.tipo

 