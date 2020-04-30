"""
LEZIONE 15
@author ludovicobesana
Corso: Introduzione a Python - Enrico Girardi
"""

"""
OPERATORI
"""
#Operatori Condizionali (IF - ELIF - ELSE)
elem1 = input("Scrivi il primo numero: \n")
elem2 = input("Scrivi il secondo numero: \n")
elem3 = input("Scrivi il terzo numero: \n")

#Controllo 1
if int (elem1) > 0 and int(elem2) < 20:
    print("caso uno")

    if int(elem1) == 9:
        print("NOVE")
    elif int(elem1) == 8:
        print("OTTO")
    else:
        print("ALTRO")

#Controllo 2
if int(elem1) > 10 or int(elem2) > 20:
    print("caso due")

elif not int(elem3):
    print("caso tre")

else:
    print("Altro caso ")

