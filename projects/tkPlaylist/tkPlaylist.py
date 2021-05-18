# -*- coding: utf-8 -*-
"""

"""
from tkinter import *
import pygame
from tkinter.messagebox import *
from tkinter import filedialog


#-------------------------------FONCTIONS---------------------------------


def importer_son(event):
    file = filedialog.askopenfilename()
    pygame.init()
    pygame.mixer.pre_init(44100, -16, 2, 2048)
    pygame.mixer.init()
    playlist.append(file)
    #TEST PRINT
    print(file)
    print (playlist)


def stop_it(event):
    pygame.mixer.music.pause()
    global pause
    pause = 1

def start_it(event):
    global pause
    if pause == 1:
        pygame.mixer.music.unpause()
        pause = 0
    else:
        try:
            pygame.mixer.music.load(playlist[index])
            pygame.mixer.music.play()
        except:
            showwarning("Error","Find a Path")

def close():
    pygame.mixer.music.stop()
    fen1.destroy()

def next_musique(event):
    global index
    index += 1
    try:
        pygame.mixer.music.load(playlist[index])
        pygame.mixer.music.play()
    except:
        showwarning("Error","Find a Path")

def previous_musique(event):
    global index
    index -= 1
    try:
        pygame.mixer.music.load(playlist[index])
        pygame.mixer.music.play()
    except:
        showwarning("Error","Find a Path")

def reint():
    pygame.mixer.music.stop()
    playlist[:] = []

 #-------------------------------Variables---------------------------------

playlist = []
global index
index = 0
global pause
pause = 0

#-------------------------------MAIN---------------------------------

fen1 = Tk()
fen1.title("Lecteur Audio en python")

menubar = Menu(fen1)
menu1 = Menu(menubar, tearoff=0)
menu1.add_command(label="Réinitialiser", command=reint)
menu1.add_command(label="Quitter", command=close)
menubar.add_cascade(label="Option", menu=menu1)
fen1.config(menu=menubar)

can1 = Canvas(fen1, height=500, width=500)
can1.pack(side=LEFT, padx=5, pady=5)

fond_decran = PhotoImage(file="img.png")
# fond_decran = PhotoImage(file="Background.gif")
can1.create_image(0,0, anchor = "nw", image = fond_decran)
can1.image = fond_decran

image_play = PhotoImage(file="img.png")
# image_play = PhotoImage(file="Play.gif")
im_play = can1.create_image(50,400, anchor = "nw", image = image_play)
can1.image = image_play

image_stop = PhotoImage(file="img.png")
# image_stop = PhotoImage(file="stop.gif")
im_stop = can1.create_image(130,400, anchor = "nw", image = image_stop)
can1.image = image_stop

image_prev = PhotoImage(file="img.png")
# image_prev = PhotoImage(file="prev.gif")
im_prev = can1.create_image(210,400, anchor = "nw", image = image_prev)
can1.image = image_prev

image_next = PhotoImage(file="img.png")
# image_next = PhotoImage(file="next.gif")
im_next = can1.create_image(290,400, anchor = "nw", image = image_next)
can1.image = image_next

image_importer = PhotoImage(file="img.png")
# image_importer = PhotoImage(file="importer.gif")
im_importer = can1.create_image(370,400, anchor = "nw", image = image_importer)
can1.image = image_importer

can1.tag_bind(im_play, '<Button-1>', start_it)
can1.tag_bind(im_stop, '<Button-1>', stop_it)
can1.tag_bind(im_next, '<Button-1>', next_musique)
can1.tag_bind(im_prev, '<Button-1>', previous_musique)
can1.tag_bind(im_importer, '<Button-1>', importer_son)


fen1.mainloop()
fen1.destroy()
