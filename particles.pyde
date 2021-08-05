# This is an exercise from Daniel Shiffman's the Nature of Code
# Particle Systems - A Technique for Modeling a Class of Fuzzy Objects
# 1983 paper by William T. Reeves
# Particle systems have these attributes: position, velocity, size, 
# color, transparency, shape, and lifetime
#
# v0.01 bouncing, fading particles with gravity
# v0.02
# v0.03
# v0.04
# v0.05

from Particle import *        
        
def setup():
    global particles
    
    size(700, 300)
    colorMode(HSB, 360, 100, 100, 100)
    
    particles = []
    
    for i in range(50):
        particles.append(Particle(random(width), random(height)))


def draw():
    global particles
    background(209, 95, 33)
    
    gravity = PVector(0, 0.2)
    
    for p in particles:
        p.apply_force(gravity)
        p.update()
        p.edges()
        p.show()


def mousePressed():
    global particles
    
    # wind = PVector(0.1, 0)
    
     
