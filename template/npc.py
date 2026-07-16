import pygame as pg
from CybrocksLibraryG import *
import os
import math as M


class NPC:
    def __init__(self, path='resources/textures/test.png', pos=(5,5), scale=1, shift=0, script=''):
        self.x,self.y = pos
        self.image = BetterImage((os.curdir + f"/resources/{self.block_type}.png"),(0,0),scale,scale)
        self.script = script
        self.dx, self.dy, self.screen_x = 0,0,0
    

    def update(self,playerpos,A,screen):
        self.draw(playerpos,A,screen)
    
    def draw(self,playerpos,A,screen):
        px,py = playerpos
        

        self.dx = self.dx - px
        self.dy = self.dy - py
        
        self.dx = (self.dx * M.cos(A))-(self.y*M.sin(A))
        self.dy = (self.dx * M.sin(A))+(self.y*M.cos(A))
        
        self.screen_x = self.dx*(0/self.dy)
        self.image.move((self.screen_x,0))
        self.image.draw()