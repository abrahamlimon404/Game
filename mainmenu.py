# BY: Melvin Galicia Diaz and Abraham Limon
import tkinter as tk
import pygame

#Creates window and terms its size and placement, to match the game itself, and configures the window
window = tk.Tk()
window.resizable(0,0)
x= window.winfo_screenwidth()
y =window.winfo_screenheight()
x1 = round(x- (x*0.40))
y1= round(y- (y*0.40))
win_placmentx = round((x/2)-(x1/2))
win_placmenty = round((y/2)-(y1/2))
window.geometry(f'{x1}x{y1}+{win_placmentx}+{win_placmenty}') 
window.config(bg="light blue")

#Plays sounds/music
pygame.mixer.init()
pygame.mixer.music.load("1. Palm Tree Shade.wav")
pygame.mixer.music.play(loops=1)

#This function gets actived whent the user pressed the start button
def gamestart():
    #closes this mainmenue and start up the game and continues polaying music
    window.destroy()
    pygame.mixer.music.stop()
    pygame.mixer.music.load("14. The Riff.wav")
    pygame.mixer.music.play(loops=1)
    pygame.mixer.music.set_volume(-2)
    import Game
    
    



#creats a label and configures and places it
Label1 = tk.Label(window,text="Inside Color Matching",font = ("Comic Sans",40))
label1_width = Label1.winfo_reqwidth()
Label1_x = (x1/2) -(label1_width/2)
Label1.place(x=Label1_x ,rely=0.2)

#Creates a button that when pressed starts the gamestart function
button1 = tk.Button(window, text="Start",command=gamestart,font = ("Comic Sans",50))
button1_width = button1.winfo_reqwidth()
button1_x = (x1/2) -(button1_width/2)
button1.place(x=button1_x ,rely=0.4)

#Creates another button that when pressed exits the program
button3 = tk.Button(window, text="Quit",command= window.destroy,font = ("Comic Sans",50))
button3_width = button3.winfo_reqwidth()
button3_x = (x1/2) -(button3_width/2)
button3.place(x=button3_x ,rely=0.6)

window.mainloop()
