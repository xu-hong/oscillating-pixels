def setup():
    size(500, 500, P3D)
    background(10)
    
    global gridsize, z_ , vertexes
    gridsize = 20
    z_ = 100
        
    
def draw():
    background(10)
    noFill()
    stroke(200)
    strokeWeight(1)
    
    global gridsize, z_
    translate(0, height/3, 0)
    rotateX(radians(60))
    
    ny = int(height*1.0/gridsize)
    nx = int(width*1.0/gridsize)
    scaler = 4.0
    # rounding up - so using 4 instead of 4.0 here
    framer = frameCount / 4
    for y in range(0, ny+1, 1):
        beginShape(TRIANGLE_STRIP)
        for x in range(0, nx+1, 1):
            z = noise(x/scaler, (y-framer)/scaler) * z_
            vertex(x*gridsize, y*gridsize, z)
            z1 = noise(x/scaler, (y+1-framer)/scaler) * z_
            vertex(x*gridsize, (y+1)*gridsize, z1)
        endShape()
            