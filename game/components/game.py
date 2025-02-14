import pygame 
import pygame.mixer
pygame.mixer.init()
from game.components.bullets.bullet_manager import BulletManager
from game.components.enemies.enemy_manager import EnemyManager
from game.components.menu import Menu
from game.components.power_ups.power_up_manager import PowerUpManager

from game.utils.constants import BG, FONT_STYLE, ICON, LASER_SOUND, GAMEOVER, INICIO, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, DEFAULT_TYPE
from game.components.spaceship import Spaceship

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        pygame.display.set_icon(GAMEOVER)
        pygame.display.set_icon(INICIO)
        
        
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.running = False
        self.game_speed = 10
        self.x_pos_bg = 0
        self.y_pos_bg = 0
        self.player = Spaceship()
        self.enemy_manager = EnemyManager()
        self.bullet_manager = BulletManager()
        self.power_up_manager = PowerUpManager()
        self.death_count = 0
        self.score = 0

        self.menu = Menu ('Press Any Key to start...', self.screen)
    
    def execute (self):
        self.running = True
        while self.running:
            if not self.playing:
                self.show_menu()
                #implementar
        pygame.display.quit()
        pygame.quit()

    def run(self):
        # Game loop: events - update - draw
        self.score = 0
        self.bullet_manager.reset()  #implementar
        self.enemy_manager.reset() #implementar
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input, self)
        self.enemy_manager.update(self)
        self.bullet_manager.update(self)
        self.power_up_manager.update(self)

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.player.draw(self.screen)
        self.enemy_manager.draw(self.screen)
        self.bullet_manager.draw(self.screen)
        self.menu.draw_score(self)
        self.power_up_manager.draw(self.screen)
        self.draw_power_up_time()
        pygame.display.update()
        #pygame.display.flip()

    def draw_background(self):
        image = pygame.transform.scale(BG, (SCREEN_WIDTH, SCREEN_HEIGHT))
        image_height = image.get_height()
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
        
        if self.y_pos_bg >= SCREEN_HEIGHT:
            self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
            self.y_pos_bg = 0
            
        self.y_pos_bg += self.game_speed

    def show_menu(self):
        half_screen_width = SCREEN_WIDTH // 2
        half_screen_height = SCREEN_HEIGHT //2

        self.menu.reset_screen_color(self.screen)
        inicio = pygame.transform.scale (INICIO, (1100,600))
        self.screen.blit(inicio, (half_screen_width -550, half_screen_height -300))
            

        if self.death_count >0:
            self.menu.update_message("PRESS ANY KEY TO CONTINUE")
         
            gameover = pygame.transform.scale (GAMEOVER, (1100,600))
            self.screen.blit(gameover, (half_screen_width -550, half_screen_height -300))
            self.menu.draw_score(self, (255, 255, 255))
            self.menu.draw_deaths(self)

            
           
            icon = pygame.transform.scale (ICON, (80,120))
            self.screen.blit(icon, (half_screen_width - 50, half_screen_height -260))
       
        

        self.menu.draw(self.screen)
        self.menu.update(self)
        
    def update_score(self):
        self.score += 1
    
    def draw_score(self):
        font = pygame.font.Font(FONT_STYLE, 30)
        text = font.render(f'Score: {self.score}', True, (255,255,255))
        text_rect = text.get_rect()
        text_rect.center = (100, 100)
        self.screen.blit(text, text_rect)
        
        
    def draw_power_up_time(self):
        if self.player.has_power_up:
            time_to_show = round((self.player.power_time_up - pygame.time.get_ticks())/1000, 2)

            if time_to_show >=0:
                font = pygame.font.Font(FONT_STYLE, 30)
                text = font.render(f'{self.player.power_up_type.capitalize()} is enable for {time_to_show} seconds', True, (255,255,255))
                text_rect = text.get_rect()
                self.screen.blit(text,(540, 50))
            else:
                self.player_has_power_up = False
                self.player.power_up_type = DEFAULT_TYPE
                self.player.set_image()
