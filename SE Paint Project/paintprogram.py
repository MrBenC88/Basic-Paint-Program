# paintprogram.py-
#By: Ben Cheung
# A program that allows the user to draw and create displays on a canvas
#using shapes and various colours. This is based on Microsoft Paint and
#has some of the same functions like eraser, pencil, etc. The user is also
#allowed to save /load.

from pygame import * 
from random import * #must have for random objects(randint)
from math import *
from os import *   # must have for opening text files
from glob import * # must have in order to define functions

display.init()   # <--Must have for caption
display.set_caption("Stick Empires PAINT")

icon=image.load("swNEW.png")#loads image for icon

display.set_icon(icon)# displays the pic as an icon
#----------------------------------------------------------------------------

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
    textArea = Rect(0,0,165,25) # location of where the text is--------Another good location:(559,676,119,40)
    
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
       
#----------------------------------------------------------------------------

#Fun logo before the program runs
screen=display.set_mode((1000,800))  #set screen size
logo=image.load("newlogo.png")    #load image for title screen
running=True                      
skipPic=image.load("skip.png")  #load image for skip picture
skipRect=Rect(900,760,40,40) #skip picture rectangle coordinates and height/width
time.wait(200)
#small evt loop
while running:
    time.wait(200)
    for evt in event.get():
        if evt.type == QUIT:
            running = False
    mouse.set_visible(False)
    screen.blit(logo,(0,0))   #blit image so that it diplays on the pygame window
    #screen.blit(skipPic,skipRect)
    mx,my=mouse.get_pos()
    mb=mouse.get_pressed()
    #screen.blit(skipPic,skipRect)

    #if mb[0]==1 and skipRect.collidepoint(mx,my):
     #   running=False

    display.flip()
    time.wait(2900)
    running = False
quit()
#------------------------------------------------------------------------------
#Fun 2 logo before the program runs
screen=display.set_mode((1000,800))  #set screen size
titlepage=image.load("titlepage2.png")    #load image for title screen
running=True                      
skipPic=image.load("skip.png")  #load image for skip picture
screen.blit(titlepage,(0,0))   #blit image so that it diplays on the pygame window
skipRect=Rect(900,760,40,40) #skip picture rectangle coordinates and height/width
#screen.blit(skipPic,skipRect)
time.wait(200)
#small evt loop
while running:
    time.wait(200)
    for evt in event.get():
        if evt.type == QUIT:
            running = False
    mouse.set_visible(False)
    mx,my=mouse.get_pos()
    mb=mouse.get_pressed()
    #screen.blit(skipPic,skipRect)

    #if mb[0]==1 and skipRect.collidepoint(mx,my):
        #running=False

    display.flip()
    time.wait(2900)
    running = False
quit()

#-----------------------------------------------------------------------------
#set screen size
screen = display.set_mode((1000,800))
mouse.set_visible(True) #show the mouse

white=((255,255,255))   #colour white

screen.fill(white)      #fills whole screen

undo=[]                 #list for undo
blankcanvas=screen.copy()    #sets variable to copying screen
undo.append(blankcanvas)     #adds the screen copy to undo list
redo=[]                      #redo list

playing=True  #a flag making sure music is on or off

points=[]                   #points list for polygon tool

start=0,0                   #start point
size=10                     #size 
fontsize=16   #the default font size

