import sys
import pygame
from settings import Settings
from ship import Ship

class AlienInvasion:
    """管理游戏资源和行为的类"""

    def __init__(self):
        """初始化游戏并创建游戏资源"""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)

    def run_game(self):
        """开始游戏的主循环"""
        while True:
            #  监视键盘和鼠标事件
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            
            #  每次循环都重绘屏幕
            self.screen.fill(self.settings.bg_color)
            # 填充背景后，调用blitme()将飞船绘制在屏幕上，确保它出现在背景前面
            self.ship.blitme()

            #  让最后一次绘制的屏幕可见
            pygame.display.flip()

if __name__ == '__main__':
    #  创建游戏实例并运行游戏
    ai = AlienInvasion()
    ai.run_game()