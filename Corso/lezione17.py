"""
LEZIONE 17
@author ludovicobesana
Corso: Introduzione a Python - Enrico Girardi
"""

"""
CICLI
    FOR
    WHILE
    BREAK, CONTINUE
    FOR ELSE
    WHILE ELSE
"""

#CICLO FOR

lista = [1,2,3,3,3,4,5,5,6]

for elemento in lista:

    if elemento == 2:
        continue  #Salta il ciclo e va avanti

    if elemento == 5:
        break #Blocca l'esecuzione del programma

    print(elemento)