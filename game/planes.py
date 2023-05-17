import globals
import projectiles
import random
import time
import pygame


class plane:
    '''
    The plane class. Creates and implements the planes. 
    '''

    direction = 'none'
    speed = 50
    x = 600
    y = 50
    size = 25
    projectileType = 0
    reloadTime = 3
    reloadTimeLeft = 3
    playerTank = False
    hp = 100
    alive = True

    def runAI(self):
        '''
        Method to control movement and direction of planes for AI-controlled planes.
        '''
        self.shoot(-200, -100)
        if random.uniform(0, 1) > 0.9995:
            if random.uniform(0, 1) > 0.6:
                self.direction = "left"
            elif random.uniform(0, 1) < 0.3:
                self.direction = "right"
            else:
                self.direction = "none"

    def tick(self, deltaTime):
        '''
        Updates the plane's position and handles reloading time.

        Args:
            deltaTime (float): The time passed since the last update.
        '''
        if self.reloadTimeLeft > 0:
            self.reloadTimeLeft = self.reloadTimeLeft - deltaTime

        if self.direction == "left":
            self.x = self.x + self.speed * deltaTime
        if self.direction == "right":
            self.x = self.x - self.speed * deltaTime

    def shoot(self, targetX, targetY):
        '''
        Fires a projectile from the plane towards the specified target.

        Args:
            targetX (int): The x coordinate of the target position.
            targetY (int): The y coordinate of the target position.
        '''
        if self.reloadTimeLeft < 0:
            print("shoot")
            self.reloadTimeLeft = self.reloadTime
            print(self.x)
            globals.proj.append(projectiles.projectilesThing(self.x, self.y + self.size + 50, 0, 0))

    def takeDmg(self, amount):
        '''
        Applies damage to the plane.

        Args:
            amount (int): The amount of damage to be applied.
        '''
        self.hp = self.hp - amount
        if self.hp <= 0:
            self.alive = False

    def draw(self):
        '''
        Draws the plane on the screen.
        '''
        pygame.draw.circle(globals.canvas, (255, 255, 255), (self.x, self.y), self.size)
