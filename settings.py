class Settings:
    """存储游戏《外星人入侵》中所有设置的类,将所有的设置都存储在一个地方,以免在代码中到处添加设置"""

    def __init__(self):
        """初始化游戏的设置"""
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)
        self.ship_speed = 1.5
