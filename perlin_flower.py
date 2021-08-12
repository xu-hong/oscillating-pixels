def setup():
    size(500, 500)
    colorMode(HSB, 100)
    background(90)
    
    global radius
    radius = 300
    
def draw():
    stroke(10, 0, 0, 30)
    strokeWeight(0.1)
    noFill()
    translate(width/2, height/2)
        
    global radius
    
    beginShape()

    for r in range(361):
        noiseFactor = noise(r*0.03, frameCount*1.0/100)
        x = radius * cos(radians(r)) * noiseFactor
        y = radius * sin(radians(r)) * noiseFactor
        vertex(x, y)
    
    endShape()
    
    radius = radius - 1
    if radius <= 0:
        noLoop()
        