import requests
from tkinter import *
from tkinter.ttk import *
from tkinter.filedialog import askopenfilename
from PIL import ImageTk , Image
class RmGui(Tk):
    
    def __init__(self):
        super().__init__()
        self.geometry("900x600")
        self.bottomframe = Frame(self,relief=SUNKEN,width=900,height=25)
        self.bottomframe.pack(fill=X,side=BOTTOM)
        self.picf1 = Frame(self,relief=SUNKEN,width=450)

    def pic_loader(self):
        self.ipath= askopenfilename(filetypes=[('JPG Files','*.jpg'),('PNG Files','*.png'),('JPEG Files','*.jpeg')]) #,
        print(self.ipath)
        Img = Image.open(self.ipath)
        oldwidth , oldheight = Img.size
        olddimension = (oldwidth,oldheight)
        self.oldpicsize = olddimension
        newwidth=450
        newheight = newwidth * oldheight//oldwidth
        resized=(newwidth,newheight)
        Img = Img.resize(resized)
        self.rImage = ImageTk.PhotoImage(Img)
        # self.rImage.image = Img
        self.piclabel1(self.rImage)
       
    def topmenu(self):
        self.topmainmenu = Menu(self)
        self.topmainmenu.add_command(label="Open",command=self.pic_loader)
        self.config(menu=self.topmainmenu)

        
    def picframe1(self):
    
        self.picf1.pack(side=LEFT,fill=BOTH,anchor="nw")
        
        self.picf2 = Frame(root,relief=SUNKEN,width=450)
        self.picf2.pack(side=RIGHT,anchor="ne",fill=BOTH)
      
    
    def piclabel1(self,rImage):  
        self.picLabel1 = Label(self.picf1,image=rImage)
        self.picLabel1.pack()

    def uploadbutton(self): 
        self.supbt=Button(self.bottomframe,text="Upload",command=self.uploadbuttonfunctionality)
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
    def uploadbuttonfunctionality(self):
        import requests

        response = requests.post(
                'https://api.remove.bg/v1.0/removebg',
                files={'image_file': open('self.path', 'rb')},
                data={'size': 'auto'},
                headers={'X-Api-Key': 'Vt1fjLMNViXdjxvLmzMq3BpD'},
            )
        if response.status_code == requests.codes.ok:
            with open('no-bg.png', 'wb') as out:
                out.write(response.content)
        else:
            print("Error:", response.status_code, response.text)
    
    def downloadbuttonfunctionality(self):
        pass
       

        


if __name__=='__main__':
    root = RmGui()
    root.topmenu()
    root.bottombarframe()
    
    root.picframe1()
    
  
    root.mainloop()


# from tkinter import Label,Tk
# from PIL import Image, ImageTk
# from tkinter.filedialog import askopenfilename
# root = Tk()

# path=askopenfilename(filetypes=[("Image File",'.jpg')])
# im = Image.open(path)
# tkimage = ImageTk.PhotoImage(im)
# myvar=Label(root,image = tkimage)
# myvar.image = tkimage
# myvar.pack()

# root.mainloop()

# import requests

# response = requests.post(
# 'https://api.remove.bg/v1.0/removebg',
# files={'image_file': open('D:\\My Photos\\Nkm Pics\\test.jpg', 'rb')},
# data={'size': 'auto'},
# headers={'X-Api-Key': 'Vt1fjLMNViXdjxvLmzMq3BpD'},
# )
# if response.status_code == requests.codes.ok:
#     with open('no-bgg.png', 'wb') as out:
#         out.write(response.content)
# else:
#     print("Error:", response.status_code, response.text)