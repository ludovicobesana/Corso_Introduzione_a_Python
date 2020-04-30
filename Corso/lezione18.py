"""
LEZIONE 18
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

a = input("Inserisci un numero:\n")

for el in range(0,int(a)):
    print(el)

if el in range(int(a)):
    print(el)

    if el == 12:
        print("HAI VINTO")
    else:
        print("HAI PERSO")