#prende il dizionario ed inverte il valore con chiave
dizionario={'A':'g', 'B':'h'}
dizionario2={}

for chiave, valore in dizionario.items(): #permette di fare un ciclo sul dizionario e vi da la chiave e il valore dell'elemento
    print(chiave ,valore) #stampa la chiave ed il valore
    dizionario2[valore] = chiave

print(dizionario2) #'g':'A', 'h':'B'



#-------------------------------------------
#dizionari di funzioni

def somma(a, b):
    return a + b

def moltiplicazione(a, b):
    return a * b

dizionario_di_funzoni = {0:somma, 1:moltiplicazione}

def main():
    val_utente = int(input("0 per sommare 1 per moltiplicare: "))
    #a = int(input("primo numero: "))
    #b = int(input("secondo numero: "))

    try:
        x = dizionario_di_funzoni[val_utente](int(input("primo numero: ")), int(input("secondo numero: "))) #scelta della funzione perchè salviamo nel dizionario le due funzioni
        print(x)
    except:
        print("hai inserito un valore errato.")

    

if __name__ == "__main__":
    main()


#----------------------------------------

def fun(lista_numeri, stampa = False):

    lista_quadrati = [x*x for x in lista_numeri]
    if stampa:
        print(lista_quadrati)
    return lista_quadrati

#fun([1,2,3,4], True) //stampa i valori della lista quadrati
#fun([1,2,3,4]) //non stampa i valori della lista quadrati
fun(stampa = True, lista_numeri = [1,2,3,4]) #anche se l'ordine è sbagliato se metti il nome della variabile lista quadrati viene stampata
