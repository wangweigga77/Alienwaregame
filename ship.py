import pygame

class Ship:
    """管理飞船的类,负责管理大部分飞船的行为"""

    def __init__(self,ai_game):
        """初始化飞船并设置其初始位置"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # 加载飞船图像并获取其外接矩阵
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # 对于每搜新飞船，都将其放在屏幕底部的中央
        self.rect.midbottom = self.screen_rect.midbottom
        # 右移标志
        self.moving_right = False
        # 左移标志
        self.moving_left = False

    def update(self):
        """根据移动标志调整飞船的位置"""
        if self.moving_right == True:
            self.rect.x += 1
        if self.moving_left ==True:
            self.rect.x -= 1


    def blitme(self):
        """在制定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)