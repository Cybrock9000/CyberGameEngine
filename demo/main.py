import pygame as pg
from pygame import gfxdraw
from settings import *
from player import *
import time
import math as M
from map import*
from os import listdir
from CybrocksLibraryG import *
import os
from npc_handler import *
from npc import *


def main():
    
    # inits

    pg.init()
    pg.mixer.init()
    
    NpcHandler = npcHandler()
    
    with open(os.curdir +'/scripts/player.cy', "r") as f:
        playerS = f.read().splitlines()
        
    with open(os.curdir +'/objects/npc.cy', "r") as f:
        npcS = f.read().splitlines()

    window = pg.display.set_mode(RES)

    pg.mouse.set_visible(False)
    pg.event.set_grab(True)

    icon = pg.image.load(os.curdir +'\icon.ico').convert_alpha()
    pg.display.set_icon(icon)
    
    clock = pg.time.Clock()
    
    bgm = pg.mixer.Sound(os.curdir +'/resources/music/bg.wav')
    channel = bgm.play(-1)

    sky = BetterImage(os.curdir +"/resources/textures/sky.webp", (0, 0), 2, 2)
    sky2 = BetterImage(os.curdir +"/resources/textures/sky.webp", (0, 0), 2, 2)
    hand = BetterImage(os.curdir +"/resources/textures/w/handEmpty.png", (RES[0]/4+15, RES[1]/4), 5, 5)
    if EHUD == True:
        hud = BetterImage(os.curdir +"/resources/textures/hud.png", (0, 0), 2, 2)
    if DARK == True:
        vig = BetterImage(os.curdir +"/resources/textures/Vignette.png", (0, 0), 2, 2)

    playerStartPos = (0, 0, 20)
    px,py,pz= playerStartPos
    
    
    jumping = False
    i = -20
    g = 0
    col = False
    grounded = True
    handbob = 0
    bobDir = 1
    
    SPEED, HEALTH, CanRun, CanCrouch = loadPlayerScripts(playerS)
    loadObjectScripts(npcS,NpcHandler)
    
    dx = 0
    dy = 0
    
    pa = 0
    pl = 0
    newwalldata = []


    running = True
    while running:
        
        dt = clock.tick(FPS) / 1000
        
        # controlls

        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE
            ):
                running = False
                
        mx, my = pg.mouse.get_pos()
        keys = pg.key.get_pressed()
        rspeed = 200
        if keys[pg.K_LSHIFT] and not crouch and CanRun:
            crouch = False
            sprinting = True
            speed = SPEED * dt *2
        elif keys[pg.K_LCTRL] and not sprinting and CanCrouch:
            crouch = True
            sprinting = False
            speed = SPEED * dt /2
        elif not keys[pg.K_LCTRL]:
            crouch = False
            sprinting = False
            speed = SPEED * dt
            
        

        '''if keys[pg.K_LEFT]:
            pa -= rspeed * dt
            if pa < 0:
                pa +=360

        if keys[pg.K_RIGHT]:
            pa += rspeed * dt
            if pa > 359:
                pa -=360
        
        if keys[pg.K_UP]:
            pl += rspeed * dt

        if keys[pg.K_DOWN]:
            pl -= rspeed * dt'''
        
        if handbob >= 10:
            bobDir = -1
        if handbob <= -10:
            bobDir = 1
        
        oldpx = px
        oldpy = py
        if keys[pg.K_w]:
            px += dx * speed
            py += dy * speed
            handbob += bobDir
            hand.move((RES[0]/4+15, RES[1]/4+handbob))

        if keys[pg.K_s]:
            px -= dx * speed
            py -= dy * speed
            handbob += bobDir
            hand.move((RES[0]/4+15, RES[1]/4+handbob))

        if keys[pg.K_d]:
            px += dy * speed
            py -= dx * speed
            handbob += bobDir
            hand.move((RES[0]/4+15, RES[1]/4+handbob))

        if keys[pg.K_a]:
            px -= dy * speed
            py += dx * speed
            handbob += bobDir
            hand.move((RES[0]/4+15, RES[1]/4+handbob))
            
            

        #print(grounded)
        # jumping
        if keys[pg.K_SPACE] and grounded == True:
            grounded = False
            jumping = True
        
        if jumping == True:
            i += 1
            if not i >= 10: #jump height
                pz = (pz + (i/15)) # the number in (i/15) is speed
            else:
                jumping = False
                i = -20
        
            
        if pz <= 20 and jumping == False and crouch == False:
            falling = True
            pz +=0.01*g
  
            g += 100 *dt #gravity
        elif pz >= 20: 
            falling  = False
            grounded = True
            g = 0
        
        if crouch and grounded and not falling and not jumping:
            pz = 29
        elif not crouch and grounded and not falling and not jumping:
            pz = 20
        
            
        mdx, mdy = pg.mouse.get_rel() # mouse movement

        mdx = max(-MOUSE_MAX_REL, min(MOUSE_MAX_REL, mdx))

        pa += (mdx * MOUSE_SENSITIVITY) *1.25 #looking r&r was too slow
 
        pl -= (mdy * MOUSE_SENSITIVITY_UD)/2 # you could snap your neck you were looking up too fast
        pl = max(-20, min(20, pl))
            
        if pa >= 360:
            pa -= 360
        if pa <= 0:
            pa += 360
            

        angle = pa * M.pi / 180
        
        #print(pl)

        dx = M.sin(angle)
        dy = M.cos(angle)

        #print(str(px) + ' ' + str(py) + ' ' + str(pz))

        # display
        
        pg.display.set_caption(f'{NAME}   FPS: {clock.get_fps():.1f}')
        window.fill('black')
        if -(pa*5.20) >= 0:
            sky.move((-(pa*5.20),-631+pl*30))
            sky2.move((-(pa*5.20)-1875,-631+pl*30))
        else:
            sky.move((-(pa*5.20),-631+pl*30))
            sky2.move((-(pa*5.20)+1875,-631+pl*30))
        sky.draw(window)
        sky2.draw(window)
        col = draw(window,px,py,pz,pa,pl,col,NpcHandler) #janky way on simple collision by using the draw method and raycaster, but it works for now
        NpcHandler.update((px,py),pa,pl,window)
        if col:
            px = oldpx
            py = oldpy
            

        hand.draw(window)   
            
        if DARK == True:
            vig.draw(window)

        if EHUD == True:
            hud.draw(window)      
           

        pg.display.flip()
        
        

    pg.quit()
        

