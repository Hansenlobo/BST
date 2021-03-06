import tkinter as tk
from tkinter import ttk
import binarysearchtreepage
from tkinter import PhotoImage
from ttkthemes import ThemedTk


# class algos(object):
#     def __init__(self, ances):
#         self.parentframe = ances
#         self.pgid = 0

#     def raise_frame(self):
#         self.openframe.tkraise()
    
#     def addalgo(self, name, w, h, img, row, col, openframe):
#         self.openframe = openframe
#         style_b = ttk.Style()
#         style_b.configure('my.TButton', font=('Helvetica', 12))
#         fr = ttk.Button(master=self.parentframe,text=name.title(),command= self.raise_frame,compound="top",style="my.TButton")
#         fr.image = tk.PhotoImage(file=img)
#         fr['image'] = fr.image
#         fr.grid(row=row, column=col, sticky="news", pady=5,padx=10)


class vALGO(object):
    def __init__(self):
        self.window = ThemedTk(theme="breeze", className="Binary Search Tree Visualization")
        self.window.rowconfigure(0, weight=1)
        self.window.columnconfigure(0, weight=1)
        self.logo = PhotoImage(file="png\\logoc.png")
        self.window.iconphoto(False, self.logo)
        self.width = self.window.winfo_screenwidth() * 3 // 4
        self.height = self.window.winfo_screenheight() * 3 // 4
        self.binarysearchtreepage = ttk.Frame(master=self.window)
        self.pages = [self.binarysearchtreepage]
        for page in self.pages:
            page.grid(row=0, column=0, sticky='news')
        binarysearchtreecontents = binarysearchtreepage.binarysearchtree_contents(self.binarysearchtreepage, self.width, self.height)
    
    def start(self):
        self.window.mainloop()


if __name__ == "__main__":
    valgo = vALGO()
    valgo.start()
