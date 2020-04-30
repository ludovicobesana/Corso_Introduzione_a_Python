"""
LEZIONE 12
@author ludovicobesana
Corso: Introduzione a Python - Enrico Girardi
"""

"""
OPERATORI
"""
#Operatori aritmetici

#Somma
print(1+2)

#Divisione
print(20/4)

#Sottrazione
print(10-3)

#Moltiplicazione
print(30+2)

#Modulo (Resto della divisione)
print(70/4)
print(70%4)

print(100%2)

#Programma che individua utilizzando il modulo se il numero è PARI o DISPARI

elem = input("Scrivi un numero: \n")

if int(elem) %2 == 0:
    print("Il numero è pari")
else:
    print("Il numero è dispari")



