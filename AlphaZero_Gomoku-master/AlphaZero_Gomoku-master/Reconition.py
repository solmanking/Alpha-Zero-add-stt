import time

import speech_recognition as sr
from gtts import gTTS
import os



r = sr.Recognizer()


def __init__(self):
    pass

def soundGet():


    soundPos(0,0)

    with sr.Microphone() as source:

        r.adjust_for_ambient_noise(source)     #去噪函數
        audio = r.listen(source,timeout=15)     #十五秒內說話
        StopSound()

    try:

        print("Result: \n" + r.recognize_google(audio, language='zh-TW'))
        result = r.recognize_google(audio, language='zh-TW')  # zh-TW
        # https://cloud.google.com/speech-to-text/docs/languages  網址到語言轉換網頁
        # Tresult = result.encode('UTF-8')
        # print(Tresult.isdigit())  #印出RESULT字串是否皆為純數
        # print(type(Tresult))
        # print(type(result))
        try:

            if isinstance(result, str):  # for python3 #如果lacation屬性是string
                print("成功讀取")

                result2 = [int(n, 10) for n in result.split(",")]  # 將字串轉成[x,y]
                # print(result2)
                print(type(result2))
                # print(len(result2))
                tresult = result[1] + "," + result[0]
                print("等待")
                time.sleep(3)
                print(tresult)
                result2.clear()


                return tresult
        except OverflowError:
            print("沒有讀取")

    except sr.UnknownValueError:
        print('輸入錯誤 請在一次')
    except sr.RequestError:
        print('輸入問題錯誤')


#s=soundGet()
#print(s)


def soundGetEN():
    #soundPos(0, 0)

    with sr.Microphone() as source:

        r.adjust_for_ambient_noise(source)  # 去噪函數
        audio = r.listen(source, timeout=15)  # 十五秒內說話

    try:

        print("Result: \n" + r.recognize_google(audio, language='en-US'))
        result = r.recognize_google(audio, language='en-US')  # zh-TW
        # https://cloud.google.com/speech-to-text/docs/languages  網址到語言轉換網頁
        # Tresult = result.encode('UTF-8')
        # print(Tresult.isdigit())  #印出RESULT字串是否皆為純數
        # print(type(Tresult))
        # print(type(result))
        #Readysound()
    except sr.UnknownValueError:
        Readysound()
        print('輸入錯誤 請在一次')
    except sr.RequestError:
        Readysound()
        print('輸入問題錯誤')


#s= soundGetEN()#試用英文語音
#print(s)


def inputsound():
    '''
    reportinput = gTTS(text="失敗三次,請等待人工輸入", lang='zh-TW')
    reportinput.save("ok.mp3")
    os.system("reportinput.mp3")
    '''
    os.system("threeerror.wav")
    print("開始人工輸入")



def Readysound():
    os.system("Error.mp3")


def StopSound():
    os.system("Stop.mp3")


#Readysound()

def soundPos(x,y):
    if(x==0 & y==0):
        '''
        print('接收位置')
        tts = gTTS(text='請輸入位置', lang='zh-TW')
        tts.save("ask.mp3")
        os.system("ask.mp3")
        '''

        print('接收位置')
        os.system("inputPls.wav")
        time.sleep(1)


def reportwork():
    reportwork = gTTS(text="輸入失敗",lang='zh-TW')
    reportwork.save("reportwork.mp3")
    os.system("reportwork.mp3")
    print("讀取語音成功")


def reportPos(move):

        pos='X'+str(move%8)+'Y'+str(move//8)
        print(move)

        time.sleep(3)

        report= gTTS(text=pos,lang='zh-TW')
        report.save("report.mp3")
        os.system("report.mp3")
        print("回報位置")

        time.sleep(2)


def reportAIPos(move):
    pos ='AI的'+'X'+ str(move % 8) + 'Y' + str(move // 8)
    print(move)
    report = gTTS(text=pos, lang='zh-TW')
    report.save("report.mp3")
    os.system("report.mp3")
    print("回報位置")

    time.sleep(3)

def soundWinner(winnum):  #播報勝利玩家


    print(winnum)
    print(type(winnum))

    winner = ''

    if(winnum ==1):
       winner = '叉'

    if(winnum ==2):
        winner ='圈'
    tts = gTTS(text='贏家是'+str(winner), lang='zh-TW')
    tts.save("Answer.mp3")
    os.system("Answer.mp3")


def soundStart():


    with sr.Microphone() as source:
        x = 0
        r.adjust_for_ambient_noise(source)     #去噪函數
        Startaudio = r.listen(source,timeout=5)     #五秒內說話
    try:

        print("Result: \n" + r.recognize_google(Startaudio, language='zh-TW'))
        Start = r.recognize_google(Startaudio, language='zh-TW')  # zh-TW
        if(Start == '開始'):
            x=1
            return x
        else:
            return x

    except :
        print("異常")
