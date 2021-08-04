import random

from two_Ds import Line, Curve, Rectangle
from Circle import Circle
from utils import w, h, frange

def _mousePressed():
    global tiles
    loop()
    tiles *= 2
    if tiles > 64:
        tiles = 1
    
def _mouseReleased():
    noLoop()
    

def setup():
    size(800,800)
    colorMode(HSB, 360, 100, 100)
    background(360)
        
    global d
    # d = Rectangle(w(0.6), h(0.1), w(0.9), h(0.99), 0.5)  
    d = Circle(0.1, 0.3, 0.005, 100)
    tiles = 1

    
def draw():
    global d, tiles
    
    background(360)
    # only for circle
    noFill()
    
    stroke(0)
    strokeWeight(w(0.001))
    
    
    d.randomize_color(distribute=False)
    d.distort(0.1)
    # d.modulate("increase")
    # d.animate()
    d.tile()
    
    # noLoop()
    
    
