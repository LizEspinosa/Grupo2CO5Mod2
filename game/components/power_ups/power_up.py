import random
from pygame.sprite import Sprite 
import pygame

from game.utils.constants import SCREEN_HEIGHT, SCREEN_WIDTH
class PowerUp(Sprite):
    def __init__(self, image, type):

        self.image = pygame.transform.scale(image, (40, 40))
        self.type = type
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(120, SCREEN_WIDTH - 120)
        self.rect.y = 0
        self.start_time = 0

    def update(self, game_speed, power_ups):
        self.rect.y += game_speed
        if self.rect.y > SCREEN_HEIGHT:
            power_ups.remove(self)

    def update_points(self, game_speed, points_ups):
        self.rect.y += game_speed
        if self.rect.y > SCREEN_HEIGHT:
            points_ups.remove(self)

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    