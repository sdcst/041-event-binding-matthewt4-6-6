import tkinter as tk
from tkinter import  *
from tkinter import ttk
import playsound as p
from PIL import ImageTk, Image

def playsound():
    p.playsound("vine-boom (1).mp3", block = False)
    
def playsound1():
    p.playsound("erm-what-the-sigma_su7GnzC.mp3", block = False)

def playsound2():
    p.playsound("wait-wait-wait-what-the-hell-legend-sound.mp3", block = False)

def playsound3():
    p.playsound("danger-alarm-sound-effect-meme.mp3", block = False)

def playsound4():
    p.playsound("oooh-my-god-vine-mp3cut.mp3", block = False)

def playsound5():
    p.playsound("perfect-fart.mp3", block = False)

def playsound6():
    p.playsound("bad-to-the-bone.mp3", block = False)

def playsound7():
    p.playsound("goofy-ahh-sounds.mp3", block = False)


def playsound8():
    p.playsound("im-on-that-good-kush_BwBIudY.mp3", block = False)

def playsound9():
    p.playsound("fire-in-the-hole-geometry-dash.mp3", block = False)

def playsound10():
    p.playsound("9-10-vine.mp3", block = False)

def playsound11():
    p.playsound("which-bomboclaat-dog-i-am.mp3", block = False)

def playsound12():
    p.playsound("movie_1 (1).mp3", block = False)

def playsound13():
    p.playsound("ring-doorbell-sound.mp3", block = False)

def playsound14():
    p.playsound("mlg-airhorn.mp3", block = False)


window = tk.Tk()
window.title("tk")
window.geometry("400x400")
window.config(bg ="gray")




b1 =  tk.Button(window,text="Vine Boom", command = playsound, width = 15)
b2 =  tk.Button(window,text="What The Sigma?", command = playsound1, width = 15)
b3 =  tk.Button(window,text="Wait Wait Wait", command = playsound2, width = 15)
b4 =  tk.Button(window,text="Alarm", command = playsound3, width = 15)
b5 =  tk.Button(window,text="Ohhh My God", command = playsound4, width = 15)
b6 =  tk.Button(window,text="Fart", command = playsound5, width = 15)
b7 =  tk.Button(window,text = "Bad To The Bone", command = playsound6, width = 15)
b8 =  tk.Button(window,text="Goofy Sounds", command = playsound7, width = 15)
b9 = tk.Button(window, text = "Im On That Good", command = playsound8, width = 15)
b10 =  tk.Button(window,text="Fire In The Hole", command = playsound9, width = 15)
b11 = tk.Button(window, text = "Vine", command = playsound10, width = 15)
b12 =  tk.Button(window,text="Bomboclat Dog", command = playsound11, width = 15)
b13 = tk.Button(window, text = "Bruh", command = playsound12, width = 15)
b14 =  tk.Button(window,text="Ring Doorbell", command = playsound13, width = 15)
b15 = tk.Button(window, text = "MLG Airhorn", command = playsound14, width = 15)

b1.place(x = 10, y = 20)
b2.place(x = 142, y = 20)
b3.place(x = 275, y = 20)
b4.place(x = 10, y = 80)
b5.place(x = 142, y = 80)
b6.place(x = 275, y = 80)
b7.place(x = 10, y = 140)
b8.place(x = 142, y = 140)
b9.place(x = 275, y = 140)
b10.place(x = 10, y = 200)
b11.place(x = 142, y = 200)
b12.place(x = 275, y = 200)
b13.place(x = 10, y = 260)
b14.place(x = 142, y = 260)
b15.place(x = 275, y = 260)



window.mainloop()