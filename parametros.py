# Argumentos predeterminados o por default-------------------------------------------
# parámetro que asume un valor predeterminado si no se proporciona un valor en la llamada

def myFun(x, y=50):
    print("x: ", x)
    print("y: ", y)

# MAIN Llamamos a myFun() con solo 1 argumento:
myFun(10)     #  x: 10    y: 50
myFun(20,80)  #  x: 20    y: 80

# Argumentos de palabras clave---------------------------------------------------
# permitir especificar el nombre del argumento con valores 

def student(firstname, lastname):
	print(firstname, lastname)

# MAIN Argumentos de palabras clave
student(firstname='Hola', lastname='que tal')
student(lastname='Hola', firstname='que tal')

# Argumentos Posicionales ----------------------------------
# Usamos el argumento Positional durante la llamada de función para que el 
# primer argumento (o valor) se asigne a name 
# y el segundo argumento (o valor) se asigne a age. 
# Al cambiar la posición, o si olvida el orden de las posiciones, los valores se pueden usar en los lugares incorrectos.

def nameAge(name, age):
        print("Hola, soy", name)
        print("Mi edad es ", age)

print("Caso-1:")
nameAge("Suraj", 27)

print("\nCaso-2:")
nameAge(27, "Suraj")

# Argumentos  de palabras clave arbitrarias -----------------------------------
# En Python, los argumentos de palabras clave arbitrarias, *args y **kwargs 
# pueden pasar una cantidad variable de argumentos a una función usando 
# símbolos especiales:
# 	*args en Python (argumentos que no son palabras clave)
# 	**kwargs en Python (argumentos de palabras clave)

# Ejemplo 1: argumento de longitud variable que no es una palabra clave
# *args para un número variable de argumentos
def myFun(*args):
      for arg in args:
           print(arg)

myFun('Hola', 'Bienvenido', 'a', 'GeeksforGeeks')

#Example 2: Variable length keyword arguments
# *kwargs for variable number of keyword arguments

def myFun(**kwargs):
    for key, value in kwargs.items():
        print("%s == %s" % (key, value))

# MAIN
myFun(first='Geeks', mid='for', last='Geeks')

#Docstring
# La primera cadena después de la función se denomina  Docstring. 
# Se utiliza para describir la funcionalidad de la función. 
# El uso de docstring es opcional, pero se considera una buena práctica.

# Una función Python 
def par_impar(x):
	"""Función para verificar si el número es par o impar"""
	if (x % 2 == 0):
		print("even")
	else:
		print("odd")

# Código del controlador para llamar a la función
par_impar(4)
print(par_impar._doc_) #Función para verificar si el número es par o impar

# Funciones recursivas en Python 
# Recursion se refiere a la llamada de de la funcion a si misma. 
# Habra entonces muchas instancias de la funcion cuando utilizamos recursion para  resolver el problema
# WARNING!!! siempre tener una forma de salida de la recursion

def factorial(n):
    if n == 0:  
        return 1
    else:
        return n * factorial(n - 1) 
      
print(factorial(4))    # 24