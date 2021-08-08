from Particle import *

# Confetti are just particles with a different show method
# note we used inheritance!
class Confetti(Particle):
    def __init__(self, x, y):
        super(Confetti, self).__init__(x, y)
        self.angle = random(TAU)
    
    
    def show(self):
        noStroke()
        # fill(map(self.angle % TAU, 0, TAU, 0, 360), 100, 100, self.lifetime)
        fill(0, 0, 100, self.lifetime)
        
        if self.finished():
            stroke(random(360), 100, 100, 100)
            # fill(random(360), 100, 100, 100)
        
        pushMatrix()
        translate(self.x, self.y)
        rotate(self.angle)
        # square(0, 0, self.r)
        rect(0, 0, self.r, self.r)
        popMatrix()
        
        self.angle += 0.2
