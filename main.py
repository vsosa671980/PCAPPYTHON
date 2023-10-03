### Preparación para Pcap

## Literales,
## Numericos, int boolean booleanos

entero = 5

## Para saber el tipo de entero que es
type(entero)

## Para trabajar en octal
octal = 0o342
print(octal)

## Para trabajar en Hexadecimal
hexadecimal = 0x3A

## Para representarlo
entero = 1_000_000
print(entero)

##Flotantes
flotante = 6.5
type(flotante)
##Podemos representarlo solo con la parte entero
flotante = 3.
## Con Anotación cientifica
flotante= 4e2 # SEria igula que indicar (4*10**2) => 400.0
print(flotante)
## Cadenas de caracteres
cadena1 = "Mi cadena"
type(cadena1)
## Cadenas multilinea
cadena2 = """
cadena Multilinea
"""
##Booleanos True or False
booleano = True
type(booleano)
## Null en python es None
ausencia = None
type(ausencia)

 ### -- OPERADORES Y EXPRESIONES --- ###
"""Si los dos son enteros el resultado es entero pero si uno de los dos es flotante
los dos son flotantes, ---la división siempre da flotante---"""
suma = 4 + 8
resta = 4 - 8
divisionEntera = 4 // 8 
exponenciación = 4 ** 5

"""La division entera nos devuelve el entero mas bajo
Cuidado cuando se trabaja con numeros negativos"""

print(4 / 3)
print(4 // 3) #Nos devuelve el entero inferior mas cercano

## OPERADORES DE COMPRACION
"""Siempre devuelven un valore booleano.
Hay que tener cuidado cuando se trabajan con diferentes tipos, ejemplo entero y flotante,
pyhton convierte el entero al flotante"""
print ( 1 == 1 )

"""Cuando comparamos un valor con una cadena no lo convierte y en este caso dara False"""
"""Si comparamos un valor booleano con un entero True -> 1 y False -> 0"""


## OPERADORES LOGICOS




