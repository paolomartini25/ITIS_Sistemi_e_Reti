#Un indirizzo MAC (Media Access Control address) è un indirizzo univoco associato dal produttore, a una NIC, 
#composto da 6 coppie di cifre esadecimali separate da due punti.
#Un esempio di MAC è 02:FF:A5:F2:55:12.
#Scrivi una funzione genera_mac che generi degli indirizzi MAC pseudo casuali.

import random

esadecimale = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F'] #è una lista che contie i possibili numer esadecimali

def main():
    for indice in range(12):
        if (indice%2 == 0 and indice != 0): #inserisce i : dopo ogni coppia di numeri
            print(':',end='')
        print(random.choice(esadecimale),end='') #stampa un numero esadecimale casuale


if __name__ == "__main__":
    main()
    