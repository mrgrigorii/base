# -*- coding: utf-8 -*-
import math
import random

class unit():
    def __init__(self, x, y):
        #print "Init Unit"
        self.x = x
        self.y = y
        self.health = 100
        self.speed = 1
        self.damage = 5
        self.defence = 50
        self.range = 10
        return

    def get_location(self):
        return self.x, self.y

    def move(self, d_x, d_y):
        #print "Move"
        self.x = self.x - d_x
        self.y = self.y - d_y
        #print self.get_location()
        return self.x, self.y

    def calc_distance(self, u):
        x = math.fabs(u.x - self.x)
        y = math.fabs(u.y - self.y)
        distance = math.sqrt(x*x + y*y)
        #print 'Distance', distance
        return distance


    def find_target(self, units):
        #print "Find Target"
        distance = 1000000
        self.target = None
        for u in units:
            if u is self:
                continue
            assert isinstance(u, unit)
            dist = self.calc_distance(u)
            if dist < distance:
                distance = dist
                self.target = u
        return self.target

    def attack(self, u):
        #print "Attack"
        if random.random()*100 > u.defence:
            u.health = u.health - self.damage
            # В классе battle проверять живы ли юниты
            return  self.damage
        return 0

    def act(self, units):
        if self.find_target(units) != None:
            distance = self.calc_distance(self.target)
            if distance <= self.range:
                self.attack(self.target)
            else:
                d_x, d_y = 0, 0
                if self.target.x > self.x:
                    d_x = - self.speed
                else:
                    d_x = self.speed
                if self.target.y > self.y:
                    d_y = - self.speed
                else:
                    d_y = self.speed
                #Черновой вариант.
                # По диагонали скорость быстрее получается
                self.move(d_x, d_y)
        return 0



