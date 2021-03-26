lista = [3, 2, -1, 6, 5]

#python style
for elemento in lista: #stampa tutti gli elementi della lista
    print(elemento)

for i in range(0, len(lista)): #C style
    print (lista[i])
#python style
for i, elemento in enumerate(lista): #crea un iteratore funzione che può essere usato nel ciclo ritorna due elementi l'indice e l'elemento
    print(f"{i}-{elemento}")

contatore = 0
while(contatore < len(lista)):
    print(lista[contatore])
    contatore = contatore + 1

# I DIZIONARI
#un dizionario è una collezione non ordinata di elementi, ciascuno dei quali è costituito da una chiave e un vaore
#ogni elemento di un dizionario è una coppia valore:chiave

dizionario = {1: "Antonelli", 2: "Becchis", 3: "Bianco", 4: "Bongiovanni", 1: "Pagliaccio"}
#per accedere al VALORE di un elemento del dizionario si utilizza la notazione
#nome_dizionario[chiave]
dizionario[19]="Orlando" #aggiungo la chiave 19 e il valore orlando
print(dizionario) #la stampa non ha un ordine ma si usa la chiave

#canzone = {"numero":1, "titolo":"Francesco Totti","Autore":"Bello Figo"}
#print(canzone["titolo"])
#print(canzone["numero"])

# file = open("instagram.csv","r")

# for riga in file:
    # print(riga, end = "")

# file.close()