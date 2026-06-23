
#im autualy going to try to comment as much as posible for this project unlike my other projects (horizon vibe)





# -------== imports ==-------

import pygame as pg
from pygame.locals import *
import time
from ENGsettings import *
from CybrocksLibrary import *
from ENGLIB import *
import shutil
import os
from os import listdir
from tkinter import messagebox,colorchooser
import tkinter as tk
import webbrowser
import re
import subprocess
import importlib.util
import array


# -------== colors ==--------------------------------------------------------------------------------------------------------------

SPECIALDARKGREY = (48, 48, 75)
ANEVENDARKERSPECIALDARKGREY = (26, 26, 43)



def main(): #looking back on it now, i could have used classes instead
    
    # -------== setting up ==--------------------------------------------------------------------------------------------------------------
    
    pg.init()
    os.environ['SDL_VIDEO_WINDOW_POS'] = "100,100"
    
    
    window = pg.display.set_mode((1,1))# (1,1) for dynamic screen scaleing
    pg.display.set_caption('Enter a name in the box :)')

    icon = pg.image.load('icon.ico').convert_alpha()
    pg.display.set_icon(icon)
    

    # -------== audio ==--------------------------------------------------------------------------------------------------------------
    
    click = pg.mixer.Sound('resources\sounds\click.wav')
    
    
    # -------== creation of project or opening it ==--------------------------------------------------------------------------------------------------------------
    
    root = tk.Tk()
    root.title("Enter Name of Project. A New Name Will Create a New Project. A preexisting Name Will Just Open it.")

    name = ""

    tk.Label(root, text="Enter Name of Project. A New Name Will Create a New Project. A Preexisting Name Will Just Open it. Want a Demonstration? Type: demo").grid(row=0, column=0)

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
    scaleScreen((1, 1), (1200, 800),window)

    # -------== init other stuff ==--------------------------------------------------------------------------------------------------------------
    
    clock = pg.time.Clock()
    pg.mouse.set_visible(False)
    

    mapPath = os.path.join(name, "map.py") #used importlib to load the map_data and wallamount
    module = importlib.util.spec_from_file_location(f"{name}_map",mapPath)
    mapFile = importlib.util.module_from_spec(module)
    module.loader.exec_module(mapFile)
    
    playerPath = os.path.join(name, "player.py")
    pmodule = importlib.util.spec_from_file_location(f"{name}_player",playerPath)
    playerFile = importlib.util.module_from_spec(pmodule)
    pmodule.loader.exec_module(playerFile)
    
    settingsPath = os.path.join(name, "settings.py")
    smodule = importlib.util.spec_from_file_location(f"{name}_settings",settingsPath)
    settingsFile = importlib.util.module_from_spec(smodule)
    smodule.loader.exec_module(settingsFile)

    scripts = [] #scripts, font and text had to be loaded early for the load scripts
    font = pg.font.SysFont('Comic Sans MS', 15)
    text = {}
    loadScripts(name,font,text)
    
    # -------== vars ==--------------------------------------------------------------------------------------------------------------
    
    #button stuff

    buttonDelay = False #single click instead of repeating output, also have to have multiple to prevent problems I totaly did not spend hours trying to figure out :/
    buttonDelay2 = False
    buttonDelay3 = False
    buttonDelay4 = False
    buttonDelay5 = False
    buttonDelay6 = False
    buttonDelay7 = False
    buttonDelay8 = False
    buttonDelay9 = False
    buttonDelay10 = False
    buttonDelay11 = False
    
    #grid and editor

    mapx = 0
    mapy = 0
    scale = 0.25
    
    cmapx = 0
    cmapy = 0
    
    pointx = 0
    pointy = 0
    pointx2 = 0
    pointy2 = 0
    point = 0
    
    gspeed = 0.5
    cspeed = 1
    
    snap = False
    
    wallColor = (255,0,0)
    grid = mapFile.wall_data
    wallamount = mapFile.wallamount
    
    #pannels

    screenA = False
    screenS = False
    screenG = False

    #other

    scrolly = 0
    
    # -------== images ==--------------------------------------------------------------------------------------------------------------
    
    cursor = BetterImage("resources/textures/mapC.png", (0, 0), 5, 5)
    Gcursor = BetterImage("resources/textures/C.png", (0, 0), 3, 3) # \/ that workerd somehow \/
    playerStart = BetterImage("resources/textures/playerStart.png",(playerFile.playerStartPos[0],playerFile.playerStartPos[1]),3, 3)
    
    # -------== buttons ==--------------------------------------------------------------------------------------------------------------
    
    creditsB = Button("resources/textures/CButton.png", (1000, 700), 3, 3) #used my button class to make buttons easyer
    helpB = Button("resources/textures/docsButton.png", (1000, 620), 3, 3)
    CompileB = Button("resources/textures/CompButton.png", (1000, 485), 3, 3)
    testB = Button("resources/textures/tButton.png", (1000, 405), 3, 3)
    PlayerSB = Button("resources/textures/PSButton.png", (1000, 325), 3, 3)
    projectFB = Button("resources/textures/PFButton.png", (1000, 245), 3, 3)
    audioB = Button("resources/textures/AButton.png", (1000, 165), 3, 3)
    settingsB = Button("resources/textures/SButton.png", (1000, 5), 3, 3)
    EaudioB = Button("resources/textures/EAButton.png", (1210, 10), 3, 3)
    scrollIB = Button("resources/textures/EAButton.png", (1210, 90), 3, 3)
    gameSB = Button("resources/textures/GSButton.png", (1000, 85), 3, 3)
    darkB = Button("resources/textures/DButton.png", (1210, 10), 3, 3)
     
    
    if EngineAudio == True:
        EaudioB.new_image("resources/textures/EATButton.png", (1210, 10), 3, 3)
    else:
        EaudioB.new_image("resources/textures/EAButton.png", (1210, 10), 3, 3)
        
    if mouseINV == True:
        scrollIB.new_image("resources/textures/scrollButtonT.png", (1210, 90), 3, 3)
    else:
        scrollIB.new_image("resources/textures/scrollButton.png", (1210, 90), 3, 3)
        
    if settingsFile.DARK == True:
        darkB.new_image("resources/textures/DTButton.png", (1210, 10), 3, 3)
    else:
        darkB.new_image("resources/textures/DButton.png", (1210, 10), 3, 3)
        
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
    splusB = Button("resources/textures/plus.png", (725, 25), 3, 3) # the s is script
    sminusB = Button("resources/textures/minus.png", (845, 25), 3, 3)
    oplusB = Button("resources/textures/plus.png", (440, 25), 3, 3) # the s is script
    ominusB = Button("resources/textures/minus.png", (560, 25), 3, 3)
    
    colorB = Button("resources/textures/color.png", (25, 635), 3, 3)
    
    pStartB = Button("resources/textures/playerB.png", (300, 635), 3, 3)
    
    wupB = Button("resources/textures/up.png", (160, 575), 3, 3)
    wdownB = Button("resources/textures/down.png", (160, 635), 3, 3)
    wleftB = Button("resources/textures/left.png", (100, 635), 3, 3)
    wrightB = Button("resources/textures/right.png", (220, 635), 3, 3)
    CspeedB = Button("resources/textures/speed1.png", (25, 700), 3, 3)
    swupB = Button("resources/textures/up.png", (160, 575), 3, 3)
    swdownB = Button("resources/textures/down.png", (160, 635), 3, 3)
    swleftB = Button("resources/textures/left.png", (100, 635), 3, 3)
    swrightB = Button("resources/textures/right.png", (220, 635), 3, 3)
    


    #blank script buttons
    bsb1 = Button("resources/textures/blankButton.png", (740, 120), 3, 3)
    bsb2 = Button("resources/textures/blankButton.png", (740, 200), 3, 3)
    bsb3 = Button("resources/textures/blankButton.png", (740, 280), 3, 3)
    bsb4 = Button("resources/textures/blankButton.png", (740, 360), 3, 3)
    bsb5 = Button("resources/textures/blankButton.png", (740, 440), 3, 3)
    bsb6 = Button("resources/textures/blankButton.png", (740, 520), 3, 3)
    bsb7 = Button("resources/textures/blankButton.png", (740, 600), 3, 3)
    bsb8 = Button("resources/textures/blankButton.png", (740, 680), 3, 3)

    #blank object buttons

    bob1 = Button("resources/textures/blankButton.png", (460, 120), 3, 3) # my army of bobs
    bob2 = Button("resources/textures/blankButton.png", (460, 200), 3, 3)
    bob3 = Button("resources/textures/blankButton.png", (460, 280), 3, 3)
    bob4 = Button("resources/textures/blankButton.png", (460, 360), 3, 3)
    bob5 = Button("resources/textures/blankButton.png", (460, 440), 3, 3)
    bob6 = Button("resources/textures/blankButton.png", (460, 520), 3, 3)
    bob7 = Button("resources/textures/blankButton.png", (460, 600), 3, 3)
    bob8 = Button("resources/textures/blankButton.png", (460, 680), 3, 3)

    # -------== main loop ==--------------------------------------------------------------------------------------------------------------
    runningMain = True
    while runningMain:
        
        # -------== controls and keys and buttons ==--------------------------------------------------------------------------------------------------------------
        
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE
            ):
                runningMain = False
                
            if event.type == MOUSEWHEEL:
                if mouseINV:
                    scrolly -= event.y*80
                else:
                    scrolly += event.y*80
                if scrolly >= 0:
                    scrolly = 0
        


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
            
            if screenA == False and not screenS == True and not screenG == True:
                
                scaleScreen((1200, 800), (1400, 800),window)
                screenA = True
                
            elif not screenS == True and not screenG == True:
                
                scaleScreen((1400, 800), (1200, 800),window)
                screenA = False


            buttonDelay4 = True
            
        elif audioB.is_pressed() and buttonDelay4 == True:
            pass
        else: 
             buttonDelay4 = False
             # I LOVE ULTRAKILL MUSIC, SPECIFICLY ORDER (thanke me later :) )
             


        if settingsB.is_pressed() and buttonDelay5 == False:
            
            clickA(click)
            
            if screenS == False and not screenA == True and not screenG == True:
                
                RES = (1400, 800)
                scaleScreen((1200, 800), (1400, 800),window)
                screenS = True
                
            elif not screenA == True and not screenG == True:
                
                scaleScreen((1400, 800), (1200, 800),window)
                screenS = False
                
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


        if EaudioB.is_pressed() and buttonDelay6 == False and screenS == True:
            
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
            
        if wupB.is_pressed() and snap == False:
            cmapy -= cspeed
        if wdownB.is_pressed() and snap == False:
            cmapy += cspeed
        if wleftB.is_pressed() and snap == False:
            cmapx -= cspeed
        if wrightB.is_pressed() and snap == False:
            cmapx += cspeed
            
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
                
            
            buttonDelay8 = True
            
        elif GspeedB.is_pressed() and buttonDelay8 == True:
            pass
        
        else: 
             buttonDelay8 = False
             
        if wplusB.is_pressed() and buttonDelay9 == False:
            
            clickA(click)
            
            if point == 0:
                point = 1
                pointx, pointy = gcloc2 #this makes clicking with the grid pointer calculate the world pos instead of the grid pos
                print((pointx,pointy))
                
            elif point == 1:
                point = 0
                pointx2, pointy2 = gcloc2
                print((pointx2,pointy2))
                grid.append([pointx,-pointy,pointx2,-pointy2, wallColor])
                wallamount += 1
                print(grid)
                savemap(name,grid,wallamount)
            
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
             
        if colorB.is_pressed() and buttonDelay11 == False:
            
            clickA(click)
            c1 = colorchooser.askcolor(title ="Choose color")
            wallColor = c1[0]
            buttonDelay11 = True
            
        elif colorB.is_pressed() and buttonDelay11 == True:
            pass
        else: 
             buttonDelay11 = False
             
        if CspeedB.is_pressed() and buttonDelay12 == False:
            
            clickA(click)
            
            if cspeed == 1:
                cspeed = 2
                CspeedB.new_image("resources/textures/speed2.png", (25, 700), 3, 3)
            elif cspeed == 2:
                cspeed = 5
                CspeedB.new_image("resources/textures/speed5.png", (25, 700), 3, 3)
            elif cspeed == 5:
                cmapx, cmapy = round(cmapx, -1), round(cmapy, -1)
                cspeed = 10
                snap = True
                CspeedB.new_image("resources/textures/speed10C.png", (25, 700), 3, 3)
            elif cspeed == 10:
                cspeed = 20
                CspeedB.new_image("resources/textures/speed20C.png", (25, 700), 3, 3)
            elif cspeed == 20:
                snap = False
                cspeed = 1
                CspeedB.new_image("resources/textures/speed1.png", (25, 700), 3, 3)
                
            
            buttonDelay12 = True
            
        elif CspeedB.is_pressed() and buttonDelay12 == True:
            pass
        
        else: 
             buttonDelay12 = False
             
        if swupB.is_pressed() and buttonDelay13 == False and snap == True:
            
            clickA(click)
            
            cmapy -= cspeed
            buttonDelay13 = True
            
        elif swupB.is_pressed() and buttonDelay13 == True:
            pass
        else: 
             buttonDelay13 = False
             
        if swdownB.is_pressed() and buttonDelay14 == False and snap == True:
            
            clickA(click)
            
            cmapy += cspeed
            buttonDelay14 = True
            
        elif swdownB.is_pressed() and buttonDelay14 == True:
            pass
        else: 
             buttonDelay14 = False
             
        if swleftB.is_pressed() and buttonDelay15 == False and snap == True:
            
            clickA(click)
            
            cmapx -= cspeed
            buttonDelay15 = True
            
        elif swleftB.is_pressed() and buttonDelay15 == True:
            pass
        else: 
             buttonDelay15 = False
             

        if swrightB.is_pressed() and buttonDelay16 == False and snap == True:
            
            clickA(click)
            
            cmapx += cspeed
            buttonDelay16 = True
            
        elif swrightB.is_pressed() and buttonDelay16 == True:
            pass
        else: 
             buttonDelay16 = False
             

        if scrollIB.is_pressed() and buttonDelay17 == False and screenS == True:
            
            clickA(click)
            EngineSfile = "ENGsettings.py"
            
            with open(EngineSfile, "r") as file:
                
                content = file.read()
            if mouseINV == False:
                
                content = re.sub(r"^mouseINV\s*=.*$","mouseINV = True",content,flags=re.MULTILINE)
                scrollIB.new_image("resources/textures/scrollButtonT.png", (1210, 90), 3, 3)
                
            else:
                content = re.sub(r"^mouseINV\s*=.*$","mouseINV = False",content,flags=re.MULTILINE)
                scrollIB.new_image("resources/textures/scrollButton.png", (1210, 90), 3, 3)
            
            with open(EngineSfile, "w") as file:
                
                file.write(content)
            buttonDelay17 = True
            tk.messagebox.showwarning("info", "Restart to take request to effect!")
            
        elif scrollIB.is_pressed() and buttonDelay17 == True:
            pass
        else: 
             
             buttonDelay17 = False
             
        if PlayerSB.is_pressed() and buttonDelay18 == False:
            
            clickA(click)
            path = os.getcwd()
            subprocess.Popen(["notepad.exe", f"{path}\{name}\player.py"])
            buttonDelay18 = True
            
        elif PlayerSB.is_pressed() and buttonDelay18 == True:
            pass
        else: 
             buttonDelay18 = False
             
        if wminusB.is_pressed() and buttonDelay19 == False:
            
            clickA(click)
            path = os.getcwd()
            if len(grid) >= 0:
                grid.pop()
                wallamount -= 1
                savemap(name,grid,wallamount)
            buttonDelay19 = True
            
        elif wminusB.is_pressed() and buttonDelay19 == True:
            pass
        else: 
             buttonDelay19 = False
             
        if pStartB.is_pressed() and buttonDelay20 == False:
            
            clickA(click)
            updatePlayerPos(name, (cmapx, -cmapy, 20))
            tk.messagebox.showwarning("info", "Restart to take request to effect in editor but should testing work!")
            buttonDelay20 = True
            
        elif pStartB.is_pressed() and buttonDelay20 == True:
            pass
        else: 
             buttonDelay20 = False
             
        if gameSB.is_pressed() and buttonDelay21 == False:
            
            clickA(click)
            
            if screenG == False and not screenA == True and not screenS == True:
                
                RES = (1400, 800)
                scaleScreen((1200, 800), (1400, 800),window)
                screenG = True
                
            elif not screenS == True and not screenA == True:
                
                scaleScreen((1400, 800), (1200, 800),window)
                screenG = False
                
            buttonDelay21 = True
            
        elif gameSB.is_pressed() and buttonDelay21 == True:
            pass
        
        else: 
             buttonDelay21 = False
             
        if darkB.is_pressed() and buttonDelay22 == False and screenG == True:
            
            clickA(click)
            updateDarkness(name, -settingsFile.DARK)
            tk.messagebox.showwarning("info", "Restart to take request to effect in editor but should testing work!")
            buttonDelay22 = True
            
        elif darkB.is_pressed() and buttonDelay22 == True:
            pass
        else: 
             buttonDelay22 = False

        # -------== drawing stuff ==--------------------------------------------------------------------------------------------------------------
        

        window.fill('black')
        mapgrid(window, name, mapx, mapy, scale,grid,wallamount)
        if point == 1:
            pg.draw.line(window,wallColor,(((pointx - mapx))* scale, ((pointy + mapy))* scale),(((cmapx - mapx))* scale, ((cmapy + mapy))* scale),2) #drawing the line for making new walls
            
        playerStart.move(((playerFile.playerStartPos[0]-mapx)*scale,(playerFile.playerStartPos[1]+mapy)*scale))
        playerStart.draw(window)
        
        gcloc = ((cmapx-mapx)*scale, (cmapy+mapy)*scale)
        gcloc2 = (cmapx, cmapy) #took me forever to realize it was just the cursor pos and not some fancy equation
        Gcursor.move(gcloc)
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
        

        #blank script buttons

        bsb1.draw(window)
        bsb2.draw(window)
        bsb3.draw(window)
        bsb4.draw(window)
        bsb5.draw(window)
        bsb6.draw(window)
        bsb7.draw(window)
        bsb8.draw(window)

        scriptsPannel(text,window,scrolly)
        
        bob1.draw(window)
        bob2.draw(window)
        bob3.draw(window)
        bob4.draw(window)
        bob5.draw(window)
        bob6.draw(window)
        bob7.draw(window)
        bob8.draw(window)
        
        #sidebar buttons
        creditsB.draw(window)
        helpB.draw(window)
        CompileB.draw(window)
        testB.draw(window)
        PlayerSB.draw(window)
        projectFB.draw(window)
        audioB.draw(window)
        settingsB.draw(window)
        gameSB.draw(window)
        
        #expanding pannel buttons
        if screenS == True:
            EaudioB.draw(window)
            scrollIB.draw(window)
            
        if screenG == True:
            darkB.draw(window)

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
        
        if snap == False:
            wupB.draw(window)
            wdownB.draw(window)
            wleftB.draw(window)
            wrightB.draw(window)
        else: 
            swupB.draw(window)
            swdownB.draw(window)
            swleftB.draw(window)
            swrightB.draw(window)
        colorB.draw(window)
        pStartB.draw(window)
        CspeedB.draw(window)
        
        splusB.draw(window)
        sminusB.draw(window)
        oplusB.draw(window)
        ominusB.draw(window)



        mpos = pg.mouse.get_pos()
        mx, my = mpos
        cursor.move((mx, my))
        cursor.draw(window)

        # -------== update screen ==--------------------------------------------------------------------------------------------------------------
        
        pg.display.set_caption(f'Engine   -={name}=-    -= Version {VERSION} =-      -= FPS: {clock.get_fps():.1f} =-      -={time.strftime('%H:%M:%S:')}=- ')

        pg.display.flip()
        clock.tick(FPS)