def ccw(A,B,C):
    return (C[1]-A[1]) * (B[0]-A[0]) > (B[1]-A[1]) * (C[0]-A[0])

def intersect(A,B,C,D):
    return ccw(A,C,D) != ccw(B,C,D) and ccw(A,B,C) != ccw(A,B,D)

def raycast(window, px, py, pz, pa, wx1, wy1, wx2, wy2):  # this checks if there is a wall the player can see
    #pg.draw.circle(window, "blue", (px, py), 5)

    for ray in range(rayAmount): #amount of rays
        
        #it is recomended to keep the fov (not the var, the cone) at around 90

        rayangle = (pa - 45 + ray * 3) * M.pi / 180 # the number *ing the ray is the angle between each ray

        dx = M.sin(rayangle)
        dy = M.cos(rayangle)

        

        rayend = (
            px + dx * rayDist,
            py + dy * rayDist
        )
        #pg.draw.line(window, "red", (px, py),rayend, 2)
        if intersect((px, py),rayend,(wx1, wy1), (wx2, wy2)):
                return False #a wall should be there


    return True #no wall :(


def raycastCOL(window, px, py, pz, pa, wx1, wy1, wx2, wy2):  # this checks for wall colision
    for ray in range(4): #amount of rays
        rayangle = (pa + ray * 90) * M.pi / 180 # the number *ing the ray is the angle between each ray

        dx = M.sin(rayangle)
        dy = M.cos(rayangle)

        sx, sy = px, py

        for move in range(15): #the dist the ray travels. AKA how fat you are
            sx += dx 
            sy += dy 
            #pg.draw.circle(window, "green", (sx, sy), 2)


            if intersect((px, py), (sx, sy),(wx1, wy1), (wx2, wy2)):
                return True #a wall is there
            
    return False #no wall
    

def reorderwalls(px, py):
    wall_distances = []

    for wall in wall_data:
        x1, y1, x2, y2, c = wall

        mx = (x1 + x2) / 2
        my = (y1 + y2) / 2

        d = dist(px, py, mx, my)
        if d <= rayDist:
            wall_distances.append((d, wall))
            

    wall_distances.sort(reverse=True)

    return [wall for d, wall in wall_distances]
        

def npcraycast(handler, px, py, newwalldata):
    newwalldata = reorderwalls(px, py)

    for npc in handler.npc_list:
        npc.wall = True

    for x1, y1, x2, y2, c in newwalldata:
        handler.raycast(px, py, x1, y1, x2, y2)

