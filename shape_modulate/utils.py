# helper function for dynamic size
def w(val=None):
    if val is not None:
        return width*val
    else:
        return width

def h(val=None):
    if val is not None:
        return height*val
    else:
        return height

def vector(p):
    x = w(p.x)
    y = h(p.y)
    return PVector(x, y)

def sw(val):
    """return scaled width (0, 1)"""
    return val*1.0/width

def sh(val):
    """return scaled height (0, 1)"""
    return val*1.0/height




# return a range of floats
SMALLEST_STEP=0.0001
def frange(b, e, step):
    b_scaled, e_scaled, step_scaled = (int(x*1.0/SMALLEST_STEP) for x in (b, e, step))
    new_range = [i*SMALLEST_STEP for i in range(b_scaled, e_scaled, step_scaled)]
    return new_range
