import graphics as g
import time

width = 400
height = 200
#sections = int(input("how many sections will be made?  "))
sections = 60
currentpos = 0
delta = round(width/sections)
currentcolor = 0
colordelta = round(255/sections)
win = g.GraphWin("window", width, height)

for i in range(sections):
    
    rect = g.Rectangle(g.Point(currentpos, 0),g.Point((delta + currentpos-1), height))
    rect.draw(win)
    rect.setFill(g.color_rgb(0, currentcolor, 0))
    rect.setOutline(g.color_rgb(0, currentcolor, 0))
    currentpos += delta
    currentcolor += colordelta


win.getMouse()
win.close()
