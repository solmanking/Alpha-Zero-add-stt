
import  random
import  pygame
pygame.init()


space =50
cell_size=40
cell_num=8
light_yellow = (247, 238, 214)  # 設定棋盤顏色
chess_arr = []

grid_size= cell_size * (cell_num-1)+space*2 #棋盤大小
screencaption = pygame.display.set_caption('FTR')
screen  = pygame.display.set_mode((grid_size,grid_size))


def chess(x):  # 得到座標後

    xi = (x - 1) / 8
    yi = (x - 1) % 8
    chess_arr.append(xi, yi)
    print("成功")

def Inputnum():


    x=input("輸入值")
    chess(x)


def gameStart():
    while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()


                screen.fill(light_yellow)
                for x in range(0,cell_size*cell_num,cell_size):
                    pygame.draw.line(screen,(200,200,200),(x+space,0+space),(x+space,cell_size*(cell_num-1)+space),1)
                for y in range(0,cell_size*cell_num,cell_size):
                    pygame.draw.line(screen,(200,200,200),(0+space,y+space),(cell_size*(cell_num-1)+space,y+space),1)

                for xi,yi in chess_arr:
                    pygame.draw.circle(screen,(205,205,205), [xi*cell_size+space,  yi*cell_size+space],16,16)
                    print("成功")
                pygame.display.update()


Inputnum()
gameStart()





'''

class Pobang(object):





  def __init__(self):
    self.space =50
    self.cell_size=40
    self.cell_num=8
    self.light_yellow = (247, 238, 214)  # 設定棋盤顏色
    self.chess_arr = []

    self.grid_size= self.cell_size * (self.cell_num-1)+self.space *2 #棋盤大小
    screencaption = pygame.display.set_caption('FTR')
    screen  = pygame.display.set_mode((self.grid_size,self.grid_size))

  def chess(self,x): #得到座標後

    xi=(x-1)/8
    yi=(x-1)%8
    self.chess_arr.append(xi,yi)


  def startgame(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()


        self.screen.fill(self.light_yellow)

        for x in range(0,self.cell_size*self.cell_num,self.cell_size):
            pygame.draw.line(self.screen,(200,200,200),(x+self.space,0+self.space),(x+self.space,self.cell_size*(self.cell_num-1)+self.space),1)
        for y in range(0,self.cell_size*self.cell_num,self.cell_size):
                pygame.draw.line(self.screen,(200,200,200),(0+self.space,y+self.space),(self.cell_size*(self.cell_num-1)+self.space,y+self.space),1)

        for xi,yi in self.chess_arr:
            pygame.draw.circle(self.screen,(205,205,205), [xi*self.cell_size+self.space,  yi*self.cell_size+self.space],16,16)

        pygame.display.update()



if __name__ == 'main':
    while(True):
        Pobang.startgame()
'''