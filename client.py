
import socket
from tkinter import *
from  threading import Thread
from PIL import ImageTk, Image
import random

screen_width = None
screen_height = None

SERVER = None
PORT = None
IP_ADDRESS = None


canvas1 = None

playerName = None
nameEntry = None
nameWindow = None

def saveName():
    global SERVER
    global playerName
    global nameWindow
    global nameEntry
    playerName = nameEntry.get()
    nameEntry.delete(0, END)
    nameWindow.destroy()
    SERVER.send(playerName.encode())

def askPlayerName():
    global playerName
    global nameEntry
    global nameWindow
    global canvas1
    global screen_width
    global screen_height

    nameWindow= Tk()
    nameWindow.title("LUDO LADDER")
    nameWindow.attributes('-fullscreen', True)
    screen_width = nameWindow.winfo_screenwidth()
    screen_height = nameWindow.winfo_screenheight()

    bg = ImageTk.PhotoImage(file="./assets/background.png")
    canvas1 = Canvas(nameWindow, width=500, height=500)
    canvas1.pack(fill="both", expand=True)

    canvas1.create_image(0,0, image=bg, anchor="nw")
    canvas1.create_text(screen_width/2, screen_height/5, text="enter name", fill="white", font=("Chalkboard SE", 100))

    nameEntry = Entry(nameWindow, width=15, justify='center', bg="white", bd=5, font=("Chalkboard SE", 50))
    nameEntry.place(x=screen_width/2-220, y=screen_height/4+100)

    button = Button(nameWindow, width=15, text="save", bg="green", bd=5, font=("Chalkboard SE", 50), command=saveName)
    button.place(x=screen_width/2-100, y=screen_height/2-30)

    nameWindow.resizable(True, True)
    nameEntry.mainloop()

def setup():
    global SERVER
    global PORT
    global IP_ADDRESS

    PORT  = 5000
    IP_ADDRESS = '127.0.0.1'

    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.connect((IP_ADDRESS, PORT))


    # Creating First Window
    askPlayerName()




setup()
