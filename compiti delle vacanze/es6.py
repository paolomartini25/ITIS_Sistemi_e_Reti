# Il file annual.csv (allegato) contiene la anomalia della temperatura globale del pianeta
# Terra dal 1880 ad oggi, proveniente da varie fonti (colonna “Source”). Scrivere un
# programma che generi un dizionario che abbia come chiave l’anno (“Year”) e valore
# la media aritmetica delle anomalie registrate dalle varie fonti durante quell’anno.
# Inoltre scrivere una funzione che dati in input due anni diversi (anno_1 e anno_2)
# trovi la anomalia massima e minima nel periodo compreso tra anno_1 e anno_2.



def max_min (anno1, anno2):

    if (anno1 > anno2):
        file = open("./annual.csv", "r")

        max = -100
        min = 100
        cont = 0

        for riga in file:
            if (cont != 0):
                contenitore = riga.split(',')
                if (int(contenitore[1]) <= anno1 and int(contenitore[1]) >= anno2):
                    if (float(contenitore[2]) > max):
                        max = float(contenitore[2]) 
                    if (float(contenitore[2]) < min):
                        min = float(contenitore[2]) 
            
            cont = cont + 1

        file.close()
        print (max)
        print (min)

    else:
        print('Il primo anno che hai inserito dovevea essere più grande del secondo.')
    
def main():
    file = open("./annual.csv", "r")
    
    dizionario = {}
    cont = 0
    anno = 0

    for riga in file:
        if (cont != 0):
            contenitore = riga.split(',')
            if (anno != int(contenitore[1])):
                anno = int(contenitore[1])
                anomalia = float(contenitore[2])
            else:
                dizionario[anno]=round((float(contenitore[2]) + anomalia) / 2, 6) # round(numero da arrotondare, numero di cifre dopo la virgola)

        cont = cont + 1

    file.close()
    print('Ora dovrai inserire due date, la prima dovrà essere più grande della seconda')
    max_min (int(input('Inserire il primo anno: ')), int(input('Inserire il secondo anno: ')))

if __name__ == "__main__":
    main()
    
    

    # print (dizionario)
