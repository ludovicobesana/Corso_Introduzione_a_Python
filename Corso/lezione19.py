"""
LEZIONE 19
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
a = int(a)

while a < 10:
    print(a)

    if a == 4:
        print("HAI VINTO")
        break

    a += 1

else:
    print("HAI PERSO!")