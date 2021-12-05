import time
import serial



COM_PORT = 'COM3'  #指定通訊戶
BAUD_RATES =9600
ser = serial.Serial(COM_PORT, BAUD_RATES)


#class transtorm(object):
  #  def __init__(self):
   #     pass


def sendData(x):

       num=str(x)
       print("num type =")
       print(type(num))
       #print(type(x))
       ser.write(num.encode())
       print("成功傳入sendPos")




#x=input().lower()
#sendData(x)


'''
def postionTrans(x,y):
        #print("AD成功讀取")

        Pos=str(x*y-1)
        print(Pos)

        ArduinoPos=Pos.encode(encoding='utf-8')

        print(type(ArduinoPos))

        ser.write(ArduinoPos)

        print("成功")



if __name__ == ('__main__'):

    postionTrans(3,3)

'''