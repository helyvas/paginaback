from flask import Flask,jsonify,request
from flask_cors import CORS
import json
from Nacimientos import nacimiento

app = Flask(__name__) 
CORS(app)
n = [] 

n.append(nacimiento('Nacimiento','18','1cm','20','Extra pequeño'))
n.append(nacimiento('Nacimiento','22','1.5cm','22','pequeño'))
n.append(nacimiento('Nacimiento','25','2cm','40','Mediano'))
n.append(nacimiento('Nacimiento','35','5cm','30','grande'))
n.append(nacimiento('Angel','125','15 cm','30','Fino'))

@app.route('/', methods = ['GET'] )
def most():
    return ("<h1>AQUI INICIA TODO MUSIC STATION CARNET: 201700852</h1>")


 
@app.route('/Datos', methods = ['GET'] )
def Obtenerdatos():
      global n
      Datos = []
      Dat = {} 
      for datos in n:
            Dat = {"Nombre":datos.getNombre(),
                   "Precio":datos.getPrecio(),
                   "Tamaño":datos.getTamanio(),
                   "Cantidad":datos.getCantidad(),
                   "Tipo":datos.getTipo()
                   }
            print(datos.getTipo()) 
            Datos.append(Dat)
      respuesta =jsonify(Datos)
      return(respuesta)

@app.route('/Datos', methods = ['POST'] ) 
def Datos(): 
      global n

      Nombre = request.json['Nombre']
      Precio = request.json['Precio']
      Tamaño = request.json['Tamaño']
      Cantidad = request.json['Cantidad'] 
      
      tipo1 = 'Extra pequeño'
      tipo2 = 'pequeño'
      tipo3 = 'mediano'
      tipo4 ='grande'
      
      #este es para localizar al usuario
      sielusuariesta = False
      for datos in n:
          if datos.getTipo() == tipo1:
                sielusuariesta = True 
                break
      if  sielusuariesta:    
             return jsonify({
                       'message':'Failed',
                        'reason':'El usuario que ingresastes ya se encuentra registrado'
                             })
      else:
             nuevo_dato = nacimiento(Nombre,Precio,Tamaño,Cantidad,tipo1)
             n.append(nuevo_dato) 
             return jsonify({
                     'message':'Success',
                      'reason' :'Se ha registrado exitosamente',
                      'tipo': datos.getTipo()
                      
             }) 

 

@app.route('/Datos/<string:nombre>', methods = ['PUT'] )
def Actualizardato(nombre):
      global n 
 
  

      for i in range(len(n)):
            if nombre == n[i].getTipo():
               n[i].setNombre(request.json['Nombre'])
               n[i].setPrecio(request.json['Precio'])
               n[i].setTamanio(request.json['Tamaño'])
               n[i].setCantidad(request.json['Cantidad'])
               n[i].setTipo(request.json['Tipo'])
               
               break

      return jsonify({'message':'se ha actualizado el dato '})


@app.route('/Datos/<string:nombre>', methods = ['GET'] )
def Consultardato(nombre):
      global n

  

      for nombres in n:
            if nombres.getTipo() == nombre:

                  Dat = {
                    'Nombre':nombres.getNombre(),
                   'Precio':nombres.getPrecio(),
                   'Tamaño':nombres.getTamanio(),
                   'Cantidad':nombres.getCantidad(),
                   'Tipo':nombres.getTipo()
                     }

                  break
      respuesta =jsonify(Dat)
      return(respuesta)
if __name__=='__main__':
    app.run( threaded = True,  host="0.0.0.0",port = 3000,debug = True)