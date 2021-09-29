from tkinter import *

main_window = Tk()
main_window.title('main window')
main_window.iconbitmap('images/windowss.ico')
main_window.geometry('500x300')

second_window = Toplevel()
second_window.title('this is second window')
second_window.iconbitmap('images/windows.ico')
second_window.geometry('900x300')

main_window.mainloop()