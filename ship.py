import pygame

class Ship:
    """管理飞船的类,负责管理大部分飞船的行为"""

    def __init__(self,ai_game):
        """初始化飞船并设置其初始位置"""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # 加载飞船图像并获取其外接矩阵
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # 对于每搜新飞船，都将其放在屏幕底部的中央
        self.rect.midbottom = self.screen_rect.midbottom

        # 使用一个浮点型属性存储self.rect的小数坐标
        self.ship_x = float(self.rect.x)

        # 右移标志
        self.moving_right = False
        # 左移标志
        self.moving_left = False

    def update(self):
        """根据移动标志调整飞船的位置"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.ship_x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.ship_x -= self.settings.ship_speed
        # 将存储飞船x小数坐标值赋给飞船方块的x坐标
        self.rect.x = self.ship_x
        
    def center_ship(self):
        """让飞船在屏幕底端居中"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.ship_x = float(self.rect.x)

    def blitme(self):
        """在制定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)