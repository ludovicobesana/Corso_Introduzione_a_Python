"""
LEZIONE 14
@author ludovicobesana
Corso: Introduzione a Python - Enrico Girardi
"""

"""
OPERATORI
"""
#Operatori booleani

#AND, OR, NOT

elem1 = input("Scrivi il primo numero: \n")
elem2 = input("Scrivi il secondo numero: \n")
elem3 = input("Scrivi il terzo numero: \n")

#AND OR

if int (elem1) > 0 and int(elem2) < 20:
    print("caso uno")

elif int(elem1) > 10 or int(elem2) > 20:
    print("caso due")

else:
    print("caso default")

elem1 = input("Scrivi il primo numero: \n")
elem2 = input("Scrivi il secondo numero: \n")
elem3 = input("Scrivi il terzo numero: \n")

#NOT

if int (elem1) > 0 and int(elem2) < 20:
    print("caso uno")

elif int(elem1) > 10 or int(elem2) > 20:
    print("caso due")

elif not int(elem3):
    print("caso tre")
