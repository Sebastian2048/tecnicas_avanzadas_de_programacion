class Automovil():
    
# variables de automovil.

    def __init__(self, color, cant_puertas, nro_chasis, nro_motor, patente, puertas_close) -> None:
        self.color = color
        self.cant_puertas = cant_puertas
        self.nro_chasis = nro_chasis
        self.nro_motor = nro_motor
        self.patente = patente
        self.puertas_close = puertas_close
        
    def __str__(self) -> str:
        return f"Vehiculo patente {self.patente} color {self.color} con {self.cant_puertas} puertas"
        
# metodos de automovil.
    def auto_abierto(self):
        return True if (self.cant_puertas > self.puertas_close) else False
    
    def auto_arranca(self):
        return True if not (self.auto_abierto()) else False
    
    def auto_estacionado(self):
        return True if (self.auto_abierto() and not self.auto_arranca()) else False
    
    def auto_circulando(self):
        return True if (self.auto_arranca()) else False
    
    def auto_parado(self):
        return True if (self.auto_arranca() and self.auto_circulando()) else False
    
    def auto_gira(self):
        if (self.auto_circulando()):
            print("atento, en cualquier momento giramos")

# Nuestro Main

#Corsa= Automovil("rojo",5, 147852 , "S123AS" , "AB432WM" , 4 )
#print(Corsa)
#if Corsa.auto_arranca():
 #   print("vamos de paseo")
#else: print("verificar las puertas")

#Corsa.puertas_close = 5

#if Corsa.auto_arranca():
 #   print("nos vamos a casa")
#else: 
 #   print("nos quedamos")
