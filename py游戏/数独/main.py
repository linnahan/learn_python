import sys

import pygame
from pygame.color import THECOLORS as COLORS

from build import print_matrix, give_me_a_game, check

# 绘制背景部分，这里就是9*9的九宫格
def draw_background():
    # white background
    screen.fill(COLORS['white'])

    # draw game board
    pygame.draw.rect(screen, COLORS['black'], (0, 0, 150, 450), 2)
    pygame.draw.rect(screen, COLORS['black'], (150, 0, 150, 450), 2)
    pygame.draw.rect(screen, COLORS['black'], (300, 0, 150, 450), 2)

    pygame.draw.rect(screen, COLORS['black'], (0, 0, 450, 150), 2)
    pygame.draw.rect(screen, COLORS['black'], (0, 150, 450, 150), 2)
    pygame.draw.rect(screen, COLORS['black'], (0, 300, 450, 150), 2)

# 将用户选中的各自背景改为蓝色块表示选中
def draw_choose():
    pygame.draw.rect(screen, COLORS['blue'], (cur_j * 50 + 2, cur_i * 50 + 2, 50 - 5, 50 - 5), 0)

# 绘制九宫格中的数字，包括本来就有的，以及用户填入的，本来就在的用灰色，用户填入的如何合法则为绿色，否则为红色，是一种提示
def check_win(matrix_all, matrix):
    if matrix_all == matrix:
        return True
    return False

# 绘制最下方的当前空格子数量以及用户的操作数量
def check_color(matrix, i, j):
    _matrix = [[col for col in row] for row in matrix]
    _matrix[i][j] = 0
    if check(_matrix, i, j, matrix[i][j]):
        return COLORS['green']
    return COLORS['red']


def draw_number():
    for i in range(len(MATRIX)):
        for j in range(len(MATRIX[0])):
            _color = check_color(MATRIX, i, j) if (i, j) in BLANK_IJ else COLORS['gray']
            txt = font40.render(str(MATRIX[i][j] if MATRIX[i][j] not in [0, '0'] else ''), True, _color)
            x, y = j * 50+15 , i * 50+5
            screen.blit(txt, (x, y))


def draw_context():
    txt = font80.render('Blank:' + str(cur_blank_size) + '   Change:' + str(cur_change_size), True, COLORS['black'])
    x, y = 10, 900
    screen.blit(txt, (x, y))


if __name__ == "__main__":
    # init pygame
    pygame.init()

    # 设置字体

    font40 = pygame.font.SysFont('Times', 40)
    font80 = pygame.font.SysFont('Times', 80)

    # create screen 500*500
    SIZE = [450, 450]
    screen = pygame.display.set_mode(SIZE)

    # variable parameter
    cur_i, cur_j = 0, 0
#    cur_blank_size = int(sys.argv[1])
    cur_blank_size = 20
    cur_change_size = 0

    # matrix abount
    MATRIX_ANSWER, MATRIX, BLANK_IJ = give_me_a_game(blank_size=cur_blank_size)
    print(BLANK_IJ)
    print_matrix(MATRIX)

    # main loop
    # 主循环，负责监听鼠标键盘时间，以及刷新界面内容，以及检查是否赢得了游戏
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break
            elif event.type == pygame.MOUSEBUTTONDOWN:
                cur_j, cur_i = int(event.pos[0] / 50), int(event.pos[1] / 50)
            elif event.type == event.type == pygame.KEYUP:
                if chr(event.key) in ['1', '2', '3', '4', '5', '6', '7', '8', '9'] and (cur_i, cur_j) in BLANK_IJ:
                    MATRIX[cur_i][cur_j] = int(chr(event.key))
                    cur_blank_size = sum([1 if col == 0 or col == '0' else 0 for row in MATRIX for col in row])
                    cur_change_size += 1
        # background
        draw_background()
        # choose item
        draw_choose()
        # numbers
        draw_number()
        # point
        draw_context()
        # flip
        pygame.display.flip()

        # check win or not
        if check_win(MATRIX_ANSWER, MATRIX):
            print('You win, smarty ass!!!')
            break

    pygame.quit()