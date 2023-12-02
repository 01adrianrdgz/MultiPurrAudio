#import modules
from tkinter import filedialog
from tkinter import *
import tkinter as tk
from PIL import *
import webbrowser
import pygame
import os

#root configuration
root = tk.Tk(className="MultiPurrAudio")
root.title("MultiPurrAudio")
root.geometry("500x330")
root.resizable(width=False, height=False)
root.config(background="#29528C")
icon = tk.PhotoImage(file="icon.png")
root.iconphoto(True,icon)

#initialize pygame's mixer
pygame.mixer.init()

#menu bar
menubar = tk.Menu(root)
root.config(menu=menubar)

#button commands
songs = []
current_song = ""
paused = False

def load_mus():
    global current_song
    root.directory = filedialog.askdirectory()
    
    for song in os.listdir(root.directory):
        name, ext = os.path.splitext(song)
        if ext == ".mp3":
            songs.append(song)
            
    for song in songs:
        songlist.insert("end", song)
        
    songlist.selection_set(0)
    current_song = songs[songlist.curselection()[0]]
    
def play_music():
    global current_song, paused
    
    if not paused:
        pygame.mixer.music.load(os.path.join(root.directory, current_song))
        pygame.mixer.music.play()
    else:
        pygame.mixer.music.unpause()
        paused = False
        
def pause_music():
    global paused
    pygame.mixer.music.pause()
    paused = True
    
def next_music():
    global current_song, paused
    
    try:
        songlist.selection_clear(0, END)
        songlist.selection_set(songs.index(current_song) + 1)
        current_song = songs[songlist.curselection()[0]]
        play_music()
    except:
        pass
        
def previous_music():
    global current_song, paused
    
    try:
       songlist.selection_clear(0, END)
       songlist.selection_set(songs.index(current_song) - 1)
       current_song = songs[songlist.curselection()[0]]
       play_music()
    except:
       pass
       
def about():
	tk.messagebox.showinfo(title="about this application", message="play all your favorite mp3 files using this app! Select a folder that contains mp3 files and they will be displayed in a list here. It's simple, yet cute software." "\n" "Proudly programmed in Ubuntu!!.")
	
def license():
        tk.messagebox.showinfo(title="license", message="This application is open source and licensed under the BSD-3 Clause license." "\n" "The mascot (MultiPurr3) and all of her artwork is licensed under CC-BY-SA 4.0.")
        
def gitrepo():
        webbrowser.open_new(r"https://github.com/01adrianrdgz/MultiPurrAudio")
        
#graphical menu bar
organize_menu = tk.Menu(menubar, tearoff=False)
menubar.add_cascade(label="organize", menu=organize_menu)
organize_menu.add_command(label="select folder", command=load_mus)

about_menu = tk.Menu(menubar, tearoff=False)
menubar.add_cascade(label="about", menu=about_menu)
about_menu.add_command(label="about this software", command=about)
about_menu.add_separator()
about_menu.add_command(label="license", command=license)
about_menu.add_separator()
about_menu.add_command(label="Github repository", command=gitrepo)

menubar.config(background="#29528C", foreground="#FFFFFF", activebackground="#43DD8D", activeforeground="#FFFFFF", borderwidth=0, font=("Monospace", 10))
organize_menu.config(background="#29528C", foreground="#FFFFFF", activebackground="#43DD8D", activeforeground="#FFFFFF", borderwidth=0, font=("Monospace", 10))
about_menu.config(background="#29528C", foreground="#FFFFFF", activebackground="#43DD8D", activeforeground="#FFFFFF", borderwidth=0, font=("Monospace", 10))

#box where the filenames of the mp3 files will appear
songlist = tk.Listbox(root, background="#C72867", foreground="#FFFFFF", highlightbackground="#C72867", borderwidth=0, width=100, height=15, font=("Monospace", 10))
songlist.pack()

#interaction buttons
play_btn_image = tk.PhotoImage(file="play.png")
pause_btn_image = tk.PhotoImage(file="pause.png")
next_btn_image = tk.PhotoImage(file="next.png")
previous_btn_image = tk.PhotoImage(file="previous.png")

#small image
smol_image = tk.PhotoImage(file="small.png")

#frame in which the buttons will be laid out
control_frame = tk.Frame(root)
control_frame.pack()
control_frame.config(background="#29528C")

#interactive graphical buttons
play_btn = tk.Button(control_frame, image=play_btn_image, borderwidth=0, background="#29528C", activebackground="#43DD8D", highlightbackground="#29528C", highlightcolor="#43DD8D", command=play_music)
pause_btn = tk.Button(control_frame, image=pause_btn_image, borderwidth=0, background="#29528C", activebackground="#43DD8D", highlightbackground="#29528C", highlightcolor="#43DD8D", command=pause_music)
next_btn = tk.Button(control_frame, image=next_btn_image, borderwidth=0, background="#29528C", activebackground="#43DD8D", highlightbackground="#29528C", highlightcolor="#43DD8D", command=next_music)
previous_btn = tk.Button(control_frame, image=previous_btn_image, borderwidth=0, background="#29528C", activebackground="#43DD8D", highlightbackground="#29528C", highlightcolor="#43DD8D", command=previous_music)

#small image
small = tk.Label(control_frame, image=smol_image)
small.config(background="#29528C")

#MultiPurr3, image and configuration
multip_img = tk.PhotoImage(file="multipurr3_idle.png")
multip = tk.Label(root, image=multip_img)
multip.config(background="#C72867")
multip.place(x=345, y=130)

#buttons position
play_btn.grid(row=0, column=1, padx=7, pady=10)
pause_btn.grid(row=0, column=2, padx=7, pady=10)
next_btn.grid(row=0, column=3, padx=7, pady=10)
previous_btn.grid(row=0, column=0, padx=7, pady=10)

#small image positions
small.grid(row=0, column=4, padx=7, pady=10)

#main loop
root.mainloop()
