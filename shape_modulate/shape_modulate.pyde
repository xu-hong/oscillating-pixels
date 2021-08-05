import random

from two_Ds import Line, Curve, Rectangle
from Circle import Circle
from utils import w, h, frange

def mousePressed():
    global tiles
    loop()
    tiles *= 2
    if tiles > 32:
        tiles = 1
    
def mouseReleased():
    noLoop()

def setup():
    size(600, 600)
    colorMode(HSB, 360, 100, 100)
    background(360)
        
    global d, tiles
    d = Line(0, 0.01, 1, 0.99, 0.5)  
    # d = Circle(0.1, 0.3, 0.005, 100)
    tiles = 1

    
def draw():
    global d, tiles
    
    background(360)
    # only for circle
    noFill()
    
    # stroke(0)
    strokeWeight(4)
    
    # d.randomize_color(distribute=False)
    d.distort(7)
    d.modulate("increase")
    d.tile(tiles)
    
    noLoop()
    
    
