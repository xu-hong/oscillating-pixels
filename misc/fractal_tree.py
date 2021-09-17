leaf_len = 3
branch_ratio = 0.618
rotate_angle = PI / 5.0

class Branch:
    def __init__(self, begin, end):
        self.begin = begin
        self.end = end
        self.leaves_added = False
        
    def is_end_leaf(self):
        return self.blen() < leaf_len
        
    def show(self):
        line(self.begin.x, self.begin.y, self.end.x, self.end.y)
        
    def blen(self):
        return PVector.sub(self.end, self.begin).mag()
        
    def branchR(self):
        p1 = PVector.sub(self.end, self.begin)
        p1.rotate(rotate_angle)
        p2 = PVector.add(self.end, p1 * branch_ratio)
        return Branch(self.end, p2)
    
    def branchL(self):
        p1 = PVector.sub(self.end, self.begin)
        p1.rotate(-rotate_angle)
        p2 = PVector.add(self.end, p1 * branch_ratio)
        return Branch(self.end, p2)
        
    
def setup():
    size(500, 500)
    background(233)
    
    global branches, blen
    branches = []
    blen = 200
    
    b0 = Branch(PVector(0,0), PVector(0, -blen))
    branches.append(b0)

        
    
def draw():
    stroke(10)
    translate(width/2, height)
    
    global branches
    
    for b in branches:
        if not b.leaves_added and not b.is_end_leaf():
            lb = b.branchL()
            rb = b.branchR()
            branches.append(lb)
            branches.append(rb)
            b.leaves_added = True
            b.show()