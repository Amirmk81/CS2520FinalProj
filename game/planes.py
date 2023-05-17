import globals
import projectiles
import random
import time
import pygame


class plane:
    '''
        The plane class. creates and implements the planes
    '''

    direction = 'none';
    speed = 50
    x = 600
    y = 50
    size = 25
    projectileType = 0
    reloadTime = 3;
    reloadTimeLeft = 3;
    playerTank = False
    hp = 100;
    alive = True;

    def runAI(self):
        '''
            Method to control movement and direction of planes
        '''
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
        '''
            Shoot method for planes
        '''
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
            globals.proj.append(projectiles.projectilesThing(self.x,self.y+self.size+50,0,0));

    def takeDmg(self, ammount):
        '''
            Damage method for planes
        '''
        self.hp = self.hp - ammount;
        if(self.hp <= 0):
            self.alive = False;

    def draw(self):
        '''
            Drew method to draw the plane
        '''
        #todo
        pygame.draw.circle(globals.canvas, (255, 255, 255), (self.x, self.y), self.size)
