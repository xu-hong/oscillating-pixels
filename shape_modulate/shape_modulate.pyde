import random

from two_Ds import Line, Curve, Rectangle
from Circle import Circle
from utils import w, h, frange

def mousePressed():
    global tiles
    loop()
    tiles *= 2
    if tiles > 64:
        tiles = 1
    
def mouseReleased():
    noLoop()
    

def setup():
    size(800,800)
    colorMode(HSB, 360, 100, 100)
    background(360)
        
    global li, c, tiles
    # li = Rectangle(w(0.6), h(0.1), w(0.9), h(0.99), 0.5)  
    li = Circle(0.1, 0.3, 0.02, 100)
    tiles = 1

    
def draw():
    global line, tiles
    
    background(360)
    li.randomize_color(distribute=False)
    li.distort(0.01)
    li.modulate("increase")
    li.tile()
    noLoop()
    
    
