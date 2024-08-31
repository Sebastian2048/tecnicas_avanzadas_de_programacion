#leer una secuencia de caracteres y contar la cant de digitos letras y otros caracteres que contiene la secuencia.
# DE = SECUENCIA USUARIO
# DS = SECUENCIA DEL USUARIO , CANT DIGITOS , CANT LETRAS, CANT OTROS CARACT. , TOTAL.
oracion = input ("ingrese su frase :")
#inicializar contadores
cont_digito = 0
cont_letra = 0
cont_caracteres = 0
#revisar que tiene la oracion ingresada
for i in range (len (oracion)):
    if oracion [i].isdigit():
        cont_digito += 1
    elif oracion [i].isalpha():
        cont_letra += 1
    else: cont_caracteres += 1
print(oracion, cont_digito , cont_letra, cont_caracteres, cont_digito+cont_letra+cont_caracteres)