class Canvas():
    def __init__(self,
            speed=0.6,
            shift=3.7,
            divide=4,
            spread1=0.05,
            spread2=0.5):
        
        self.cells = []
        self.n_cell_x = width
        self.n_cell_y = height
        self.speed = speed
        self.shift = shift
        self.divide = divide 
        self.spread1 = spread1
        self.spread2 = spread2
    
    def build(self):
        for x in range(self.n_cell_x):
            for y in range(self.n_cell_y):
                cell = Cell(x, y)
                self.cells.append(
                    cell
                    .set_speed(self.speed)
                    .shift(self.shift)
                    .divide(self.divide)
                    .spread(self.spread1, self.spread2))
                

class Cell():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.n_cell_x = width

        # default graphing configs
        self.speed = 1.0/5
        self.divider = 4.2
        self.shifter = 0.4
        self.bcolor = 0
        self.ecolor = 360
        
        # additive attributes
        self._jitter = 0
        self._osc = 0
        self._n_osc = 0
        
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
        if s > 10:
            print("Speed must be between 0 and 10")
            return self
        self.speed = s
        return self
    
    def jitter(self):
        # use perlin noise
        self._jitter = map(noise(self.x, self.y, frameCount*self.speed), 0, 1, 0, PI)
        
    def osc(self, divider=None, shifter=None, speed=None):
        if divider is None:
            divider = self.divider
        if shifter is None:
            shifter = self.shifter
        if speed is None:
            speed = self.speed
            
        # oscilate with basic sine wave
        x_div = self.x * ( 1 + divider )
        y_shi = self.y * ( 1 + shifter )
        
        deg = map(x_div, 0, self.n_cell_x, 0, TWO_PI)
        phase = y_shi * TWO_PI
        time_mod = radians(frameCount*speed)
        
        self._osc +=  sin( deg + phase + time_mod )
        self._n_osc += 1
        
    def get_color(self):
        # get default oscillation
        self.osc()
        c = map( self._osc, -1 * self._n_osc, 1 * self._n_osc, self.bcolor, self.ecolor)

        return color(c, 80, 80)
        
        
def setup():
    size(500, 500)
    colorMode(HSB, 360, 100, 100)
    
    global canvas 
    canvas = Canvas(speed=8, shift=99, divide=0.2, spread1=0.2, spread2=0.4)
    canvas.build()
                
        
def draw():
    global canvas
    
    loadPixels()
    
    for i, cell in enumerate(canvas.cells):
        cell.osc(divider=10, shifter=1, speed=0.5)
        pixels[i] = cell.get_color()
    
    updatePixels()