#textbox is for boxes with labels on them

import sys, pygame
from aligntypes import hor_align_types, vert_align_types

class textbox():
    #basic fields
    rect_box= 0, 0, 200, 50
    color = 155, 155, 155
    textcolor = 0, 0, 0
    fontsize = 30
    # used for aligning text
    hor_align = hor_align_types['center']
    vert_align = vert_align_types['center']

    def set_text_color(self,textcolor): # sets the text color
        self.textcolor = textcolor
        if self.textbox != None:
            self._render_box();
    def set_text(self,text,fontsize): # sets the text and renders it
        self.fontsize = fontsize
        self.text = text;
        self.font = pygame.font.Font('freesansbold.ttf', self.fontsize)
        self._render_box();
    def set_position(self, x, y):
        w,h = self.rect_box[2],self.rect_box[3]
        self.rect_box = x, y, w, h
    def _render_box(self):
        self.textbox = self.font.render(self.text,True,self.textcolor)
    def draw(self,screen):
        self.box = pygame.draw.rect(screen, self.color, self.rect_box)

        pos = self._align_text()
        screen.blit(self.textbox, pos)
    def _align_text(self):
        textRect = self.textbox.get_rect()
        x = 0
        y = 0
        #align x
        if self.hor_align==hor_align_types['center']:
            x = self.box.centerx - textRect.w / 2
        elif self.hor_align==hor_align_types['right']:
            x = self.box.x
        elif self.hor_align==hor_align_types['left']:
            x = self.box.x+self.box.w-textRect.w
        # align y
        if self.vert_align == vert_align_types['center']:
            y = self.box.centery - textRect.h / 2
        elif self.vert_align == vert_align_types['top']:
            y = self.box.y
        elif self.vert_align == vert_align_types['bottom']:
            y = self.box.y + self.box.h - textRect.h
        # return coords
        return x,y
