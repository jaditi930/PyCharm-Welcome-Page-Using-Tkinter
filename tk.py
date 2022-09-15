from tkinter import *
from PIL import ImageTk,Image
window=Tk()
window.geometry("644x434")
window.minsize(300,370)
window.title("Pycharm")

image1 = Image.open("PyCharm_Icon.svg.png")
image1 = image1.resize((40, 40))
test = ImageTk.PhotoImage(image1)

label1 = Label(image=test) 
label1.place(relx=0.5,rely=0.1,anchor="center")

text=Label(text="Pycharm Community Edition",font=("Helvetica", 15))
text.place(rely=0.2,relx=0.5,anchor="center")
text1=Label(text="Version 2.0.2",fg="grey",font="comicsansms 10")
text1.place(relx=0.5,rely=0.25,anchor="center")

create=Image.open("magic-wand.png")
create=create.resize((10,10))
create_img=ImageTk.PhotoImage(create)
create_label=Label(text="  Create New Project",image=create_img,compound="left",anchor="center")
create_label.place(rely=0.4,relx=0.4)

open=Image.open("folder.png")
open=open.resize((10,10))
open_img=ImageTk.PhotoImage(open)
open_label=Label(text="  Open",image=open_img,compound="left",anchor="center")
open_label.place(rely=0.45,relx=0.4)

dwld=Image.open("download.png")
dwld=dwld.resize((10,10))
dwld_img=ImageTk.PhotoImage(dwld)
dwld_label=Label(text="  Create New Project",image=dwld_img,compound="left",anchor="center")
dwld_label.place(rely=0.5,relx=0.4)

create1=Image.open("configuration.png")
create1=create1.resize((10,10))
img1=ImageTk.PhotoImage(create1)

create2=Image.open("gethelp.jpg")
create2=create2.resize((15,15))
img2=ImageTk.PhotoImage(create2)

f1=Frame()
f1.pack(side=BOTTOM,anchor="se")
img_label1=Label(f1,text="  Configure",image=img1,compound="left",anchor="center")
img_label2=Label(f1,text="  Get Help",image=img2,compound="left",anchor="center")
img_label1.pack(side=RIGHT,padx=10,pady=10)
img_label2.pack(side=RIGHT,padx=10,pady=10)

window.mainloop()

