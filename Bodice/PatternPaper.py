import pygame

pygame.init()
(width, height) = (1300, 1200)
screen = pygame.display.set_mode((width, height))

background_colour = (255, 255, 255)
screen.fill(background_colour)

pygame.display.set_caption('Tutorial 1')

pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()
