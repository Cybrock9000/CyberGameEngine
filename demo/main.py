import pygame as pg
from settings import *
from player import *
import time
import math as M
from map import*
from os import listdir
from CybrocksLibraryG import *


def main():
    
    # inits

    pg.init()

    window = pg.display.set_mode(RES)

    pg.mouse.set_visible(False)
    pg.event.set_grab(True)

    icon = pg.image.load('icon.ico').convert_alpha()
    pg.display.set_icon(icon)
    
    clock = pg.time.Clock()
    

    sky = BetterImage(f"{NAME}/resources/textures/sky.webp", (0, 0), 2, 2)
    sky2 = BetterImage(f"{NAME}/resources/textures/sky.webp", (0, 0), 2, 2)
    if EHUD == True:
        hud = BetterImage(f"{NAME}/resources/textures/hud.png", (0, 0), 2, 2)
    if DARK == True:
        vig = BetterImage(f"{NAME}/resources/textures/Vignette.png", (0, 0), 2, 2)

    
    px,py,pz= playerStartPos
    
    jumping = False
    i = -20
    g = 0
    col = False
    grounded = True
    
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
        if keys[pg.K_LSHIFT] and not crouch:
            crouch = False
            sprinting = True
            speed = SPEED * dt *2
        elif keys[pg.K_LCTRL] and not sprinting:
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
            
        

        oldpx = px
        oldpy = py
        if keys[pg.K_w]:
            px += dx * speed
            py += dy * speed

        if keys[pg.K_s]:
            px -= dx * speed
            py -= dy * speed

        if keys[pg.K_d]:
            px += dy * speed
            py -= dx * speed

        if keys[pg.K_a]:
            px -= dy * speed
            py += dx * speed

            

            
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
  
            g += 12 #gravity
        else: 
            falling  = False
            grounded = True
            g = 0
        
        if crouch and grounded and not falling and not jumping:
            pz = 30
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
        col = draw(window, px, py, pz, pa, pl, col) #janky way on simple collision by using the draw method and raycaster, but it works for now
        if col:
            px = oldpx
            py = oldpy
            
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
        rayangle = (pa - 45 + ray * 10) * M.pi / 180 # the number *ing the ray is the angle between each ray

        dx = M.sin(rayangle)
        dy = M.cos(rayangle)

        sx, sy = px, py

        for move in range(rayDist): #the dist the ray travels
            sx += dx 
            sy += dy 

            #pg.draw.circle(window, "red", (sx, sy), 2)

            if intersect((px, py), (sx, sy),(wx1, wy1), (wx2, wy2)):
                return False #a wall should be there


    return True #no wall :(

def intersect(A,B,C,D):
    return ccw(A,C,D) != ccw(B,C,D) and ccw(A,B,C) != ccw(A,B,D)

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
        

def draw(window,px,py,pz,pa,pl,col):    #drawing walls and such
    col = False
    newwalldata = reorderwalls(px, py)
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
            mx, my = midp2(x1,y1,x2,y2)


            d = max(1, dist(px, py, mx, my))
            c2 = int((c[0] / (d))*SHADOW_DIST+1),int((c[1] / (d))*SHADOW_DIST+1),int((c[2] / (d))*SHADOW_DIST+1)
            if c2 >= c:
                c2 = c
        else:
            c2 = c
        pg.draw.polygon(window,c2,((wallx[walls][0],wally[walls][0]),(wallx[walls][1],wally[walls][1]),(wallx[walls][3],wally[walls][3]),(wallx[walls][2],wally[walls][2])))
    return col
        

    
#math functions 
def dist(x1,y1,x2,y2): # swear that the math library had a distance formula
    return(M.sqrt(M.pow((x2-x1),2)+M.pow((y2-y1),2)))

def midp(x1,y1,x2,y2):
    return((x1 + x2) / 2, (y1 + y2) / 2)

def midp2(x1,y1,x2,y2):
    return(x1 + x2) / 2, (y1 + y2) / 2

if __name__ == "__main__":
    main()
