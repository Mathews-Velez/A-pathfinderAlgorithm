import sys, pygame
from textbox import textbox
from inputbox import inputbox, input_types
from eventsystem import run_events, init_events

white =255, 255, 255

boxes = []
buttons = []
# game loop is ran every iteration
# main function for drawing the screen and buttons
def game_loop(screen):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        screen.fill(white)
        draw_screen(screen)
        run_events(event)

# draws all the boxes on the screen
def draw_screen(screen):
    for box in boxes:
        box.draw(screen)

#TODO: make a script for each type of screen
def init_title():
    #submit box
    submit_box = textbox()
    submit_box.set_position(150, 400)
    submit_box.set_text('Begin',30)
    boxes.append(submit_box)
    """ Input boxes """
    # rip to the code repetition
    input_box_color =  230, 230, 230
    #width box
    width_box = inputbox()
    width_box.set_position(10,200)
    width_box.color = input_box_color
    width_box.set_text('width',15)
    width_box.input_type = input_types['numeric']
    boxes.append(width_box)
    buttons.append(width_box)
    #width box
    height_box = inputbox()
    height_box.set_position(290,200)
    height_box.color = input_box_color
    height_box.set_text('height',15)
    height_box.input_type = input_types['numeric']
    boxes.append(height_box)
    buttons.append(height_box)

# main inits pygame and starts the game loop
def main():
    #init pygame
    pygame.init()
    screen = pygame.display.set_mode((500,500))
    init_events()
    init_title()
    #draw the screen with each iteration
    while 1:
        game_loop(screen)
        pygame.display.update()

main()