class Cell():
    global cells, n_cell_x, n_cell_y, cell_size
    def __init__(self, x, y, cell_size):
        self.x = x
        self.y = y
        self.cell_size = cell_size
        self.c = None
        
        # default graphing configs
        self.speed = 1.0/5
        self.divider = 4.2
        self.shifter = 0.4
        self.bcolor = 0
        self.ecolor = 360
        
    def spread(self, b, e=None):
        """Accepts 1 or 2 arguments,
        if it's 1 argument, it means the width of the spread of the color wheel;
        if they are 2 arguments, they mean the begin and end.
        """
        if b < 0 or b > 1:
            print("""Begin color must be between 0 and 1""")
            return self
        
        if e is not None and (e < 0 or e > 1):
            print("""End color must be between 0 and 1""")
            return self
        
        if e is not None:
            self.bcolor = int(360.0*b)
            self.ecolor = int(360.0*e)
        else:
            self.bcolor = int( 360 * (1 - b)/2.0 )
            self.ecolor = int( 360 * (1 + b)/2.0 )
        return self
        
    def divide(self, d):
        self.divider = d
        return self
    
    def shift(self, s):
        self.shifter = map(s, 0, 100, 0, 1)
        return self
        
    def set_speed(self, s):
        """The smaller the s, the slower"""
        if s > 1:
            print("Speed must be between 0 and 1")
            return self
        self.speed = s
        return self
        
    def get_color(self):
        # strategies to generate colors
        # use perlin noise
        # c = map(noise(self.x, self.y, frameCount/10.0), 0, 1, 0, 360)
        # use sine wave
        x_div = self.x * ( 1 + self.divider )
        y_shi = self.y * ( 1 + self.shifter )
        deg = radians(map(x_div, 0, n_cell_x, 0, 360))
        phase = y_shi * TWO_PI
        time_mod = radians(frameCount*self.speed)
        c = map( sin( deg + phase + time_mod ), -1, 1, self.bcolor, self.ecolor)
        return c
        
    def update(self):
        self.c = self.get_color()
        fill(self.c, 70, 70)
        strokeWeight(0)
        rect(self.x*cell_size, self.y*cell_size, cell_size, cell_size)
     
        
def setup():
    size(500, 500)
    colorMode(HSB, 360, 100, 100)
    background(300, 0, 100)
    
    global cells, n_cell_x, n_cell_y, cell_size
    cells = []
    cell_size = 10
    n_cell_x = width/cell_size
    n_cell_y = height/cell_size
    
    for x in range(n_cell_x):
        for y in range(n_cell_y):
            cell = Cell(x, y, cell_size)
            cells.append(cell.set_speed(0.6).shift(3.7).divide(4).spread(0.05, 0.5))
                
        
def draw():
    global cells, n_cell_x, n_cell_y, cell_size
    background(240, 0, 100)
    
    for cell in cells:
        cell.update()