screen.fill((255,255,255))
pencilRect = Rect(170,640,40,40) #  the rectangle in which the 
eraserRect = Rect(220,640,40,40) #  picture/image would be attached to
lineRect=Rect(270,640,40,40)     # It sets the postion of the rectangles
brushRect=Rect(320,640,40,40)
bucketfillRect=Rect(370,640,40,40)
sprayRect=Rect(420,640,40,40)
circleRect=Rect(470,640,40,40)
rectangleRect=Rect(520,640,40,40)
ellipseRect=Rect(570,640,40,40)
polyRect=Rect(620,640,40,40)
rectfillRect=Rect(670,640,40,40)
starRect=Rect(720,640,40,40)
undoRect=Rect(770,640,40,40)
redoRect=Rect(820,640,40,40)
saveRect=Rect(770,690,40,40)
loadRect=Rect(820,690,40,40)
restartRect=Rect(820,274,40,40)
eyedropperRect=Rect(820,234,40,40)
textRect=Rect(720,685,40,40)
questionmarkRect=Rect(820,184,40,40)
playingRect=Rect(820,144,40,40)
copyRect=Rect(570,685,40,40)
pasteRect=Rect(620,685,40,40)
fontRect=Rect(670,685,40,40)

#stamp rectangles positions
minerRect=Rect(173,100,40,40)
swordRect=Rect(223,100,40,40)
archerRect=Rect(273,100,40,40)
mericRect=Rect(323,100,40,40)
magiRect=Rect(373,100,40,40)
speartonRect=Rect(423,100,40,40)
ninjaRect=Rect(473,100,40,40)
flyarcherRect=Rect(523,100,40,40)
engiantRect=Rect(573,100,40,40)
bomberRect=Rect(623,100,40,40)
medusaRect=Rect(673,100,40,40)
deadRect=Rect(723,100,40,40)

#----------------------------------------------------------------------------
#Paint Picker Rectangle Position

paintpickerRect=Rect(825,324,20,274) #paint picker rectangle size

canvasRect=Rect(169,146,648,474) #---- the size of the canvas

tool=""   # need only if no default tool is needed
tool="pencil" # pencil is the starting default tool in this program

#----------------------------------------------------------------------------

music=["Call to Arms.mp3","Field Memories.mp3","Order rebellion.mp3"]
init()# need init to initialize the mixer


mixer.music.load("Call to Arms.mp3")       # load a MUSIC object
#mixer.music.load(choice(music))       # load a MUSIC object
mixer.music.play(-1)    #plays the loaded music object infinite times
#mixer.music.queue("Field Memories.mp3")


##mixer.music.load("Field Memories.mp3")
##mixer.music.play(1)

#---------------------------------------------------------------------------
init()   #must have for font
arialFont2 = font.SysFont("Times New Roman", 27)#gets font by setting variable


#----------------------------------------------------------------------------
background=image.load("backgroundNEW_.png")

eraserpic=image.load("erasernew.png")       #load all images to assigned pic
pencilpic=image.load("Pencil New.png")          
linepic=image.load("LineIconNEW.png")
brushpic=image.load("brushNEW.png")
bucketfillPic=image.load("bucket NEW.png")
sprayPic=image.load("spraypaintnew.png")
circlePic=image.load("CircleNEW.png")
rectanglePic=image.load("rectangle_iconNEW.png")
ellipsePic=image.load("eclipse.png")
polyPic=image.load("polygon_iconNEW.png")
rectfillPic=image.load("filledrect.png")
starPic=image.load("star.png")
undoPic=image.load("Undo copy.png")
redoPic=image.load("Redo copy.png")
savePic=image.load("save copy.png")
loadPic=image.load("upload copy.png")
restartPic=image.load("restart.png")
eyedropperPic=image.load("eyedropper.png")
questionmarkPic=image.load("q.png")
pausePic=image.load("pause copy.png")
playPic=image.load("play copy.png")
textPic=image.load("text.png")
fontPic=image.load("Font.png")
copyPic=image.load("copy_icon.png")
pastePic=image.load("paste copy.png")

#stamp pics
minerPic=image.load("miner copy.png")
swordPic=image.load("swordwrath.png")
archerPic=image.load("archidon.png")
mericPic=image.load("meric.png")
magiPic=image.load("magikill.png")
speartonPic=image.load("spearton.png")
ninjaPic=image.load("shadowrath.png")
flyarcherPic=image.load("allbowtross.png")
engiantPic=image.load("enslavedgiant.png")
bomberPic=image.load("bomber.png")
medusaPic=image.load("medusa.png")
deadPic=image.load("dead.png")

