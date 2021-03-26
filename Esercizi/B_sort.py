n = int(input("Quanto è lunga la lista? "))
lista = [0] * n

cont = 0
j = 0

for cont in range (n):
    lista[cont] = int(input("inserire il %d  elemento : " %cont))

for cont in range (n-1):
    for j in range (n-cont-1):
        if (lista[j]>lista[j+1]):
            appoggio = lista[j]
            lista[j] = lista[j+1]
            lista[j+1] = appoggio

print(f"la lista ordinata: {lista}")
