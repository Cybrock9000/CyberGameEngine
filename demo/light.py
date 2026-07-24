import pygame as pg
from CybrocksLibraryG import *
import os
import math as M
from settings import *
import json
import state
import main


class LIGHT:
    def __init__(self, script=''):
        with open(os.path.join(os.curdir, script), "r") as f:
            data = json.load(f)
            
        self.x,self.y,self.z = data['pos']
        self.strength = data['strength']
        self.image = BetterImage(data['path'],(0,0),data['scale'],data['scale'])
        self.dx, self.dy, self.screen_x = 0,0,0
        self.wall = True
        self.remove = False
    

    def update(self,playerpos,A,pL,screen,pz):
        self.draw(playerpos,A,pL,screen,pz)
        #self.move(playerpos)
        

    
    def draw(self, playerpos, pA, pL, screen, pz):
        if not self.wall:
            return
        px, py = playerpos
        A = M.radians(pA)

        dx = self.x - px
        dy = self.y - py

        rot_x = dx * M.cos(A) - dy * M.sin(A)
        rot_y = dx * M.sin(A) + dy * M.cos(A)

        if rot_y <= 0:
            return
        if self.x == px and self.y == py:
            return



        screen_x = 600 + (rot_x / rot_y) * FOV
        
        d = max(1, self.dist(px, py, self.x, self.y))
        scale = 1
        scale = (scale / d)*500+1 #100 - dist(self.x,self.y,px,py)
        y_offset = self.z * scale 
        pz2 = (pz-20)*((30/self.dist(px, py, self.x, self.y))*50)
        #self.image.move((screen_x, -(pL)+400))
        self.image.centerscale((screen_x, pL*30+400-pz2 - y_offset),scale)
        
        self.image.draw(screen)
        

    def dist(self,x1,y1,x2,y2): #might add this to the lib because i use it so much
        return(M.sqrt(M.pow((x2-x1),2)+M.pow((y2-y1),2)))


    def raycast(self, px, py, wx1, wy1, wx2, wy2):
        if self.intersect((self.x, self.y),(px, py),(wx1, wy1),(wx2, wy2)): #easy
            self.wall = False


        

    def ccw(self,A,B,C):
        return (C[1]-A[1]) * (B[0]-A[0]) > (B[1]-A[1]) * (C[0]-A[0])

    def intersect(self,A,B,C,D):
        return self.ccw(A,C,D) != self.ccw(B,C,D) and self.ccw(A,B,C) != self.ccw(A,B,D)