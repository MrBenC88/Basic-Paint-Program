from pygame import *
from random import *
from glob import *

''' -------------------------------------------------------------
    getName
    -------------------------------------------------------------
    Because pygame likes to crash you can copy and paste my getName
    function into your program and use it, free of charge.  You
    may want to change the size of the rectange, it's location, the
    font, and the colour so that it matches your program.
    ------------------------------------------------------------- '''
def getName():
    ans = ""                    # final answer will be built one letter at a time.
    arialFont = font.SysFont("Times New Roman", 16)
    back = screen.copy()        # copy screen so we can replace it when done
    textArea = Rect(5,5,200,25) # make changes here.
    
    pics = glob("*.bmp")+glob("*.jpg")+glob("*.png")
    n = len(pics)
    choiceArea = Rect(textArea.x,textArea.y+textArea.height,textArea.width,n*textArea.height)
    draw.rect(screen,(220,220,220),choiceArea)        # draw the text window and the text.
    draw.rect(screen,(0,0,0),choiceArea,1)        # draw the text window and the text.
    for i in range(n):
        txtPic = arialFont.render(pics[i], True, (0,111,0))   #
        screen.blit(txtPic,(textArea.x+3,textArea.height*i+choiceArea.y))
        
    typing = True
    while typing:
        for e in event.get():
            if e.type == QUIT:
                event.post(e)   # puts QUIT back in event list so main quits
                return ""
            if e.type == KEYDOWN:
                if e.key == K_BACKSPACE:    # remove last letter
                    if len(ans)>0:
                        ans = ans[:-1]
                elif e.key == K_KP_ENTER or e.key == K_RETURN : 
                    typing = False
                elif e.key < 256:
                    ans += e.unicode       # add character to ans
                    
        txtPic = arialFont.render(ans, True, (0,0,0))   #
        draw.rect(screen,(220,255,220),textArea)        # draw the text window and the text.
        draw.rect(screen,(0,0,0),textArea,2)            #
        screen.blit(txtPic,(textArea.x+3,textArea.y+2))
        
        display.flip()
        
    screen.blit(back,(0,0))
    return ans
       
    


    
screen = display.set_mode((1000,600))
display.set_caption("Right Click to type")
font.init()                                 # must have this in your program for my font to work

comicFont = font.SysFont("Comic Sans MS", 20)

screen.fill((222,222,222))
running =True
y = 20
message = ""
while running:
    click = False
    for e in event.get():
        if e.type == QUIT:
            running = False
                
    mb = mouse.get_pressed()
    mx,my = mouse.get_pos()

    if mb[2]==1:
        txt = getName()                     # this is how you would call my getName function
                                            # your main loop will stop looping until user hits enter
        txtPic = comicFont.render(txt, True, (255,0,0))
        screen.blit(txtPic,(100,100))

    display.flip()

font.quit()
del comicFont

quit()
