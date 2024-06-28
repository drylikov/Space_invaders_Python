import pygame

class Ship():

    def __init__(self, screen):
        # gun initialization
        self.screen = screen
        self.image = pygame.image.load('images/ship_1.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.center = float(self.rect.centerx)
        self.rect.bottom = self.screen_rect.bottom
        self.mright = False
        self.mleft = False

    def render(self):
        # gun rendering
        self.screen.blit(self.image, self.rect)

    def ship_position(self):
        # update gun position on the screen
        if self.mright and self.rect.right < self.screen_rect.right:
            self.center += 0.5
        if self.mleft and self.rect.left > 0:
            self.center -= 0.5

        self.rect.centerx = self.center