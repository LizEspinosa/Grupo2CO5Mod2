


import random

import pygame
from game.components.power_ups.shield import Shield
from game.components.power_ups.points import Points

from game.utils.constants import SPACESHIP_SHIELD


class PowerUpManager:
    def __init__(self):
        self.points_ups = []
        self.power_ups = []
        self.duration = random.randint(3, 5)
        self.when_appears = random.randint(5000, 10000)

    def update(self, game):
        current_time = pygame.time.get_ticks()

        if len(self.power_ups) == 0 and current_time >= self.when_appears:
            self.generate_power_up(game)
            self.generate_points()

        for power_up in self.points_ups:
            power_up.update_points(game.game_speed, self.points_ups)
            if power_up.type == 'points':
                    game.score += 50
        
        for power_up in self.power_ups:
            power_up.update(game.game_speed, self.power_ups)

            if game.player.rect.colliderect(power_up.rect):
                power_up.start_time = pygame.time.get_ticks()
                #implementar en game y player
                game.player.power_up_type = power_up.type
                game.player.has_power_up = True
                game.player.power_time_up = power_up.start_time + (self.duration * 1000)
                game.player.set_image((65, 75), SPACESHIP_SHIELD)
                self.power_ups.remove(power_up)

    

    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)
        
        for power_up in self.points_ups:
            power_up.draw(screen)

    def generate_power_up(self, game):
        power_up = Shield()
        self.when_appears += random.randint(5000, 10000)
        self.power_ups.append(power_up)
    
    def generate_points(self):
        points_up = Points() 
        self.when_appears += random.randint(5000, 10000)
        self.points_ups.append(points_up)

    def reset(self):
        self.power_ups = [] 
        self.points_ups = []