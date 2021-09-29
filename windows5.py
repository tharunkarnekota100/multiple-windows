from tkinter import *
from PIL import Image, ImageTk            #install pillow

main_window = Tk()
main_window.title('main window')
main_window.iconbitmap('images/windowss.ico')
main_window.geometry('500x300')

img =''
def open_window():
    global img
    second_window = Toplevel()
    second_window.title('this is second window')
    second_window.iconbitmap('images/windows.ico')

    # taking image is a three step process

    img = ImageTk.PhotoImage(Image.open('images/backgrounddd.png'))   #main window will acess only global variables
    img_label=Label(second_window,image=img)
    img_label.pack(padx=10,pady=10)

open_window_btn =Button(main_window,text='open next window', font=('',16),command=open_window)
open_window_btn.pack(pady=(60,0))

main_window.mainloop()