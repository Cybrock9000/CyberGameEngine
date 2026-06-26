
#this is a code editor for the engine and I would eventually like to make it into my main


import pygame as pg
from pygame.locals import *
from pygame._sdl2 import Window
import os
import tkinter as tk
from tkinter import filedialog
import sys
from CybrocksLibrary import *
import json



def main():
    
    # -------== setting up ==--------------------------------------------------------------------------------------------------------------
    
    #the usual stuff
    pg.init()
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    
    window = pg.display.set_mode((1600,930), pg.NOFRAME)
    sdl_window = Window.from_display_module()
    
    font = pg.font.SysFont('Consolas', 20)
    sideFont = pg.font.SysFont('bold Consolas', 20)
    
    code = []
    line = ''


    '''loaded_lines = load().splitlines()

    if loaded_lines:
        code = loaded_lines[:-1]
        line = loaded_lines[-1]'''
    

    lookingatline = len(code) + 1
    uppercase = False
    scrolly = 0

    # -------== colors ==--------------------------------------------------------------------------------------------------------------

    pallet = pg.image.load((os.getcwd() + "/IDEresources/textures/p.png")) #thanks to the people on stack overflow for loading colors from a pic
    image_rect = pallet.get_rect()
    
    window.fill((0,0,0))
    window.blit(pallet, image_rect)
    screensurf = pg.display.get_surface() #gets colors from picture for more customization
    
    p = 0 #pallet, which is y so there could be multiple in one pic

    main = screensurf.get_at((0,p))
    bg = screensurf.get_at((1,p))
    margin = screensurf.get_at((3,p))
    textHighlight = screensurf.get_at((4,p))
    text1 = screensurf.get_at((2,p))
    titleBar = screensurf.get_at((5,p))
    
    with open(os.getcwd() + "/IDEresources/languages/python.json", "r") as py: #load programing languages
        specialwords = json.load(py)
        
        for keyword, data in specialwords.items():
            palette_index = data[0]
            data[0] = screensurf.get_at((palette_index, p))
    
    def drawcolorwords(surface, font, text, x, y):
        words = text.split(" ")
        cx = x

        for word in words: #checks to see if its in the list and colors it here
            color = text1 #normal text

            for keyword, data in specialwords.items(): 
                kcolor = data[0]
                mode = data[1]

                if mode == 0:
                    if word == keyword: #color only if its exact like as
                        color = kcolor
                        break

                elif mode == 1:
                    if word.startswith(keyword): #color the full thing like print() (or even printasdjfhlaksjdhf wich i will have to fix soon)
                        color = kcolor
                        break

            rendered = font.render(word, True, color)
            surface.blit(rendered, (cx, y))

            cx += rendered.get_width()

            space = font.render(" ", True, text1)
            surface.blit(space, (cx, y))
            cx += space.get_width()

    closeB = Button("IDEresources/textures/closeB.png", (1575,5), 1, 1)
    minB = Button("IDEresources/textures/minB.png", (1545,5), 1, 1)


    running = True
    while running:

        # -------== key buttons ==--------------------------------------------------------------------------------------------------------------
        for event in pg.event.get():
            
            if event.type == MOUSEWHEEL:
                        scrolly -= event.y
            if scrolly <= 0:
                        scrolly = 0
                        
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
                elif pg.key.name(event.key) == "caps lock":
                    if uppercase == True:
                        uppercase = False
                    else:
                        uppercase = True
                elif pg.key.name(event.key) == "f1": #(maybe) temporary save
                    save(code + [line])
                elif pg.key.name(event.key) == "f2":
                    loaded = load()

                    if loaded:
                        lines = loaded.splitlines()

                        if lines:
                            code = lines[:-1]
                            line = lines[-1]
                        else:
                            code = []
                            line = ""

                        lookingatline = len(code) + 1
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
                    if uppercase:
                        line += pg.key.name(event.key).upper()
                    else:
                        line += event.unicode
                        
                
            print(lookingatline)
            #print(pg.key.name(event.key))



        # -------== buttons ==--------------------------------------------------------------------------------------------------------------
        if closeB.is_pressed():
            running = False

        if minB.is_pressed():
            pg.display.iconify()




        # -------== drawing ==--------------------------------------------------------------------------------------------------------------
        window.fill(bg)
        pg.draw.rect(window, margin, [0, 90, 45, 930])

              

        for i in range(33):
            numbers = sideFont.render(str(1+i+scrolly), False, textHighlight)
            window.blit(numbers, (5, (i*25+100)))
        
        y = 95
        for line_text in code:
            drawcolorwords(window, font, line_text, 50, y-(scrolly*25))
            y += 25
            
        line2 = str(line) + '|'
        drawcolorwords(window, font, line2, 50, (lookingatline*25+70)-(scrolly*25))
        
        pg.draw.rect(window, titleBar, [0, 0, 1600, 30])
        pg.draw.rect(window, main, [0, 30, 1600, 60])
        
        closeB.draw(window)  
        minB.draw(window)
        
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
        


def load():
    root = tk.Tk()
    root.withdraw()

    filename = filedialog.askopenfilename(
        title="Open File",
        filetypes=[("All Files", "*.*")]
    )

    root.destroy()

    if not filename:
        return None

    with open(filename, "r") as f:
        return f.read()




if __name__ == "__main__":
    
    main()
    


pg.quit()