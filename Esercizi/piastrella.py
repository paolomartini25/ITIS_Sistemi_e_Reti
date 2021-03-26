OSTACOLO = -1

#def controllo_celle_adiacenti(p, x, y):



def numero_piatrelle_libere(p):
    pavimento_numerato = []
    cont = -1
    for riga in p:
        lista = []
        for piastrella in riga:
            if piastrella  == 0:
                cont += 1
                lista.append(cont)
            else :
                lista.append(OSTACOLO)

        pavimento_numerato.append(lista)
    return pavimento_numerato

def main():
    pavimento = [[1,1,0,0,0,0], [0,0,0,0,1,0], [1,0,1,0,0,0], [0,0,1,0,1,0], [0,0,1,0,0,0]]
    print(numero_piatrelle_libere(pavimento))


if __name__ == "__main__":
    main()