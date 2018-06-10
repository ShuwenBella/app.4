import math

####################
# helper functions #
#------------------#

def polar2cart(phi, r):
    x = r * math.cos(phi)
    y = r * math.sin(phi)

    return (x,y)

def cart2polar(x,y):
    r = math.sqrt(x*x + y*y)
    phi = math.atan2(y, x)

    return (phi, r)

def norm(x,y):
    return math.sqrt(x**2 + y**2)

#------------------#
# helper functions #
####################


def Phi(u,v):
    x = (1 + (1./3.)*v) * math.cos(math.pi / 6. * u)
    y = (1 + (1./3.)*v) * math.sin(math.pi / 6. * u)

    return (x,y)

def Jacobian(u,v):
    dxdu = -math.pi / 6. * (1 + (1./3.)*v) * math.sin(math.pi / 6. * u)
    dydu =  math.pi / 6. * (1 + (1./3.)*v) * math.cos(math.pi / 6. * u)

    dxdv = (1./3.) * math.cos(math.pi / 6. * u)
    dydv = (1./3.) * math.sin(math.pi / 6. * u)

    return ((dxdu, dxdv), (dydu, dydv))

def invJacobian(u,v):
    J = Jacobian(u,v)
    iDetJ = 1. / (J[0][0]*J[1][1] - J[0][1]*J[1][0])
    return ((iDetJ * J[1][1], -iDetJ * J[0][1]), (-iDetJ * J[1][0], iDetJ * J[0][0]))


def update(u, v, x, y):
    P = Phi(u,v)
    invJ = invJacobian(u,v)
    
    du = invJ[0][0] * (x - P[0]) + invJ[0][1] * (y - P[1])
    dv = invJ[1][0] * (x - P[0]) + invJ[1][1] * (y - P[1])

    return (du,dv)

u, v = 1.5, 1.5
phi, r = math.pi / 12., 11. / 6.

x,y = polar2cart(phi,r)

# stencil walk
#while norm((x - Phi(u,v)[0]),(y - Phi(u,v)[1])) > 1e-5:
#    dx = update(u,v,x,y)
#    u = u + dx[0]
#    v = v + dx[1]

for i in range(1):
    dx = update(u,v,x,y)
    u = u + dx[0]
    v = v + dx[1]

print "Input:"
print "(phi,r) = " + str((phi,r))
print "(x,y) = " + str((x,y))
print "-----------------------------------"
print "Result of stencil walk:"
print "(u,v) = " + str((u,v))
print "(x,y) = " + str(Phi(u,v))

x, y = Phi(u,v)
phi, r = cart2polar(x, y)
print "(phi,r) = " + str((phi,r))
