import sys, pygame
from textbox import textbox
white =255, 255, 255
def game_loop(screen,boxes):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        screen.fill(white)
        draw_title(screen,boxes)

def draw_title(screen,boxes):
    boxes['submit_box'].draw(screen)
def init_title():
    submit_box = textbox()
    submit_box.set_text('Begin',30)
    return submit_box

def main():
    #init pygame
    pygame.init()
    screen = pygame.display.set_mode((500,500))
    #get boxes
    boxes = {
        'submit_box' : init_title()
    }
    #draw the screen with each iteration
    while 1:
        game_loop(screen,boxes)
        pygame.display.update()


main()