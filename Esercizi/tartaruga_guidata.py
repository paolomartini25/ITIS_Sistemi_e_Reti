import turtle

robot = turtle.Turtle()
win = turtle.Screen()

lung = 30

robot.home()

def controllo():
    if (robot.ycor() + lung) > win.window_height()/2:
        return 1
    elif (robot.ycor() - lung) < -1 * win.window_height() / 2: 
        return 2
    elif (robot.xcor() + lung) > win.window_width()/2:
        return 3
    elif (robot.xcor() - lung) < -1 * win.window_width() / 2:
        return 4
    elif (robot.xcor() - lung) < -1 * win.window_width() / 2 and (robot.ycor() - lung) < -1 * win.window_height() / 2: 
        return 5
    else:
        robot.position()
        return 0

def avanti():
    if controllo() != 1 and controllo() != 5: 
        robot.setheading(90)
        robot.forward(lung)
        print(controllo())
    else:
        pass

def indietro():
    if controllo() != 2 and controllo() != 5: 
        robot.setheading(270)
        robot.forward(lung)
        print(controllo())
    else:
        pass

def destra():
    if controllo() != 3 and controllo() != 5: 
        robot.setheading(0)
        robot.forward(lung) 
        print(controllo())
    else:
        pass

def sinistra():
    if controllo() != 4 and controllo() != 5: 
        robot.setheading(180)
        robot.forward(lung)
        print(controllo())
    else:
        pass

win.title("my game")
win.bgcolor("red")
win.setup(width = 800, height = 800)

win.listen()
win.onkey(avanti, "w")
win.onkey(indietro, "s")
win.onkey(destra, "d")
win.onkey(sinistra, "a")

win.mainloop()

# dander __
#if __name__ = "__main__"
#   blu blu
#   bla bla
#   main()
# per richiamare il main


