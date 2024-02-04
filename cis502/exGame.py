import pygame

from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
    K_0,
    K_1,
    K_2
)

pygame.init()
screen = pygame.display.set_mode([800,600])
shapes = []
cur_shape = "C"
av_shapes = ["C","S","T"]
clr = (255,255,255)
running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == K_ESCAPE:
                clr = (0,0,0)
            elif event.key == K_UP:
                shapes = []
            elif event.key == K_0:
                cur_shape = av_shapes[0]
            elif event.key == K_1:
                cur_shape = av_shapes[1]
        elif event.type == pygame.MOUSEBUTTONDOWN:
            shapes.append((pygame.mouse.get_pos(),cur_shape))
    # Fill the background with white
    screen.fill(clr)

    # Draw a solid blue circle in the center
    pygame.draw.circle(screen,(0,0,255),(255,255),75)
    for pos,shapeType in shapes:
        if(shapeType == "C"):
            pygame.draw.circle(screen,(0,0,255),pos,75)
        elif(shapeType == "S"):
            pygame.draw.circle(screen,(0,255,0),pos,25)

    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()