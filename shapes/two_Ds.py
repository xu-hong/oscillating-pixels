import random
from utils import w, h, sw, sh, vector

class TwoD(object):
    def __init__(self, x1, y1, x2, y2, randomness=0.5):
        # basic
        self.x1 = w(x1)
        self.y1 = h(y1)
        self.x2 = w(x2)
        self.y2 = h(y2)
        self.x1s = x1
        self.x2s = x2
        self.y1s = y1
        self.y2s = y2
        self.randomness = randomness

        # color 
        self.random_color = False
        self.distribute_color = False
        self.fills = None

        # distort
        self.distort_magnitude = 0
        self.modulated = False
        self.mtype = "uniform"
        
    def _set_color(self):
        color = random.randint(0, 360)
        stroke(color, 70, 70)
        self._set_fill(color)
    
    def _set_fill(self, color):
        if self.fills:
            fill(color, 70, 70, 75)

    def _generate_tile_coordinates(self, n):
        """Return a list of (x,y) coordinates of each tile."""

        # canvas at each step begins at (x, y),
        # x and y being integer indexes,
        # i.e. (x/n, y/n) in a scaled world.
        # and points begin with an offset added,
        # i.e. ((1 + x1s), (1 + y1s))
        coordinates = []
        for x in range(n):
            x = x * 1.0
            for y in range(n):
                y = y * 1.0                
                # scaled coordinates
                x1 = (x/n) + (1.0/n) * self.x1s
                y1 = (y/n) + (1.0/n) * self.y1s
                x2 = (x/n) + (1.0/n) * self.x2s
                y2 = (y/n) + (1.0/n) * self.y2s
                
                p1 = PVector(x1, y1)
                p2 = PVector(x2, y2)
                simple_line = [vector(p) for p in (p1, p2)]
    
                coordinates.append(simple_line)
        return coordinates
    
    def _generate_tile_modulate_params(self, n):
        """Used for modulating distort magnitude within tiles.

        Accepts current types of moduldation:
        
        uniform: default, no modulation
        jump:
        increase:
        wave:
        triangle:
        random:
        """
        max_mag = self._get_distort_magnitude()
        mtype = self.mtype
        mags = []

        for x in range(n):
            for y in range(n):
                pos = (y*n+x) * 1.0 / n**2
                if mtype == "uniform":
                    mags.append(max_mag)
                elif mtype == "wave":
                    # picked 3 for no reason
                    z = 3 * TWO_PI * pos
                    mags.append(1.0 * sin(z) * max_mag)
                elif mtype == "increase":
                    mags.append(1.0 * pos * max_mag)
                elif mtype == "jump":
                    # picked some magic numbers: after 50% starts to distort
                    if pos < 0.5:
                        mags.append(0)
                    else:
                        mags.append((pos-0.5) * max_mag * 10)
                elif mtype == "triangle":
                    dis2m = abs(pos - 0.5)
                    mags.append(1.0 * (1 - 2*dis2m) * max_mag)
                elif mtype == "random":
                    dice = random.random()
                    # some magical gate I picked
                    if dice > 0.80 and dice <= 0.90:
                        mags.append(1.0 * dice * max_mag)
                    else:
                        mags.append(0)
                else:
                    print("Unacceptable type: ", mtype)
                    mags = [max_mag] * n * n
                    break
        return mags
    
    def _get_next_distort(self, p1, magnitude=1.0):
        """Takes one vector and generate the next for plotting.
        Called in self._distort()"""
        pa = PVector.random2D().mult(0.05*magnitude)
        pa = vector(pa)
        pa = PVector.add(p1, pa)
        return pa
    
    def _distort(self, ss, ee, magnitude=3):
        """Accept two PVectors and a magnitude integer."""
        if magnitude <= 0:
            return [ss, ee]
        
        distance = PVector.sub(ee, ss).mag()
        scaler = distance * 1.0 / sqrt(width**2 + height**2)
        
        # begin with the middle point
        this_point = PVector.add(ss, ee).mult(0.5)
        finals = []
        n_distorts = int(magnitude)
        for i in range(n_distorts):
            p1 = self._get_next_distort(this_point, scaler)
            finals.append(p1)
            this_point = p1
        return [ss] + finals + [ee]
    
    def _get_vectors(self, vectors=None):
        if vectors is None:
            p1 = PVector(self.x1, self.y1)
            p2 = PVector(self.x2, self.y2)
            vectors = [p1, p2]
        return vectors

    def _get_distort_magnitude(self, distort_magnitude=None):
        if distort_magnitude is None:
            distort_magnitude = self.distort_magnitude
        return distort_magnitude

    def distort(self, magnitude=3):
        self.distort_magnitude = magnitude
        
    def randomize_color(self, distribute=False, fills=None):
        self.random_color = True
        self.distribute_color = distribute
        self.fills = fills
        
    def set_randomness(self, r):
        """Set the basic randomness within the shape.
        Used for controlling angles."""
        if r > 1 or r < 0:
            print("""Randomness must be a number between 0 and 1!
                  0 means no randomness. 0.5 is max random.""")
        else:
            self.randomness = r
            
    def plot_function(self, *args):
        pass
          
    def draw(self, vectors=None, distort_magnitude=None):
        """The main draw function. It will draw the individual shape"""
        vectors = self._get_vectors(vectors)
        distort_magnitude = self._get_distort_magnitude(distort_magnitude)

        r = random.random()
        if r > self.randomness:
            ss = PVector(vectors[0].x, vectors[0].y)
            ee = PVector(vectors[1].x, vectors[1].y)
        else:  
            ss = PVector(vectors[1].x, vectors[0].y)
            ee = PVector(vectors[0].x, vectors[1].y)  
        
        distorted = self._distort(ss, ee, distort_magnitude)   
        
        # "connect" two or more points in the list
        for s, e in zip(distorted[:-1], distorted[1:]):
            self.plot_function(s.x, s.y, e.x, e.y)            
                
    def tile(self, n):
        coordinates = self._generate_tile_coordinates(n)
        if self.random_color:
            self._set_color()

        if self.modulated:
            modulates = self._generate_tile_modulate_params(n)
            for li, md in zip(coordinates, modulates):
                if self.distribute_color:
                    self._set_color()
                self.draw(li, md)
        else:
            for li in coordinates:
                if self.distribute_color:
                    self._set_color()
                self.draw(li)
    
    def modulate(self, mtype="uniform"):
        self.modulated = True
        self.mtype = mtype
            
        
