import pygame,sys       #引用
#import pygame.freetype


pygame.init()       #初始化
#print(pygame.display.Info())
#vInfo = pygame.display.Info()
#size = width, height = vInfo.current_w, vInfo.current_h
size = width, height = 600,400
screen = pygame.display.set_mode(size,pygame.NOFRAME)
speed = [1,1]
BLACK = 0,0,0
ball = pygame.image.load('PYG02-ball.gif')
ballrect = ball.get_rect()
icon = pygame.image.load('PYG03-flower.png')
pygame.display.set_icon(icon)
pygame.display.set_caption('碰撞壁球')
fps = 300
fclock = pygame.time.Clock()
still = False
bgColor = pygame.Color('black')

'''RED = pygame.Color('red')
font = pygame.freetype.Font('C://windows//Fonts//msyh.ttc')
w_ball, w_ballrect = font.render('ball',fgcolor=RED,size=50)'''

def RGBChannel(a):  #颜色通道错误处理
    return 0 if a < 0 else (255 if a > 255 else int(a))

while True:
    for event in pygame.event.get():       #获取事件并遍历
        if event.type == pygame.QUIT:       #退出
            sys.exit()
        elif event.type == pygame.KEYDOWN:      #键盘左右上下
            if event.key == pygame.K_LEFT:
                speed[0] = speed[0] if speed[0] == 0 else (abs(speed[0])-1)*int(speed[0]/abs(speed[0]))
            elif event.key == pygame.K_RIGHT:
                speed[0] = speed[0] + 1 if speed[0] >= 0 else speed[0] - 1
            elif event.key == pygame.K_UP:
                speed[1] = speed[1] + 1 if speed[1] >= 0 else speed[1] -1
            elif event.key == pygame.K_DOWN:
                speed[1] = speed[1] if speed[1] == 0 else (abs(speed[1])-1)*int(speed[1]/abs(speed[1]))
            #elif event.key == pygame.K_ESCAPE:
                #sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:      #鼠标点击
            if event.button == 1:
                still = True
        elif event.type == pygame.MOUSEBUTTONUP:       #鼠标松开
            still = False
            if event.button == 1:
                ballrect = ballrect.move(event.pos[0]-ballrect.centerx,\
                                         event.pos[1]-ballrect.centery)
        elif event.type == pygame.MOUSEMOTION:         #鼠标移动
            if event.buttons[0] == 1:
                ballrect = ballrect.move(event.pos[0]-ballrect.centerx,\
                                         event.pos[1]-ballrect.centery)
        elif event.type == pygame.VIDEORESIZE:         #窗口尺寸
            size = width, height = event.size[0], event.size[1]
            screen = pygame.display.set_mode(size, pygame.RESIZABLE)

    if pygame.display.get_active() and not still:     #判断是否活动bool值，即非最小化
        ballrect = ballrect.move(speed[0], speed[1])
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
        if ballrect.right > width and ballrect.right + speed[0] > width:
            speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]
        if ballrect.bottom > height and ballrect.bottom + speed[1] > height:
            speed[1] = -speed[1]

    #颜色通道
    bgColor.r = RGBChannel((ballrect.left+ballrect.right)/2*255/width)
    bgColor.g = RGBChannel((ballrect.top+ballrect.bottom)/2*255/height)
    bgColor.b = RGBChannel(min(speed[0],speed[1])*255/max(speed[0],speed[1])*255)

    screen.fill(bgColor)
    screen.blit(ball,ballrect)      #ball图层汇总到主图层的rect区域
    pygame.display.update()     #刷新屏幕
    fclock.tick(fps)    #控制帧速度，即窗口刷新速度