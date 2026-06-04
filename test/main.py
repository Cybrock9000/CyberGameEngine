import pygame as pg
from settings import *
import time
import math as M
from map import*


def main():
    
    # inits

    pg.init()

    window = pg.display.set_mode(RES)

    icon = pg.image.load('icon.ico').convert_alpha()
    pg.display.set_icon(icon)
    
    clock = pg.time.Clock()
    
    px = 0
    py = 0
    pz = 0
    
    dx = 0
    dy = 0
    
    pa = 0
    pl = 0

    running = True
    while running:
        
        dt = clock.tick(FPS) / 1000
        
        # controlls

        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE
            ):
                running = False
        
        keys = pg.key.get_pressed()
        rspeed = 200
        speed = SPEED * dt
        

        if keys[pg.K_LEFT]:
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
            pl -= rspeed * dt
        
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
        
        if keys[pg.K_q]:
            pz +=1
        
        if keys[pg.K_e]:
            pz -=1
            

        angle = pa * M.pi / 180

        dx = M.sin(angle)
        dy = M.cos(angle)

        print(str(px) + ' ' + str(py) + ' ' + str(pz))

        # display
        
        pg.display.set_caption(f'{NAME}   FPS: {clock.get_fps():.1f}')
        window.fill('black')
        draw(window,px,py,pz,pa,pl)
        pg.display.flip()
        clock.tick(FPS)
        

    pg.quit()
        

def ccw(A,B,C):
    return (C[1]-A[1]) * (B[0]-A[0]) > (B[1]-A[1]) * (C[0]-A[0])

def intersect(A,B,C,D):
    return ccw(A,C,D) != ccw(B,C,D) and ccw(A,B,C) != ccw(A,B,D)

def raycast(window, px, py, pz, pa, wx1, wy1, wx2, wy2):  # this checks if there is a wall the player can see
    pg.draw.circle(window, "blue", (px, py), 5)

    for ray in range(rayAmount): #amount of rays
        rayangle = (pa - 45 + ray * 10) * M.pi / 180 # the number *ing the ray is the angle between each ray

        dx = M.sin(rayangle)
        dy = M.cos(rayangle)

        sx, sy = px, py

        for move in range(rayDist): #the dist the ray travels
            sx += dx 
            sy += dy 

            pg.draw.circle(window, "red", (sx, sy), 2)

            if intersect((px, py), (sx, sy),(wx1, wy1), (wx2, wy2)):
                return False #a wall should be there

    return True #no wall :(
            
    


def draw(window,px,py,pz,pa,pl):    #drawing walls and such
    for walls in range(wallamount):
        
        radcos = M.cos(pa/180*M.pi)/2
        radsin = M.sin(pa/180*M.pi)/2

        
        x1, y1, x2, y2, c = wall_data[walls] # wall cords and color
        
        wx1, wy1 = x1 - px, y1 - py
        wx2, wy2 = x2 - px, y2 - py
        
        if raycast(window, px, py, pz, pa, x1, y1, x2, y2) == True:
            continue
        pg.draw.line(window,c,(x1,y1),(x2,y2),2)
        
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

        pg.draw.polygon(window,c,((wallx[walls][0],wally[walls][0]),(wallx[walls][1],wally[walls][1]),(wallx[walls][3],wally[walls][3]),(wallx[walls][2],wally[walls][2])))

    
def dist(x1,y1,x2,y2):
    return(M.sqrt(M.pow((x2-x1),2)+M.pow((y2-y1),2)))


if __name__ == "__main__":
    main()