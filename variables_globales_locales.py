def potencia(base,exponente):
    variable_local_potencia="soy una variable local a la funcion potencia"
    acumuladorProductos=1
    for i in range(exponente):
        acumuladorProductos*=base
        print("***********")
        print("------ dentro fn potencia -----")
        print("------ dentro del for ---------")
        print(" i es local al for - valor i : ",i)
        print(" variable local a fn potencia ",variable_local_potencia)
        print(" variable global a potencia(local al Main) :",variable_local_MAIN)
    print("-------- salida del for ---------")
    print(" i es local al for - valor i : ",i)
    print(" variable local a fn potencia ",variable_local_potencia)
    print("variable global a potencia(local al Main) :",variable_local_MAIN)
    return acumuladorProductos  

# MAIN-------------
variable_local_MAIN="soy una variable local al MAIN => global a todos"
base=int(input("ingrese base "))
exponente=int(input("ingrese exponente "))
resultado=potencia(base,exponente)
print("///////////////////////////////")
print("------ MAIN -------------------")
print(base,"elevado a",exponente," = ",resultado)
print("variable global a potencia(local al Main) :",variable_local_MAIN)
#print(" variable local a fn potencia ",variable_local_potencia)