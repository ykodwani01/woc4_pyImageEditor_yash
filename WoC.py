
from argparse import FileType
import os
from msilib.schema import RadioButton
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from PIL import Image, ImageTk
root =Tk()

root.geometry("500x500")



def onopen():
    root.filename=filedialog.askopenfilename(title="select file",initialdir="/Users/admin/")
    my_label=Label(text=root.filename).pack()
    global my_img,img,x
    img=Image.open(root.filename)
    my_img= ImageTk.PhotoImage(img)
    x=Label(image=my_img)
    x.pack()
    

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
   img=img.convert("1")
   
   my_img= ImageTk.PhotoImage(img)
   x.configure(image=my_img)


def onsave():
    f = filedialog.asksaveasfile(initialfile = 'Untitled.jpg',defaultextension=".jpg",filetypes=[("All Files","*.*"),("PNG","*.png"),("JPEG","*jpg")]) 
    img.save(f)
file_button = Button( root,text="Open file",command=onopen,fg="black").pack()
rotate_button = Button( root,text="Rotate file",command=onrotate,fg="red").pack()
flip_button = Button(root,text="Flip right",command=flipr,fg="Blue").pack()
bw_button = Button(root,text="Convert in BW",command=onbw,fg="white",bg="Black").pack()
save_button = Button(root,text="Save",command=onsave,fg="Blue",bg="Yellow").pack()

root.mainloop()
