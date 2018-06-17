import random
import math

#init variables
size = 256
kernelwidth = 11

#define vector field
def vecField(x, y):
    center = size/2
    vx = float(y) - float(center)
    vy = float(center) - float(x)
    l = math.sqrt(vx * vx + vy * vy)
    if l != 0:
        vx = vx / l
        vy = vy / l

    return (vx, vy)

#clamping to image sizes
#set p to 0 if negative and to size-1 if to greater
def checkBounds(p):
        #your code here
    return p

#bilinear interpolation
#img is defined at integer valued indices
def imgAt(img, x, y):
        #your code here
    return ret



#init random number image of appropriate size
img = 
#initialize output image of appropriate size
lic =


#################################################
#write noise image to 'assignment6.1-noise.pgm' in PGM format
#open file
f = ...

#write header

#write image information

#close file
#################################################



#################################################
#perform lic
    #initialize res with img at current position

    #perfom K explicit euler steps in positive direction
    #K = kernelwidth/2

        #compute new coordinates
        #clamp coordinates
                        
        #get image at new position using bilinear interpolation
        #add to res
    
    #perfom K explicit euler steps in negative direction
    #K = kernelwidth/2

        #compute new coordinates
        #clamp coordinates
                        
        #get image at new position using bilinear interpolation
        #add to res        
              
    #normalize by kernelwidth and set lic pixel in output image
#################################################


#################################################
#write output lic image to 'assignment6.1.pgm'
#open file
f = ...

#write header

#write image information


#close file
#################################################