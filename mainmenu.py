import tkinter as tk
import pygame

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
pygame.mixer.init()
pygame.mixer.music.load("1. Palm Tree Shade.wav")
pygame.mixer.music.play(loops=1)
def gamestart():
    window.destroy()
    pygame.mixer.music.stop()
    pygame.mixer.music.load("14. The Riff.wav")
    
    pygame.mixer.music.play(loops=1)
    pygame.mixer.music.set_volume(-2)
    import Game


Label1 = tk.Label(window,text="Inside Color Matching",font = ("Comic Sans",40)).place(x=350,y=40)
button1 = tk.Button(window, text="Start",command= gamestart,font = ("Comic Sans",50)).place(x=500,y=150)
button3 = tk.Button(window, text="Quit",command= window.destroy,font = ("Comic Sans",50)).place(x=500,y=450)

window.mainloop()