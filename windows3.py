from tkinter import *
from PIL import Image, ImageTk            #install pillow

main_window = Tk()
main_window.title('main window')
main_window.iconbitmap('images/windowss.ico')
main_window.geometry('500x300')

#Creating second window
second_window = Toplevel()
second_window.title('this is second window')
second_window.iconbitmap('images/windows.ico')

# taking image is a three step process

img = ImageTk.PhotoImage(Image.open('images/backgrounddd.png'))
img_label=Label(second_window,image=img)
img_label.pack(padx=10,pady=10)



main_window.mainloop()