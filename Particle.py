# -*- coding: utf-8 -*- 


class Particle:
    def __init__(self, x, y):
        self.pos = PVector(x, y)
        self.vel = PVector.random2D().mult(5)
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
        
        self.lifetime -= random(1)
        
    
    def edges(self):
        if self.pos.x + self.r > width or self.pos.x - self.r < 0:
            self.vel.x *= -1
        
        if self.pos.y + self.r > height or self.pos.y - self.r < 0:
            self.vel.y *= -1
        
        
            
        
        
    def apply_force(self, force): # force is a Force PVector
        # F=ma, so I think we are assuming m=1
        self.acc.add(force)
        
