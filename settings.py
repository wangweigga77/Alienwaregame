class Settings:
    """存储游戏《外星人入侵》中所有设置的类,将所有的设置都存储在一个地方,以免在代码中到处添加设置"""

    def __init__(self):
        """初始化游戏的设置"""
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (255,255,255)
        # 飞船的速度
        self.ship_speed = 1.5
        self.ship_limit = 3
        # 子弹的设置
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        # 设置飞船载弹量
        self.bullets_allowed = 8
        # 外星人的设置
        self.alien_speed = 10.0
        self.fleet_drop_speed = 10
        # fleet_direction为1表示右移，为-1表示左移
        self.fleet_direction = 1
