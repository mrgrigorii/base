from visual import*
from SimplePhysics import*

#time delta t sec
dt = 0.001
# calculateses betveen draw
N = 100


planets = []
planet_1 = sphere(make_trail=True, pos = vector(-50,0,0), radius = 5.5, color = color.green, mass = 1e6, speed = vector(1,0,0), acel = vector(0,0,0), posDUB = vector(-50,0,0))
planets.append(planet_1)
planet_2 = sphere(make_trail=True, pos = vector(0,0,0), radius = 10.5, color = color.orange, mass = 1e6, speed = vector(0,0,1), acel = vector(0,0,0), posDUB = vector(0,0,0))
planets.append(planet_2)
planet_3 = sphere(make_trail=True, pos = vector(0,40,0), radius = 5.5, color = color.red, mass = 1e6, speed = vector(0,0,0), acel = vector(0,0,0), posDUB = vector(0,40,0))
#planets.append(planet_3)
planet_4 = sphere(make_trail=True, pos = vector(0,50,40), radius = 5.5, color = color.white, mass = 1e6, speed = vector(0,0,0), acel = vector(0,0,0), posDUB = vector(0,50,40))
#planets.append(planet_4)
#arrow(pos=vector(1,0,0), axis=vector(+1,+3,0), color = color.red)

r = vector (-3,4,0)
print GravForce(planet_1, planet_2)

#MoveAll(planets,dt)

while True:
    rate(400)  # 10 calculate in second
    flag = False
    for i in range(N):
        MoveAll(planets,dt, flag)
    flag = True
    MoveAll(planets,dt, flag)
    #F = GravForce(planet_1,planet_2)
    #planet_1.acel = Acel(planet_1, planet_2.pos - planet_1.pos, F)
    #planet_2.acel = Acel(planet_2, planet_1.pos - planet_2.pos, F)
    #planet_1 = Move(planet_1,dt)
    #planet_2 = Move(planet_2,dt)
    #planet_1.pos[1] = planet_1.pos[1]+1000
    #print "planet_1", planet_1.pos
    #print "planet_2", planet_2.pos
	


    
    
    
