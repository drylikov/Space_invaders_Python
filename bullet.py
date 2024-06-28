import pygame

class Bullet(pygame.sprite.Sprite):

    def __init__(self, screen, ship):
        # bullet initialization with ship
        super(Bullet, self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, 4, 12)
        self.color = 255, 99, 71
        self.speed = 1.5
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        self.y = float(self.rect.y)

    def update(self):
        # bullet move
        self.y -= self.speed
        self.rect.y = self.y

    def bullet_render(self, ):
        # bullet rendering
        pygame.draw.rect(self.screen, self.color, self.rect)