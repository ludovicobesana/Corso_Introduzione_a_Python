"""
LEZIONE 6
@author ludovicobesana
Corso: Introduzione a Python - Enrico Girardi
"""

lista1 = ['a','b','c']
lista2 = ['c','f','g']

lista0 = [lista1,lista2]

print(lista0)
print("*************")

for i in lista0:
    #print(i)
    for e in i:
        print(e)
"""
#Concatenazione
concat = lista1+lista2
print(concat)
"""

print("\n")
lista3 = []
print("Lista 3 vuota: ")
print(lista3)
print("\n")

#Ciclo

for i in lista0:
    #print(i)
    for e in i:
        #print(e)
        lista3.append(e)
print("\n")
print("Lista 3 piena: ")
print(lista3)