#--------------------------------------------------------------------------
screen.blit((background),(0,0))             # loads image for background
screen.blit(eraserpic,eraserRect)           # loads Eraser Image
screen.blit(pencilpic,pencilRect)           # loads Pencil Image
screen.blit(linepic,lineRect)               # loads Line Image,etc..
screen.blit(brushpic,brushRect)
screen.blit(bucketfillPic,bucketfillRect)
screen.blit(sprayPic,sprayRect)
screen.blit(circlePic,circleRect)
screen.blit(rectanglePic,rectangleRect)
screen.blit(ellipsePic,ellipseRect)
screen.blit(polyPic,polyRect)
screen.blit(rectfillPic,rectfillRect)
screen.blit(starPic,starRect)
screen.blit(undoPic,undoRect)
screen.blit(redoPic,redoRect)
screen.blit(savePic,saveRect)
screen.blit(loadPic,loadRect)
screen.blit(restartPic,restartRect)
screen.blit(eyedropperPic,eyedropperRect)
screen.blit(questionmarkPic,questionmarkRect)
screen.blit(pausePic,playingRect)
screen.blit(textPic,textRect)
screen.blit(fontPic,fontRect)
screen.blit(copyPic,copyRect)
screen.blit(pastePic,pasteRect)

#stamps
screen.blit(minerPic,minerRect)
screen.blit(swordPic,swordRect)
screen.blit(archerPic,archerRect)
screen.blit(mericPic,mericRect)
screen.blit(magiPic,magiRect)
screen.blit(speartonPic,speartonRect)
screen.blit(ninjaPic,ninjaRect)
screen.blit(flyarcherPic,flyarcherRect)
screen.blit(engiantPic,engiantRect)
screen.blit(bomberPic,bomberRect)
screen.blit(medusaPic,medusaRect)
screen.blit(deadPic,deadRect)

colour=((0,0,0))
#colour=black is needed so the program doesn't crash if a colour isn't picked
#----------------------------------------------------------------------------
t=2
tt=10
t2=10 #----the default thickness/radius so that the program doesn't crash
t3=2
t4=1
t5=20
t6=10
t7=2



