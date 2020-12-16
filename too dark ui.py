from tkinter import *
from tkinter import filedialog
import imageio
import os
import shutil
import numpy as np
from tkinter.ttk import *
import tkinter as tk

dark = Tk()
dark.title('Dark image detector')


def folder1():
    global folder_selected1
    folder_selected1 = filedialog.askdirectory()
    Button1['text'] = folder_selected1


progress = Progressbar(dark, orient=HORIZONTAL, length=250, mode='determinate')


def start_sorting():
    for subdir, dirs, files in os.walk(folder_selected1):
        if '.DS_Store' in files:
            files.remove('.DS_Store')
        for file in files:
            progress['maximum'] = len(files)
            os.chdir(folder_selected1)
            f = imageio.imread(file)

            def img_estim(img, thrshld):
                # print(np.mean(img)) debuging
                if np.mean(img) >= s.get():
                    if not os.path.exists("good"):
                        os.makedirs("good")
                    shutil.move(file, 'good')
                    # print('good') debuging
                else:
                    if not os.path.exists("dark"):
                        os.makedirs("dark")
                    shutil.move(file, 'dark')
                    # print('bad') debuging
                progress.step()
            dark.update()
            img_estim(f, 127)


start = Button(dark, text='Start', command=start_sorting)
Button1 = tk.Button(dark, text="Select input folder",
                    activeforeground="blue", command=folder1)
s = tk.Scale(dark, bg='white', fg='black', label='Set the darkness threshold',
             from_=0, to=200, orient=HORIZONTAL, length=200,)
l = Label(dark, width=20, text='empty')

Button1.pack()
s.pack()
progress.pack()
start.pack()
dark.mainloop()
