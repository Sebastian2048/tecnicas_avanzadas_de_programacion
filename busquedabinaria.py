from random import randrange
from math import log2

nro = randrange(1, 300, 1)
max_valor = 300
min_valor = 0

cant_op = round(log2(max_valor))

for i in range (cant_op):
    medio = (max_valor - min_valor) // 2 + min_valor

    if ( medio == nro):
        print("lo encontraste")
        break
    elif ( nro > medio):
        min_valor = medio +1
    else: max_valor = medio -1
