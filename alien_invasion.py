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
            self._check_events()
            self.ship.update()
            self._update_screen()

    def _check_events(self):
        #  监视键盘和鼠标事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    # 右移标志为真
                    self.ship.moving_right = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    # 右移标志位假
                    self.ship.moving_right = False
            
    def _update_screen(self):
        #  填充主窗口背景色
        self.screen.fill(self.settings.bg_color)
        # 填充背景后，调用blitme()将飞船绘制在屏幕上，确保它出现在背景前面
        self.ship.blitme()
        # 将绘制的图像刷新在屏幕上
        pygame.display.flip()

if __name__ == '__main__':
    #  创建游戏实例并运行游戏
    ai = AlienInvasion()
    ai.run_game()