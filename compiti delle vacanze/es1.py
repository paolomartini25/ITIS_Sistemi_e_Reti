# Scrivi una funzione generatrice di password. La funzione deve generare una stringa alfanumerica di 8 caratteri qualora l'utente voglia una password semplice, 
# o di 20 caratteri ascii qualora desideri una password più complicata.

import random

scelta=int(input('Inserisci 0 se vuoi che il programma generi una password semplice da 8 caratteri alfanumerici\nInserisci 1 se vuoi che il programma generi una password complessa da 20 caratteri ascii: '))

if (scelta == 0):#l'utente decide tra il generare una password corta o lunga, se decide quella corta:

    alfabeto = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    password = []

    controllo = random.randint(0,1) # questa variabile contiene casualmente 1 o 0 che sono rispettivamente la generazione di un numero o di una lettera 
    cont = 0 #questa variabile conta le ripetizioni tra numeri e lettere, se ci sono molti numeri ci sarà un numero grande positivo, se ci sono molte lettere ci sarà un mumero piccolo negativo

    print("la password generata è:")

    for indice in range(8):
        if(controllo == 1):
            password.append(random.randint(0,9)) # genero un numero randomico compreso tra 0 e 9
            cont = cont + 1 # incremento la variabile contatore
        else:
            password.append(alfabeto[random.randint(0,25)])# genero una ettera dell'alfabeto casuale
            cont = cont - 1 # decremento la variabile contatore

        controllo = random.randint(0,1) #genero casualmente la scelta tra 0 e 1

        if (cont>=2): # se il contatore sele sopra il due
            #il contatore viene settato a zero e il programma è obbligato a generare una lettera
            controllo=0
            cont = 0
        elif (cont<=-2):# se il contatore sele sopra il due
            #il contatore viene settato a zero e il programma è obbligato a generare un numero
            controllo=1
            cont = 0

    for elemento in password: #stampo la password generata
        print(elemento,end='')

elif (scelta == 1): #se decide quella lunga:
    print("la password generata è:")

    for indice in range(20):
        print(chr(random.randint(33,126)),end='')#viene generato e stampato un carattere ascii casuale
