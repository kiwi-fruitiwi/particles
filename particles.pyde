# This is an exercise from Daniel Shiffman's the Nature of Code
# Particle Systems - A Technique for Modeling a Class of Fuzzy Objects
# 1983 paper by William T. Reeves
# Particle systems have these attributes: position, velocity, size, 
# color, transparency, shape, and lifetime
#
# v0.01 bouncing, fading particles with gravity
# v0.02 randomized initial velocity to create fireworks
# v0.03
# v0.04
# v0.05
# TODO: we are at 5:15 of the video now 
# https://www.youtube.com/watch?v=syR0klfncCk&list=PLRqwX-V7Uu6ZV4yEcW3uDwOgGXKUUsPOM&index=33


from Particle import *        
        
def setup():
    global particles
    
    size(700, 300)
    colorMode(HSB, 360, 100, 100, 100)
    
    particles = []
    
    for i in range(500):
        # particles.append(Particle(random(width), random(height)))
        particles.append(Particle(width/2, height/2))


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
    
    wind = PVector(0.5, 0)
    
    for p in particles:
        p.apply_force(wind)
        p.update()
        p.edges()
        p.show()
    
     
