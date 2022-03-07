import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien

class AlienInvasion:
    """管理游戏资源和行为的类"""

    def __init__(self):
        """初始化游戏并创建游戏资源"""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self._create_fleet()

    def _create_fleet(self):
        """创建外星人群组"""
        # 创建一个外星人，然后计算一行可以容纳多少个外星人
        # 外星人的间距等于一个外星人宽度
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)
        
        # 计算屏幕可容纳多少行外星人
        ship_height = self.ship.rect.height
        available_space_y = self.settings.screen_height - (8 * alien_height) - ship_height
        number_rows = available_space_y // (2 * alien_height)

        # 创建外星人矩阵
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)

    def _create_alien(self, alien_number, row_number):
            """创建第alien_number个外星人"""
            alien = Alien(self)
            alien_width, alien_height = alien.rect.size
            self.alien_x = alien_width + (2 * alien_width * alien_number)
            alien.rect.x = self.alien_x
            self.alien_y = alien_height + (2 * alien_height * row_number)
            alien.rect.y = self.alien_y
            self.aliens.add(alien)

    def run_game(self):
        """开始游戏的主循环"""
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_screen()

    def _check_events(self):
        """实时监听鼠标和键盘的事件"""
        #  实时监测键盘和鼠标事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # 监听退出事件
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                # 监听安键事件
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                # 监听松键事件
                self._check_keyup_events(event)

    def _check_keydown_events(self,event):
        """按键事件响应"""
        if event.key == pygame.K_RIGHT:
           # 右移标签为真
           self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            # 左移标签为真
            self.ship.moving_left = True  
        elif event.key == pygame.K_q:
            # 退出游戏
            sys.exit()
        elif event.key == pygame.K_SPACE:
            # 调用辅助方法_fire_bullet()发射子弹
            self._fire_bullet()

    def _fire_bullet(self):
        """创建一颗子弹,并将其加入编组bullets中"""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _check_keyup_events(self, event):
        """松键事件响应"""
        if event.key == pygame.K_RIGHT:
            # 右移标签为假
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            #  左移标签为假
            self.ship.moving_left = False

    def _update_bullets(self):
        """更新子弹位置,并将超出屏幕的子弹删除"""
        # 对编组调用update()时，编组自动其中的每个精灵调用bullet.update()
        self.bullets.update()
        # 删除消失的子弹,因为for循环遍历列表时，Python要求该列表的长度在整个循环中保持不变，
        # 所以不能从for循环遍历的列表中删除元素，所以必须遍历编组的副本。
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
                        
    def _update_screen(self):
        """更新屏幕绘制的内容并刷新在屏幕上"""
        # 填充主窗口背景色
        self.screen.fill(self.settings.bg_color)
        # 填充背景后，调用blitme()将飞船绘制在屏幕上，确保它出现在背景前面
        self.ship.blitme()
        # 通过迭代将bullets.sprites()列表中的所有精灵绘制到屏幕上
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        # 向外星人编组调用draw()时，Pygame将把编组中的每个元素会知道属性rect指定的位置
        # 方法draw()接受一个参数，参数指定将编组中的元素绘制到那个surface上
        self.aliens.draw(self.screen)

        # 将绘制的图像刷新在屏幕上
        pygame.display.flip()

if __name__ == '__main__':
    #  创建游戏实例并运行游戏
    ai = AlienInvasion()
    ai.run_game()