import pygame
from .. import setup, tools
from .. import constants as C


class Coin(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.animation_timer = 0
        self.animation_frames = 4  # 动画帧数
        self.setup_sprite()
        
    def setup_sprite(self):
        """设置金币精灵"""
        # 创建一个简单的金币图像
        self.image = pygame.Surface((16, 16))
        self.image.fill(C.YELLOW)
        pygame.draw.circle(self.image, (255, 215, 0), (8, 8), 8)
        # 添加一些细节
        pygame.draw.circle(self.image, C.YELLOW, (8, 8), 5)
        pygame.draw.circle(self.image, (255, 215, 0), (8, 8), 3)
        
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        self.start_y = self.y
        self.bounce_height = 10
        self.original_pos = (self.x, self.y)
        
    def update(self, game_info, *args):
        """更新金币动画"""
        # 简单的上下浮动效果
        self.animation_timer += 1
        offset = abs((self.animation_timer % 40) - 20) / 2  # 产生上下浮动效果
        self.rect.y = self.start_y - offset