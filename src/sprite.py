import pygame


class Sprite:

    def __init__(self, x, y, filename):
        self.x = x
        self.y = y
        self.img = pygame.image.load(filename)
        self.w = self.img.get_width()
        self.h = self.img.get_height()

    def draw(self, win):
        win.blit(self.img, (self.x, self.y))

    def collide(self, sprite):
        mask = pygame.mask.from_surface(self.img)
        sprite_mask = pygame.mask.from_surface(sprite.img)

        offset = (self.x - sprite.x, self.y - sprite.y)

        return sprite_mask.overlap(mask, offset)
