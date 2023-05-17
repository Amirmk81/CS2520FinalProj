import globals
import pygame

class projectilesThing:
    '''
    The projectile class. Creates and implements the projectile.
    '''

    xSpeed = 0
    ySpeed = 0
    x = 0
    y = 0
    damage = 100
    exist = True

    def __init__(self, x, y, xSpeed, ySpeed):
        '''
        Initializes the projectile object with the given parameters.

        Args:
            x (int): The initial x position of the projectile.
            y (int): The initial y position of the projectile.
            xSpeed (int): The initial speed of the projectile in the x direction.
            ySpeed (int): The initial speed of the projectile in the y direction.
        '''
        self.x = x
        self.y = y
        self.xSpeed = xSpeed
        self.ySpeed = ySpeed

    def tick(self, deltaTime, gravity):
        '''
        Updates the projectile's position and checks for collisions with tanks and planes.

        Args:
            deltaTime (float): The time passed since the last update.
            gravity (int): The strength of the gravitational force affecting the projectile.
        '''
        self.ySpeed = self.ySpeed + gravity * deltaTime
        self.y = self.y + self.ySpeed * deltaTime
        self.x = self.x + self.xSpeed * deltaTime

        for i in globals.tanks:
            if abs(i.x - self.x) <= i.size and abs(i.y - self.y) <= i.size:
                i.takeDmg(self.damage)
                self.exist = False

        for i in globals.planes:
            if abs(i.x - self.x) <= i.size and abs(i.y - self.y) <= i.size:
                i.takeDmg(self.damage)
                self.exist = False

    def draw(self):
        '''
        Draws the projectile on the screen.
        '''
        pygame.draw.circle(globals.canvas, (255, 0, 0), (self.x, self.y), 10)
