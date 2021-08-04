from utils import frange, w, h
from two_Ds import TwoD

class Circle(TwoD):
    def __init__(self, radius_min, radius_max, radius_step, num_points):
        """Draw circles with points."""
        self.radius_min = radius_min
        self.radius_max = radius_max
        self.radius_step = radius_step
        # technical this is the number of sides
        self.num_points = num_points
        super(Circle, self).__init__(0, 0, 0, 0)

    # modulate parameters used in animation
    @property
    def z(self):
        return frameCount/300.0

    @property
    def z2(self):
        return frameCount/200.0

    def make_circle(self, radius, amount_to_nudge):
        """return a list of coordinates pairs for the circle"""
        points = []
        radian_per_step = TWO_PI / self.num_points

        theta = 0
        while theta <= TWO_PI:
            x = 0.5 + radius * cos(theta)
            y = 0.5 + radius * sin(theta)
            
            points.append([x, y])
            
            theta += radian_per_step
        
        if amount_to_nudge > 0:
            points = self._distort(points, amount_to_nudge)
        return points

    def _distort(self, points, amount_to_nudge):
        distorted = []
        for x, y in points: 
            # we want to scale the noise according 
            # to how far the points are from the center
            distance = dist(0.5, 0.5, x, y)
            # The Perlin noise function becomes zero when x and y are both whole numbers.
            # So, to avoid this, we want to shift our coordinates before sampling. 
            noise_fn = lambda x, y: noise(
                                        (x + 0.31) * distance * 1.5 + self.z2,
                                        (y - 1.73) * distance * 1.5 + self.z2,
                                        self.z)
            
            if amount_to_nudge > 0:
                # modulate
                # amount_to_nudge = amount_to_nudge * (1 - cos(z) * 0.08) 
                local_theta = noise_fn(x, y) * PI * 3
                x = x + amount_to_nudge * cos(local_theta)
                y = y + amount_to_nudge * sin(local_theta)

            distorted.append([x, y])

        return distorted
        
    def animate(self):
        pass
        
    def draw(self, radius=None):
        radius = radius or self.radius_min
        points = self.make_circle(radius, self.distort_magnitude)
        beginShape()
        for x, y in points:
            vertex(w(x), h(y))
        endShape()
    
    def tile(self, n=None):
        for radius in frange(self.radius_min, self.radius_max, self.radius_step):
            if self.distribute_color:
                self._set_color()
            self.draw(radius)
            