# -------== ZA GRID!!!!!!!!!!!!! ==--------------------------------------------------------------------------------------------------------------

def mapgrid(window,name, x, y, scale, grid, wallamount): #this is how the map is drawn in the grid
    
    for walls in range(wallamount):
        x1, y1, x2, y2, c = grid[walls]
        pg.draw.line(window,c,(((x1-x)*scale),((-y1+y)*scale)),((x2-x)*scale,(-y2+y)*scale),2) #drawing walls
    #this whole script was easyer than I thought
    
# -------== Pannels ==--------------------------------------------------------------------------------------------------------------
def loadScripts(name,font,text):
    global scripts
    path = os.getcwd()
    scripts = os.listdir((f'{path}/{name}/scripts'))
    '''print((f'{path}/{name}/scripts'))
    print(scripts)'''
    for script in scripts:
        text[script] = font.render(script, False, (0, 0, 0))


def scriptsPannel(text, screen, scrolly):
    e = 0
    for i in text:
        e += 1
        ypos = (80 * e) + scrolly + 60
        if ypos <= 120 or ypos >= 750: 
            pass
        else:
            screen.blit(text[i], (760, ypos))
            
        
def clickA(click): #me being lazy
    if EngineAudio == True:
        click.play()

def scaleScreen(start_res, end_res,window):
    start_w, start_h = start_res
    end_w, end_h = end_res

    steps = 10
    

    scaleIMG = BetterImage("resources/textures/scale.png",(0,0),1, 1)


    for i in range(steps + 1):
        t = i / steps

        w = int(start_w + (end_w - start_w) * t)
        h = int(start_h + (end_h - start_h) * t)

        pg.display.set_mode((w, h))
        window.fill('black')
    
        pg.draw.rect(window, SPECIALDARKGREY, [0, 400, 400, 400], 0) #this drawing part is to make sure it doesnt look wierd when scailing
        pg.draw.rect(window, SPECIALDARKGREY, [400, 0, 1200, 800], 0)
        pg.draw.rect(window, ANEVENDARKERSPECIALDARKGREY, [390, 0, 10, 800], 0)
        pg.draw.rect(window, ANEVENDARKERSPECIALDARKGREY, [670, 0, 10, 800], 0)
        pg.draw.rect(window, ANEVENDARKERSPECIALDARKGREY, [390, 100, 560, 10], 0)
        pg.draw.rect(window, ANEVENDARKERSPECIALDARKGREY, [950, 0, 10, 800], 0)
        pg.draw.rect(window, ANEVENDARKERSPECIALDARKGREY, [0, 550, 400, 10], 0)
        pg.draw.rect(window, ANEVENDARKERSPECIALDARKGREY, [0, 400, 400, 10], 0)
        pg.draw.rect(window, ANEVENDARKERSPECIALDARKGREY, [950, 570, 600, 10], 0)
        pg.draw.rect(window, ANEVENDARKERSPECIALDARKGREY, [1190, 0, 10, 800], 0)
        pg.draw.rect(window, ANEVENDARKERSPECIALDARKGREY, [0, 400, 10, 800], 0)
        pg.draw.rect(window, ANEVENDARKERSPECIALDARKGREY, [0, 790, 1400, 10], 0)
        scaleIMG.draw(window) # image to make it look even smoother
        pg.display.flip()
        pg.time.delay(5) #speed



if __name__ == "__main__":
    main()
    


pg.quit()