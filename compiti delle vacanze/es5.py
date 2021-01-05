"""
Paolo Marini 
4^b Robotica
Esercizio dello Snake
"""
import turtle 
import time 
import random 
  
delay = 0.1
punteggio = 0
record = 0

  
  
# creazione della finestra
wn = turtle.Screen() 
wn.title("Snake Game")                                              #titolo della finestra
wn.bgcolor("green")                                                 #il colore dello sfondo è verde
wn.setup(width=600, height=600)                                     #dimensione della finestra
wn.tracer(0)                                                        #il ritardo nella creazione della finestrA
  
# creazione della testa dello snake
head = turtle.Turtle() 
head.shape("square")                                                #la turtle con la funzione shape diventa della forma inserita tra le virgolette, ovvero quadrata
head.color("white")                                                 #la turtle diventa bianca
head.penup()                                                        #la turtle viene "alzata" dalla tela digitale, in modo che non scriva
head.goto(0, 0)                                                     #la turtle viene spostata alle coordinate 0, 0
head.direction = "Stop"                                             #la turtle viene fermata
  
# creazione del cibo
food = turtle.Turtle() 
food.speed(0)                                                       #il cibo non deve muoversi, quindi la sua velocità di movimento è impostata a 0
food.shape('circle')                                                #la turtle diventa quadrata
food.color('red')                                                   #la turtle diventa rossa
food.penup()                                                        #la turtle viene alzata
food.goto(0, 100)                                                   #la turtle viene spostata alle coordinate 0, 100

#creazione della scritta del punteggio
pen = turtle.Turtle() 
pen.speed(0)                                                        #la scritta non deve muoversi
pen.shape("turtle")                                                 #la turtle diventa a forma di tartaruga
pen.color("white")                                                  #la turtle diventa bianca, quindi la scritta sarà bianca
pen.penup()                                                         #la turtle viene alzata
pen.hideturtle()                                                    #la turtle viene resa invisivile
pen.goto(0, 250)                                                    #la turtle viene spostata alle coordinate 0, 250
pen.write("Punteggio : 0  Record : 0", align="center", font=("Comic Sans MS", 24, "bold")) #viene scritto il punteggio iniziale con allineamento centrale in grassetto
  
  
  
# assegnazione della direzione 
def goup(): 
    if head.direction != "down": 
        head.direction = "up"
  
  
def godown(): 
    if head.direction != "up": 
        head.direction = "down"
  
  
def goleft(): 
    if head.direction != "right": 
        head.direction = "left"
  
  
def goright(): 
    if head.direction != "left": 
        head.direction = "right"
  
  
def move(): 
    if head.direction == "up": 
        y = head.ycor() 
        head.sety(y+20) 
    if head.direction == "down": 
        y = head.ycor() 
        head.sety(y-20) 
    if head.direction == "left": 
        x = head.xcor() 
        head.setx(x-20) 
    if head.direction == "right": 
        x = head.xcor() 
        head.setx(x+20) 
  
  
          
wn.listen() 
wn.onkeypress(goup, "w") 
wn.onkeypress(godown, "s") 
wn.onkeypress(goleft, "a") 
wn.onkeypress(goright, "d") 
  
segments = [] #segmens conterrà la coda
  
  
  
# Main Gameplay 
while True: 
    wn.update() 
    #controllo della collisione coi bordi
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290: 
        time.sleep(1) 
        head.goto(0, 0) 
        head.direction = "Stop"
        for segment in segments:                                    #sposta la testa e tutta la coda al centro della finestra
            segment.goto(1000, 1000) 
        segments.clear()                                            #la coda viene ripulita
        punteggio = 0
        delay = 0.1
        pen.clear() 
        pen.write("Punteggio : {} Record : {} ".format( punteggio, record), align="center", font=("Comic Sans MS", 24, "bold")) 
    
    #controllo della collisione della testa con il cibo
    if head.distance(food) < 20: 
        #il cibo viene rigenerati un una posizione randomica
        x = random.randint(-270, 270) 
        y = random.randint(-270, 270) 
        food.goto(x, y) 
  
        # Creazione della coda
        new_segment = turtle.Turtle() 
        new_segment.speed(0)    
        new_segment.shape("square")                                 #forma della coda
        new_segment.color("blue")                                   #colore della coda
        new_segment.penup() 
        segments.append(new_segment) 
        delay -= 0.001
        punteggio += 1                                              #incremento del punteggio
        if punteggio > record: 
            record = punteggio 
        pen.clear() 
        pen.write("Punteggio : {} Record : {} ".format( punteggio, record), align="center", font=("Comic Sans MS", 24, "bold")) 
    
    #la coda segue la testa
    #vengono spostati tutti i segmenti eccetto il primo
    for index in range(len(segments)-1, 0, -1):                     #il for andrà dalla numero della lunghezza della coda a 1 
        x = segments[index-1].xcor()                                #ascissa del segmento precedente della coda
        y = segments[index-1].ycor()                                #ordinata del segmento precedente della coda
        segments[index].goto(x, y)                                  #il segmento viene sposato nella posizione del segmento precedente
    
    #viene spostato il primo segmento
    if len(segments) > 0:                                           #se la lnghezza dello snake è maggiore di 0  
        x = head.xcor()                                             #ascissa della coda
        y = head.ycor()                                             #ordinata della coda
        segments[0].goto(x, y)                                      #il primo segmento della coda viene spostato nella posizione della testa

    move()                                                          #la funzione move() fa spostare la testa

    # ricerca della collisione della testa con la coda
    for segment in segments: 
        if segment.distance(head) < 20: 
            time.sleep(1) 
            head.goto(0, 0) 
            head.direction = "stop"
            for segment in segments:                                #sposta la testa e tutta la coda al centro della finestra
                segment.goto(1000, 1000)
            segments.clear()                                        #la coda viene ripulita
  
            punteggio = 0
            delay = 0.1
            pen.clear() 
            pen.write("Punteggio : {} Record : {} ".format( punteggio, record), align="center", font=("Comic Sans MS", 24, "bold")) 
    time.sleep(delay) 
  
wn.mainloop() 