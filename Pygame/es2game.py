"""
Il nostro amico Bob dopo alcune commissioni in giro per la città di Flatland deve rientrare a casa. Purtroppo Bob soffre di momentanee perdite di memoria!
Questa volta la sua amnesia dura ben 60 minuti e durante questi 60 minuti Bob adotta la seguente strategia per tentare di rientrare a casa. Ogni minuto decide a caso tra:
procedere 10 m verso Nord
procedere 10 m verso Sud
procedere 10 m verso Est
procedere 10 m verso Ovest
Simulare l’intero percorso compiuto da Bob, supponendo che il punto di partenza abbia coordinate (0,0) e salvarlo all’interno di un dizionario opportunamente strutturato.
Disegnare il percorso compiuto da Bob dentro una schermata di pygame.
Infine salvare il percorso di Bob dentro un file .csv opportunamente strutturato.

BONUS: ogni volta in cui Bob passa in un punto della città di Flatland in cui è già passato, stampare a schermo le coordinate del punto.
"""
import pygame #istallata da noi
import sys #nativa = preistallata
import random
import csv

TIMEAMNESIA = 61
NERO = (0,0,0)
BIANCO = (255,255,255)
ROSSO = (255,0,0)
DIM = (600, 600)

percorso = {}
def controllaSePassato(lung, posx, posy):
    trovato = 0
    
    for i in range(0,lung):
        if (percorso[i][0]==posx and percorso[i][1]==posy and trovato == 0):
            print("Sei gia passato di quà: " + str(posx) + "x" + str(posy) + "\n")
            trovato = 1
            
        
    

def generaPercorso():
    posx = 0
    posy = 0
    percorso[0] = (posx, posy)

    for i in range(1, TIMEAMNESIA):
        x = random.randint(0,3)
        if (x == 0):
            posy= posy - 30
        elif (x == 1):
            posx = posx + 30
        elif (x == 2):
            posy = posy + 30
        elif (x == 3):
            posx = posx - 30

        controllaSePassato(i, posx, posy)
        percorso[i] = (posx, posy)
        
    
    print("bru")

def salvasufile():
    csvfile = open('file.csv', 'w')
    csvwriter = csv.writer(csvfile)
    for chiave, valore in percorso.items():
        lista = [chiave, valore[0], valore [1]]
        csvwriter.writerow(lista)
        print (lista)
    csvfile.close()    

def main():
    generaPercorso()
    salvasufile()
    
    pygame.init()
    global finestra
    finestra = pygame.display.set_mode(DIM)
    finestra.fill(NERO)
    cont = 0
    while True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if (cont < TIMEAMNESIA-1):
            pygame.draw.line(finestra,ROSSO,(percorso[cont][0]+(DIM[0]/2),percorso[cont][1]+(DIM[0]/2)),(percorso[cont+1][0]+(DIM[0]/2),percorso[cont+1][1]+(DIM[0]/2)))
            cont += 1
        

        pygame.display.update() #aggiorna le modifiche fatte alla finestra
        

if __name__ == "__main__":
    main()
