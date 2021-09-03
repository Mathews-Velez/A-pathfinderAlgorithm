import pygame
# An event type is a pygame event,
# This is a list that defines some implemented pygame events
event_types = {
    'mouse0_down': pygame.MOUSEBUTTONDOWN,
    'keydown': pygame.KEYDOWN,
    'keyup': pygame.KEYUP,
}
# stores the events themselves
events = {}

# Contains a list of functions that are associated with an event
class eventcontainer:
    def __init__(self):
        self.events = []
    def run(self,event):
        for event_function in self.events:
            event_function(event)
    def append(self,event_function):
        self.events.append(event_function)

# Provides functions for classes that listen to events
class eventlistener:
    # adds an event
    def _add_event(self,event_type,event):
        add(event_type,event)

# inits the eventsystem
def init_events():
    # initialize a list for every event type
    for event_type in event_types.keys():
        events[event_type] = eventcontainer()

# Runs the current pygame event
# Is ran during the game_loop
def run_events(event):
    for key in event_types.keys():
        if event.type == event_types[key]:
            events[key].run(event)

# Adds an event to the events list
# should be called via the eventlistener
def add(event_type, event_function):
    if not(event_type in event_types.keys()):
        raise Exception("The event type "+event_type+" is not implemented")
    events[event_type].append(event_function)
