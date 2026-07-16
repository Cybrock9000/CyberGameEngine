import pygame as pg
from CybrocksLibraryG import *
import os
import math as M
from settings import *


class NPC:
    def __init__(self, path='resources/textures/test.png', pos=(0,0), scale=1, shift=0, script=''):
        self.x,self.y = pos
        self.image = BetterImage(path,(0,0),scale,scale)
        self.script = script
        self.dx, self.dy, self.screen_x = 0,0,0
        self.wall = True
    

    def update(self,playerpos,A,pL,screen):
        self.draw(playerpos,A,pL,screen)
    
    def draw(self, playerpos, pA, pL, screen):
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

        focal = 600

        screen_x = 600 + (rot_x / rot_y) * focal
        
        d = max(1, self.dist(px, py, self.x, self.y))
        scale = 1
        scale = (scale / d)*500+1 #100 - dist(self.x,self.y,px,py)


        #self.image.move((screen_x, -(pL)+400))
        self.image.centerscale((screen_x, pL*30+400),scale)
        
        self.image.draw(screen)
        

    def dist(self,x1,y1,x2,y2): #might add this to the lib because i use it so much
        return(M.sqrt(M.pow((x2-x1),2)+M.pow((y2-y1),2)))


    def raycast(self, px, py, wx1, wy1, wx2, wy2):
        if self.intersect((self.x, self.y),(px, py),(wx1, wy1),(wx2, wy2)):
            self.wall = False


        

    def ccw(self,A,B,C):
        return (C[1]-A[1]) * (B[0]-A[0]) > (B[1]-A[1]) * (C[0]-A[0])

    def intersect(self,A,B,C,D):
        return self.ccw(A,C,D) != self.ccw(B,C,D) and self.ccw(A,B,C) != self.ccw(A,B,D)