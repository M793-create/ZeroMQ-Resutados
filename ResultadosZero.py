# Se importa zeromq
import zmq
# Se importa time
import time

# Se crea un zmq context
context = zmq.Context()
# Se crea un publisher socket
socket = context.socket(zmq.PUB)

#Direccion IP y puerto donde el servidor escucha las solicitudes
socket.bind("tcp://127.0.0.1:%s" % "5580")

# Tiempo
start = time.time()
# 100 Repeticiones
for x in range (100):
    # Se establece la connectionfilter
    connectionFilter = "Marvin"
    # Datos de envio
    msgToPublish = "Holaa"

    
    print("%s %s" % (connectionFilter, msgToPublish))
        
    socket.send_string("%s,%s" % (connectionFilter, msgToPublish))
  
end = time.time()
# Imprimir tiempo en milisegundos
print((end - start)*1000)