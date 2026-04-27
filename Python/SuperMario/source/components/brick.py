import pygame
from .. import setup, tools
from .. import constants as C


class Brick(pygame.sprite.Sprite):
    def __init__(self, x, y, brick_type='normal', color=C.BROWN):
        super().__init__()
        self.x = x
        self.y = y
        self.brick_type = brick_type
        self.color = color
        self.setup_sprite()
        
    def setup_sprite(self):
        """设置砖块精灵"""
        self.image = pygame.Surface((32, 32))
        self.image.fill(self.color)
        
        # 添加砖块纹理效果
        pygame.draw.rect(self.image, (self.color[0]-30, self.color[1]-30, self.color[2]-30), (0, 0, 32, 32), 2)
        
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        
    def update(self, game_info, *args):
        """更新砖块状态"""
        # 砖块通常不需要更新，除非有特殊行为
        pass