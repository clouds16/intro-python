import graphics as g
import time as t

width = 600
height = 400

def house():
    sky = g.Rectangle(g.Point(0,0), g.Point(600,400))
    sky.setFill("skyblue")
    sky.draw(win)
    
    #line one
    roof1 = g.Line(g.Point(300,100), g.Point(200,200))
    roof1.draw(win)
    #line 2
    roof2 = roof1 = g.Line(g.Point(300,100), g.Point(400,200))
    roof1.draw(win)
    
    #grass rectangles
    grassleft = g.Rectangle(g.Point(400,400), g.Point(600,375))
    grassleft.setFill("green")
    grassleft.draw(win)

    #grass reactangle right side
    grassright = g.Rectangle(g.Point(0,400), g.Point(200,375))
    grassright.setFill("green")
    grassright.draw(win)
    
    #house rectangles
    house = g.Rectangle(g.Point(200,400), g.Point(400,200))
    house.draw(win)
    house.setFill("brown")
    door = g.Rectangle(g.Point(250,400), g.Point(300,300))
    door.setFill("white")
    door.draw(win)
    
    #text
    label = g.Text(g.Point(250,275), "Hectors House")
    label.draw(win)
    


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


win = g.GraphWin("animation", 600, 400 )
house()
animatecir()
win.getMouse()
win.close()
