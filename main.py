
#im autualy going to try to comment as much as posible for this project unlike my other projects 




# -------== imports ==-------

import pygame as pg
from pygame.locals import *
import time
from ENGsettings import *
from CybrocksLibrary import *
from ENGLIB import *
import shutil
import os
from tkinter import messagebox
import tkinter as tk
import webbrowser
import re
import subprocess
import importlib.util


# -------== colors ==--------------------------------------------------------------------------------------------------------------

SPECIALDARKGREY = (48, 48, 75)
ANEVENDARKERSPECIALDARKGREY = (26, 26, 43)



def main():
    
    # -------== setting up ==--------------------------------------------------------------------------------------------------------------
    
    pg.init()
    
    RES = (1200, 800) # res as moved here for dynamic screen scaleing
    window = pg.display.set_mode(RES)
    pg.display.set_caption('Enter a name in the box :)')

    icon = pg.image.load('icon.ico').convert_alpha()
    pg.display.set_icon(icon)
    

    # -------== audio ==--------------------------------------------------------------------------------------------------------------
    
    click = pg.mixer.Sound('resources\sounds\click.wav')
    
    
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
    

    updatename(name)
    

    # -------== init other stuff ==--------------------------------------------------------------------------------------------------------------
    
    clock = pg.time.Clock()
    pg.mouse.set_visible(False)
    
    
    # -------== vars ==--------------------------------------------------------------------------------------------------------------
    
    #button stuff

    buttonDelay = False #single click instead of repeating output, also have to have multiple to prevent problems I totaly did not spend hours trying to figure out
    buttonDelay2 = False
    buttonDelay3 = False
    buttonDelay4 = False
    buttonDelay5 = False
    buttonDelay6 = False
    buttonDelay7 = False
    buttonDelay8 = False
    buttonDelay9 = False
    
    #grid and editor

    mapx = 0
    mapy = 300
    scale = 0.25
    
    cmapx = 0
    cmapy = 0
    
    pointx = 0
    pointy = 0
    pointx2 = 0
    pointy2 = 0
    point = 0
    
    gspeed = 0.5
    
    #pannels

    screenA = False
    screenS = False

    #other

    scrolly = 0
    
    # -------== images ==--------------------------------------------------------------------------------------------------------------
    
    cursor = BetterImage("resources/textures/mapC.png", (0, 0), 5, 5)
    Gcursor = BetterImage("resources/textures/C.png", (0, 0), 3, 3)

    # -------== buttons ==--------------------------------------------------------------------------------------------------------------
    
    creditsB = Button("resources/textures/CButton.png", (1000, 700), 3, 3)
    helpB = Button("resources/textures/docsButton.png", (1000, 620), 3, 3)
    CompileB = Button("resources/textures/CompButton.png", (1000, 480), 3, 3)
    testB = Button("resources/textures/tButton.png", (1000, 400), 3, 3)
    PlayerSB = Button("resources/textures/PSButton.png", (1000, 320), 3, 3)
    projectFB = Button("resources/textures/PFButton.png", (1000, 240), 3, 3)
    audioB = Button("resources/textures/AButton.png", (1000, 160), 3, 3)
    settingsB = Button("resources/textures/SButton.png", (1000, 90), 3, 3)
    EaudioB = Button("resources/textures/EAButton.png", (1210, 10), 3, 3)
    
    
    if EngineAudio == True:
        EaudioB.new_image("resources/textures/EATButton.png", (1210, 10), 3, 3)
    else:
        EaudioB.new_image("resources/textures/EAButton.png", (1210, 10), 3, 3)
        
    upB = Button("resources/textures/up.png", (160, 425), 3, 3)
    downB = Button("resources/textures/down.png", (160, 485), 3, 3)
    leftB = Button("resources/textures/left.png", (100, 485), 3, 3)
    rightB = Button("resources/textures/right.png", (220, 485), 3, 3)
    GspeedB = Button("resources/textures/speedpoint5.png", (25, 460), 3, 3)
    zoomB = Button("resources/textures/setzoomto1.png", (320, 460), 3, 3)
    
    zplusB = Button("resources/textures/plus.png", (100, 425), 3, 3) # the z is zoom
    zminusB = Button("resources/textures/minus.png", (220, 425), 3, 3)
    wplusB = Button("resources/textures/plus.png", (100, 700), 3, 3) # the w is wall
    wminusB = Button("resources/textures/minus.png", (220, 700), 3, 3)
    
    
    
    wupB = Button("resources/textures/up.png", (160, 575), 3, 3)
    wdownB = Button("resources/textures/down.png", (160, 635), 3, 3)
    wleftB = Button("resources/textures/left.png", (100, 635), 3, 3)
    wrightB = Button("resources/textures/right.png", (220, 635), 3, 3)


    # -------== main loop ==--------------------------------------------------------------------------------------------------------------
    
    running = True
    while running:
        
        # -------== controls and keys and buttons ==--------------------------------------------------------------------------------------------------------------
        
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE
            ):
                running = False
                
            if event.type == MOUSEWHEEL:
                scrolly += event.y
                print(scrolly)
        


        if creditsB.is_pressed() and buttonDelay == False:
            
            clickA(click)
            webbrowser.open('https://cybrock9000.github.io/CyberWolfGames')
            buttonDelay = True
            
        elif creditsB.is_pressed() and buttonDelay == True:
            pass
        else: 
             buttonDelay = False
        


        if helpB.is_pressed() and buttonDelay2 == False:
            
            clickA(click)
            webbrowser.open('https://cybrock9000.github.io/CyberWolfGames/engineDocs.html')
            buttonDelay2 = True
            
        elif helpB.is_pressed() and buttonDelay2 == True:
            pass
        else: 
             buttonDelay2 = False
             


        if testB.is_pressed() and buttonDelay3 == False:
            
            clickA(click)
            subprocess.run(["python", f"{name}/main.py"])
            buttonDelay3 = True
            
        elif testB.is_pressed() and buttonDelay3 == True:
            pass
        else: 
             buttonDelay3 = False
             


        if audioB.is_pressed() and buttonDelay4 == False:
            clickA(click)
            
            if screenA == False and not screenS == True:
                
                RES = (1400, 800)
                screenA = True
                
            elif not screenS == True:
                
                RES = (1200, 800)
                screenA = False
                
            window = pg.display.set_mode(RES)
            buttonDelay4 = True
            
        elif audioB.is_pressed() and buttonDelay4 == True:
            pass
        else: 
             buttonDelay4 = False
             # I LOVE ULTRAKILL MUSIC, SPECIFICLY ORDER (thanke me later :) )
             


        if settingsB.is_pressed() and buttonDelay5 == False:
            
            clickA(click)
            
            if screenS == False and not screenA == True:
                
                RES = (1400, 800)
                screenS = True
                
            elif not screenA == True:
                
                RES = (1200, 800)
                screenS = False
                
            window = pg.display.set_mode(RES)
            buttonDelay5 = True
            
        elif settingsB.is_pressed() and buttonDelay5 == True:
            pass
        
        else: 
             buttonDelay5 = False
             

        if projectFB.is_pressed() and buttonDelay7 == False:
            
            clickA(click)
            path = os.getcwd()
            subprocess.Popen(f'explorer /commit,"{path}\{name}\"')
            buttonDelay7 = True
            
        elif projectFB.is_pressed() and buttonDelay7 == True:
            pass
        else: 
             buttonDelay7 = False


        if EaudioB.is_pressed() and buttonDelay6 == False:
            
            clickA(click)
            EngineSfile = "ENGsettings.py"
            
            with open(EngineSfile, "r") as file:
                
                content = file.read()
            if EngineAudio == False:
                
                content = re.sub(r"^EngineAudio\s*=.*$","EngineAudio = True",content,flags=re.MULTILINE)
                EaudioB.new_image("resources/textures/EATButton.png", (1210, 10), 3, 3)
                
            else:
                content = re.sub(r"^EngineAudio\s*=.*$","EngineAudio = False",content,flags=re.MULTILINE)
                EaudioB.new_image("resources/textures/EAButton.png", (1210, 10), 3, 3)
            
            with open(EngineSfile, "w") as file:
                
                file.write(content)
            buttonDelay6 = True
            tk.messagebox.showwarning("info", "Restart to take request to effect!")
            
        elif EaudioB.is_pressed() and buttonDelay6 == True:
            pass
        else: 
             
             buttonDelay6 = False
             


        if upB.is_pressed():
            mapy += gspeed
        if downB.is_pressed():
            mapy -= gspeed
        if leftB.is_pressed():
            mapx -= gspeed
        if rightB.is_pressed():
            mapx += gspeed
            
        if zplusB.is_pressed():
            scale += 0.01
        if zminusB.is_pressed():
            scale -= 0.01
            
        if wupB.is_pressed():
            cmapy += 1
        if wdownB.is_pressed():
            cmapy -= 1
        if wleftB.is_pressed():
            cmapx -= 1
        if wrightB.is_pressed():
            cmapx += 1
            
        if GspeedB.is_pressed() and buttonDelay8 == False:
            
            clickA(click)
            
            if gspeed == 0.5:
                gspeed = 1
                GspeedB.new_image("resources/textures/speed1.png", (25, 460), 3, 3)
            elif gspeed == 1:
                gspeed = 2
                GspeedB.new_image("resources/textures/speed2.png", (25, 460), 3, 3)
            elif gspeed == 2:
                gspeed = 5
                GspeedB.new_image("resources/textures/speed5.png", (25, 460), 3, 3)
            elif gspeed == 5:
                gspeed = 10
                GspeedB.new_image("resources/textures/speed10.png", (25, 460), 3, 3)
            elif gspeed == 10:
                gspeed = 0.5
                GspeedB.new_image("resources/textures/speedpoint5.png", (25, 460), 3, 3)
                
            window = pg.display.set_mode(RES)
            buttonDelay8 = True
            
        elif GspeedB.is_pressed() and buttonDelay8 == True:
            pass
        
        else: 
             buttonDelay8 = False
             
        if wplusB.is_pressed() and buttonDelay9 == False:
            
            clickA(click)
            
            if point == 0:
                point = 1
                pointx = cmapx / scale + mapx #this makes clicking with the grid pointer calculate the world pos instead of the grid pos
                pointy = mapy - cmapy / scale - 300
                print((pointx,pointy))
            elif point == 1:
                point = 0
                pointx2 = cmapx / scale + mapx
                pointy2 = mapy - cmapy / scale -300
                print((pointx2,pointy2))
            
            buttonDelay9 = True
            
        elif wplusB.is_pressed() and buttonDelay9 == True:
            pass
        else: 
             buttonDelay9 = False
             
        if zoomB.is_pressed() and buttonDelay10 == False:
            
            clickA(click)
            
            scale = 1
            buttonDelay10 = True
            
        elif zoomB.is_pressed() and buttonDelay10 == True:
            pass
        else: 
             buttonDelay10 = False
        

        # -------== drawing stuff ==--------------------------------------------------------------------------------------------------------------
        

        window.fill('black')
        mapgrid(window, name, mapx, mapy, scale)
        if point == 1:
            pg.draw.line(window,'purple',(((pointx - mapx))* scale, ((-pointy + mapy))* scale -300),(((cmapx - mapx))* scale, ((-cmapy + mapy))* scale -300),2)

        Gcursor.move(((mapx - cmapx), (mapy + -cmapy)))
        Gcursor.draw(window)
        
        pg.draw.rect(window, SPECIALDARKGREY, [0, 400, 400, 400], 0) #background
        pg.draw.rect(window, SPECIALDARKGREY, [400, 0, 1200, 800], 0)
                                                            #[x,y,w,h]
        pg.draw.rect(window, ANEVENDARKERSPECIALDARKGREY, [390, 0, 10, 800], 0) #lines
        pg.draw.rect(window, ANEVENDARKERSPECIALDARKGREY, [670, 0, 10, 800], 0)
        pg.draw.rect(window, ANEVENDARKERSPECIALDARKGREY, [390, 100, 560, 10], 0)
        pg.draw.rect(window, ANEVENDARKERSPECIALDARKGREY, [950, 0, 10, 800], 0)
        pg.draw.rect(window, ANEVENDARKERSPECIALDARKGREY, [0, 550, 400, 10], 0)
        pg.draw.rect(window, ANEVENDARKERSPECIALDARKGREY, [0, 400, 400, 10], 0)
        pg.draw.rect(window, ANEVENDARKERSPECIALDARKGREY, [950, 570, 600, 10], 0)
        pg.draw.rect(window, ANEVENDARKERSPECIALDARKGREY, [1190, 0, 10, 800], 0)
        pg.draw.rect(window, ANEVENDARKERSPECIALDARKGREY, [0, 400, 10, 800], 0)
        pg.draw.rect(window, ANEVENDARKERSPECIALDARKGREY, [0, 790, 1400, 10], 0)
        
        
        #sidebar buttons
        creditsB.draw(window)
        helpB.draw(window)
        CompileB.draw(window)
        testB.draw(window)
        PlayerSB.draw(window)
        projectFB.draw(window)
        audioB.draw(window)
        settingsB.draw(window)
        
        #expanding pannel buttons
        if screenS == True:
            EaudioB.draw(window)

        #map movement buttons
        upB.draw(window)
        downB.draw(window)
        leftB.draw(window)
        rightB.draw(window)
        GspeedB.draw(window)
        zplusB.draw(window)
        zminusB.draw(window)
        zoomB.draw(window)
        
        #wall editor buttons
        wplusB.draw(window)
        wminusB.draw(window)
        wupB.draw(window)
        wdownB.draw(window)
        wleftB.draw(window)
        wrightB.draw(window)
        



        mpos = pg.mouse.get_pos()
        mx, my = mpos
        cursor.move((mx, my))
        cursor.draw(window)

        # -------== update screen ==--------------------------------------------------------------------------------------------------------------
        
        pg.display.set_caption(f'Engine   -={name}=-    -= Version {VERSION} =-      -= FPS: {clock.get_fps():.1f} =- ')

        pg.display.flip()
        clock.tick(FPS)

    pg.quit()


# -------== ZA GRID!!!!!!!!!!!!! ==--------------------------------------------------------------------------------------------------------------

def mapgrid(window,name, x, y, scale): #this is how the map is drawn in the grid

    mapPath = os.path.join(name, "map.py") #used importlib to load the map_data and wallamount
    module = importlib.util.spec_from_file_location(f"{name}_map",mapPath)
    mapFile = importlib.util.module_from_spec(module)
    module.loader.exec_module(mapFile)

    grid = mapFile.wall_data
    wallamount = mapFile.wallamount
    
    for walls in range(wallamount):
        x1, y1, x2, y2, c = grid[walls]
        pg.draw.line(window,c,(((x1-x)*scale),((-y1+y)*scale)),((x2-x)*scale,(-y2+y)*scale),2) #drawing walls
    #this whole script was easyer than I thought
    
    

def mapEditor(window,name):
    pass
    
def clickA(click):
    if EngineAudio == True:
        click.play()

if __name__ == "__main__":
    main()