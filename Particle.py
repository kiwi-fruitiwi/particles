# -*- coding: utf-8 -*- 


class Particle(PVector):
    def __init__(self, x, y):
        super(Particle, self).__init__(x, y)
        # self.pos = PVector(x, y)
        # self.vel = PVector.random2D().mult(random(0.05, 2))
        self.vel = PVector(random(-2, 2), random(0, -1))
        self.acc = PVector(0, 0)
        self.r = int(random(4, 16))
        
        # we want to tie the lifetime to the transparency
        # as lifetime decreases, our particle fades away
        self.lifetime = random(50, 100)
    
    
    def finished(self):
        return self.lifetime < 0
        
    
    def show(self):
        stroke(0, 0, 100, self.lifetime)
        
        # fill(map(self.lifetime, 0, 100, 0, 360), 100, 100, self.lifetime)
        fill(0, 0, 100, self.lifetime)
        
        if self.finished():
            stroke(random(360), 100, 100, 100)
            # fill(random(360), 100, 100, 30)
            
        circle(self.x, self.y, self.r)         
        # rect(self.x, self.y, self.r, self.r)
        
    
    def update(self):
        self.vel.add(self.acc)
        self.add(self.vel)
        self.acc = PVector(0, 0)
        
        
        # hacked-in air resistance?
        self.vel.mult(0.99)        
        self.lifetime -= random(1)
        
        
    
    # check to make sure our particle is constrained within the edges
    # of the canvas. invert velocity if it goes past an edge to give a
    # "bounce" effect. 
    def edges(self):
        if self.x + self.r >= width:
            self.vel.x *= -1
            
            # this extra line is needed to constrain our particle's position
            # within the canvas
            self.x = width - self.r
            
        if self.x - self.r <= 0:
            self.vel.x *= -1
            self.x = self.r
        
        if self.y + self.r >= height:
            self.vel.y *= -1
            self.y = height - self.r
            
        if self.y - self.r <= 0:
            self.vel.y *= -1
            self.y = self.r

        
    def apply_force(self, force): # force is a Force PVector
        # F=ma, so I think we are assuming m=1
        self.acc.add(force)
