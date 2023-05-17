from globals import *
from tank import *
from projectiles import *
from planes import *
import time
import pygame

print(pygame.ver)  # Print the version of Pygame

deltaTime = 0
startTime = time.time()
endTime = time.time()

gravity = 100
playerTank = 0

globals.tanks.append(tank())  # Create a new tank object and add it to the list of tanks
globals.tanks.append(tank())  # Create another tank object and add it to the list of tanks
tanks[playerTank].playerTank = True  # Set the first tank in the list as the player-controlled tank
tanks[playerTank].x = 100  # Set the initial x position of the player tank

globals.planes.append(plane())  # Create a new plane object and add it to the list of planes

globals.proj.append(projectilesThing(0, 0, 0, 0))  # Create a new projectile object and add it to the list of projectiles

# Setup drawing window
globals.canvas = pygame.display.set_mode([1200, 700])

# Game loop
while True:
    endTime = time.time()
    deltaTime = endTime - startTime
    startTime = time.time()

    for i in tanks:
        if i.alive:
            if not i.playerTank:
                i.runAI()  # Run AI logic for non-player tanks
            else:
                # Get user input
                events = pygame.event.get()
                for event in events:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_a:
                            i.direction = "right"  # Set tank direction to right when 'a' key is pressed
                        if event.key == pygame.K_d:
                            i.direction = "left"  # Set tank direction to left when 'd' key is pressed
                        if event.key == pygame.K_SPACE:
                            print("click")  # Print "click" when spacebar is pressed
                            mousex, mousey = pygame.mouse.get_pos()
                            i.shoot(mousex - i.x, mousey - i.y)  # Shoot a projectile towards the mouse position

            i.tick(deltaTime)  # Update tank logic
            i.draw()  # Draw the tank

    for i in globals.planes:
        if i.alive:
            i.runAI()  # Run AI logic for planes
            i.tick(deltaTime)  # Update plane logic
            i.draw()  # Draw the plane

    for i in proj:
        if i.exist:
            i.tick(deltaTime, gravity)  # Update projectile logic with gravity
            i.draw()  # Draw the projectile

    pygame.display.flip()  # Update the display
    globals.canvas.fill((0, 0, 0))  # Clear the canvas for the next frame
