from Particle import *
from Confetti import *

class Emitter:    
    # x, y is where our Emitter starts emitting
    def __init__(self, x, y, type):
        self.pos = PVector(x, y)
        self.particles = []
        self.emission_rate = 1
        self.type = type
        
            
    def show(self):
        for p in self.particles:
            p.show()
    
    
    def emit(self, quantity):
        for i in range(self.emission_rate):
            # particles.append(Particle(random(width), random(height)))
            # particles.append(Particle(width/2, height/2))
            if self.type == "particle":
                self.particles.append(Particle(self.pos.x, self.pos.y))
            
            if self.type == "confetti":
                self.particles.append(Confetti(self.pos.x, self.pos.y))
                
    
    def apply_force(self, force):
        for p in self.particles:
            p.apply_force(force)   
    
    
    def update(self):
        self.emit(self.emission_rate)
        
        # we loop backwards because we want to remove elements from the list
        for i in range(len(self.particles)-1, 0, -1):
            p = self.particles[i]
            
            p.update()
            p.edges()
            
            
            # remove particles past their lifetime ; ;
            if p.finished():
                p.show()
                self.particles.pop(i)            