def draw(window,px,py,pz,pa,pl,col,NpcHandler):    #drawing walls and such
    col = False
    newwalldata = reorderwalls(px, py)
    npcraycast(NpcHandler,px,py,newwalldata)
    
    for walls in range(len(newwalldata)):
        
        radcos = M.cos(pa/180*M.pi)/2
        radsin = M.sin(pa/180*M.pi)/2

        x1, y1, x2, y2, c = newwalldata[walls] # wall cords and color
        
        wx1, wy1 = x1 - px, y1 - py
        wx2, wy2 = x2 - px, y2 - py
        
        if raycastCOL(window, px, py, pz, pa, x1, y1, x2, y2):
            col = True

        if raycast(window, px, py, pz, pa, x1, y1, x2, y2):
            continue
        
        #print(col)
        #pg.draw.line(window,c,(x1,y1),(x2,y2),2)
        
        socialdistfromcameradist = 0.1
        
        wallx[walls][0] = wx1 * radcos - wy1 * radsin
        wallx[walls][1] = wx2 * radcos - wy2 * radsin
        wallx[walls][2] = wallx[walls][0]
        wallx[walls][3] = wallx[walls][1]

        wally[walls][0] = wy1 * radcos + wx1 * radsin
        wally[walls][1] = wy2 * radcos + wx2 * radsin
        wally[walls][2] = wally[walls][0]
        wally[walls][3] = wally[walls][1]
        
        if dist(wallx[walls][1],wallx[walls][0],wallx[walls][3],wallx[walls][2]) <= 0:
            pass
        
        near = 0.1

        if wally[walls][0] < near:
            wally[walls][0] = near

        if wally[walls][1] < near:
            wally[walls][1] = near
            
        if wally[walls][2] < near:
            wally[walls][2] = near
        
        if wally[walls][3] < near:
            wally[walls][3] = near

        wallz[walls][0] = 0-pz+((pl*wally[walls][0])/32)
        wallz[walls][1] = 0-pz+((pl*wally[walls][1])/32)
        wallz[walls][2] = wallz[walls][0]+40
        wallz[walls][3] = wallz[walls][1]+40
        
        wallx[walls][0] = wallx[walls][0]*FOV/wally[walls][0]+600 #screen pos for x and y for both top and bottom of the wall
        wally[walls][0] = wallz[walls][0]*FOV/wally[walls][0]+400
        wallx[walls][1] = wallx[walls][1]*FOV/wally[walls][1]+600
        wally[walls][1] = wallz[walls][1]*FOV/wally[walls][1]+400
        wallx[walls][2] = wallx[walls][2]*FOV/wally[walls][2]+600
        wally[walls][2] = wallz[walls][2]*FOV/wally[walls][2]+400
        wallx[walls][3] = wallx[walls][3]*FOV/wally[walls][3]+600
        wally[walls][3] = wallz[walls][3]*FOV/wally[walls][3]+400
        
        
        '''if wallx[0]>0 and wallx[0]<1200 and wally[0]>0 and wally[0]<800:
            pg.draw.circle(window,'red',(wallx[0],wally[0]),3)
        if wallx[1]>0 and wallx[1]<1200 and wally[1]>0 and wally[1]<800:
            pg.draw.circle(window,'red',(wallx[1],wally[1]),3)'''
            
        if DARK == True:
            mx = (x1 + x2) / 2
            my = (y1 + y2) / 2

            d = max(1, dist(px, py, mx, my))
            c2 = int((c[0] / (d))*SHADOW_DIST+1),int((c[1] / (d))*SHADOW_DIST+1),int((c[2] / (d))*SHADOW_DIST+1)
            if c2 >= c:
                c2 = c
        else:
            c2 = c
        #pg.gfxdraw.textured_polygon(window,((wallx[walls][0],wally[walls][0]),(wallx[walls][1],wally[walls][1]),(wallx[walls][3],wally[walls][3]),(wallx[walls][2],wally[walls][2])),image,0,0)
        pg.draw.polygon(window,c2,((wallx[walls][0],wally[walls][0]),(wallx[walls][1],wally[walls][1]),(wallx[walls][3],wally[walls][3]),(wallx[walls][2],wally[walls][2])))
        
    return col
        

    
#math functions
def dist(x1,y1,x2,y2):
    return(M.sqrt(M.pow((x2-x1),2)+M.pow((y2-y1),2)))

def midp(x1,y1,x2,y2):
    return((x1 + x2) / 2, (y1 + y2) / 2)

def loadPlayerScripts(lines):
    SPEED = 100 #default speed value

    for line in lines:
        line = line.strip()

        if not line or line.startswith("*"):
            continue

        if line == "Done":
            break

        parts = line.split(maxsplit=1)

        key = parts[0]
        value = parts[1] if len(parts) > 1 else ""

        if key == "SHealth":
            HEALTH = int(value)

        elif key == "SSpeed":
            SPEED = float(value)

        elif key == "SCanRun":
            CanRun = value.startswith("T") #if its T then its true

        elif key == "SCanCrouch":
            CanCrouch = value.startswith("T")
            
    return SPEED, HEALTH, CanRun, CanCrouch



def loadObjectScripts(lines,NpcHandler):

    for line in lines:
        line = line.strip()

        if not line or line.startswith("*"):
            continue

        if line == "Done":
            break

        parts = line.split(maxsplit=1)

        key = parts[0]
        value = parts[1] if len(parts) > 1 else ""

        if key == "NPCList":
            startlist = value
            for npc in startlist:
                NpcHandler.npc_list.append(NPC(path='resources/textures/test.png', pos=(5,5), scale=5, shift=0, script=''))
                
    

if __name__ == "__main__":
    main()
