from tkinter import *
from tkinter.ttk import *
from tkinter.filedialog import askopenfilename , asksaveasfilename
from PIL import ImageTk , Image
import tkinter.messagebox as tmsg
import requests
import os.path

class RmGui(Tk):
    
    def __init__(self):
        super().__init__()
        self.iconbitmap('main.ico')
        self.title("Bg_Remover")
        self.geometry("900x600")
        self.bottomframe = Frame(self,relief=SUNKEN,width=900,height=25)
        self.bottomframe.pack(fill=X,side=BOTTOM)
        self.picf1 = Frame(self,relief=SUNKEN,width=450)
        self.minsize(900,600)
        self.maxsize(900,600)
        self.yourapikey = 'Vt1fjLMNViXdjxvLmzMq3BpD' #paste the key inside the single quotes.
       
   
    def pic_loader(self):          #Fuction to load picture inside the program

        self.ipath= askopenfilename(filetypes=[('JPG Files','*.jpg'),('PNG Files','*.png'),('JPEG Files','*.jpeg')]) #,
        if os.path.exists(self.ipath):

            self.originalpath = self.ipath
            Img=self.picresizedpreview(self.ipath)
            self.rImage = ImageTk.PhotoImage(Img)
            
            self.piclabel1(self.rImage)  
        else:
            tmsg.showinfo("Error","File Open Action Aborted By the User")
        
        
       
    def topmenu(self): #will create the top menu for the program
        self.topmainmenu = Menu(self)
        self.topmainmenu.add_command(label="Open",command=self.pic_loader)
        self.topmainmenu.add_command(label="How to Start",command=self.howtostart)
        self.topmainmenu.add_command(label="About",command=self.aboutloader)
        self.config(menu=self.topmainmenu)

    def aboutloader(self):        #about option method
        tmsg.showinfo("Message From Developer","This App is Created and Managed by Navdeep Mishra")
    def howtostart(self):         #how to start method
        tmsg.showinfo("How to Start","1)Click on Open and Select Your Desired Image\n2)Click On Upload Button (One Time Only and don't touch anything, just wait)\n3)A Window will popup automatically when everything is done, just save the file")
        
    def picframe1_2(self):            #pic1 frame packer and pic2 frame creater and packer method
    
        self.picf1.pack(side=LEFT,fill=BOTH,anchor="nw")
        self.picf2 = Frame(root,relief=SUNKEN,width=450)
        self.picf2.pack(side=RIGHT,anchor="ne",fill=BOTH)

    def picresizedpreview(self,imag):  #Return a resized image for the preview in the application window
        try:
            Img = Image.open(imag)
            originalwidth , originalheight = Img.size
            self.originalimagesize = (originalwidth,originalheight)
            
            newwidth=450
            newheight = newwidth * originalheight//originalwidth
            resized=(newwidth,newheight)
            Img = Img.resize(resized)
            return Img
        except AttributeError as ee:
            tmsg.showinfo("Error","File Open Action Aborted By the User")

    def piclabel2load(self): #method that shows the picture inside frame
        Img=self.picresizedpreview(self.nImage)
        self.nImage = ImageTk.PhotoImage(Img)

        self.piclabel2 = Label(self.picf2,image = self.nImage)

        self.piclabel2.pack()

    def piclabel1(self,rImage):  #method that shows the picture inside frame
        self.picLabel1 = Label(self.picf1,image=rImage)
        self.picLabel1.pack(side=LEFT,anchor="nw")

    def uploadbutton(self):  #Will Create Upload button 
        self.supbt=Button(self.bottomframe,text="Upload",command=self.uploadbuttonfunctionality)
        self.supbt.pack(side=LEFT,anchor="se")

    def bottomlabel(self):   #bottom status bar 
        self.cstatus = StringVar()
        self.cstatus.set("Ready")
        self.sbar = Label(self.bottomframe,textvariable=self.cstatus)
        self.sbar.pack(side=LEFT,fill=X,expand=1,anchor="sw",ipady=2,pady=(2,0))

    def bottombarframe(self): #Creates bottom frame
        self.bottomlabel()
        self.uploadbutton()
            
    def uploadbuttonfunctionality(self):                #Fuctionality for the the upload button
        try:
            if os.path.exists(self.ipath):
                tmsg.showinfo("Important Message","Don't Double Press the button and Don't Drag the Application.If Application Shows not responding,Don't Worry application is still working in background just wait for AutoFile Save or until any Message pop up")
                # self.pathupdater()        
             
                self.cstatus.set("Working on it. Please Wait....") 
                self.sbar.update()
                response = requests.post(
                        'https://api.remove.bg/v1.0/removebg',
                        files={'image_file': open(self.ipath, 'rb')},
                        data={'size': 'auto'},
                        headers={'X-Api-Key': self.yourapikey},
                    )
                if response.status_code == requests.codes.ok:
                   
                    newfilepath = self.downloadfunctionality()
                
                    with open(newfilepath, 'wb') as out:
                        out.write(response.content)
                    
                    self.nImage = newfilepath
                    self.piclabel2load()
                    self.cstatus.set("File Saved Succesfully")     
                    
                else:
                
                    tmsg.showinfo("Error","Error Code: "+str(response.status_code))
                    self.cstatus.set("Error Occured")
                    self.sbar.update()
            else:
                tmsg.showerror("Error","Image is not loaded into the Previewer.")
        except requests.exceptions.ConnectionError:
           
            tmsg.showinfo("Error","Connection Error")
        except AttributeError as e:
            tmsg.showinfo("Error","Open the Image in the image previewer first")
        except FileNotFoundError:
            tmsg.showinfo("Error","No Valid File Found. Open the Image in the image previewer first")
            self.cstatus.set("Ready")
            self.sbar.update()
            
    def downloadfunctionality(self): 
        
        files = [  
                ('Png Files', '*.png'), 
                ] 
        newfilepath = asksaveasfilename(filetypes = files, defaultextension = files) 
        return newfilepath    

        
# //////////////////////////Program will Start From here.//////////////////////////////

if __name__=='__main__':
    root = RmGui()
    root.topmenu() #Calling the Menu creater Function
    root.bottombarframe()  #Calling the Bottom bar Frame that contains the staus bar and upload button Funciton
    root.picframe1_2()   #Calling Pic frame 1 and 2
    root.mainloop() #Mainloop Funciton

