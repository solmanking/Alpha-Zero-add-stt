# -*- coding: utf-8 -*-
"""
human VS AI models
Input your move in the format: 2,3

@author: Junxiao Song
"""

from __future__ import print_function
import pickle
from game import Board, Game
from mcts_pure import MCTSPlayer as MCTS_Pure
from mcts_alphaZero import MCTSPlayer
from policy_value_net_numpy import PolicyValueNetNumpy

from Reconition import soundGet
from Reconition import soundStart

from Write_txt import write
from Write_txt import cleanNote

#import GUI as gui


#from anotherTestMap import VisBoard

#from  Arduino_Trasform import sendData   #Arduino 呼叫

# from policy_value_net import PolicyValueNet  # Theano and Lasagne
# from policy_value_net_pytorch import PolicyValueNet  # Pytorch
# from policy_value_net_tensorflow import PolicyValueNet # Tensorflow
# from policy_value_net_keras import PolicyValueNet  # Keras




class Human(object):
    """
    human player 人玩家的操作方面
    """

    def __init__(self): #程式執行後馬上執行的
        self.player = None

    def set_player_ind(self, p):
        self.player = p

        self.errorcount=3

    def get_action(self, board):
        try:
            if(self.errorcount>0):
                location = soundGet()#設location=輸入的值  這裡改語音輸入
            else:
                location = input("開啟手動輸入: ")#失敗三次轉手動

            if isinstance(location, str):  # for python3 #如果lacation屬性是string
                location = [int(n, 10) for n in location.split(",")]#將字串轉成[x,y]
            print("location[x,y]是")
            print(location)


            move = board.location_to_move(location) #move為用location[x,y]引到game得到x*8+y的值
            print("move x*8+y =")
            print(move)#確認move的值

            #sendData(move)          #傳給Arduino值
            print(type(move))

            #write(move)
            write(move)
            self.errorcount=3



        except Exception as e:
            move = -1
        if move == -1 or move not in board.availables: #move=-1或不在(7，7)之內的話重來
            print("invalid move")
            self.errorcount-=1
            move = self.get_action(board) #輸出重來
        #write(move)
        return move   ##回傳move值

    def __str__(self):
        return "Human {}".format(self.player)  #看不懂 先擱著


class start(object):
        #####程式居然從這邊開始......
    def run(EndorStart):
        if(EndorStart==1):
            n = 5
            width, height = 8, 8
            model_file = 'best_policy_8_8_5.model'
            try:
                board = Board(width=width, height=height, n_in_row=n)  #建立game,class Board的實體
                #print(board.width)
                game = Game(board)  #建立game.class Game實體


                # ############### human VS AI ###################
                # load the trained policy_value_net in either Theano/Lasagne, PyTorch or TensorFlow

                # best_policy = PolicyValueNet(width, height, model_file = model_file)
                # mcts_player = MCTSPlayer(best_policy.policy_value_fn, c_puct=5, n_playout=400)

                # load the provided model (trained in Theano/Lasagne) into a MCTS player written in pure numpy
                try:
                    policy_param = pickle.load(open(model_file, 'rb'))
                except:
                    policy_param = pickle.load(open(model_file, 'rb'),
                                               encoding='bytes')  # To support python3
                best_policy = PolicyValueNetNumpy(width, height, policy_param)
                mcts_player = MCTSPlayer(best_policy.policy_value_fn,
                                         c_puct=5,
                                         n_playout=400)  # set larger n_playout for better performance

                # uncomment the following line to play with pure MCTS (it's much weaker even with a larger n_playout)
                # mcts_player = MCTS_Pure(c_puct=5, n_playout=1000)

                # human player, input your move in the format: 2,3

                human = Human()




                # set start_player=0 for human first
                game.start_play(human, mcts_player, start_player=0, is_shown=1)#mcts_player  human

                #gui.tink().window()

                '''
                re =input('again? input R')
                print(re)
                print(type(re))
                Retry(re)
                '''



            except KeyboardInterrupt:
                print('\n\rquit')




if __name__ == '__main__':       #主動建立start class 要回復把class start刪除 並把此式 除了 start.run(1)以外回復 1是開始 2是結束
    #run()
    cleanNote() #清空上一局的紀錄
    #VisBoard.drawmap(1)

    def Retry(re):
         if (re == 'R'or'r'):
            print('在開始')
            start.run(1)
         else:
            print('謝謝遊玩')


    while True:
        x = soundStart()
        if (x == 1):
            start.run(1)
            break

