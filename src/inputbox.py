#inputbox inherits from textbox
#the difference is that inputting keys (after clicking on it) it sets the text modifier
import pygame
from textbox import textbox
from eventsystem import eventlistener

# special keycodes
SPACE = 32
RETURN_KEY = 271
A_KEY = 91
Z_KEY = 122
ZERO = 48
NINE = 57
SHIFT = 304

# input types serve to indicate what can be typed in the box
input_types = {
    'all':0,
    'alpha_numeric':1,
    'numeric':2,
}

class inputbox(textbox,eventlistener):
    input_text = ""
    input_type = input_types['alpha_numeric']
    max_characters = 0 # 0 max chars = no limit
    def __init__(self):
        self.focused = False
        self._set_clicked()
        self._set_keytyping()
    def _set_clicked(self):
        # custom mouseclick function
        # basically sets focused to false if it clicks outside of the box, vice versa if its inside the box
        def clicked(event):
            if pygame.mouse.get_pressed()[0] == 1:
                x, y = pygame.mouse.get_pos()
                in_rect = self.box.collidepoint(x, y)
                self.focused = in_rect
        self._add_event('mouse0_down',clicked)
    def _set_keytyping(self):
        def keypressing_event(event):
            if self.focused:
                self._process_keyinput(event)
        self._add_event("keydown", keypressing_event)
    def _process_keyinput(self,event):
        # Exit if there's control characters being inserted
        key = event.key
        character = event.unicode
        if key < SPACE:
            return
        if key == RETURN_KEY: #unfocus if the user presses enter
            self.focused = False
            return
        # check according to input type
        if self.input_type == input_types['alpha_numeric']:
           if not self._is_alpha(key) and not self._is_number(key): # if its not a letter or number, exit
               return
        elif self.input_type == input_types['numeric']:  # if its not a number, exit
           if not self._is_number(key):
               return

        self.input_text += character
        self.set_text(self.input_text, self.fontsize)

    def _is_alpha(self,key):
        return (key <= Z_KEY) and (key >= A_KEY)
    def _is_number(self,key):
        return (key <= NINE) and (key >= ZERO)
