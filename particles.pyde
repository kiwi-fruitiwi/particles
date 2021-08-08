# This is an exercise from Daniel Shiffman's the Nature of Code
# Particle Systems - A Technique for Modeling a Class of Fuzzy Objects
# 1983 paper by William T. Reeves
# Particle systems have these attributes: position, velocity, size, 
# color, transparency, shape, and lifetime
#
# v0.01 bouncing, fading particles with gravity
# v0.02 randomized initial velocity to create fireworks
# v0.03 sparkler! remove particles past their lifetime
# v0.04 emitters + confetti, apply_force in emitter
# v0.05
# TODO: we are at 5:15 of the video now 
# https://www.youtube.com/watch?v=syR0klfncCk&list=PLRqwX-V7Uu6ZV4yEcW3uDwOgGXKUUsPOM&index=33


from Particle import *        
from Emitter import *      
from Confetti import *
                       
def setup():
    global emitters
    
    size(700, 700)
    colorMode(HSB, 360, 100, 100, 100)
    rectMode(CENTER)
    
    emitters = []
    # emitters.append(Emitter(width/2, height/8))
    # noCursor()
    

def draw():
    global emitters
    background(209, 95, 33)
    
    total_particles = 0
            
    gravity = PVector(0, 0.1)
    wind = PVector(random(-0.2, 0.2), random(-0.1, 0.1))
    MAX = 0.1
    
    for emitter in emitters:
        # emitter.apply_force(gravity.add(wind))
        # emitter.apply_force(PVector(0, -0.1))
        emitter.apply_force(PVector(map(mouseX, 0, width, -MAX, MAX), 
                                    map(mouseY, 0, height, -MAX, -MAX)))
        emitter.update()
        emitter.show()
        total_particles += len(emitter.particles)
    
    fill(0, 0, 100)
    text(total_particles, 10, height-50)


def mousePressed():
    global emitters
    
    if mouseButton == LEFT:
        print "left"
        emitters.append(Emitter(mouseX, mouseY, "particle"))
    else:
        emitters.append(Emitter(mouseX, mouseY, "confetti"))
    
    # for p in particles:
    #     p.apply_force(wind)
    #     p.update()
    #     p.edges()
    #     p.show()
    

def keyPressed():
    global emitters
    
    if key == "r":
        emitters = []
    
    
