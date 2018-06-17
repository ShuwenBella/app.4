import random
import math

#init variables
size = 256
kernelwidth = 10

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

def checkBounds(p):
    if p < 0:
        p = 0
    if p > (size-1):
        p = (size-1)
    return p

def imgAt(img, x, y):
    dx = x - math.floor(x)
    dy = y - math.floor(y)
    i0 = img[int(math.floor(y) * size + math.floor(x))]
    i1 = img[int(math.floor(y) * size + math.ceil(x))]
    i2 = img[int(math.ceil(y) * size + math.floor(x))]
    i3 = img[int(math.ceil(y) * size + math.ceil(x))]

    i01 = dx * i1 + (1.0 - dx) * i0
    i23 = dx * i3 + (1.0 - dx) * i2

    ret = dy * i23 + (1.0 - dy) * i01
    return ret

#init random number image of appropriate size
img = [random.randint(0,255) for _ in xrange(size*size)]

#write to PGM
f = open('img.pgm', 'w')
f.write('P2\n')
f.write(str(size) + ' ' + str(size) + '\n')
f.write('255\n')

for y in range(0, size):
    for x in range(0, size):
        f.write(str(int(img[y*size + x])) + ' ')

f.close()


lic = [0] * (size*size)
#perform lic
for y in range(0, size):
    for x in range(0, size):
        res = imgAt(img, x, y)
        curX = x
        curY = y
        for i in range(1, kernelwidth/2):
            (vx, vy) = vecField(curX, curY)
            curX = curX + vx
            curX = checkBounds(curX)
            curY = curY + vy
            curY = checkBounds(curY)
            res = res + imgAt(img, curX, curY)
        curX = x
        curY = y
        for i in range(1, kernelwidth/2):
            (vx, vy) = vecField(curX, curY)
            curX = curX - vx
            curX = checkBounds(curX)
            curY = curY - vy
            curY = checkBounds(curY)
            res = res + imgAt(img, curX, curY)
        lic[y*size + x] = res / float(kernelwidth)


#write to PGM
f = open('lic.pgm', 'w')
f.write('P2\n')
f.write(str(size) + ' ' + str(size) + '\n')
f.write('255\n')

for y in range(0, size):
    for x in range(0, size):
        f.write(str(int(lic[y*size + x])) + ' ')
    f.write('\n ')
f.close()
