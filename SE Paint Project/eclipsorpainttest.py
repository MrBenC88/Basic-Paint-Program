#testundo_edo.py

from pygame import*

screen=display.set_mode((1000,800))
running=True


tool=""
undorect=Rect(770,640,40,40)
redorect=Rect(820,640,40,40)


undoPic=image.load("Undo copy.png")
redoPic=image.load("Redo copy.png")
epic=image.load("eclipsor.jpg")

colour=((255,255,255))
screen.fill((colour))



canvas=Rect(169,146,648,474)
screen.blit(epic,(0,0,1000,800))

screen.blit(undoPic,undorect)
screen.blit(redoPic,redorect)

init()
arialFont2 = font.SysFont("Times New Roman", 26)

draw.rect(screen,(255,255,255),(169,146,648,474),2)
undo=[]
redo=[]

while running:
    click=False
    for evt in event.get():
        if evt.type == QUIT:
            running = False

##        if evt.type==MOUSEBUTTONDOWN:
##            if evt.button==2:
##                click==True
        if evt.type==MOUSEBUTTONUP :
            #if canvas.collidepoint(mx,my) and evt.button == 1:
            if canvas.collidepoint(mx,my) and mb[0]==1:
                change = screen.copy()
                undo.append(change)
            if undorect.collidepoint(mx,my) and mb[2]==1:
                if len(undo) >1 :
                    tool="undo"
                    redo.append(undo[len(undo)-1])
                    undo.remove(undo[len(undo)-1])
                    screen.blit(undo[len(undo)-1],(0,0))
            if redorect.collidepoint(mx,my) and mb[2]==1 :
                if len(redo) > 0:
                    tool="redo"
                    screen.blit(redo[len(redo)-1],(0,0))
                    undo.append(redo[len(redo)-1])
                    redo.remove(redo[len(redo)-1])
            #screen.blit(redo[len(redo)-1],(169,146))

                

            
    mx,my=mouse.get_pos()
    mb=mouse.get_pressed()

    #screen.set_clip(canvas)
    if mb[0] == 1:
        screen.set_clip(canvas)
        draw.line(screen,(255,255,255),(mx,my),(x0,y0),(3))
        screen.set_clip(None)
        
    crect=Rect(0,0,100,100)
    draw.rect(screen,(255,0,0),crect)
    if canvas.collidepoint(mx,my):
        txtPos=arialFont2.render(str(mx)+","+str(my),True,(0,0,0))
        screen.blit(txtPos,crect)

    if mb[2]==1 or mb[0]==1:
        print(tool)

    x0=mx
    y0=my
    display.flip()
quit()
            
