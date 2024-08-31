# Algoritmo ProcesarTRIANGULOS
# D.E: a,b,c,altura DOUBLE  y  elegirAreaPerimetro string
# D.S: Perimetro, Area Double y  tipotriangulo STRING
# Comenzar
     # LeerDatos(a,b,c);
      #tipotriangulo = IdentificarTipoTriangulo(a,b,c);
      #eligeArea = ElegirAreaOPerimetro()
      #Si (eligeArea)
          #entonces   Area=CalcularArea(base,altura);
          #sino         Perimetro =CalcularPERIMETRO(a,b,c);
       #ImprimirResultados(resultado)
#fin
from math import sqrt, log10

def es_triangulo (a,b,c):
    return (a+b>c) and (a+c>b) and (c+b>a)

def cual_es_tu_tipo(a,b,c):
    if (a==b) and (a==c):
        tipo = "triangulo equilatero"
    elif (a==c) or (a==b):
        tipo = "triangulo isoceles"
    else: tipo = "triangulo escaleno"
    return tipo

def formula_heron (a,b,c):
    s = (a+b+c)/2
    return sqrt (s*(s-a)*(s-b)*(s-c))

def elegir_area_perimetro ():
    if (input ("ingrese 'perimetro o area' ") == "perimetro"):
        perimetro = a+b+c
        area = None
    else: 
        area = formula_heron (a,b,c)
        perimetro = None
    return perimetro, area

def imprimir_resultado (tipo_de_triangulo , calculo_a , calculo_p):
    """imprime resultado"""
    print("mi triangulo es " + tipo_de_triangulo)
    if (calculo_a == None):
        print("el perimetro del triangulo es " , calculo_p )
    else: print("el area del triangulo es" , calculo_a)

a = float (input("ingrese el lado a "))
b = float (input("ingrese el lado b "))
c = float (input("ingrese el lado c "))

if (es_triangulo (a,b,c)):
    tipo_de_triangulo = cual_es_tu_tipo (a,b,c)
    calculo_p , calculo_a = elegir_area_perimetro ()
    imprimir_resultado (tipo_de_triangulo , calculo_a , calculo_p)
else: print("eso no es un triangulo")
imprimir_resultado()