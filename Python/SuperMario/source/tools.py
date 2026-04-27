# 工具和游戏主控
import os
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
