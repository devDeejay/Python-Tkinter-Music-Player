import os
import webbrowser
from tkinter import *
from tkinter import Tk
from tkinter import filedialog
import winsound
import pygame

#---------Making the Window and Frames----------
root = Tk()#defining the window and storing in the variable roo7t
frame1 = Frame(root)
menu = Menu(frame1)
root.config(menu=menu)

# ---------Various Functions-------------


root.filename=""
root.playlist = []
root.pauseFlag=False
i = 0

def newFile():
     winsound.Beep(2000,1000) #('frequency','duration')
def openFile():
    root.filename = filedialog.askopenfilename(initialdir = "/",title = "Select your cool music track",filetypes = (("mp3 Music Files","*.mp3"),("m4a Music Files","*.m4a")))
    root.playlist.append(root.filename)
    print(" Added " + root.filename)
    print(root.playlist)
    root.screenMessage.set("Good! Now Press on the Play Button")
def save():
    print("Saved")
def saveAs():
    print("Saved As")
def cut():
    print("Cuts the text")
def playMusic():
    try:
        if(root.pauseFlag == True):
            pygame.mixer.music.unpause()
        else:
            print("Playing")
            pygame.mixer.init()
            pygame.mixer.music.load(root.playlist[i])
            pygame.mixer.music.play()
            root.screenMessage.set("Playing " + root.playlist[i])
    except:
        print("Couldnot play the music")

def pauseMusic():
    pygame.mixer.music.pause()
    root.pauseFlag = True
    root.screenMessage.set("Paused")

def stopMusic():
    pygame.mixer.music.fadeout(600)
    root.screenMessage.set("End of Playback!")

def prevMusic():
    try:
        if(root.playlist[i-1]):
            pygame.mixer.music.load(root.playlist[i-1])
            pygame.mixer.music.play()
    except:
        print("No previous songs")

def nextMusic():
    try:
        if(root.playlist[i+1]):
            pygame.mixer.music.load(root.playlist[i+1])

    except:
        print("End of PlayList, Please add more songs")

def end():
    exit()
def help():
    webbrowser.open("https://telegram.me/trivedi")
def contact():
    webbrowser.open("https://telegram.me/trivedi")

#---------Creating Menus----------
subMenu = Menu(menu)
menu.add_cascade(label="Media", menu=subMenu)#Cascading Options on the ToolBar Such as: File Edit
subMenu.add_command(label="New File", command=newFile)
subMenu.add_command(label="Open File", command=openFile)
subMenu.add_separator()
subMenu.add_command(label="Save PlayList", command=save)
subMenu.add_command(label="SaveAs", command=saveAs)
subMenu.add_separator()
subMenu.add_command(label="exit", command=exit)

editMenu = Menu(menu)
menu.add_cascade(label="Edit",menu=editMenu)
editMenu.add_command(label="Cut",command=cut)
editMenu.add_command(label="Copy",command=cut)
editMenu.add_command(label="Paste",command=cut)

contactMenu = Menu(menu)
menu.add_cascade(label="Contact",menu=contactMenu)
contactMenu.add_command(label="Help",command=help)
contactMenu.add_command(label="Report Error",command=contact)
contactMenu.add_command(label="Contribute",command=cut)


#---------Creating Tri-color Labels----------
one = Label(root, text="Welcome", bg="orange",fg="white")
one.pack(fill=X)
two = Label(root, text="To Our First Music Player", bg="white",fg="blue")
two.pack(fill=X)
three = Label(root, text="Created By DevX", bg="green",fg="white")
three.pack(fill=X)

topFrame = Frame(root)#definig a frame that will contain the Widgets
topFrame.pack()
bottomFrame = Frame(root) #Similarly, definging the next Frame
bottomFrame.pack(side=BOTTOM)

#---------Various Buttons----------

button1 = Button(topFrame, text="Previous", fg="red", command=prevMusic) #Positioning Button as (<FrameName>,<Text to Appear>,<Text Color>)
button1.pack(side=LEFT,padx=5,pady=20)
button2 = Button(topFrame, text="Play",fg="green", command=playMusic)
button2.pack(side=LEFT,padx=5,pady=20)
button3 = Button(topFrame, text="Pause",fg="black", command=pauseMusic)
button3.pack(side=LEFT,padx=5,pady=20)
button5 = Button(topFrame, text="Stop",fg="red", command=stopMusic)
button5.pack(side=LEFT,padx=5,pady=20)
button4 = Button(topFrame, text="Next",fg="blue", command=nextMusic)
button4.pack(side=LEFT,padx=5,pady=20)

#-----------The status Bar--------------
root.screenMessage = StringVar()
label = Message( root, textvariable=root.screenMessage, relief=RAISED )
root.screenMessage.set("Welcome, to Tesy Music Player")
label.pack(side=BOTTOM,fill=X)


root.mainloop()#refreshing the window so that it stays on the screen
