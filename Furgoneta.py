# Importar la clase Vehiculo
from Vehiculo import *

class Furgoneta(Vehiculo):
    
    def __init__(self, patente, marca, modelo) -> None:
        super().__init__(patente, marca, modelo)
        self.carga = 0
        
    def __str__(self) -> str:
        return super().__str__() + f" cargada con {self.carga} kg"
    
    def chequeo(self):
        return super().chequeo() and 0 <= self.carga <= 1000
    
    def cargarfurgoneta(self, cargaenkilos):
        if self.chequeo() and (1000 - self.carga) >= cargaenkilos:
            self.carga += cargaenkilos
            print(f"usted aun puede cargar {1000 - self.carga} kilos")
        else:
            print("no se puede cargar debido a problemas en los limites de carga")
    
    def descargarfurgoneta(self, cargaenkilos):
        if self.chequeo() and self.carga >= cargaenkilos:
            self.carga -= cargaenkilos
            print(f"usted aun puede descargar {self.carga} kilos")
        else: 
            print(f"problemas en el limite de descarga, usted solo puede descargar {self.carga}")
            
# Main de prueba
Parner = Furgoneta("INF013", "peugeot", "patagonia")
print(Parner)

print(Parner.chequeo())

Parner.arrancar()

Parner.acelerar()
Parner.acelerar()
Parner.acelerar()
Parner.acelerar()
Parner.acelerar()

if Parner.circulando():
    print("el vehiculo esta en movimiento")
else: 
    print("el vehiculo no se mueve")

if Parner.estacionado():
    print("el vehiculo estaciono")

Parner.stop()

Parner.cargarfurgoneta(1000)

print(Parner.chequeo())

Parner.arrancar()

Parner.acelerar()
Parner.acelerar()
Parner.acelerar()
Parner.acelerar()
Parner.acelerar()

if Parner.circulando():
    print("el vehiculo esta en movimiento")
else: 
    print("el vehiculo no se mueve")

if Parner.estacionado():
    print("el vehiculo estaciono")

Parner.stop()

Parner.descargarfurgoneta(650)

print(Parner.chequeo())

Parner.arrancar()

Parner.acelerar()
Parner.acelerar()
Parner.acelerar()
Parner.acelerar()
Parner.acelerar()

if Parner.circulando():
    print("el vehiculo esta en movimiento")
else: 
    print("el vehiculo no se mueve")

if Parner.estacionado():
    print("el vehiculo estaciono")

Parner.stop()

Parner.cargarfurgoneta(300)
Parner.descargarfurgoneta(150)