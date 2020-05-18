import pygame,sys   #引用


pygame.init()   #初始化
screen = pygame.display.set_mode((600,400))     #主图层
pygame.display.set_caption('Pygame游戏开始之旅')      #窗口标题

while True:    #循环
    for event in pygame.event.get():    #遍历循环事件队列
        if event.type == pygame.QUIT:    #控制退出
            sys.exit()
    pygame.display.update()     #窗口更新