# -*- coding: utf-8 -*- 


class Particle:
    def __init__(self, x, y):
        self.pos = PVector(x, y)
        self.vel = PVector.random2D().mult(random(3, 20))
        self.acc = PVector(0, 0)
        self.r = 4
        
        # we want to tie the lifetime to the transparency
        # as lifetime decreases, our particle fades away
        self.lifetime = 100
    
    
    def show(self):
        stroke(0, 0, 100, self.lifetime)
        fill(0, 0, 100, self.lifetime)
        circle(self.pos.x, self.pos.y, self.r) 
        
    
    def update(self):
        self.vel.add(self.acc)
        self.pos.add(self.vel)
        self.acc = PVector(0, 0)
        
        
        # hacked-in air resistance?
        self.vel.mult(0.999)
        
        self.lifetime -= random(0.5)
        
    
    # check to make sure our particle is constrained within the edges
    # of the canvas. invert velocity if it goes past an edge to give a
    # "bounce" effect. 
    def edges(self):
        if self.pos.x + self.r >= width:
            self.vel.x *= -1
            
            # this extra line is needed to constrain our particle's position
            # within the canvas
            self.pos.x = width - self.r
            
        if self.pos.x - self.r <= 0:
            self.vel.x *= -1
            self.pos.x = self.r
        
        if self.pos.y + self.r >= height:
            self.vel.y *= -1
            self.pos.y = height - self.r
            
        if self.pos.y - self.r <= 0:
            self.vel.y *= -1
            self.pos.y = self.r
        
        
            
        
        
    def apply_force(self, force): # force is a Force PVector
        # F=ma, so I think we are assuming m=1
        self.acc.add(force)
        
