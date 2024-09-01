from Vehiculo import *

Camion = Vehiculo("AB432WM","fiat", "siena")
print(Camion)

Camion.chequeo()

Camion.arrancar()

Camion.acelerar()
Camion.acelerar()
Camion.acelerar()

Camion.circulando()
if (Camion.circulando()):
    print("el vehiculo esta en movimiento")
else: 
    print("el vehiculo no se mueve")

if Camion.estacionado():
    print("el camion estaciono")
    
Camion.stop()