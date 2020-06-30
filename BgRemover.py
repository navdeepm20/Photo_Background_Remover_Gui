import requests
from tkinter import *
from tkinter.ttk import *
from tkinter.filedialog import askopenfilename , asksaveasfilename
from PIL import ImageTk , Image
import tkinter.messagebox as tmsg
import requests
import os.path
import os
class RmGui(Tk):
    
    def __init__(self):
        super().__init__()
        self.title("Bg_Remover")
        self.geometry("900x600")
        self.bottomframe = Frame(self,relief=SUNKEN,width=900,height=25)
        self.bottomframe.pack(fill=X,side=BOTTOM)
        self.picf1 = Frame(self,relief=SUNKEN,width=450)
        self.minsize(900,600)
        self.maxsize(900,600)


    def pic_loader(self):

        self.ipath= askopenfilename(filetypes=[('JPG Files','*.jpg'),('PNG Files','*.png'),('JPEG Files','*.jpeg')]) #,
        if os.path.exists(self.ipath):
            self.originalpath = self.ipath
            self.originaldirpathsave()
            Img=self.picresizedpreview(self.ipath)
            self.rImage = ImageTk.PhotoImage(Img)
            # self.rImage.image = Img
            self.piclabel1(self.rImage)  
        else:
            tmsg.showinfo("Error","File Open Action Aborted By the User")
        
        
       
    def topmenu(self):
        self.topmainmenu = Menu(self)
        self.topmainmenu.add_command(label="Open",command=self.pic_loader)
        self.topmainmenu.add_command(label="How to Start",command=self.howtostart)
        self.topmainmenu.add_command(label="About",command=self.aboutloader)

        self.config(menu=self.topmainmenu)
    def aboutloader(self):
        tmsg.showinfo("Message From Developer","This App is Created and Managed by Navdeep Mishra")
    def howtostart(self):
        tmsg.showinfo("How to Start","1)Click on Open and Select Your Desired Image\n2)Click On Upload Button (One Time Only and don't touch anything, just wait)\n3)A Window will popup automatically when everything is done, just save the file")
        
    def picframe1_2(self):
    
        self.picf1.pack(side=LEFT,fill=BOTH,anchor="nw")
        
        self.picf2 = Frame(root,relief=SUNKEN,width=450)
        self.picf2.pack(side=RIGHT,anchor="ne",fill=BOTH)

    def picresizedpreview(self,imag):
        try:
            Img = Image.open(imag)
            oldwidth , oldheight = Img.size
            
            newwidth=450
            newheight = newwidth * oldheight//oldwidth
            resized=(newwidth,newheight)
            Img = Img.resize(resized)
            return Img
        except AttributeError as ee:
            tmsg.showinfo("Error","File Open Action Aborted By the User")

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
   

    def bottomlabel(self):
        self.cstatus = StringVar()
        self.cstatus.set("Ready")
        self.sbar = Label(self.bottomframe,textvariable=self.cstatus)
        self.sbar.pack(side=LEFT,fill=X,expand=1,anchor="sw",ipady=2,pady=(2,0))

    def bottombarframe(self):
        self.bottomlabel()
        self.uploadbutton()
        # self.downloadbutton()
    def originaldirpathsave(self):
        temppath  = self.originalpath.split('/')
        self.originalpath = ""
        for i in range(0,len(temppath)-1):
            self.originalpath += temppath[i]+r'/'
       


    def pathupdater(self):
        try:
            trimmedpath = self.ipath.split('/')
            
            self.ipath = ""
            pathlength = len(trimmedpath)
            for i in range(0,pathlength):
                if i == pathlength -1:
                    self.ipath += trimmedpath[i]
                    
                    break
                self.ipath += trimmedpath[i]+ r'\\'
        except AttributeError as e:
           
            self.cstatus.set("Ready")
            self.sbar.update()

            tmsg.showinfo("Error","Image path not Found")
            
    def uploadbuttonfunctionality(self):
        try:
            tmsg.showinfo("Message","Don't Double Press the button and Don't Drag the Application. Wait for AutoFile Save or until any Message pop up")
            self.pathupdater()
            
            self.cstatus.set("Working on it. Please Wait....") 
            self.sbar.update()
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

                self.nImage = newfilepath.split('/')
                
                
                self.nImage = newfilepath
                self.piclabel2load()
           
                self.cstatus.set("File Saved Succesfully")     
                
            else:
               
                tmsg.showinfo("Error",response.status_code)

        except requests.exceptions.ConnectionError:
           
            tmsg.showinfo("Error","Connection Error")
        except AttributeError as e:
            tmsg.showinfo("Error","Open the Image in the image previewer first")
        except FileNotFoundError:
            tmsg.showinfo("Error","Open the Image in the image previewer first")
            self.cstatus.set("Ready")
            self.sbar.update()
            
   

    def downloadbuttonfunctionality(self):
        
        files = [  
                ('Png Files', '*.png'), 
                ] 
        newfilepath = asksaveasfilename(filetypes = files, defaultextension = files) 
        return newfilepath    

        
# //////////////////////////Program will Start From here.//////////////////////////////

if __name__=='__main__':
    root = RmGui()
    root.topmenu()
    root.bottombarframe() 
    root.picframe1_2()   
    root.mainloop()

