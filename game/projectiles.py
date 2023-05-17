import globals
import pygame

class projectilesThing:
    xSpeed = 0;
    ySpeed = 0;
    x = 0;
    y = 0;
    damage = 100
    exist = True;
    def __init__(self,x,y,xSpeed,ySpeed):
        self.x = x;
        self.y = y;
        self.xSpeed = xSpeed;
        self.ySpeed = ySpeed;

    def tick(self, deltaTime, gravity):
        self.ySpeed = self.ySpeed + gravity*deltaTime
        self.y = self.y + self.ySpeed*deltaTime
        self.x = self.x + self.xSpeed*deltaTime

        for i in globals.tanks:
            if abs(i.x - self.x) <= i.size and abs(i.y - self.y) <= i.size:
                i.takeDmg(self.damage)
                self.exist = False;

        for i in globals.planes:
            if abs(i.x - self.x) <= i.size and abs(i.y - self.y) <= i.size:
                i.takeDmg(self.damage)
                self.exist = False;

    def draw(self):
        pygame.draw.circle(globals.canvas, (255, 0, 0), (self.x, self.y), 10)
