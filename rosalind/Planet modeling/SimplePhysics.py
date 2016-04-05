#Constants
import math
from visual import*

G = 6.67545e-11
q = 1 # ocruglenie


def GravForce(item1, item2):
    #print "GraveForce", (G*item1.mass*item2.mass)/(Dist(item1,item2)**2)
    #print Dist(item1,item2), item1.pos, item2.pos
    return (G*item1.mass*item2.mass)/(Dist(item1,item2)**2)
     
    
def Dist(a,b):
    a = a.pos
    b = b.pos
    #print "Dist", round(math.sqrt(round((a[0]-b[0])**2,q) + round((a[1]-b[1])**2,q) + (round((a[2]-b[2])**2,q))),q)
    return math.sqrt((a[0]-b[0])**2+ (a[1]-b[1])**2 + (a[2]-b[2])**2)
    
def Acel(obj1, vect, force):
    vect = vect.norm()
    obj1.acel = obj1.acel + vect*((force)/obj1.mass)
    #print "REAcel",  obj1.acel
    return (force*vect)/obj1.mass
    
def Move(o1,dt, flag):
    # if flag = true - move planet, else calculate next position and speed 
    o1.posDUB = o1.posDUB + o1.speed*dt
    o1.speed = o1.speed + o1.acel*dt
    #move
    if flag:
        o1.pos = o1.posDUB
    return o1

def MoveAll(planets, dt, flag):
    rs = {}   #distances
    gfs = {}  #grave forces
    #calculate 
    for i in range(len(planets)):
        for j in range(len(planets)):
            if j==i: continue  # pass self
            if (i,j) in gfs: continue # dont calculat twice
            #rs[i,j] = Dist(planets[i],planets[j]) # 1,2 distance = 2,1 distance
            #rs[j,i] = rs[i,j]
            gfs[i,j] = GravForce(planets[i],planets[j]) # 1,2 force = 2,1 force
            gfs[j,i] = gfs[i,j]
    #print rs, gfs
    # move it
    for i in range(len(planets)):
        for j in gfs.keys():
            if j[0] != i: continue
            planets[i].acel = planets[i].acel + Acel(planets[i], planets[j[1]].pos - planets[i].pos, gfs[j])
        Move(planets[i],dt, flag)
    
            
            
    
    
    