mx,my = (0,0)    #start point
num=mx,my     
screenpic=screen.copy() #copys the screen
screencopy=screen.copy()
running =True     
while running:
    click=False      #click is for when the mouse is mb[0]==1

    for e in event.get():    #event loop
        if e.type == QUIT:
            usure=input("Are you sure you are going to exit?")
            usure.lower()
            if usure=="yes":
                print("Thank-you for using Stick Empires PAINT")
                running = False
                
            if usure=="no":
                print("You may continue working.")
                
            #the above input confirms that the user is exiting

            
        if e.type==MOUSEBUTTONDOWN:
            start1=mouse.get_pos()    #gets pos of mouse
            start2=mouse.get_pos()
            x=mx
            y=my
            back=screen.copy()
            screenc=screen.copy()
            startx,starty=mouse.get_pos()
            cmx,cmy=mouse.get_pos()
            c2mx,c2my=mouse.get_pos()    #Gets position of the mouse(x,y)
            c1mx,c1my=mouse.get_pos()
            screencopy=screen.copy()

            if e.button==1:
                start=e.pos
                bmx,bmy=e.pos
                click=True   #click is True only when mb[0]==1
            if e.button ==4: #the scroll up button
                t+=1
                tt+=1
                t2+=1
                t3+=1
                t4+=1
                t5+=1
                t6+=1
                t7+=1
            if e.button==5: #the scroll down button
                t-=1
                tt-=1
                t2-=1
                t3-=1
                t4-=1
                t5-=1
                t6-=1
                t7-=1    #if mb[0]==1 and skipRect.collidepoint(mx,my)
        if t<0:            #ensures that the thickness can never be a negative
            t=0
        if t2<0:
            t2=0
        if t3<0:
            t3=0
        if t4<0:
            t4=0
        if t5<0:
            t5=0
        if t6<0 or t6==0:
            t6=1
        if tt<0:
            tt=0
        if t7<0:
            t7=0
        if t7<4 or t7==4:
            t7=2

        if e.type==MOUSEBUTTONUP:  #event type
            screenc=screen.copy()
            points.append((mx,my))   #mx, my are added to the list

            #This is undo/redo
            if canvasRect.collidepoint(mx,my) and mb[0]==1:
                change = screen.copy() #whenever the user clicks mouse button 1
                undo.append(change)    # it takes a pic of it and adds to undo list
            if undoRect.collidepoint(mx,my) and mb[0]==1: #when user clicks on cavas
                if len(undo) >1 :   #and the length of list undo is more than one
                    tool="undo"     
                    redo.append(undo[len(undo)-1])  #redo list adds the image
                    undo.remove(undo[len(undo)-1])  #removes from undo list
                    screen.blit(undo[len(undo)-1],(0,0))  #blits the last pic in list
            if redoRect.collidepoint(mx,my) and mb[0]==1 :
                if len(redo) > 0:   #ensures that the list index is not out of range
                    tool="redo"
                    screen.blit(redo[len(redo)-1],(0,0)) #blit the last pic on list
                    undo.append(redo[len(redo)-1]) # adds it to undo list 
                    redo.remove(redo[len(redo)-1]) # and removes from redo list


            #all the above if statments needed for allowing the user
            #to change the thickness
            
    mb = mouse.get_pressed()     #defines the mouse being pressed
    omx,omy=mx,my                #defines the mouse position
    o2mx,o2my=mx,my
    olldmx,olldmy=mx,my
    
    oldmx,oldmy=mx,my
    oldmb=mb
    mx,my = mouse.get_pos()
    mx1,my1 = mouse.get_pos()#   <------Many new mx,my's 
    a1mx,a1my = mouse.get_pos()         #for not mixing up the tools
    mb=mouse.get_pressed()

    screen.set_clip(None)
    posRect=Rect(173,0,96,40)          #mx,my coordinate view box
    draw.rect(screen,(50,100,255),posRect) # draws the light blue rectangle
    if canvasRect.collidepoint(mx,my):
        #screen.set_clip(None)
        txtPos=arialFont2.render(str(mx-169)+","+str(my-146),True,(0,0,0))
        screen.blit(txtPos,posRect)
        #screen.set_clip(canvasRect)
    
    starlist=[(mx,my-40),(mx+28,my+35),(mx-40,my-10),(mx+40,my-10),(mx-28,my+35)]
    #list for star points

    if click and paintpickerRect.collidepoint(mx,my):
        if mb[0]==1:
            colour=screen.get_at((mx,my))# gets the colour at the the mouse's
            draw.rect(screen,colour,(173,40,96,40) )
    screen.set_clip(canvasRect)         # position and only allows the user
    #screen.set_clip(None)              # to paint or draw in the canvas  
    
#_______________________________________________________________________________________________
        #sets tools to designated areas
    
    if pencilRect.collidepoint(mx,my)and click:# collidepoint is when the  
        tool="pencil"                           # mouse's point is in the rectangle
        
    if eraserRect.collidepoint(mx,my)and click:
        draw.rect(screen,(255,0,0),eraserRect,2)
        tool="eraser"
    if lineRect.collidepoint(mx,my)and click:
        tool="line"
    if brushRect.collidepoint(mx,my)and click:
        tool="brush"
    if bucketfillRect.collidepoint(mx,my)and click:
        screen.fill(colour)#fills whole screen with user's desired colour
    if sprayRect.collidepoint(mx,my)and click:
        tool="spraypaint"
    if circleRect.collidepoint(mx,my)and click:
        tool="circle"
    if rectangleRect.collidepoint(mx,my)and click:
        tool="rectangle"        
    if ellipseRect.collidepoint(mx,my) and click:
        tool="ellipse"
    if polyRect.collidepoint(mx,my) and click:
        tool="polygon"
    if rectfillRect.collidepoint(mx,my) and click:
        tool="filledrect"
    if starRect.collidepoint(mx,my) and click:
        tool="star"


    if playingRect.collidepoint(mx,my) and click and playing==True:
        mixer.music.pause()     #pauses the music
        screen.set_clip(None)   #unsets the clip
        screen.blit(playPic,playingRect)   #change the image
        playing=False   #flag confirming that playing is equal to false
        screen.set_clip(canvasRect)  #set the clip to canvas
        
    elif playingRect.collidepoint(mx,my) and click and playing==False:
        mixer.music.unpause()   #unpauses the music
        screen.set_clip(None)   #unset clip
        screen.blit(pausePic,playingRect) #change the image
        playing=True
        screen.set_clip(canvasRect) #set the clip to canvas
