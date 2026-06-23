
#this is a code editor for the engine and I would eventually like to make it into my main


import pygame as pg
from pygame._sdl2 import Window
import os
import tkinter as tk
import sys
from CybrocksLibrary import *



def main():
    
    # -------== setting up ==--------------------------------------------------------------------------------------------------------------
    
    #the usual stuff
    pg.init()
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    
    window = pg.display.set_mode((1200,750), pg.NOFRAME)
    sdl_window = Window.from_display_module()
    
    font = pg.font.SysFont('Consolas', 20)
    sideFont = pg.font.SysFont('bold Consolas', 20)
    

    code = []
    line = ''
    lookingatline = 1


    # -------== colors ==--------------------------------------------------------------------------------------------------------------

    pallet = pg.image.load("resources/textures/p.png") #thanks to the people on stack overflow
    image_rect = pallet.get_rect()
    
    window.fill((0,0,0))
    window.blit(pallet, image_rect)
    screensurf = pg.display.get_surface() #gets colors from picture for more customization
    
    p = 1

    main = screensurf.get_at((0,p))
    bg = screensurf.get_at((1,p))
    margin = screensurf.get_at((3,p))
    textHighlight = screensurf.get_at((4,p))
    text1 = screensurf.get_at((2,p))
    titleBar = screensurf.get_at((5,p))
    

    closeB = Button("resources/textures/closeB.png", (1175,5), 1, 1)
    minB = Button("resources/textures/minB.png", (1145,5), 1, 1)


    running = True
    while running:

        # -------== key buttons ==--------------------------------------------------------------------------------------------------------------
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if pg.key.name(event.key) == "space":
                    line = line + ' '
                elif pg.key.name(event.key) == "tab":
                    line = line + '    '
                elif pg.key.name(event.key) == "backspace":
                    if line == '':
                        if lookingatline != 1:
                            lookingatline -= 1
                            line = code.pop()
                    else:
                        line = line[:-1]
                elif pg.key.name(event.key) == "left shift": #all these blank passes to prevent you doing = hleft shiftello
                    pass
                elif pg.key.name(event.key) == "right shift":
                    pass
                elif pg.key.name(event.key) == "left ctrl":
                    pass
                elif pg.key.name(event.key) == "right ctrl":
                    pass
                elif pg.key.name(event.key) == "left alt":
                    pass
                elif pg.key.name(event.key) == "right alt":
                    pass
                elif pg.key.name(event.key) == "f1": #temporary save
                    save(code + [line])
                elif pg.key.name(event.key) == "f2":
                    pass
                elif pg.key.name(event.key) == "f3":
                    pass
                elif pg.key.name(event.key) == "f4":
                    pass
                elif pg.key.name(event.key) == "f5":
                    pass
                elif pg.key.name(event.key) == "f6":
                    pass
                elif pg.key.name(event.key) == "f7":
                    pass
                elif pg.key.name(event.key) == "f8":
                    pass
                elif pg.key.name(event.key) == "f9":
                    pass
                elif pg.key.name(event.key) == "f10":
                    pass
                elif pg.key.name(event.key) == "f11":
                    pass
                elif pg.key.name(event.key) == "f12":
                    pass
                elif pg.key.name(event.key) == "numlock":
                    pass
                elif pg.key.name(event.key) == "escape": #quit
                    #running = False
                    pass
                elif pg.key.name(event.key) == "return": #enter
                    code.append(line)
                    line = ""
                    lookingatline += 1
                else:
                    line += pg.key.name(event.key)
                
                print(line)
                print(pg.key.name(event.key))
                


        # -------== buttons ==--------------------------------------------------------------------------------------------------------------
        if closeB.is_pressed():
            running = False

        if minB.is_pressed():
            pg.display.iconify()




        # -------== drawing ==--------------------------------------------------------------------------------------------------------------
        window.fill(bg)
        pg.draw.rect(window, titleBar, [0, 0, 1200, 30])
        pg.draw.rect(window, main, [0, 30, 1200, 60])
        pg.draw.rect(window, margin, [0, 90, 45, 750])

        closeB.draw(window)  
        minB.draw(window)      

        for i in range(27):
            numbers = sideFont.render(str(i), False, textHighlight)
            window.blit(numbers, (5, (i*25+100)))
        
        y = 95
        for line_text in code:
            renderedlines = font.render(line_text, False, text1)
            window.blit(renderedlines, (50, y))
            y += 25
            
        text = font.render(line, False, textHighlight)
        window.blit(text, (50, (lookingatline*25+70)))
        
        pg.display.flip()
        



def save(code):
    root = tk.Tk()
    root.title("Name and file type. (example = file.txt)")

    name = ""

    tk.Label(root, text="Name and file type. (example = file.txt)").grid(row=0, column=0)

    nameEntry = tk.Entry(root)
    nameEntry.grid(row=1, column=0)

    def submit():
        nonlocal name
        name = nameEntry.get()
        root.destroy()

    submitButton = tk.Button(root, text="OK", command=submit)
    submitButton.grid(row=2, column=0, columnspan=2)

    root.mainloop()
    with open(name, "w") as f:
        for line in code:
            f.write(line + "\n")
        
        





if __name__ == "__main__":
    
    main()
    


pg.quit()