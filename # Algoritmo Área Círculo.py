# Algoritmo Área Círculo 
#    DE: radio (decimal)
#    DS: Area   (decimal)
# Inicio
#        leer (radio) 
#        Asignar a área círculo el resultado de Pi x radio x radio
#        mostrar El área es: área círculo
# fin
# Problema de donde obtenemos el valor de PI LIBRERIAS DE PYTHON =>math
# DICHO POPULAR "no volamos porque en python no esta esa libreria"

# importo la libreria math
from math import pi 

radio = int (input("Ingrese el radio del Círculo: "))
radio += 1.8
if (radio < 0):
    print("EL RADIO DEBE SER MAYOR O IGUAL A CERO")
else:
    print(f"el area del circulo con radio  {radio} es {pi * radio**2}")

contador = 7
contador = contador + 3
print (contador)
contador -= 2
print (contador)