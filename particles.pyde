# This is an exercise from Daniel Shiffman's the Nature of Code
# Particle Systems - A Technique for Modeling a Class of Fuzzy Objects
# 1983 paper by William T. Reeves
# Particle systems have these attributes: position, velocity, size, 
# color, transparency, shape, and lifetime
#
# v0.01 bouncing, fading particles with gravity
# v0.02 randomized initial velocity to create fireworks
# v0.03 sparkler! remove particles past their lifetime
# v0.04
# v0.05
# TODO: we are at 5:15 of the video now 
# https://www.youtube.com/watch?v=syR0klfncCk&list=PLRqwX-V7Uu6ZV4yEcW3uDwOgGXKUUsPOM&index=33


from Particle import *        
        
def setup():
    global particles
    
    size(700, 700)
    colorMode(HSB, 360, 100, 100, 100)
    
    particles = []
    noCursor()
    


def draw():
    global particles
    background(209, 95, 33)
    for i in range(3):
        # particles.append(Particle(random(width), random(height)))
        # particles.append(Particle(width/2, height/2))
        particles.append(Particle(mouseX, mouseY))
    
    gravity = PVector(0, 0.2)
    
    
    # we loop backwards because we want to remove elements from the list
    # as we go. we're removing the particles past their lifetime ; ;
    for i in range(len(particles)-1, 0, -1):
        p = particles[i]
        
        p.apply_force(gravity)
        p.update()
        # p.edges()
        p.show()
        
        if p.finished():
            fill(90, 100, 100, 80)
            p.show()
            particles.pop(i)
    
    
    fill(0, 0, 100)
    text(len(particles), 10, height-50)


def mousePressed():
    global particles
    
    wind = PVector(0.5, 0)
    
    for p in particles:
        p.apply_force(wind)
        p.update()
        p.edges()
        p.show()
    
     
