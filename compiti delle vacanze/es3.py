#Nella serie di Fibonacci, ciascun numero della serie è la somma dei due numeri nella serie che lo precedono, ad esempio:
#1, 1, 2, 3, 5, 8, 13 (...)
#Scrivi una funzione ricorsiva che restituisce in output i numeri della sequenza di Fibonacci, entro una soglia specifica impostata dall'utente.

def fibonacci(a, b, limite, cont): #a è il numero che precede il numero attuale della serie di fibonacci mentre b è il numero percedente al numero perecedente, limite è la soglia impostata dall'utente mentre cont è una variabile che viene incrementata ogni volta ed è il numero di numeri già stampati, deve essere minore del limite
    if (cont == 1):
        print(a) #primo num
    if (cont<limite):
        cont=cont+1
        print (a+b) # stamppo il numero della sequenza di fibonacci
        fibonacci(a+b, a, limite, cont) #richiamo la funzione e passo come parametri la somma dei due numeri precedenti e il numero precendente

def main():
    limite=int(input("quanti numeri della serie si fibonacci vuoi avere? "))
    fibonacci(1, 0, limite, 1)


if __name__ == "__main__":
    main()