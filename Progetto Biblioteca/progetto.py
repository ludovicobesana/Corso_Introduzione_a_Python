"""
ARCHIVIO LIBRI
@author ludovicobesana
Corso: Introduzione a Python - Enrico Girardi
"""
#Aggiungo la libreria json
import json

#Carico i dati da file .json
with open('archivio.json','r') as file:
    archivio =  json.load(file)

# Condizione di partenza
condizione = True

menu = """\nMENU
        0- Stampa Menu 
        1- Aggiungi Autore
        2- Aggiungi Libro
        3- Stampa Archivio 
        4- Stampa Autori 
        5- Salva 
        ESCI. [Esci]
        """
print(menu)

while condizione == True:

    comando = input('Scegli in comando:\n')

    #ESCI- Fine programma
    if comando == 'ESCI':
        condizione = False
        print("FINE PROGRAMMA")
        break

    #0- Stampa menu
    if int(comando) == 0:
        print(menu)

    #1- Input nuovo autore
    elif int(comando) == 1:
        autore = input("Aggiungi un nuovo autore:\n")
        archivio[autore] = []

    #2- Input nuovo libro ad un autore
    elif int(comando) == 2:

        #Lista degli autori
        lista_autori = []
        i = 0
        for el in archivio.keys():
            print("\tAUTORE: "+str(el)+' CODICE:'+str(i))
            lista_autori.append(el)
            i += 1

        #Input Autore
        id_autore = input("Scrivi l'ID dell'autore  del libro:\n")
        autore = lista_autori[int(id_autore)]

        #Input Titolo
        libro = input("Scrivi il nome del libro:\n")
        archivio[autore].append(libro)

    #3- Stampa generale
    elif int(comando) == 3:
        print("\nIL NOSTRO ARCHIVIO:\n")

        for k,v in archivio.items():
            print("\nAUTORE: "+str(k))
            print("\tLIBRI: ")
            for el in v:
                print("\t\t"+str(el))

    #4- Stampa Autori
    elif int(comando) == 4:
        print("ELENCO AUTORI:")
        for el in archivio.keys():
            print("\t"+str(el))

    #Salva i dati nel file .json
    elif int(comando) == 5:
        with open('archivio.json', 'w') as file:
            json.dump(archivio, file)

"""

[

{'Dante': [ 
    {'libro':'La Vita Nuova', 'isbn':'5636363', 'data-pubbblciazione':'1300'},
    {'libro':'La Vita Nuova', 'isbn':'5636363', 'data-pubbblciazione':'1300'}
    ]
    
{'autore':'Ungaretti', 'libri':['Libro1', 'Libro2], 'isbn':'563636234433', 'data-pubbblciazione':'1900'}

]

{'Dante': ['La Divina Commedia', 'La Vita Nuova'], 'Pascal': ['LibroPSca']}
"""