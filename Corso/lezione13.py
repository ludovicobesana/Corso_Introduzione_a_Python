"""
LEZIONE 13
@author ludovicobesana
Corso: Introduzione a Python - Enrico Girardi
"""

"""
OPERATORI
"""
#Operatori di confronto

a = 10
b = 20

#Uguaglianza
print(a == b)

#Maggiore e minore
print(a > b)
print(a < b)

#Diverso
print(a != b)

a = 10
b = 10

#Maggiore e minore
print(a >= b)
print(a <= b)

#Programma che individua utilizzando il modulo se il numero è PARI o DISPARI

elem1 = input("Scrivi il primo numero: \n")
elem2 = input("Scrivi il secondo numero: \n")

if int(elem1) <= int(elem2):
    print("Il primo numero è minore uguale al secondo")
else:
    print("Il primo numero è maggiore uguale al secondo")

if int(elem1) < int(elem2):
    print("Il primo numero è minore al secondo")
elif int(elem1) > int(elem2):
    print("Il primo numero è maggiore al secondo")
elif int(elem1) == int(elem2):
    print("Il primo numero è uguale al secondo")

