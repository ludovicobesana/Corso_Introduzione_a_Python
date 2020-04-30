"""
LEZIONE 16
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

#CICLO WHILE

condizione = True

while condizione == True:
    print("VERA")
    elem= input("Inserisci un numero\n")
    if int(elem)%2 == 0: #Se il numero è pari, il resto della divisione è uguale a 0
        condizione = False
        print("FINE DEL PROGRAMMA")