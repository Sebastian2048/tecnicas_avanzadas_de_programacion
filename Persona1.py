from Perro import *

class Persona():
    #variables de clase 
    _tienelunares=False
    __tienepecas=False 
    tienecanas=False

#Constructor
    def __init__(self, nombre, apellido,trabaja, edad) -> None:
        self.nombre=nombre
        self.apellido=apellido
        self._trabaja=trabaja
        self.__edad=edad

#Metodos
#Metodos de consulta
    def edad(self):         # OJO no olvidarse nunca Nunca NUNCA el self como parametro en cada metodo
        return self.__edad
    
    def __str__(self) -> str:
        return self.apellido.upper() + ", " + self.nombre.capitalize() + " tiene " + str(self.edad()) +" años"


#################### MAIN
andrea=Persona("andrea","dosantos",True,37)
print(andrea)
andrea.apellido = "storniolo"
print(andrea.apellido)
sebastian= Persona("Sebastian", "Molina", False, 30)
print(sebastian)
print(andrea.tienecanas)
#print(sebastian.__tienepecas)
print(not sebastian._tienelunares)
sebastian._tienelunares = True
print(sebastian._tienelunares)
print(andrea._tienelunares)
invitados= [andrea, sebastian]
print(invitados)
for item in invitados:
    print(item)

coker = Perro ("coker", "fatiga" , "marron")
print(coker)
coker.ladrar()



#print(andrea.__edad)
print(andrea.edad())
#print(andrea.__tienepecas)
#print(andrea._tienelunares)
#print(andrea.tienecanas)
#andrea.__tienepecas=True
#andrea._tienelunares=True
#andrea.tienecanas=True
#print(andrea.__tienepecas)
#print(andrea._tienelunares)
#print(andrea.tienecanas)