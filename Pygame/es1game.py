#disegno il pavimento con ostacoli
import pygame #istallata da noi
import sys #nativa = preistallata
import random
NERO = (0,0,0)
BIANCO = (255,255,255)
ROSSO = (255,0,0)
pavimento = [[1,1,0,0,0,0], [0,0,0,0,1,0], [1,0,1,0,0,0], [0,0,1,0,1,0], [0,0,1,0,0,0]]

NRIGHE = 5
NCOLONNE = 6
DIM = (600, 600)



def drawgrid():
    dimensionex = DIM[0]//NCOLONNE #divisione intera
    dimensioney = DIM[1]//NRIGHE
    
    conty = 0

    for y in range(0, DIM[0], dimensioney):
        riga = pavimento[conty]

        if (conty<NRIGHE-1):
            conty+=1

        contx=0
        for x in range(0, DIM[1], dimensionex):
            colonna = riga[contx]

            if (contx<NCOLONNE-1):
                contx+=1

            if colonna  == 0:
                piastrella = pygame.Rect(x,y,dimensionex,dimensioney)
                pygame.draw.rect(finestra, BIANCO, piastrella, 1)
            else :
                ostacolo = pygame.Rect(x,y,dimensionex,dimensioney)
                pygame.draw.rect(finestra, ROSSO, ostacolo) #se metto 1 in fondo si vede solo il bordo rosso
    

def main():
    #genPavimento()
    pygame.init()
    global finestra
    finestra = pygame.display.set_mode(DIM)
    finestra.fill(NERO)
    cont = 0
    while True:
        drawgrid()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update() #aggiorna le modifiche fatte alla finestra

if __name__ == "__main__":
    main()

#da mettere a posto il generatore casuale di pavimento
"""
pavimento = []
PROBABILITA_OSTACOLO = 0.20 #20% di possibilità che esca l'ostacolo

def genPavimento():
    for y in range(0, NRIGHE):
        if (y<NRIGHE-1):
            pavimento.append([])
            for a in range(0, NCOLONNE):
                if (y<NCOLONNE-1):
                    x = random.random()
                    if x<PROBABILITA_OSTACOLO:
                        pavimento[y].append(1)
                    else:
                        pavimento[y].append(0)
"""