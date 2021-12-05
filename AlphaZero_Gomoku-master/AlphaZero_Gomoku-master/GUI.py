import tkinter as tk

import human_play as human

class tink(object):
    def __init__(self):
        self.Pywin =0
        self.Azwin =0
        self.window = tk.Tk()


    def windows(self,x):


       self.window.title('My window')

       self.window.geometry('500x300')
       self.window.maxsize(1024,600)



       if(x==1):
            self.Pywin+=1
       if(x==-1):
            self.Azwin+=1


       numberX="玩家贏"+str(self.Pywin)
       numberY="Az贏"+str(self.Azwin)
       Py =tk.Label(self.window, text=numberX,bg='green',width=30,height=5)
       Az =tk.Label(self.window, text=numberY, bg='red', width=30, height=5)

       Py.pack()
       Az.pack()
       self.window.mainloop()


tink().windows(1)