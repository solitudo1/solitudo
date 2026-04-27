import pygame
from .. import setup, tools
from .. import constants as C


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, enemy_type, direction='left'):
        super().__init__()
        self.x = x
        self.y = y
        self.enemy_type = enemy_type
        self.direction = direction
        self.v_x = 1 if direction == 'right' else -1
        self.v_y = 0
        self.gravity = C.GRAVITY
        self.setup_sprites()
        
    def setup_sprites(self):
        """设置敌人精灵图像"""
        self.frames = []
        
        # 根据敌人类型设置不同的颜色
        if self.enemy_type == C.GOOMBA:
            color = C.BROWN
        else:
            color = C.GREEN
            
        # 创建简单图像作为占位符
        img = pygame.Surface((32, 32))
        img.fill(color)
        self.frames.append(img)
        
        self.frame_index = 0
        self.image = self.frames[self.frame_index]
        self.rect = pygame.Rect(self.x, self.y, 32, 32)
        self.state = 'walk'
        
    def update(self, game_info, level):
        """更新敌人状态"""
        self.handle_state()
        self.apply_gravity()
        self.rect.x += self.v_x
        self.rect.y += self.v_y
        
    def handle_state(self):
        """处理敌人状态"""
        if self.state == 'walk':
            self.v_x = 1 if self.direction == 'right' else -1
        elif self.state == 'fall':
            pass  # 下落状态由重力处理
            
    def apply_gravity(self):
        """应用重力"""
        if self.rect.y < C.SCREEN_H - 50 - self.rect.height:
            self.v_y += self.gravity
        else:
            self.v_y = 0
            self.rect.y = C.SCREEN_H - 50 - self.rect.height


class Goomba(Enemy):
    def __init__(self, x, y, direction='left'):
        super().__init__(x, y, C.GOOMBA, direction)
        
    def setup_sprites(self):
        """设置Goomba图像"""
        # 创建棕色Goomba图像
        img = pygame.Surface((32, 32))
        img.fill(C.BROWN)
        # 添加眼睛
        pygame.draw.circle(img, C.WHITE, (10, 12), 5)
        pygame.draw.circle(img, C.BLACK, (10, 12), 2)
        pygame.draw.circle(img, C.WHITE, (22, 12), 5)
        pygame.draw.circle(img, C.BLACK, (22, 12), 2)
        self.frames = [img]
        self.frame_index = 0
        self.image = self.frames[self.frame_index]
        self.rect = pygame.Rect(self.x, self.y, 32, 32)
        self.state = 'walk'


class Koopa(Enemy):
    def __init__(self, x, y, direction='left'):
        super().__init__(x, y, C.KOOPA, direction)
        
    def setup_sprites(self):
        """设置Koopa图像"""
        # 创建绿色Koopa图像
        img = pygame.Surface((32, 48))
        img.fill(C.GREEN)
        # 添加壳的细节
        pygame.draw.rect(img, (0, 100, 0), (0, 0, 32, 48), 2)
        self.frames = [img]
        self.frame_index = 0
        self.image = self.frames[self.frame_index]
        self.rect = pygame.Rect(self.x, self.y, 32, 48)
        self.state = 'walk'