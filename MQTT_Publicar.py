#importación de librerías
import paho.mqtt.client as mqttClient
import time


"""Aquí debes crear las variables en donde recibirás los datos del sensor"""
var1
var2

"""Envío de datos a través de MQTT"""
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Conectado al broker")
        global Connected    #Variable global
        Connected = True    #Señal de conexión
    else:
         print("Fallo en la conexion")

Connected = False                   #Variable global para verificar estado de conexión
broker_address= "broker.hivemq.com" #Aquí se coloca la dirección de broker
port = 1883                         #Puerto por default 1883
"""para modificar el tag se debe usar la siguiente estructura:
/IoT/Estacion/(Número de Estación)/Parametros"""
tag="/IoT/Estacion/1/Temperatura"   #Etiqueta

client = mqttClient.Client("Python")             #creamos una nueva instancia
#client.username_pw_set(user, password=password)  #establece usuario y contraseña
client.on_connect= on_connect                    #adjunta función
client.connect(broker_address, port=port)        #conecta al broker
client.loop_start()         #inicia el ciclo
while Connected != True:    #Espera la conexión
    time.sleep(0.1)

    try:                    #método de envío de información
        value = '{"l":"'+str(var1)+'","t":"'+str(var2)+'"}'
        print(tag, value)
        client.publish(tag,value,qos=2)
        time.sleep(1)
    except KeyboardInterrupt: #Cuando detenemos el envío se desconecta del servidor
        print("Envío de mensajes detenido por el usuario")
        client.disconnect()
        client.loop_stop()