######


        
    if saveRect.collidepoint(mx,my) and click:
        screen.set_clip(None)   #must turn the clip off so user can input text
        filename= getName()     # calls the function getName()
        if ".png" or ".jpg" or ".bmp" not in filename:
            filename+=".png"
        image.save(screen.subsurface(canvasRect),filename) #saves image  
        screen.set_clip(canvasRect)   # turns on the clip again

#----------------------------------------------------------------------------
                    
        #allows user to load a chosen picture to the canvas
    if loadRect.collidepoint(mx,my) and click:
        screen.set_clip(None)  #must turn the clip off so user can input text
        loadfile= getName()     # calls the function
        pic=image.load(loadfile)  
        screen.set_clip(canvasRect)   #turns the clip on again
        screen.blit(pic,canvasRect)   #load the image onto the canvas
        
        
    if restartRect.collidepoint(mx,my) and click:
        screen.fill((255,255,255))       #fills the entire screen with white
        
    if eyedropperRect.collidepoint(mx,my) and click:
        tool="eyedropper"
        
    if questionmarkRect.collidepoint(mx,my) and click:
        startfile("help.txt")   #opens the help text file

    if textRect.collidepoint(mx,my) and click:
        tool="text"

    if fontRect.collidepoint(mx,my) and click:
        #this recieves input from the user on the python shell
        screen.set_clip(None)
        fontsize=int(getName())  #converts string to integer
        screen.set_clip(canvasRect)
        
    if copyRect.collidepoint(mx,my) and click:
        tool="copy"

    if pasteRect.collidepoint(mx,my) and click:
        tool="paste"

#----------------------------------------------------------------------------
        #stamps------------if mouse coordinates are in the rect and they click
    if minerRect.collidepoint(mx,my) and click:
        tool="miner"   #sets tool
    if swordRect.collidepoint(mx,my) and click:
        tool="swordwrath"
    if archerRect.collidepoint(mx,my) and click:
        tool="archer"
    if mericRect.collidepoint(mx,my) and click:
        tool="meric"
    if magiRect.collidepoint(mx,my) and click:
        tool="magikill"
    if speartonRect.collidepoint(mx,my) and click:
        tool="spearton"
    if ninjaRect.collidepoint(mx,my) and click:
        tool="shadowrath"
    if flyarcherRect.collidepoint(mx,my) and click:
        tool="allbowtross"
    if engiantRect.collidepoint(mx,my) and click:
        tool="enslavedgiant"
    if bomberRect.collidepoint(mx,my) and click:
        tool="bomber"
    if medusaRect.collidepoint(mx,my) and click:
        tool="medusa"
    if deadRect.collidepoint(mx,my) and click:
        tool="dead"

        
