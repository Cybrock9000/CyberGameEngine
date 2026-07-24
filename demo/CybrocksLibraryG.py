


# /\ all other stuff was deleted because of bloatware /\ (learn microsoft)


import pygame as pg

class Button:
    def __init__(self, image_path, pos, scalew = 1.0, scaleh = 1.0):
        self.image = pg.image.load(image_path).convert_alpha()
        
        og_width = self.image.get_width()
        og_height = self.image.get_height()
        new_width = int(og_width * scalew)
        new_height = int(og_height * scaleh)
        self.image = pg.transform.scale(self.image, (new_width, new_height))
        
        self.rect = self.image.get_rect(topleft = pos)
        
    def draw(self, window):
        window.blit(self.image, self.rect)
        
    def is_pressed(self):
        mouse_pos = pg.mouse.get_pos()
        mouse_pressed = pg.mouse.get_pressed()[0]
        
        if self.rect.collidepoint(mouse_pos):
            if mouse_pressed:
                return True
        return False
    
    def move(self, pos):
        self.rect = self.image.get_rect(topleft = pos)
        
    def new_image(self,image_path,pos,scalew = 1.0,scaleh = 1.0): #just a copy of the init
        self.image = pg.image.load(image_path).convert_alpha()
        
        og_width = self.image.get_width()
        og_height = self.image.get_height()
        new_width = int(og_width * scalew)
        new_height = int(og_height * scaleh)
        self.image = pg.transform.scale(self.image, (new_width, new_height))
        
        self.rect = self.image.get_rect(topleft = pos)
        
        
class BetterImage:
    def __init__(self, image_path, pos, scalew=1.0, scaleh=1.0):
        # Store the original image
        self.original_image = pg.image.load(image_path).convert_alpha()

        # Current image starts as a copy
        self.image = self.original_image.copy()

        self.og_width = self.original_image.get_width()
        self.og_height = self.original_image.get_height()

        self.new_width = int(self.og_width * scalew)
        self.new_height = int(self.og_height * scaleh)

        self.image = pg.transform.scale(
            self.original_image,
            (self.new_width, self.new_height)
        )

        self.rect = self.image.get_rect(topleft=pos)

    def draw(self, window):
        window.blit(self.image, self.rect)

    def move(self, pos):
        self.rect = self.image.get_rect(topleft=pos)
        
    def centermove(self, pos):
        self.rect = self.image.get_rect(center=pos)

    def scale(self, pos, scale):
        self.new_width = max(1, int(self.og_width * scale))
        self.new_height = max(1, int(self.og_height * scale))

        self.image = pg.transform.scale(
            self.original_image,
            (self.new_width, self.new_height)
        )

        self.rect = self.image.get_rect(topleft=pos)
        
    def centerscale(self, pos, scale):
        self.new_width = max(1, int(self.og_width * scale))
        self.new_height = max(1, int(self.og_height * scale))

        self.image = pg.transform.scale(self.original_image,(self.new_width, self.new_height))

        self.rect = self.image.get_rect(center=pos)

    def new_image(self, image_path, pos, scalew=1.0, scaleh=1.0):
        self.original_image = pg.image.load(image_path).convert_alpha()
        self.image = self.original_image.copy()

        self.og_width = self.original_image.get_width()
        self.og_height = self.original_image.get_height()

        self.new_width = int(self.og_width * scalew)
        self.new_height = int(self.og_height * scaleh)

        self.image = pg.transform.scale(
            self.original_image,
            (self.new_width, self.new_height)
        )

        self.rect = self.image.get_rect(topleft=pos)

    def centernew_image(self, image_path, pos, scalew=1.0, scaleh=1.0):
            self.original_image = pg.image.load(image_path).convert_alpha()
            self.image = self.original_image.copy()
    
            self.og_width = self.original_image.get_width()
            self.og_height = self.original_image.get_height()
    
            self.new_width = int(self.og_width * scalew)
            self.new_height = int(self.og_height * scaleh)
    
            self.image = pg.transform.scale(
                self.original_image,
                (self.new_width, self.new_height)
            )
    
            self.rect = self.image.get_rect(center=pos)