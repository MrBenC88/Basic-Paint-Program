#paint_project_plan.py

# PAINT PROJECT

tool="pencil"#-> have variables for each tool

1. load pictures
2. draw screen(photoshop)

pencilRect=Rect(10,100,30,30)
while running:
    event loop
    #  <----------------screen.blit(pencilPic,pencilRect)
    mx,my=mouse.get_pos()
    mb=mouse.get_pressed()
    #select tools

    if pencilRect.collidepoint((mx,my)) and mb[0]==1 : #  <click on pencil tool>
        tool="pencil"
    if < click on eraser tool> :
        tool="eraser"


    #use selected tool
    if <click on the canvas>:
        if tool=="pencil":
            draw.line(screen,colour,(oldmx,oldmy),(mx,my))
        if tool == "eraser":
            <eraser stuff>
            
