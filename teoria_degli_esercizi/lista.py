numero = 7 #è un oggetto ovvero un istanza della classe int
#esempio di f-string
print(f"il valore di numero è {numero}")
#esempio di concatenazione di stringe
print("il valore di numero è "+str(numero))

s1 = 'Ciao'
s2 = "un'altra stringa"

print(s1 == s2)
#python è un linguaggio orientato agli oggetti in python tutto è un oggetto
#COLLEZIONI: liste, tuple, dizionari

#LISTE: sono "simili" agli array del c

lista = [3,5,1,6,7]
print(f"la lista è: {lista}")

#FUNZIONI
def lamiafunzione(argomento1, argomento2):
    #codice della funzione indentato
    return argomento1

print(lamiafunzione)

#PYTHON STYLE :)
for elemento in lista: 
    print(elemento)
print("--------------------")

for indice, elemento in enumerate(lista):
    print(f"indice:{indice} - elemento: {lista[indice]}")

print("--------------------")


#c sTyLe :(
lunghezza = len(lista)
for indice in range(0, lunghezza):
    print(lista[indice])
    print(f"indice: {indice} - elemento{lista[indice]}")

lista = []
valore = 0
while (int(valore) != -1):
    valore = input("inserisci un valore: ")
    lista.append(int(valore))
print(lista)
