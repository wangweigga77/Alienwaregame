# Alienwaregame 
Practicing a project.
Use python to program a Alienwaregame
Ok ,let's go!
项目开发技巧笔记：
在大型项目中，经常需要在添加新代码前重构既有代码。重构旨在简化既有代码的结构，使其更容易扩展。
辅助方法在类中执行任务，但并非是通过实例调用的。在Python中，辅助方法的名称以单个下划线打头。
2022-3-1日计划：
1、设置飞船移动速度，可在Settings()类中增加飞船移动速度设置ship.speed = 1.5,为浮点数类型，并要修改Ship()类中的飞船坐标移动和绘制方法
2、设置飞船移动的边界不超出游戏边界，在Ship()类中修改移动标志的测试中，增加边界检测条件
3、重构alien_invasion.py中的_checi_event()方法,将_check_KEYDOWN(event)和_check_KEYUP(event)方法独立出来两个新方法供调用；
4、在_check_KEYDOWN(event)方法中，新增检测按键Q，按下后出发sys.exit()退出游戏；
5、设置游戏全屏，在alien_invasion.py中，修改__init__()方法，修改初始化参数，并取全屏的宽高参数，并调用Sitting()方法进行全屏游戏
2022-3-4日计划：
1、创建子弹类的文件bullet.py，要批量控制子弹，则引入继承了模块pygame.sprite的Sprite()类-精灵类，可将游戏中的相关元素（即子弹）进行编组，
   进而同时操作编组中的所有元素；
2、在Bullet类中，使用pygame.Rect()类绘制表示子弹的矩形，并将其初始化到正确的位置
3、在Bulletl类中，将子弹的y坐标使用小数存储，一遍后续通过小数来控制游戏速度
4、在settings中增加子弹的设置，包括子弹的移动速度，宽、高、颜色
5、在模块bullet.py中，增加Bullet类的行为update()和draw_bullet(), update()更新管理子弹的位置，需要绘制子弹是时，调用draw_bullet()
