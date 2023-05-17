import globals
import projectiles
import random
import time
import pygame

class tank:

    direction = 'none';
    speed = 50
    x = 600
    y = 650
    size = 25
    projectileType = 0
    reloadTime = 3;
    reloadTimeLeft = 3;
    playerTank = False
    hp = 100;
    alive = True;

    def runAI(self):
        self.shoot(-200,-100);
        if(random.uniform(0, 1) > 0.9995):
            if(random.uniform(0, 1) > 0.6):
                self.direction = "left"
            elif(random.uniform(0, 1) < 0.3):
                self.direction = "right"
            else:
                self.direction = "none"

    def tick(self, deltaTime):
        if self.reloadTimeLeft > 0:
            self.reloadTimeLeft = self.reloadTimeLeft - deltaTime;

        if(self.direction == "left"):
            self.x = self.x + self.speed * deltaTime
        if(self.direction == "right"):
            self.x = self.x - self.speed * deltaTime;



    def shoot(self, targetX, targetY):
        #print(self.reloadTimeLeft)
        if(self.reloadTimeLeft < 0):
            print("shoot");
            self.reloadTimeLeft = self.reloadTime;
            #p = projectiles.projectiles()
            #p.x = self.x;
            #p.y = self.y;
            #p.xSpeed = (targetX-self.x)/(targetY-self.y);
            #p.ySpeed = (targetY-self.y)/(targetX-self.x);
            print(self.x);
            globals.proj.append(projectiles.projectiles(self.x,self.y-self.size-50,targetX,targetY));

    def takeDmg(self, ammount):
        self.hp = self.hp - ammount;
        if(self.hp <= 0):
            self.alive = False;

    def draw(self):
        #todo
        pygame.draw.circle(globals.canvas, (255, 255, 255), (self.x, self.y), self.size)