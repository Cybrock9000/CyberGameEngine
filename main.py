
#im autualy going to try to comment as much as posible for this project unlike my other projects 




# -------== imports ==-------
import pygame as pg
import time
from ENGsettings import *
from CybrocksLibrary import Button
import shutil
import os
import tkinter as tk
import webbrowser
import re
import subprocess


# -------== colors ==--------------------------------------------------------------------------------------------------------------

SPECIALDARKGREY = (48, 48, 75)
ANEVENDARKERSPECIALDARKGREY = (26, 26, 43)



def main():
    
    # -------== setting up ==--------------------------------------------------------------------------------------------------------------
    
    pg.init()

    window = pg.display.set_mode(RES)
    pg.display.set_caption('Enter a name in the box :)')

    icon = pg.image.load('icon.ico').convert_alpha()
    pg.display.set_icon(icon)
    

    # -------== audio ==--------------------------------------------------------------------------------------------------------------
    
    
    
    
    # -------== creation of project or opening it ==--------------------------------------------------------------------------------------------------------------
    
    root = tk.Tk()
    root.title("Enter Name of Project. A New Name Will Create a New Project. A preexisting Name Will Just Open it.")

    name = ""

    tk.Label(root, text="Enter Name of Project. A New Name Will Create a New Project. A preexisting Name Will Just Open it.").grid(row=0, column=0)

    nameEntry = tk.Entry(root)
    nameEntry.grid(row=1, column=0)

    def submit():
        nonlocal name
        name = nameEntry.get()
        root.destroy()

    submitButton = tk.Button(root, text="OK", command=submit)
    submitButton.grid(row=2, column=0, columnspan=2)

    root.mainloop()

    
    s = 'template'
    d = name
    if not os.path.exists(d):
        shutil.copytree(s, d)
    else:
        pass
    

    fileS = f"{name}/settings.py" #change the name in the settings.py of the project

    with open(fileS, "r") as file:
        content = file.read()


    content = re.sub(r"^NAME\s*=.*$",f"NAME = '{name}'",content,flags=re.MULTILINE)

    with open(fileS, "w") as file:
        file.write(content)
    

    # -------== init other stuff ==--------------------------------------------------------------------------------------------------------------
    
    clock = pg.time.Clock()
    
    
    # -------== vars ==--------------------------------------------------------------------------------------------------------------
    
    buttonDelay = False #single click instead of repeating output
    
    mapx = 0
    mapy = 0
    

    # -------== buttons ==--------------------------------------------------------------------------------------------------------------
    
    creditsB = Button("resources/textures/CButton.png", (1000, 700), 3, 3)
    helpB = Button("resources/textures/docsButton.png", (1000, 620), 3, 3)
    CompileB = Button("resources/textures/CompButton.png", (1000, 480), 3, 3)
    testB = Button("resources/textures/tButton.png", (1000, 400), 3, 3)
    PlayerSB = Button("resources/textures/PSButton.png", (1000, 320), 3, 3)
    
    upB = Button("resources/textures/up.png", (160, 425), 3, 3)
    downB = Button("resources/textures/down.png", (160, 485), 3, 3)
    leftB = Button("resources/textures/left.png", (100, 485), 3, 3)
    rightB = Button("resources/textures/right.png", (220, 485), 3, 3)


    # -------== main loop ==--------------------------------------------------------------------------------------------------------------
    
    running = True
    while running:
        
        # -------== controls and keys and buttons ==--------------------------------------------------------------------------------------------------------------
        
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE
            ):
                running = False
        
        if creditsB.is_pressed() and buttonDelay == False:
            
            webbrowser.open('https://cybrock9000.github.io/CyberWolfGames')
            buttonDelay = True
        elif creditsB.is_pressed() and buttonDelay == True:
            pass
        else: 
             buttonDelay = False
        
        if helpB.is_pressed() and buttonDelay == False:
            webbrowser.open('https://cybrock9000.github.io/CyberWolfGames/engineDocs.html')
            buttonDelay = True
        elif helpB.is_pressed() and buttonDelay == True:
            pass
        else: 
             buttonDelay = False
             
        if testB.is_pressed() and buttonDelay == False:
            subprocess.run(["python", f"{name}/main.py"])
            buttonDelay = True
        elif testB.is_pressed() and buttonDelay == True:
            pass
        else: 
             buttonDelay = False
             
        if upB.is_pressed():
            mapy += 0.01
        if downB.is_pressed():
            mapy -= 0.01
        if leftB.is_pressed():
            mapx -= 0.01
        if rightB.is_pressed():
            mapx += 0.01
        

        # -------== drawing stuff ==--------------------------------------------------------------------------------------------------------------
        
        window.fill('black')
        pg.draw.rect(window, SPECIALDARKGREY, [0, 400, 400, 400], 0)
        pg.draw.rect(window, SPECIALDARKGREY, [400, 0, 1200, 800], 0)
        pg.draw.rect(window, ANEVENDARKERSPECIALDARKGREY, [390, 0, 10, 800], 0)
        pg.draw.rect(window, ANEVENDARKERSPECIALDARKGREY, [670, 0, 10, 800], 0)
        pg.draw.rect(window, ANEVENDARKERSPECIALDARKGREY, [390, 100, 560, 10], 0)
        pg.draw.rect(window, ANEVENDARKERSPECIALDARKGREY, [950, 0, 10, 800], 0)
        pg.draw.rect(window, ANEVENDARKERSPECIALDARKGREY, [0, 550, 400, 10], 0)
        pg.draw.rect(window, ANEVENDARKERSPECIALDARKGREY, [950, 570, 400, 10], 0)
        
        creditsB.draw(window)
        helpB.draw(window)
        CompileB.draw(window)
        testB.draw(window)
        PlayerSB.draw(window)

        upB.draw(window)
        downB.draw(window)
        leftB.draw(window)
        rightB.draw(window)
        

        # -------== update screen ==--------------------------------------------------------------------------------------------------------------
        
        pg.display.set_caption(f'Engine   -={name}=-    -= Version {VERSION} =-      -= FPS: {clock.get_fps():.1f} =- ')

        pg.display.flip()
        clock.tick(FPS)

    pg.quit()


if __name__ == "__main__":
    main()