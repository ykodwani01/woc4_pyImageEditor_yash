
from argparse import FileType
import os
from msilib.schema import RadioButton
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from PIL import Image, ImageTk
from PIL import ImageEnhance,ImageFilter
root =Tk()

root.geometry("1600x1200")



def onopen():
    root.filename=filedialog.askopenfilename(title="select file",initialdir="/Users/admin/")
    my_label=Label(text=root.filename).pack()
    global my_img,img,x
    img=Image.open(root.filename)
    
    img=img.resize((500,500),Image.ANTIALIAS)
    my_img= ImageTk.PhotoImage(img)
    x=Label(image=my_img)
    x.place(anchor=NW)
    



def onrotate():
    global img,x,my_img
    img=img.rotate(90)
    my_img= ImageTk.PhotoImage(img)
    x.configure(image=my_img)
    

def flipr():
    global img,my_img,x
    img = img.transpose(Image.FLIP_LEFT_RIGHT)
    my_img= ImageTk.PhotoImage(img)
    x.configure(image=my_img) 


def onbw():
   global img,my_img,x 
   img=img.convert("L")
   
   my_img= ImageTk.PhotoImage(img)
   x.configure(image=my_img)


def onsave():
    f = filedialog.asksaveasfile(initialfile = 'Untitled.jpg',defaultextension=".jpg",filetypes=[("All Files","*.*"),("PNG","*.png"),("JPEG","*jpg")]) 
    img.save(f)


def sepia():
    global img,x,my_img
    rgb2sep=(
        0.393, 0.769, 0.180423, 0,
        0.349, 0.686, 0.16729, 0,
        0.272334, 0.534, 0.131, 0

    )
    img=img.convert("RGB",rgb2sep)
    my_img= ImageTk.PhotoImage(img)
    x.configure(image=my_img)

def slide(var):
    global img,x,my_img
    img1=ImageEnhance.Brightness(img)
    factor=hor1.get()/100
    img=img1.enhance(factor)
    my_img= ImageTk.PhotoImage(img)
    x.configure(image=my_img)



file_button = Button( root,text="Open file",command=onopen,fg="black").pack()
rotate_button = Button( root,text="Rotate file",command=onrotate,fg="red").pack()
flip_button = Button(root,text="Flip right",command=flipr,fg="Blue").pack()
bw_button = Button(root,text="Convert in BW",command=onbw,fg="white",bg="Black").pack()
save_button = Button(root,text="Save",command=onsave,fg="Blue",bg="Yellow").pack(pady=10)
sepia_button = Button(root,text="Sepia",command=sepia,fg="Brown",bg="Yellow").pack(pady=10)
my_lbl=Label(root,text="Brightness").pack()
hor1=Scale(root,from_=0, to=100,orient=HORIZONTAL).pack()
button=Button(root,text="Apply Brightness",command=slide).pack()



root.mainloop()