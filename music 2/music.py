from tkinter import *
import os
import pygame
from pygame import mixer

# -------------------- Main Window --------------------
root = Tk()
root.title("Music Player")
root.geometry("920x670+290+85")
root.configure(bg="purple")
root.resizable(True, True)

pygame.mixer.init()

# -------------------- Functions --------------------

def playsong():
    song = playlist.get(ACTIVE)
    mixer.music.load(song)
    mixer.music.play()
    print("Playing")

def pausesong():
    mixer.music.pause()
    print("Paused")

def rewindsong():
    mixer.music.rewind()
    print("Rewind")

def stopsong():
    mixer.music.stop()
    print("Stopped")

# -------------------- Icon Image --------------------
img = PhotoImage(file="My project-1.png")
Label(root, image=img, bg="purple").pack()

# -------------------- Button Images --------------------
prev_image = PhotoImage(file=r"C:\Users\HP\Desktop\python\review 2.png")
play_image = PhotoImage(file=r"C:\Users\HP\Desktop\python\play2.png")
pause_image = PhotoImage(file=r"C:\Users\HP\Desktop\python\pause 2.png")

# -------------------- Playlist --------------------
playlist = Listbox(root,
                   selectmode=SINGLE,
                   bg='violet',
                   font=('Algerian', 15),
                   fg="green",
                   height=20,
                   width=25,
                   bd=0)

playlist.place(x=27, y=30)

# -------------------- Load Songs --------------------
os.chdir(r"C:\Users\HP\Desktop\python\music 2")
songs = os.listdir()

for song in songs:
    playlist.insert(END, song)

# -------------------- Buttons --------------------
prev_btn = Button(root,
                  image=prev_image,
                  bg="purple",
                  bd=0,
                  command=rewindsong,
                  cursor='hand2')

prev_btn.place(x=100, y=500)

play_btn = Button(root,
                  image=play_image,
                  bg="purple",
                  bd=0,
                  command=playsong,
                  cursor='hand2')

play_btn.place(x=400, y=500)

pause_btn = Button(root,
                   image=pause_image,
                   bg="purple",
                   bd=0,
                   command=pausesong,
                   cursor='hand2')

pause_btn.place(x=700, y=500)

# -------------------- Run App --------------------
root.mainloop()
