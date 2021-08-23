import random

# return a range of floats
SMALLEST_STEP=0.0001
def frange(b, e, step):
    b_scaled, e_scaled, step_scaled = (int(x*1.0/SMALLEST_STEP) for x in (b, e, step))
    new_range = [i*SMALLEST_STEP for i in range(b_scaled, e_scaled, step_scaled)]
    return new_range

def setup():
    size(500, 500)
    colorMode(HSB, 360, 100, 100, 100)
    background(0, 0, 100, 80)
    
    global radius, beam_long, peak_r, amp, fft, mic
    radius = 100
    peak_r = 200
    beam_long = 200
    
def draw():
    background(0, 0, 100, 80)
    stroke(10, 0, 0, 100)
    strokeWeight(0.1)
    noFill()
    translate(width/2, height/2)
    

    global radius, beam_long, peak_r, mic, amp, fft
    
    for r in frange(0.1, 360.1, 0.1):
        # beam_length = random.gammavariate(alpha=1, beta=0.5) * beam
        
        dis = abs(r - peak_r)
        if dis > 180:
            dis = 360 - dis
        dis_func = 1.0 / (1 + exp(dis/20.0))
        beam_length = noise(r, frameCount/10.0) * beam_long * dis_func

            
        x1 = radius * cos(radians(r))
        y1 = radius * sin(radians(r))
        x2 = (radius + beam_length) * cos(radians(r))
        y2 = (radius + beam_length) * sin(radians(r))
        line(x1, y1, x2, y2)
