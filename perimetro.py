# PerimetroFigura
# DE: N, M entero
# DS: Perimetro  real

#Obtengo lobtengo datos entrada
N= int(input("Ingrese Perimetro del rectángulo:"))
M= int(input("Ingrese Perimetro del triangulo:"))

# realizo calculo
b=N/3
a=b/2
c=(M-b)/2

Perímetro = 2*a + 2*c + b

#Mostrar en Pantalla el resultado 
print("El perímetro es " + str(Perímetro))