from Vehiculo import *
class Furgoneta(Vehiculo):
    
    def __init__(self, patente, marca, modelo) -> None:
        super().__init__(patente, marca, modelo)
        self.carga = 0
        
    def __str__(self) -> str:
        return super().__str__() + f"cargada con {self.carga} kg"
    
    def chequeo(self):
        return super().chequeo() and self.carga >= 0 and self.carga <= 1000
    
    def cargarfurgoneta(self,cargaenkilos):
        if self.chequeo() and ((1000 - self.carga) >= cargaenkilos) :
            self.carga += cargaenkilos
            print("usted aun puede cargar" + int(1000-cargaenkilos) + " kilos")
        else:
            print("no se puede cargar debido a problemas en los limites de carga")
    
    def descargarfurgoneta(self, cargaenkilos):
        if self.chequeo () and self.carga >= cargaenkilos:
            self.carga -= cargaenkilos
        else: 
            print(f"problemas en el limite de descarga, usted solo puede descargar {self.carga}")
            
#main de prueba
Parner = Furgoneta("INF013","peugeot","patagonia")
print(Parner)

Parner.chequeo()

Parner.arrancar()

Parner.acelerar()
Parner.acelerar()
Parner.acelerar()
Parner.acelerar()
Parner.acelerar()

Parner.circulando()
if (Parner.circulando()):
    print("el vehiculo esta en movimiento")
else: 
    print("el vehiculo no se mueve")

if Parner.estacionado():
    print("el vehiculo estaciono")

Parner.stop()

cargaenkilos = 200

Parner.cargarfurgoneta(320)

Parner.descargarfurgoneta(120)