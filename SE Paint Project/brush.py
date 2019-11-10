from pygame import *

running = True
screen = display.set_mode((800,600))
ox,oy = (0,0)
while running:
    for evt in event.get():
        if evt.type == QUIT:
            running = False
    
    mb = mouse.get_pressed()
    mx,my = mouse.get_pos()
    if mb[0]==1:
        draw.circle(screen,(255,255,255),(mx,my),5)
        dx=mx-ox
        dy=my-oy
        dist= int((dx**2 + dy**2)**0.5)
        for i in range(dist):
            fx= int(ox + i/dist*dx)
            fy= int(oy + i/dist*dy)
            draw.circle(screen,(255,255,255),(fx,fy),5)
    ox,oy=mx,my
    if mb[2] == 1:
        screen.fill((0,0,0))
    display.flip()
quit()

        
