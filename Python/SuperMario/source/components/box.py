import pygame
from .. import setup, tools
from .. import constants as C


class Box(pygame.sprite.Sprite):
    def __init__(self, x, y, box_content='coin', is_used=False):
        super().__init__()
        self.x = x
        self.y = y
        self.box_content = box_content
        self.is_used = is_used
        self.animation_timer = 0
        self.animation_start_y = y
        self.animation = False
        self.animation_state = 0
        self.setup_sprite()
        
    def setup_sprite(self):
        """设置问号箱精灵"""
        self.image = pygame.Surface((32, 32))
        
        if not self.is_used:
            # 黄色箱子带问号
            self.image.fill((255, 192, 0))  # 黄色
            font = pygame.font.Font(None, 24)
            qmark = font.render("?", True, (150, 0, 0))  # 深红色问号
            text_rect = qmark.get_rect(center=(16, 16))
            self.image.blit(qmark, text_rect)
        else:
            # 已使用的灰色箱子
            self.image.fill((100, 100, 100))  # 灰色
            
        # 添加边框
        pygame.draw.rect(self.image, (100, 60, 0), (0, 0, 32, 32), 2)
        
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        
    def update(self, game_info, *args):
        """更新箱子状态"""
        if self.animation:
            self.animate_opening()
    
    def open_box(self):
        """打开箱子"""
        if not self.is_used:
            self.is_used = True
            self.animation = True
            self.setup_sprite()  # 更新图像为已使用状态
            self.animation_start_y = self.rect.y
    
    def animate_opening(self):
        """开箱动画"""
        self.animation_state += 1
        if self.animation_state < 10:
            self.rect.y = self.animation_start_y - 1
        elif self.animation_state < 20:
            self.rect.y = self.animation_start_y + 1
        else:
            self.animation = False
            self.animation_state = 0
            self.rect.y = self.animation_start_y