class Line(TwoD):
    def plot_function(self, *args):
        return line(*args)

class VLine(TwoD):
    """A Vera Molnar Line"""
    def __init__(self, x1, y1, x2, y2, randomness):
        super(VLine, self).__init__(x1, y1, x2, y2, randomness=randomness)
        if randomness:
            print("Randomness parameter is disabled in Vline class.")
   
    def plot_function(self, *args):
        x1, y1, x2, y2 = args
        x_mid = (x1 + x2)/2.0
        xm1 = random.uniform(x1, x_mid)
        xm2 = random.uniform(x_mid, x2)
        line(x1, y1, xm1, y2)
        line(xm1, y1, xm2, y2)
        line(xm2, y1, x2, y2)
    
    def distort(self, magnitude):
        print("VLine.distort() is disabled.")
    
    def set_randomness(self, magnitude):
        print("VLine.set_randomness() is disabled.")

    def modulate(self, mtype):
        print("VLine.modulate() is disabled.")

   
class Curve(TwoD):
    def plot_function(self, *args):
        x1, y1, x2, y2 = args
        bezier(x1, y1, x2, y1, x1, y2, x2, y2)


class Rectangle(TwoD):
    def plot_function(self, x1, y1, x2, y2, rotate_angle):
        rectMode(CORNERS)
        pushMatrix()
        translate(x1, y1)
        random_angle = random.uniform(0, rotate_angle)
        rotate(radians(random_angle))
        rect(0, 0, x2-x1, y2-y1)
        popMatrix()

    def _distort(self, ss, ee, magnitude):
        """Obsolete: it's not working as expected.
        Overriding _distort in super.

        Accept two PVectors and a magnitude integer.
        Here magnitude means the rotate degree."""
        pushMatrix()
        middle = PVector((ss.x+ee.x)/2.0, (ss.y+ee.y)/2.0)
        translate(middle.x, middle.y)
        m2s = PVector.sub(ss, middle)
        m2e = PVector.sub(ee, middle)
        rr = random.uniform(radians(-magnitude), radians(magnitude))
        m2s.rotate(rr)
        m2e.rotate(rr)

        # reconstruct starting and ending points
        ss = PVector.add(middle, m2s)
        ee = PVector.add(middle, m2e)
        popMatrix()

        return [ss, ee]

    def draw(self, vectors=None, distort_magnitude=None):
        vectors = self._get_vectors(vectors)
        distort_magnitude = self._get_distort_magnitude(distort_magnitude)      
        self.plot_function(vectors[0].x, vectors[0].y,
                            vectors[1].x, vectors[1].y,
                            distort_magnitude)
