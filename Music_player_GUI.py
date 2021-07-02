from pygame import mixer
import time
from tkinter import *


def Play():
    mixer.music.play()

def Pause():
    mixer.music.pause()

def Resume():
    mixer.music.unpause()

def Exit():
    root.destroy()

if __name__ == '__main__':
    mixer.init()
    mixer.music.load("Dilwale.mp3")
    mixer.music.set_volume(0.7)

    root=Tk()
    root.geometry("500x100")
    root.title("Music Player")

    Label(root,text="Rutuja's Music Player",font="Helvetica 15 bold",bg="mistyrose").pack(fill=X)

    f1=Frame(root)

    b1 = Button(f1, bg="mistyrose", fg="black", font="Helvetica 12 bold", text="Play", relief=SUNKEN, command=Play)
    b1.pack(side=LEFT, padx=15, fill=X)

    b1 = Button(f1, bg="mistyrose", fg="black", font="Helvetica 12 bold", text="Pause", relief=SUNKEN, command=Pause)
    b1.pack( side=LEFT, padx=15, fill=X)

    b2 = Button(f1, bg="mistyrose", fg="black", font="Helvetica 12 bold", text="Resume", relief=SUNKEN, command=Resume)
    b2.pack(side=LEFT, padx=15, fill=X)

    b3 = Button(f1, bg="mistyrose", fg="black", font="Helvetica 12 bold", text="Exit", relief=SUNKEN, command=Exit)
    b3.pack( side=LEFT, padx=15, fill=X)
    f1.pack(side=BOTTOM,pady=(0,16))

    root.mainloop()

