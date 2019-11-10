#graph5.py
#this program displays a picture of background and prints out the colour of the
#area selected and diplays it on the top left corner
from pygame import*

screen=display.set_mode((1000,800))
massey=image.load("backgroundNEW_.png")
running=True

while running:
    for evt in event.get():
        if evt.type == QUIT:
            running = False
    screen.blit(massey,(0,0))
    mx,my=mouse.get_pos()
    mb=mouse.get_pressed()
    if mb[0] >= 1:
        c= screen.get_at((mx,my))
        draw.rect(screen,c,(0,0,50,50))
        print(mx,my)



    
    display.flip()
quit()
            
