import pygame
from eventsystem import eventlistener

class button(eventlistener):
    """Left Mouse button clicking"""
    # Set the event
    mouse1_events = []
    def mouse1_click(self,event_function):
        def mouse1_click_event(event):
            if pygame.mouse.get_pressed()[0]==1:
                x, y = pygame.mouse.get_pos()
                if self.box.collidepoint(x, y):
                    event_function()

        self._add_event("mouse0_down",mouse1_click_event)






