import sys, pygame
hor_align_types={
    'center':1,
    'right':2,
    'left':3
}
vert_align_types={
    'center':1,
    'top':2,
    'bottom':3
}

class textbox:
    #basic fields
    rect_box= 150, 400, 200, 50
    color= 155, 155, 155
    textcolor = 0, 0, 0
    fontsize = 30
    # used for aligning text
    hor_align = hor_align_types['center']
    vert_align = vert_align_types['center']

    def __init__(self):
        pass
    def set_text_color(self,textcolor): # sets the text color
        self.textcolor = textcolor
        if self.text != None:
            self.text = self.font.render(text,True,self.textcolor)
    def set_text(self,text,fontsize): # sets the text and renders it
        self.fontsize = fontsize
        self.font = pygame.font.Font('Font/DejaVuSans-BoldOblique.ttf', self.fontsize)
        self.text = self.font.render(text,True,self.textcolor)
    def draw(self,screen):
        self.box = pygame.draw.rect(screen, self.color, self.rect_box)

        pos = self._align_text()
        screen.blit(self.text, pos)
    def _align_text(self):
        textRect = self.text.get_rect()
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
