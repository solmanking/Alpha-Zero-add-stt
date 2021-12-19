


def __init__(self):
    pass


def write(pos):
    #f = open("test.txt", 'a+')

    posX = [pos // 8, pos % 8]
    with open("test.txt", 'a+' ) as filetxt:
        print(posX,file=filetxt)




    #f.write(posX)
    #f.write('\n')
    #f.close()
    print("存取位置成功")


def writeWin(winner):
    with open("test.txt",'a+') as filetxt:
        print(winner+"是贏家",file=filetxt)



def cleanNote():
    with open("test.txt", 'a+') as filetxt:
        filetxt.truncate(0)