import pygame
from .. import setup, tools
from .. import constants as C


class Player(pygame.sprite.Sprite):
    def __init__(self, name='mario'):
        super().__init__()
        self.name = name
        self.setup_states()
        self.setup_images()
        self.setup_rectangle()
        self.v_x = 0  # 水平速度
        self.v_y = 0  # 垂直速度
        self.direction = 'right'  # 方向
        self.is_jumping = False
        self.is_crouching = False
        self.on_ground = False
        self.can_jump = True
        
    def setup_states(self):
        """设置玩家状态"""
        self.small_state = True
        self.big_state = False
        self.fire_state = False
        self.invincible = False
        
    def setup_images(self):
        """加载玩家图片"""
        self.frames = []
        # 创建一个简单的矩形图像作为占位符
        # 在实际游戏中这里应该从精灵表中加载图像
        img = pygame.Surface((32, 32))
        img.fill(C.RED)
        self.frames.append(img)
        
        img = pygame.Surface((32, 64))
        img.fill(C.RED)
        self.big_frames = [img]
        
        self.frame_index = 0
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect()
        
    def setup_rectangle(self):
        """设置玩家碰撞矩形"""
        self.rect = self.image.get_rect()
        
    def update(self, keys):
        """更新玩家状态"""
        self.handle_keys(keys)
        self.apply_gravity()
        self.check_bounds()
        
        # 更新图像根据大小状态
        if self.big_state:
            self.image = self.big_frames[self.frame_index]
            self.rect = self.image.get_rect(center=self.rect.center)
        else:
            self.image = self.frames[self.frame_index]
            
    def handle_keys(self, keys):
        """处理按键输入"""
        if keys[pygame.K_LEFT]:
            self.v_x = -C.PLAYER_SPEED
            self.direction = 'left'
        elif keys[pygame.K_RIGHT]:
            self.v_x = C.PLAYER_SPEED
            self.direction = 'right'
        else:
            self.v_x = 0
            
        if keys[pygame.K_SPACE] and self.on_ground and self.can_jump:
            self.jump()
            
    def jump(self):
        """跳跃动作"""
        self.v_y = C.JUMP_STRENGTH
        self.is_jumping = True
        self.on_ground = False
        self.can_jump = False
        
    def apply_gravity(self):
        """应用重力"""
        if not self.on_ground:
            self.v_y += C.GRAVITY
        else:
            self.can_jump = True  # 可以再次跳跃
            
        # 更新位置
        self.rect.x += self.v_x
        self.rect.y += self.v_y
        
        # 检查是否着陆
        if self.rect.bottom >= C.SCREEN_H - 50:  # 假设地面高度
            self.rect.bottom = C.SCREEN_H - 50
            self.v_y = 0
            self.on_ground = True
            self.is_jumping = False
            
    def check_bounds(self):
        """检查边界"""
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > C.SCREEN_W:
            self.rect.right = C.SCREEN_W
            
    def transform_to_big(self):
        """变大"""
        self.small_state = False
        self.big_state = True
        
    def transform_to_fire(self):
        """获得火焰能力"""
        if self.big_state:
            self.fire_state = True