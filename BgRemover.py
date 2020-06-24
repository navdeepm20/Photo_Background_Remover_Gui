import requests
from tkinter import *
from tkinter.ttk import *

class RmGui(Tk):
    
    def __init__(self):
        super().__init__()
        self.geometry("900x600")
        self.bottomframe = Frame(self,relief=SUNKEN,width=900,height=25)
        self.bottomframe.pack(fill=X,side=BOTTOM)
        self.picf1 = Frame(self,relief=SUNKEN,width=450)

    def picframe1(self):
        self.picf1.pack(side=LEFT,fill=BOTH,anchor="nw")
        
        self.picf2 = Frame(root,relief=SUNKEN,width=450)
        self.picf2.pack(side=RIGHT,anchor="ne",fill=BOTH)
      
    
    def piclabel1(self):  
        pass

    def uploadbutton(self): 
        self.supbt=Button(self.bottomframe,text="Upload")
        self.supbt.pack(side=LEFT,anchor="se")
        
    def downloadbutton(self):
        

        self.dwbt=Button(self.bottomframe,text="Download")
        self.dwbt.pack(side=LEFT,anchor="se")
    
    def bottomlabel(self):
        self.cstatus = StringVar()
        self.cstatus.set("Ready")
        self.sbar = Label(self.bottomframe,textvariable=self.cstatus)
        self.sbar.pack(side=LEFT,fill=X,expand=1,anchor="sw",ipady=2,pady=(2,0))

    def bottombarframe(self):
        self.bottomlabel()
        self.uploadbutton()
        self.downloadbutton()
        
       

        


if __name__=='__main__':
    root = RmGui()
    
    root.bottombarframe()
    root.picframe1()
    
    # root.downloadbutton()
    # root.uploadbutton()
    root.mainloop()