# EJEMPLO 1
def duplicar(x):
    print("valor recibido x: ",x)
    x *= 2
    print("valor x  despues de duplicar: ",x)
    return x
#Main
n= 1
print("valor n: ",n)
duplicar(n)
print("valor n despues duplicar(n) : ",duplicar(n))

n=[1,2,3,4]
print("valor n: ",n)
duplicar(n)
print("valor n despues duplicar(n) : ",duplicar(n))