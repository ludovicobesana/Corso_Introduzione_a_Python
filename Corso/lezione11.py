"""
LEZIONE 11
@author ludovicobesana
Corso: Introduzione a Python - Enrico Girardi
"""

#Lista
lista = [0,1,2,3]
print(lista)

lista.append(4)
print(lista)

lista.extend(5)
print(lista)

#Tupla (è una lista non modificabile)

tupla1 = (1,2,3,4,1,1,1,1,4,6,3,4)

#Count
print(tupla1.count(1))

#Index
print(tupla1.index(1))
