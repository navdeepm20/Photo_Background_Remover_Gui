import requests
from tkinter import *
from tkinter.ttk import *

class RmGui(Tk):
    
    def __init__(self):
        super().__init__()
        self.geometry("900x600")
    def picframe1(self):
        self.picf1 = Frame(root,relief=SUNKEN,width=450,height=570)
        self.picf1.pack(side=LEFT,anchor="nw")
        self.picf2 = Frame(root,relief=SUNKEN,width=450,height=570)
        self.picf2.pack(side=RIGHT,anchor="ne")
      

    def piclabel1(self):  
        pass

    def uploadbutton(self):
        self.supbt=Button(root,text="Upload")
        self.supbt.pack(side=RIGHT,anchor="sw")
    def downloadbutton(self):
        self.dwbt=Button(root,text="Download")
        self.dwbt.pack(side=RIGHT,anchor="sw")

    def fstatusbar(self):
        self.cstatus = StringVar()
        self.cstatus.set("Ready")
        self.sbar = Label(self,textvariable=self.cstatus,relief=SUNKEN)
       
        
        self.downloadbutton()
        self.uploadbutton()
        self.sbar.pack(side=LEFT,fill=X,expand=1,anchor="sw",ipady=3)
        


if __name__=='__main__':
    root = RmGui()
    # root.picframe1()
    root.fstatusbar()
    root.mainloop()