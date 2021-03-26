import turtle #importo la libreria turtle e tutto ciò che contiene
#from turtle import * importo tutte le cassi e le posso usare direttamente col loro nome

l = int(input("inserire il numero dei lati "))
robot = turtle.Turtle()
robot.begin_fill()
win = turtle.Screen()
count = l

while(count > 0):
    def jump():
        robot.forward(40)
        robot.left(360/l)
        count = count-1
        print("jump")
robot.end_fill()

win.title("my game")
win.bgcolor("green")
win.setup(width = 800, height = 800)

win.listen() #mette la finestra in ascolto per esempio per i tasti
win.onkey(jump, "space")

win.mainloop()