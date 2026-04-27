import pygame
from .. import setup, tools
from .. import constants as C


class MainMenu:
    def __init__(self):
        self.screen = None
        self.next = 'level'
        self.done = False
        self.sound_manager = None
        self.persist = {}
        self.finished = False
        self.viewport = setup.SCREEN.get_rect()
        self.setup_main_menu_items()
        
    def setup_main_menu_items(self):
        """设置主菜单项"""
        self.title_font = pygame.font.Font(None, 74)
        self.button_font = pygame.font.Font(None, 48)
        
        # 标题
        self.title_label = self.title_font.render('SUPER MARIO', True, C.YELLOW)
        self.title_rect = self.title_label.get_rect(center=(C.SCREEN_W//2, C.SCREEN_H//4))
        
        # 开始按钮
        self.start_label = self.button_font.render('START GAME', True, C.WHITE)
        self.start_rect = self.start_label.get_rect(center=(C.SCREEN_W//2, C.SCREEN_H//2))
        
        # 退出按钮
        self.quit_label = self.button_font.render('QUIT', True, C.WHITE)
        self.quit_rect = self.quit_label.get_rect(center=(C.SCREEN_W//2, C.SCREEN_H//2 + 60))
        
        # 选择项
        self.selected_option = 0
        self.options = [self.start_rect, self.quit_rect]
        
    def startup(self, current_time, persist):
        """启动主菜单"""
        self.start_time = current_time
        self.persist = persist
        self.finished = False
        
    def cleanup(self):
        """清理主菜单"""
        self.done = False
        return self.persist
        
    def update(self, surface, keys, current_time):
        """更新主菜单"""
        self.handle_events(keys)
        self.draw(surface)
        
    def handle_events(self, keys):
        """处理菜单事件"""
        if keys[pygame.K_UP]:
            self.selected_option = (self.selected_option - 1) % len(self.options)
        elif keys[pygame.K_DOWN]:
            self.selected_option = (self.selected_option + 1) % len(self.options)
        elif keys[pygame.K_RETURN]:
            if self.selected_option == 0:  # 开始游戏
                self.done = True
            elif self.selected_option == 1:  # 退出游戏
                pygame.quit()
                
    def draw(self, surface):
        """绘制主菜单"""
        surface.fill(C.BLACK)
        
        # 绘制标题
        surface.blit(self.title_label, self.title_rect)
        
        # 绘制选项并高亮选中项
        for i, option in enumerate(self.options):
            if i == self.selected_option:
                # 高亮选中的选项
                highlight = pygame.Surface((option.width + 20, option.height + 10))
                highlight.set_alpha(128)
                highlight.fill(C.BLUE)
                surface.blit(highlight, (option.x - 10, option.y - 5))
                
            if i == 0:
                surface.blit(self.start_label, self.start_rect)
            else:
                surface.blit(self.quit_label, self.quit_rect)
                
        # 提示控制
        hint_font = pygame.font.Font(None, 24)
        hint = hint_font.render('Use UP/DOWN to select, ENTER to confirm', True, C.WHITE)
        hint_rect = hint.get_rect(center=(C.SCREEN_W//2, C.SCREEN_H - 50))
        surface.blit(hint, hint_rect)