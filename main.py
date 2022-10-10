import pygame
import time

win = pygame.display.set_mode((500, 500))
wall = pygame.Rect(0, 460, 500, 40)
block1 = pygame.Rect(200, 400, 100, 40)
block2 = pygame.Rect(330, 320, 100, 40)
block3 = pygame.Rect(50, 220, 100, 40)
block4 = pygame.Rect(380, 120, 100, 40)
hero = pygame.Rect(50, 300, 50, 50)
clock = pygame.time.Clock()

t = 1
g_y = 1
v_y = 0
v_x = 0

while True:
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and g_y == 0:
                start_time = time.time()
            elif event.key == pygame.K_RIGHT and g_y == 0:
                start_time = time.time()
        elif event.type == pygame.KEYUP:
            if (event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT) and g_y == 0:
                v_y = -6
                g_y = 1
                v_x = time.time() - start_time
                t = 1

                if event.key == pygame.K_LEFT:
                    v_x = -v_x

    win.fill(0xdddddd)
    pygame.draw.rect(win, 0x00ff77, wall)
    pygame.draw.rect(win, 0xdd5f5f, hero)
    pygame.draw.rect(win, 0x3d3dff, block1)
    pygame.draw.rect(win, 0x3d3dff, block2)
    pygame.draw.rect(win, 0x3d3dff, block3)
    pygame.draw.rect(win, 0x3d3dff, block4)

    s_y = v_y * t + 0.5 * g_y * (t ** 2)
    s_x = v_x * t

    hero.y += s_y
    hero.x += s_x

    t += 1

    if hero.colliderect(wall):
        g_y = 0
        v_y = 0
        v_x = 0
        hero.y = wall.y - hero.h
    elif hero.colliderect(block1):
        g_y = 0
        v_y = 0
        v_x = 0
        hero.y = block1.y - hero.h
    elif hero.colliderect(block2):
        g_y = 0
        v_y = 0
        v_x = 0
        hero.y = block2.y - hero.h
    elif hero.colliderect(block3):
        g_y = 0
        v_y = 0
        v_x = 0
        hero.y = block3.y - hero.h
    elif hero.colliderect(block4):
        g_y = 0
        v_y = 0
        v_x = 0
        hero.y = block4.y - hero.h

    pygame.display.update()
