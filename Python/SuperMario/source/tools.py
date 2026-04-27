# 工具和游戏主控
import os
import pygame
import random

from . import constants as C
from .state import main_menu, level, load_screnn


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_mode(C.SCREEN_SIZE)
        self.screen = pygame.display.get_surface()
        self.clock = pygame.time.Clock()
        self.keys = pygame.key.get_pressed()
        self.running = True
        self.state_dict = {}
        self.state_name = None
        self.current_state = None
        self.setup_states()
        
    def setup_states(self):
        """设置游戏状态"""
        self.state_dict = {
            'main_menu': main_menu.MainMenu(),
            'level': level.Level(),
            'game_over': load_screnn.GameOver(),
            'victory': load_screnn.Victory()
        }
        self.state_name = 'main_menu'
        self.current_state = self.state_dict[self.state_name]
        self.current_state.startup(0.0, {'score': 0, 'lives': 3, 'coins': 0})
    
    def update(self):
        """更新游戏"""
        if self.current_state.done:
            self.flip_state()
        # 获取按键状态
        keys = pygame.key.get_pressed()
        self.current_state.update(self.screen, keys, pygame.time.get_ticks())
    
    def flip_state(self):
        """切换游戏状态"""
        previous, self.current_state = self.current_state, self.state_dict[self.current_state.next]
        previous.cleanup()
        self.state_name = self.current_state.next
        self.current_state.startup(pygame.time.get_ticks(), previous.persist)
    
    def run(self):
        """运行游戏主循环"""
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    break
                elif event.type == pygame.KEYDOWN:
                    self.keys = pygame.key.get_pressed()
                elif event.type == pygame.KEYUP:
                    self.keys = pygame.key.get_pressed()
                    
            if not self.running:
                break
                
            self.update()
            pygame.display.update()
            self.clock.tick(C.FPS)
            
        pygame.display.quit()


def load_graphics(path, accept=(".jpg", ".png", ".bmp", ".gif")):
    graphics = {}
    for pic in os.listdir(path):
        name, ext = os.path.splitext(pic)
        if ext.lower() not in accept:
            continue
        img = pygame.image.load(os.path.join(path, pic)).convert_alpha()
        graphics[name] = img
    return graphics


def get_image(sheet, x, y, width, height, colorkey, scale):
    image = pygame.Surface((width, height))
    image.blit(
        sheet, (0, 0), (x, y, width, height)
    )  # 0，0 代表画到哪个位置，x,y,w,h代表sheet里哪个区域要取出来
    image.set_colorkey(colorkey)
    image = pygame.transform.scale(image, (width * scale, height * scale))
    return image