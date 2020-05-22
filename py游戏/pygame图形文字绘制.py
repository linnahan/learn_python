import pygame,sys
from math import pi
import pygame.freetype


pygame.init()
screen = pygame.display.set_mode((600,400))
pygame.display.set_caption('Pygame图形文字绘制')
GOLD = 255,215,0
RED = pygame.Color('red')
WHITE = 255,255,255
GREEN = pygame.Color('green')

#r1rect = pygame.draw.rect(screen,GOLD,(100,100,200,100),0)
#r2rect = pygame.draw.rect(screen,RED,(210,210,200,100),5)

e1rect = pygame.draw.ellipse(screen, GREEN, (50,50,500,300), 3)
c1rect = pygame.draw.circle(screen, GOLD, (200,180), 30, 5)
c2rect = pygame.draw.circle(screen, GOLD, (400,180), 30)
r1rect = pygame.draw.rect(screen, RED, (170,130,60,10), 3)
r2rect = pygame.draw.rect(screen, RED, (370,130,60,10))
plist = [(295,170),(285,250),(260,280),(340,280),(315,250),(305,170)]
l1rect = pygame.draw.lines(screen, GOLD, True, plist, 2)
a1rect = pygame.draw.arc(screen, RED, (200,220,200,100), 1.4*pi, 1.9*pi, 3)

ft = pygame.freetype.Font('C://windows//Fonts//msyh.ttc',36)
f1rect = ft.render_to(screen,(0,0),'眯眼笑',fgcolor=GOLD,size=50)   #返回rect
f2surf, f2rect = ft.render('haa~',fgcolor=GOLD,size=50)        #返回绘制的绘图层surf和图形rect

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    screen.blit(f2surf,(480,0))
    pygame.display.update()