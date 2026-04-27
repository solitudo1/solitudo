import pygame
from .. import setup, tools
from .. import constants as C
from ..components import player, enemy, brick, coin, box


class Level:
    def __init__(self):
        self.screen = None
        self.next = 'game_over'
        self.done = False
        self.sound_manager = None
        self.persist = {}
        self.finished = False
        self.viewport = setup.SCREEN.get_rect()
        
        # 游戏对象组
        self.player_group = None
        self.enemy_group = None
        self.brick_group = None
        self.coin_group = None
        self.box_group = None
        self.all_sprites = None
        
        # 游戏状态
        self.game_info = None
        self.player = None
        self.camera_x = 0
        
        # UI
        self.info_bar = None
        
    def startup(self, current_time, persist):
        """启动关卡"""
        self.start_time = current_time
        self.persist = persist
        self.game_info = persist
        self.finished = False
        self.setup_background()
        self.setup_level_components()
        
    def setup_background(self):
        """设置背景"""
        self.background = pygame.Surface(C.SCREEN_SIZE)
        self.background.fill(C.BLUE)  # 天空蓝色
        
        # 添加一些云朵
        for i in range(5):
            x = (i * 200) % C.SCREEN_W
            y = 50 + (i * 20) % 100
            pygame.draw.ellipse(self.background, C.WHITE, (x, y, 100, 50))
        
        # 添加地面
        pygame.draw.rect(self.background, C.GREEN, (0, C.SCREEN_H - 50, C.SCREEN_W, 50))
        
    def setup_level_components(self):
        """设置关卡组件"""
        self.player = player.Player()
        self.player.rect.x = 100
        self.player.rect.y = C.SCREEN_H - 150
        self.player_group = pygame.sprite.Group(self.player)
        
        # 创建精灵组
        self.enemy_group = pygame.sprite.Group()
        self.brick_group = pygame.sprite.Group()
        self.coin_group = pygame.sprite.Group()
        self.box_group = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()
        
        # 将玩家加入所有精灵组
        self.all_sprites.add(self.player)
        
        # 创建一些敌人
        goomba1 = enemy.Goomba(400, C.SCREEN_H - 82)
        goomba2 = enemy.Goomba(600, C.SCREEN_H - 82)
        self.enemy_group.add(goomba1, goomba2)
        self.all_sprites.add(goomba1, goomba2)
        
        # 创建一些砖块
        for i in range(10):
            brick_obj = brick.Brick(300 + i * 32, C.SCREEN_H - 82, 'normal', C.BROWN)
            self.brick_group.add(brick_obj)
            self.all_sprites.add(brick_obj)
        
        # 创建一些金币
        for i in range(5):
            coin_obj = coin.Coin(250 + i * 100, 300)
            self.coin_group.add(coin_obj)
            self.all_sprites.add(coin_obj)
        
        # 创建一些问号箱
        box1 = box.Box(500, 300, 'coin')
        box2 = box.Box(700, 200, 'mushroom')
        self.box_group.add(box1, box2)
        self.all_sprites.add(box1, box2)
        
        # 设置地面
        self.ground_height = C.SCREEN_H - 50
        
    def cleanup(self):
        """清理关卡"""
        self.done = False
        self.persist = {
            'score': self.game_info.get('score', 0),
            'lives': self.game_info.get('lives', 3),
            'coins': self.game_info.get('coins', 0)
        }
        return self.persist
        
    def update(self, surface, keys, current_time):
        """更新关卡"""
        self.handle_events(keys)
        self.update_objects(current_time)
        self.check_collisions()
        self.draw(surface)
        
    def handle_events(self, keys):
        """处理游戏事件"""
        self.player.update(keys)
        
        # 更新其他游戏对象
        for enemy in self.enemy_group:
            enemy.update(self.game_info, self)
        for coin in self.coin_group:
            coin.update(self.game_info)
        for box in self.box_group:
            box.update(self.game_info)
        
    def update_objects(self, current_time):
        """更新游戏对象"""
        # 简单的相机跟随玩家
        if self.player.rect.x > C.SCREEN_W / 2:
            self.camera_x = self.player.rect.x - C.SCREEN_W / 2
        else:
            self.camera_x = 0
            
        # 限制相机不要超出关卡边界
        if self.camera_x < 0:
            self.camera_x = 0
    
    def check_collisions(self):
        """检查碰撞"""
        # 玩家与金币的碰撞
        coin_hits = pygame.sprite.spritecollide(self.player, self.coin_group, True)
        for coin in coin_hits:
            # 增加分数
            self.game_info['coins'] = self.game_info.get('coins', 0) + 1
            
        # 玩家与问号箱的碰撞
        box_hits = pygame.sprite.spritecollide(self.player, self.box_group, False)
        for box in box_hits:
            # 如果从下方撞击箱子
            if (self.player.v_y > 0 and 
                self.player.rect.bottom <= box.rect.top + 10 and 
                self.player.rect.bottom >= box.rect.top):
                box.open_box()
                # 给玩家奖励
                if box.box_content == 'coin':
                    self.game_info['coins'] = self.game_info.get('coins', 0) + 1
                elif box.box_content == 'mushroom':
                    self.player.transform_to_big()
                    
        # 玩家与敌人的碰撞
        enemy_hits = pygame.sprite.spritecollide(self.player, self.enemy_group, False)
        for enemy in enemy_hits:
            # 如果从上方踩到敌人
            if (self.player.v_y > 0 and 
                self.player.rect.bottom <= enemy.rect.top + 10 and 
                self.player.rect.bottom >= enemy.rect.top):
                self.enemy_group.remove(enemy)
                self.all_sprites.remove(enemy)
                self.player.v_y = C.JUMP_STRENGTH * 0.7  # 反弹
            else:
                # 玩家受伤
                pass
                
        # 检查玩家是否掉下地图
        if self.player.rect.top > C.SCREEN_H:
            self.done = True
            self.next = 'game_over'
        
    def draw(self, surface):
        """绘制关卡"""
        # 绘制背景
        surface.blit(self.background, (-self.camera_x % C.SCREEN_W, 0))
        surface.blit(self.background, (-(self.camera_x % C.SCREEN_W) + C.SCREEN_W, 0))
        
        # 绘制所有精灵（考虑相机偏移）
        for sprite in self.all_sprites:
            screen_pos = (sprite.rect.x - int(self.camera_x), sprite.rect.y)
            surface.blit(sprite.image, screen_pos)
        
        # 绘制UI信息
        self.draw_info(surface)
        
    def draw_info(self, surface):
        """绘制游戏信息"""
        font = pygame.font.Font(None, 36)
        
        # 分数
        score_text = font.render(f"Coins: {self.game_info.get('coins', 0)}", True, C.WHITE)
        surface.blit(score_text, (20, 20))
        
        # 生命值
        lives_text = font.render(f"Lives: {self.game_info.get('lives', 3)}", True, C.WHITE)
        surface.blit(lives_text, (20, 60))
        
        # 关卡
        level_text = font.render("Level: 1-1", True, C.WHITE)
        surface.blit(level_text, (20, 100))