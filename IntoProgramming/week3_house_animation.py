import graphics as g
import time as t
import math as m 

width = 600
height = 400


def house():
    roof1 = g.Line(g.Point(300,100), g.Point(200,200))
    roof1.draw(win)

    roof2 = roof1 = g.Line(g.Point(300,100), g.Point(400,200))
    roof1.draw(win)

    house = g.Rectangle(g.Point(200,400), g.Point(400,200))
    house.draw(win)
    house.setFill("brown")
    door = g.Rectangle(g.Point(250,400), g.Point(300,300))
    door.setFill("white")
    door.draw(win)


def animatecir():

    x=30
    y=30
    
    cir = g.Circle(g.Point(x,y), 40)
    cir.draw(win)
    cir.setFill("yellow")

    win.getMouse()
    
    for i in range(500):
        
        dx= 1
        dy= .1
        cir.move(dx,dy)
        t.sleep(.02)

if __name__ == "__main__":
    win = g.GraphWin("animation", 600, 400 )

    house()
    animatecir()
    win.getMouse()
    win.close()
  
    pass
