import requests
from tkinter import *
from tkinter.ttk import *
from tkinter.filedialog import askopenfilename , asksaveasfilename
from PIL import ImageTk , Image

class RmGui(Tk):
    
    def __init__(self):
        super().__init__()
        self.title("Bg_Remover")
        self.geometry("900x600")
        self.bottomframe = Frame(self,relief=SUNKEN,width=900,height=25)
        self.bottomframe.pack(fill=X,side=BOTTOM)
        self.picf1 = Frame(self,relief=SUNKEN,width=450)


    def pic_loader(self):
        self.ipath= askopenfilename(filetypes=[('JPG Files','*.jpg'),('PNG Files','*.png'),('JPEG Files','*.jpeg')]) #,
        # print(self.ipath)
        Img=self.picresizedpreview(self.ipath)
        self.rImage = ImageTk.PhotoImage(Img)
        # self.rImage.image = Img
        self.piclabel1(self.rImage)
       
    def topmenu(self):
        self.topmainmenu = Menu(self)
        self.topmainmenu.add_command(label="Open",command=self.pic_loader)
        self.config(menu=self.topmainmenu)

        
    def picframe1_2(self):
    
        self.picf1.pack(side=LEFT,fill=BOTH,anchor="nw")
        
        self.picf2 = Frame(root,relief=SUNKEN,width=450)
        self.picf2.pack(side=RIGHT,anchor="ne",fill=BOTH)
    def picresizedpreview(self,imag):
        Img = Image.open(imag)
        oldwidth , oldheight = Img.size
        # olddimension = (oldwidth,oldheight)
        # self.oldpicsize = olddimension
        newwidth=450
        newheight = newwidth * oldheight//oldwidth
        resized=(newwidth,newheight)
        Img = Img.resize(resized)
        return Img

    def piclabel2load(self):
        Img=self.picresizedpreview(self.nImage)
        self.nImage = ImageTk.PhotoImage(Img)

        self.piclabel2 = Label(self.picf2,image = self.nImage)

        self.piclabel2.pack()

    def piclabel1(self,rImage):  
        self.picLabel1 = Label(self.picf1,image=rImage)
        self.picLabel1.pack()

    def uploadbutton(self): 
        self.supbt=Button(self.bottomframe,text="Upload",command=self.uploadbuttonfunctionality)
        self.supbt.pack(side=LEFT,anchor="se")
        
    def downloadbutton(self):
        

        self.dwbt=Button(self.bottomframe,text="Download")
        self.dwbt.pack(side=LEFT,anchor="se")
    # def imageresizer(self):

    def bottomlabel(self):
        self.cstatus = StringVar()
        self.cstatus.set("Ready")
        self.sbar = Label(self.bottomframe,textvariable=self.cstatus)
        self.sbar.pack(side=LEFT,fill=X,expand=1,anchor="sw",ipady=2,pady=(2,0))

    def bottombarframe(self):
        self.bottomlabel()
        self.uploadbutton()
        self.downloadbutton()
    def pathupdater(self):
        trimmedpath = self.ipath.split('/')
        # print(trimmedpath)
        self.ipath = ""
        pathlength = len(trimmedpath)
        for i in range(0,pathlength):
            if i == pathlength -1:
                self.ipath += trimmedpath[i]
                print(self.ipath)
                break
            self.ipath += trimmedpath[i]+ r'\\'
           
    def uploadbuttonfunctionality(self):
        try:
            import requests
            self.pathupdater()
            response = requests.post(
                    'https://api.remove.bg/v1.0/removebg',
                    files={'image_file': open(self.ipath, 'rb')},
                    data={'size': 'auto'},
                    headers={'X-Api-Key': 'Vt1fjLMNViXdjxvLmzMq3BpD'},
                )
            if response.status_code == requests.codes.ok:
                newfilepath = self.downloadbuttonfunctionality()

                with open(newfilepath, 'wb') as out:
                    out.write(response.content)

                # self.nImage = newfilepath.split('/')
                # for i in self.nImage:
                #     self.nImage = i
                # print(self.nImage)
                self.nImage = newfilepath
                self.piclabel2load()
                
                
            else:
                print("Error:", response.status_code, response.text)
        except requests.exceptions.ConnectionError:
            print("Connection Refused")
        
    def downloadbuttonfunctionality(self):
        
        files = [  
                ('Png Files', '*.png'), 
                ] 
        newfilepath = asksaveasfilename(filetypes = files, defaultextension = files) 
        return newfilepath    

        


if __name__=='__main__':
    root = RmGui()
    root.topmenu()
    root.bottombarframe()
    
    root.picframe1_2()
    # root.piclabel2load()    
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