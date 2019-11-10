#Brush Fix

from pygame import *
from random import *
from math import *
screen=display.set_mode((1024,768))
running=True
currentColour=(255,0,0)
#=========================================================================#
radius=10                                               #Size for jet tools
mx=0
my=0
#=========================================================================#
while running:
    for evt in event.get():
        if evt.type==QUIT:
            running=False
    omx=mx                                              #Old Mx, for jet tools
    omy=my                                              #Old My, for jet tools
    mx,my=mouse.get_pos()
    mb=mouse.get_pressed()
    #=====================================================================#
    if mb[0]==1:
        draw.circle(screen,currentColour,(mx,my),radius)
        for i in range (-10,10):
            draw.line(screen,currentColour,(mx+i,my),(omx+i,omy),1)
            draw.line(screen,currentColour,(mx,my+i),(omx,omy+i),1)
        
    #=====================================================================#
    display.flip()
quit()
