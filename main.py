import pygame

win = pygame.display.set_mode((500, 500))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    pygame.display.update()
