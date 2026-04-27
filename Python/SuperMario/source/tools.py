# 工具和游戏主控
import pygame
import random

from . import constants as C


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_mode(C.SCREEN_SIZE)
        self.screen = pygame.display.get_surface()
        self.clock = pygame.time.Clock()
        self.keys = pygame.key.get_pressed()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.display.quit()
                    return
                elif event.type == pygame.KEYDOWN:
                    self.keys = pygame.key.get_pressed()
                elif event.type == pygame.KEYUP:
                    self.keys = pygame.key.get_pressed()
            self.screen.fill(
                (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            )
            pygame.display.update()
            self.clock.tick(60)
