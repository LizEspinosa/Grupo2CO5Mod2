

import pygame
import os

# Global Constants
TITLE = "Spaceships Game"
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
FPS = 30
IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")

# Assets Constants
ICON = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship.png"))

SHIELD = pygame.image.load(os.path.join(IMG_DIR, 'Other/shield.png'))

BG = pygame.image.load(os.path.join(IMG_DIR, 'Other/Track.png'))

HEART = pygame.image.load(os.path.join(IMG_DIR, 'Other/SmallHeart.png'))

GAMEOVER = pygame.image.load(os.path.join(IMG_DIR, "Other/GameOver.png"))
POINTS = pygame.image.load(os.path.join(IMG_DIR, "Other/estrellas.png"))
INICIO = pygame.image.load(os.path.join(IMG_DIR, "Other/inicio.png"))
LASER_SOUND = pygame.mixer.Sound(os.path.join(IMG_DIR, "Other/laser.mp3"))
EXPLOSION = pygame.mixer.Sound(os.path.join(IMG_DIR, "Other/explosion.mp3"))
MUSIC = pygame.mixer.Sound(os.path.join(IMG_DIR, "Other/music.mp3"))
DEFAULT_TYPE = "default"
SHIELD_TYPE = 'shield'
POINTS_TYPE = 'points'

SPACESHIP = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship.png"))
SPACESHIP_SHIELD = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship_shield.png"))
BULLET = pygame.image.load(os.path.join(IMG_DIR, "Bullet/bullet_1.png"))

BULLET_ENEMY = pygame.image.load(os.path.join(IMG_DIR, "Bullet/bullet_2.png"))
ENEMY_1 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_1.png"))
ENEMY_2 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_2.png"))



FONT_STYLE = 'freesansbold.ttf'