from globals import *
from tank import *
from projectiles import *
import time
import pygame

print (pygame.ver)


deltaTime = 0;
startTime = time.time();
endTime = time.time();

gravity = 100
playerTank = 0

globals.tanks.append(tank())
globals.tanks.append(tank())
tanks[playerTank].playerTank = True;

globals.proj.append(projectiles(0,0,0,0))

#setup drawing window
globals.canvas = pygame.display.set_mode([1200, 700])

#game loop
while(True):
    endTime = time.time();
    deltaTime = endTime - startTime
    startTime = time.time()

    for i in tanks:
        if(i.alive):
            if i.playerTank:
                i.runAI();
            else:
                #get user input
                events = pygame.event.get()
                for event in events:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_a:
                            i.direction = "left"
                        if event.key == pygame.K_d:
                            i.direction = "right"
                        if event.key == pygame.K_SPACE:
                            print("click")
                            mousex, mousey = pygame.mouse.get_pos()
                            i.shoot(mousex-i.x,mousey-i.y)



                j = 0
                #print("awaint user input")
            i.tick(deltaTime);
            i.draw();

    for i in proj:
        if(i.exist):
            i.tick(deltaTime, gravity);
            i.draw();


    pygame.display.flip()
    globals.canvas.fill((0, 0, 0))