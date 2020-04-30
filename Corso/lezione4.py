"""
LEZIONE 4
@author ludovicobesana
Corso: Introduzione a Python - Enrico Girardi
"""

#Liste

variabile = 'testo variabile'
lista = [1,2,5,6,'testo', variabile, 40, 'testo2', 56]
#Se scrivo una variabile lista subito dopo all'altra vado a sovrascriverla
lista = [0,1,2,3,4,5,6,7,8,9,10]

#Stampa
#print(lista)

#Esempio di stampa in un ciclo
for i in lista:
    print(i)

#Slice (Fare a fette)
lista_spezzata1 = lista[0:3]
#Attenzione: si comincia da 0
#Attenzione: gli elementi sono esclusivi, ovvero esclude l'ultimo valore
print(lista_spezzata1)

#Passo - Prende gli elementi ogni x elementi

print(lista[1:5:2])

#IN = se è presente
print(lista)

elemento = input("Scrivi un numero:\n")
elemento = int(elemento)

if elemento in lista:
    print("E' nella lista")
else:
    print("Non è nella lista")

#Concatenare le liste
lista1 = [0,1,2,3,4,5]
lista2 = [5,6,7,8,9,10]

lista3 = lista1+lista2

print(lista3)

#Ripetizione
#Operatore * (Ripete gli elementi n volte)
lista = [1,2,3]
output = lista*3

print(output)

#Lunghezza in una lista
lista= [0,1,2,3,4,5,6,7,8,9,10]
lunghezza = len(lista)

print(lunghezza)
print(len(lista))

#Minimo e Massimo
lista = [30,41,2,3,4,5,6,7,8,9,10]
minimo = min(lista)
print("L'elemento minimo è:" +str(minimo))

massimo = max(lista)
print(massimo)
print("L'elemento massimo è:" +str(massimo))




