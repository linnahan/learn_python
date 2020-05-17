import pygame,sys


pygame.init()
screen = pygame.display.set_mode((600,400))
pygame.display.set_caption('Pygame探索')

'''探索事件'''
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            print('[KEYDOWN]',event.unicode,event.key,event.mod)    #键盘
        elif event.type == pygame.MOUSEMOTION:
            print('[MOUSEMOTTON]',event.pos,event.rel,event.buttons)    #窗口坐标，相对坐标，鼠标点击
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print('[MOUSEBUTTONDOWN]',event.button,event.pos)        #点击鼠标

    pygame.display.update()