import pygame
import time
pygame.init()

win = pygame.display.set_mode((500, 500))
wall = pygame.Rect(0, 460, 500, 40)
blocks = [
    pygame.Rect(200, 400, 100, 40),
    pygame.Rect(330, 320, 100, 40),
    pygame.Rect(50, 220, 100, 40),
    pygame.Rect(380, 120, 100, 40),
]
hero = pygame.Rect(50, 300, 50, 50)
apple = pygame.Rect(100, 30, 30, 30)

hero_image = pygame.image.load('assets/hero.png')
block_image = pygame.image.load('assets/block.png')
bg_image = pygame.image.load('assets/bg.png')
apple_image = pygame.image.load('assets/apple.png')
font = pygame.font.SysFont('Arial', 32)

is_finished = False
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

    win.blit(bg_image, [0, 0])
    pygame.draw.rect(win, [40, 40, 80], wall)
    win.blit(hero_image, hero)
    win.blit(apple_image, apple)

    for block in blocks:
        win.blit(block_image, block)

    if is_finished:
        text = font.render('Вы прошли игру!!!', True, (255, 255, 255))
        win.blit(text, [10, 50])

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

    if hero.colliderect(apple):
        print('Вы прошли игру!!!')
        is_finished = True

    for block in blocks:
        if hero.colliderect(block):
            g_y = 0
            v_y = 0
            v_x = 0
            hero.y = block.y - hero.h

    pygame.display.update()
