import random
import matplotlib.pyplot as plt
import math


class Bound:
    def __init__(self, s = -1, e = 1):
        if e > 0:
            self.e = e
        else:
            print('Error! e > 0')
        if s < 0:
            #self.s = random.gauss(7, 2)      
            self.s = random.uniform(2, 10)
            #self.s = random.choice([random.gauss(6, 0.3), random.gauss(4, 0.3), \
            #    random.gauss(10, 0.3),random.gauss(8, 0.3), random.gauss(2, 0.3) ])  
        else:
            self.s = s
        self.bound = 1
            
    def calc_stregth(self, x):
        if self.e*x > self.s:
            self.bound = 0
            return 0
        else:
            self.bound = 1
            return self.e*x
        

class Bounds:
    def __init__(self, n):
        self.bounds = []
        for i in range(n):
            self.bounds.append(Bound())
        
    def calc_all_strength(self, x):
        s = 0
        for i in self.bounds:
            s = s + i.calc_stregth(x)
        return s
        
    def calc_x(self, strength, dx):
        rez_x = []
        rez_s = []
        rez_d = []
        x = dx
        while abs(strength - self.calc_all_strength(x)) > 0.001*strength:
            s = self.calc_all_strength(x)
            #print (x, s)
            if s == 0:
                print('Limit off')
                return 'Limit off', s, rez_x, rez_s, rez_d
            rez_x.append(x)
            rez_s.append(s)
            rez_d.append(self.calc_d())
            x = x + dx
        return x, s, rez_x, rez_s, rez_d
    
    def calc_d(self):
        n = 0
        for i in self.bounds:
            if i.bound == 1:
                n = n + 1
        l = len(self.bounds)
        return (0.0 + l - n) / l
    
    def __str__(self):
        n = 0
        for i in self.bounds:
            if i.bound == 1:
                n = n +1
        l = len(self.bounds)
        return 'All bounds: ' + str(l) + ' broken bounds: ' + str(l - n)



b = Bound()
#print b, b.e, b.s
#print b.calc_stregth(1), b.bound, b.calc_stregth(2), b.bound

bounds = Bounds(1000)


    
#print('Strength:', bounds.calc_all_strength(0.1), ' ', bounds)
#print('X:', bounds.calc_x(270, 0.01))
#print 'Strength:', bounds.calc_all_strength(3), ' ', bounds

x, s, rez_x, rez_s, rez_d = bounds.calc_x(31000, 0.01)
print(x,s)
#plt.plot([1, 3, 2, 4],[2,3,5,6])
plt.plot(rez_x,rez_s)
plt.xlabel('e')    # обозначение оси абсцисс
plt.ylabel('s')    # обозначение оси ординат
plt.savefig('plot1.png', dpi=500)
plt.show()

plt.plot(rez_d,rez_s)
plt.xlabel('d')    # обозначение оси абсцисс
plt.ylabel('s')    # обозначение оси ординат
plt.savefig('plot2.png', dpi=500)
plt.show()
