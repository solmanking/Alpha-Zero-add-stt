import pygame
from rtsMap import *
import sys


class VisBoard(object):

    def __init__(self):
        pass

    def drawmap(self):

        pygame.init()
        screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])# 設定銀幕大小
        pygame.display.set_caption("gobang")
        light_yellow = (247, 238, 214)  # 設定棋盤顏色
        map=Map(CHESS_LEN,CHESS_LEN) #設定 線條長度
       # map.drawChess(screen)  # 旗子

       # map.reset()
        pygame.draw.rect(screen, light_yellow, pygame.Rect(0, 0, MAP_WIDTH, SCREEN_HEIGHT))  # 繪製正方形
        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(MAP_WIDTH, 0, INFO_WIDTH, SCREEN_HEIGHT))  # 繪製白色背景
        map.drawBackground(screen)  # 畫棋盤線條
        map.drawChess(screen)  # 旗子

        while True:

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()




def input(self):

    x=3
    y=2
    Map.getMapUnitRect(x,y)


if __name__=='__main__':
    VisBoard.drawmap(1)
    input()
