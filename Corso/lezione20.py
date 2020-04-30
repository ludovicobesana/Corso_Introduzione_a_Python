"""
LEZIONE 20
@author ludovicobesana
Corso: Introduzione a Python - Enrico Girardi
"""

"""
FUNZIONI
"""

#FUNZIONE

def somma(a,b):
    c = int(a) + int(b)
    return c

def moltiplicazione(a,b):
    c = int(a) * int(b)
    return c

#VARIABILE CON FUNZIONE

dastampare = somma(2,4)
print(dastampare)

dastampare2 = moltiplicazione(2,4)
print(dastampare2)