#----------------------------------------------------------------------------
        #TOOLS
    if mb[0]==1 and canvasRect.collidepoint(mx,my):
        if tool=="pencil" and mb[0]==1:
            draw.line(screen,colour,(mx,my),(x0,y0),1)           
            # Draws line from old mx,my to new mx,my
            
        if tool=="eraser" and mb[0]==1:
            draw.circle(screen,white,(mx,my),tt)
            dx1=mx-ox1  #get the x value
            dy1=my-oy1  #get the y value
            dist1= int((dx1**2 + dy1**2)**0.5)#distance formula to find all points
            for i in range(dist1): # between new circle and old circle
                fx1= int(ox1 + i/dist1*dx1)#draw circle between 2 points/circles
                fy1= int(oy1 + i/dist1*dy1)
                draw.circle(screen,white,(fx1,fy1),tt)   

        if tool=="line" and mb[0]==1:
            screen.blit(screencopy,(0,0))
            draw.line(screen,colour,start,(mx1,my1),t3)

        if tool=="brush" and mb[0]==1:
            draw.circle(screen,colour,(mx,my),t2)
            dx=mx-ox
            dy=my-oy
            dist= int((dx**2 + dy**2)**0.5)#same code as eraser just different colour
            for i in range(dist):
                fx= int(ox + i/dist*dx)
                fy= int(oy + i/dist*dy)
                draw.circle(screen,colour,(fx,fy),t2)
                    
    ##randomized dots of one colour are displayed within a circle
        if tool=="spraypaint" and mb[0]==1:
            for i in range(5):
                sprayposx=randint(mx-20,mx+20)#Randomizes the circles
                sprayposy=randint(my-20,my+20)
                distance=((((mx-sprayposx)**2)+((my-sprayposy)**2))**0.5)
                #above is the distance formula to find every point
                if distance <=10:#sets the distance to be less or equal to 10
                    draw.circle(screen,colour,(sprayposx,sprayposy),(t4))
                    
        if tool=="circle" and mb[0]==1:
            screen.blit(screencopy,(0,0))#takes a copy of the screen
            elli=Rect(cmx,cmy,mx-cmx,my-cmy)#x,y,height and width
            elli.normalize()#ensures that there are no negatives
            if elli.width>4 and elli.height>4:#the height and width must be at least 4 pixels long 
                draw.ellipse(screen,colour,elli,t7) #draw ellipse
            
        if tool=="rectangle" and mb[0]==1:
            screen.blit(screencopy,(0,0)) #blit image so that user can drag around the box from one corner
            draw.rect(screen,colour,(x,y,mx-x,my-y),t6)

        if tool=="ellipse" and mb[0]==1 :
            screen.blit(screencopy,(0,0))
            elli1=Rect(cmx,cmy,mx-cmx,my-cmy)
            elli1.normalize()#-This will flip the width or height
                             #of a rectangle if it has a negative size
            draw.ellipse(screen,colour,elli1) #no thickness for filled ellipse

        if tool=="polygon" and mb[0]==1:
            screen.blit(screenc,(0,0))
            if len(points) > 0:#ensures there's a point to connect to
                draw.line(screen,colour,points[-1],(mx,my),t4)
            #^draws a line from the last point in the list to new point

        if tool=="filledrect" and mb[0]==1:
            screen.blit(screencopy,(0,0))#displays the screen copy
            draw.rect(screen,colour,(cmx,cmy,mx-cmx,my-cmy))
            # ^ draws a rect from the mx,my height and width

        if tool=="star" and mb[0]==1:
            screen.blit(screencopy,(0,0))
            draw.polygon(screen,colour,starlist)#draw the star following star list


