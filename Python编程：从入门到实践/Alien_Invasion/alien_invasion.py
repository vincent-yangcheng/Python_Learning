import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from alien import Alien

def run_game():
    #初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    #设置背景色
    bg_color = (230, 230, 230)

    #创建一艘飞船
    ship = Ship(ai_settings, screen)

    #创建一个用于存储子弹的编组
    bullets = Group()

    #创建一群外星人
    aliens = Group()


    gf.create_fleet(ai_settings, screen, aliens)


    #开始游戏的主循环
    while True:

        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
        gf.update_aliens(ai_settings, aliens)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)
        #gf.create_fleet(ai_settings, screen, aliens)


        #删除已经消失的子弹
        #for bullet in bullets.copy():
        #   if bullet.rect.bottom <= 0:
        #       bullets.remove(bullet)
        print(len(bullets))


        #gf.update_screen(ai_settings, screen, ship, bullets)
        
        #每次循环时都重绘屏幕
       # screen.fill(ai_settings.bg_color)
       # ship.blitme()
        
        #让最近绘制的屏幕可见
        #pygame.display.flip()

run_game()
