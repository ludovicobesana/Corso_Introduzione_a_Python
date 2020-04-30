"""
LEZIONE 10
@author ludovicobesana
Corso: Introduzione a Python - Enrico Girardi
"""

#DIZIONARI

dizionario = {}

#chiave: key + valore: value

print("PRIMA")
dizionario = {'nome':'mario', 'cognome':'rossi'}
print(dizionario)

print("\nDOPO")
dizionario['nome'] = 'giuseppe'
print(dizionario)

#Possiamo scegliere di stampare il valore o la chiave
print("\nSTAMPA K,V ITEMS - 1")
for k,v in dizionario.items():
    print("chiave: "+str(k)+" valore: "+str(v))

print("\nSTAMPA V ITEMS - 2")
for k,v in dizionario.items():
    print("\t valore: "+str(v))

print("\nSTAMPA ELEMENTO - 3")
for el in dizionario.values():
    print("\t elemento: "+str(el))

print("\nSTAMPA ELEMENTO - CHIAVI")
for el in dizionario.keys():
    print("\t elemento: "+str(el))