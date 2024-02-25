import sys 
import pygame 
from pygame.sprite import Group
from button import Button
from alien import Alien
from ship import Ship
from settings import Settings
from game_stats import GameStats
import game_functions as gf
from scoreboard import Scoreboard 

def run_game(): 
    #Initialize game and create a screen object
    pygame.init()
    ai_settings=Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings,screen,stats)
    ship=Ship(ai_settings,screen)
    play_button = Button(ai_settings,screen,"Play")
    aliens = Group()
    bullets = Group()
    #Start the main loop for the game. 
    
    gf.create_fleet(ai_settings,screen,ship,aliens)
    music = pygame.mixer.music.load("music_and_sfx/alien_invasion.mp3")
    pygame.mixer.music.play(-1)
    # laser_sfx = 

    while True: 
        gf.check_events(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets)
        if stats.game_active: 
            ship.update()
            gf.update_bullets(ai_settings,screen,stats,sb,ship,aliens,bullets)
            gf.update_aliens(ai_settings,stats,sb,screen,ship,aliens,bullets)
    
        gf.update_screen(ai_settings,screen,stats,sb,ship,aliens,bullets,play_button) 

        

run_game()
