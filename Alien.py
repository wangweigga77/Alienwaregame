import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """创建表示单个外星人的类"""
    def __init__(self, ai_game):
        """初始化外星人并设置其初始位置"""
        super().__init__()
        self.screen = ai_game.screen
        
        # 加载外星人图像并设置其rect属性
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # 设置外星人的初始位置在屏幕左上角附近
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # 精确保存外星人的x坐标
        self.alien_x = float(self.rect.x)