#----------------------------------------------------------------------------
        #stamps---takes a picture and allows user to continue
        #to press mouse and make images
        if tool=="miner" and mb[0]==1:
            screen.blit(screencopy,(0,0))    #copys screen
            screen.blit(minerPic,(mx-10,my-10)) #blits image with the mouse centre on pic
        
        if tool=="swordwrath" and mb[0]==1:
            screen.blit(screencopy,(0,0))
            screen.blit(swordPic,(mx-10,my-10))

        if tool=="archer" and mb[0]==1:
            screen.blit(screencopy,(0,0))
            screen.blit(archerPic,(mx-10,my-10))
            
        if tool=="meric"and mb[0]==1:
            screen.blit(screencopy,(0,0))
            screen.blit(mericPic,(mx-10,my-10))
            
        if tool=="magikill" and mb[0]==1:
            screen.blit(screencopy,(0,0))
            screen.blit(magiPic,(mx-10,my-10))
            
        if tool=="spearton" and mb[0]==1:
            screen.blit(screencopy,(0,0))
            screen.blit(speartonPic,(mx-10,my-10))

        if tool=="shadowrath" and mb[0]==1:
            screen.blit(screencopy,(0,0))
            screen.blit(ninjaPic,(mx-10,my-10))

        if tool=="allbowtross" and mb[0]==1:
            screen.blit(screencopy,(0,0))
            screen.blit(flyarcherPic,(mx-10,my-10))

        if tool=="enslavedgiant" and mb[0]==1:
            screen.blit(screencopy,(0,0))
            screen.blit(engiantPic,(mx-10,my-10))

        if tool=="bomber" and mb[0]==1:
            screen.blit(screencopy,(0,0))
            screen.blit(bomberPic,(mx-10,my-10))

        if tool=="medusa" and mb[0]==1:
            screen.blit(screencopy,(0,0))
            screen.blit(medusaPic,(mx-10,my-10))

        if tool=="dead" and mb[0]==1:
            screen.blit(screencopy,(0,0))
            screen.blit(deadPic,(mx-10,my-10))                
#--------------------------------------------------------------------------
        # eyedropper tool
        if tool=="eyedropper" and mb[0]==1:
            colour=screen.get_at((mx,my)) #gets colour at mouse position

        if tool=="text" and mb[0]==1:
            ans=""   # the text that theh user types
            typing = True #flag stating that typing is on
            while typing:
                for e in event.get():   #evt loop
                    if e.type == QUIT:
                        event.post(e)   # puts QUIT back in event list so main quits
                        #return ""
                    if e.type == KEYDOWN:
                        if e.key == K_BACKSPACE:    # remove last letter
                            if len(ans)>0:
                                ans = ans[:-1]
                        elif e.key == K_KP_ENTER or e.key == K_RETURN : 
                            typing = False    #turns off typing
                        elif e.key < 256:
                            ans += e.unicode       # add character to ans

                    

                        #print("texttool","------",ans)
                display.flip()
        
                screen.blit(back,(0,0)) 
                #return ans        
                textbox=(x,y,mx-x,my-y) #where the user enters text
                arialFont = font.SysFont("Times New Roman", fontsize) #type of font
                txtPic2 = arialFont.render(ans, True, (0,0,0)) #render text
                screen.blit(txtPic2,(textbox))#load onto screen
            if tool!="text":   #sets the tool to pencil if tool is no longer text
                tool="pencil"
    

        if tool=="copy":
            screen.blit(screencopy,(0,0))
            cx=(mx-bmx)   #the x value
            cy=(my-bmy)   # the y value
            draw.rect(screen,(100,100,100),(bmx,bmy,cx,cy),1) #draws a grey rectangle to show what the user is copying
            copyrectangle=Rect(bmx,bmy,cx,cy)  #size of the rectangle/the coordinates
            copyrectangle.normalize()#ensures there are no negative values
        
            copypic=screen.subsurface(copyrectangle).copy() #copys the image in the rectangle


        if tool=="paste":
            screen.blit(screencopy,(0,0)) #blit the original copy on the screen
            
            screen.set_clip(canvasRect) #set the clip on canvas
            screen.blit(copypic,(mx+(cx/2),my+(cy/2))) #centres the copied image
            screen.set_clip(canvasRect)#set the clip to canvas

            #FIX screen.blit(undo[-1],(0,0))

    nmx,nmy=mx,my
    ox,oy=mx,my        #new mx,my's
    ox1,oy1=mx,my
    x0=mx
    y0=my
    
    
    display.flip() 
quit()



