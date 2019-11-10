#undo_redo_try.py

from pygame import *

running = True
screen = display.set_mode((800,600))
screen.fill((255,255,255))

undo=[]
redo=[]
#several changes I made to polgon:
points = [] 
click = 0   #the counter for the amount of time passed after initial click
back = screen.copy() #copy the screen at the start of the function
#    (before you start your polygon(), copy the screen)
drewpolygon = False  #checks if user drew polygon
#drewpolygon is crucial because the point on where the double click occurs
#is gonna be added, making the next polygon connected to the first T_T
while running:
    for evt in event.get():
        if evt.type == QUIT:
            running = False
        if evt.type == MOUSEBUTTONDOWN:
            if click < 140 and len(points) >= 3: ##you can change this # if you want
                #it just adjusts how fast the user must click (dont go below 100)
                #a polygon must have 3 sides, so you naturally need 3 points
                points.append(points[0]) #you need the first point to close off the polygon
                draw.polygon(screen,(0,0,0),points,1) #draw a closed polygon
                points = [] #reset the points
                drewpolygon = True #user has drawn polgon
            click = 0   #reset click
            back = screen.copy()
            undo.append(back)
            startx,starty = mouse.get_pos()
#you should do undo redo all in the MOUSEBUTTONUP event, cuz thats where
# you are done drawing all your stuff :D
        if evt.type == MOUSEBUTTONUP:
            if drewpolygon == False: #if user didnt draw a new polygon add point
                points.append((mx,my))
            else:
                drewpolygon = False  #resets so that the points can be added

    click += 1
    mx,my = mouse.get_pos()
    mb = mouse.get_pressed()

    if mb[2]==1:
        redo.append(undo[-1])
            
    if mb[0] == 1:
        screen.blit(back,(0,0))
        if len(points) > 0:
            draw.line(screen,(0,0,0),points[-1],(mx,my),1)
        else:
            draw.line(screen,(0,0,0),(mx,my),(mx,my),1)
    if mb[2]==1 :
        screen.blit(undo[-1],(0,0))

    display.flip()
quit()
