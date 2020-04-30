"""
LEZIONE 8
@author ludovicobesana
Corso: Introduzione a Python - Enrico Girardi
"""

from traceback import print_last

lista1 = ['a','b','c']
lista2 = ['c','f','g']

a = lista1.extend(lista2)

print(a)

#APPEND

lista1.append([1,2,3])
print("\nAPPEND")
print(lista1)

#EXTEND

lista1.extend([1,2,3])
print("\nEXTEND")
print(lista1)
