import pygame
from .. import setup, tools
from .. import constants as C


class LoadScreen:
    def __init__(self):
        self.screen = None
        self.next = None
        self.done = False
        self.sound_manager = None
        self.persist = {}
        self.finished = False
        self.viewport = setup.SCREEN.get_rect()
        
    def startup(self, current_time, persist):
        """启动加载屏幕"""
        self.start_time = current_time
        self.persist = persist
        self.finished = False
        
    def cleanup(self):
        """清理加载屏幕"""
        self.done = False
        return self.persist
        
    def update(self, surface, keys, current_time):
        """更新加载屏幕"""
        if current_time - self.start_time > 2000:  # 显示2秒
            self.done = True


class GameOver(LoadScreen):
    def __init__(self):
        super().__init__()
        self.next = 'main_menu'
        
    def startup(self, current_time, persist):
        """启动游戏结束画面"""
        self.start_time = current_time
        self.persist = persist
        self.finished = False
        self.game_over_image = self.make_game_over_image()
        
    def make_game_over_image(self):
        """创建游戏结束文字"""
        font = pygame.font.Font(None, 74)
        game_over_text = font.render('GAME OVER', True, C.WHITE)
        rect = game_over_text.get_rect(center=C.SCREEN_SIZE[0]//2, C.SCREEN_SIZE[1]//2)
        return (game_over_text, rect)
        
    def update(self, surface, keys, current_time):
        """更新游戏结束画面"""
        surface.fill(C.BLACK)
        surface.blit(*self.game_over_image)
        
        if current_time - self.start_time > 3000:  # 显示3秒
            self.done = True


class Victory(LoadScreen):
    def __init__(self):
        super().__init__()
        self.next = 'main_menu'
        
    def startup(self, current_time, persist):
        """启动胜利画面"""
        self.start_time = current_time
        self.persist = persist
        self.finished = False
        self.victory_image = self.make_victory_image()
        
    def make_victory_image(self):
        """创建胜利文字"""
        font = pygame.font.Font(None, 74)
        victory_text = font.render('YOU WIN!', True, C.YELLOW)
        rect = victory_text.get_rect(center=(C.SCREEN_SIZE[0]//2, C.SCREEN_SIZE[1]//2))
        return (victory_text, rect)
        
    def update(self, surface, keys, current_time):
        """更新胜利画面"""
        surface.fill(C.BLUE)
        surface.blit(*self.victory_image)
        
        if current_time - self.start_time > 3000:  # 显示3秒
            self.done = True