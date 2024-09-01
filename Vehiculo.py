class Vehiculo():
    
# estado de vehiculo.

    def __init__(self, patente, marca, modelo) -> None:
        self.patente = patente
        self.marca = marca
        self.modelo = modelo
        self.__enmarcha = False
        self.__estacionado = True
        self.__kmxhora = 0
        
    def __str__(self) -> str:
        estado = " y esta en marcha" if self.__enmarcha else " y esta parado" + f" a {self.__kmxhora} km/h"
        return f"{self.patente} {self.marca} {self.modelo} "
    
# metodo de vehiculo

    def chequeo(self):
        return (not self.__enmarcha and self.__estacionado and self.__kmxhora == 0)
    
    def arrancar(self):
        if self.chequeo():
            self.__enmarcha = True
            self.__estacionado = False
            self.__kmxhora = 10
            print(self, f"arrancamos, salimos del estacionamiento y aceleramos de 0 a {self.__kmxhora} km/h")
        else: 
            self.__enmarcha = False
            self.__estacionado = True
            print ("por problemas internos no se puede arrancar el vehiculo")

    def acelerar(self):
        if (self.__enmarcha and not self.__estacionado):
            self.__kmxhora +=10
            print(f"el vehiculo patente {self.patente} acelero y ahora va a {self.__kmxhora} km/h")
        else: 
            print (f"el vehiculo patente {self.patente} no acelero y mantiene velocidad de {self.__kmxhora} km/h")

    def stop(self):
        if self.__enmarcha:
            self.__enmarcha = False
            self.__estacionado = True
            self.__kmxhora = 0  # Añadir para poner la velocidad a 0 al detenerse
            print("El vehículo ha parado.")
        else:
            print("El vehículo sigue en movimiento.")

    def circulando(self):
        return self.__enmarcha
    
    def estacionado(self):
        return self.__estacionado
    