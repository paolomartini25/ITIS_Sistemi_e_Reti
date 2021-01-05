#Il ROT-15 è un semplice cifrario monoalfabetico, in cui ogni lettera del messaggio da cifrare viene sostituita con quella posta 15 posizioni più avanti nell'alfabeto.
#Scrivi una semplice funzione in grado di criptare una stringa passata, o decriptarla se la stringa è già stata precedentemente codificata.

alfabeto = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def decripta(lettera):
    for indice, elemento in enumerate(alfabeto):
        if (lettera == elemento):
            num = indice - 15 #ritorno alla lettera originale scorrendo indietro nella lista di 15 posizioni 
            originale = alfabeto[num]
            print(originale,end='')
            

    

def cripta(lettera):
    for indice, elemento in enumerate(alfabeto):
        if (lettera == elemento):
            num = indice + 15
            if (num>25):
                num = num -26
            criptata = alfabeto[num]
            print(criptata,end='')
            

if __name__ == "__main__":

    scelta=int(input('Inserisci 0 se vuoi decriptare una strnga.\nInserisci 1 se vuoi criptare una stringa '))

    if (scelta == 0):#l'utente decide tra decriptare e criptare, se decide di decriptare:
        stringa = input("Inserisci la stringa ")
        i = 0
        for i in range(0, len(stringa)):
            decripta(stringa[i])
    else:                                       #se decide di criptare:
        stringa = input("Inserisci la stringa ")
        i = 0
        for i in range(0, len(stringa)):
            cripta(stringa[i])
    

"""

"""