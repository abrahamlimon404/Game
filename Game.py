import tkinter 
import random 
from pygame import mixer
from tkinter.constants import CENTER, DISABLED
mixer.init()
correct_answer_mp3=mixer.Sound("Audio1.mp3")
wrong_answer_mp3 = mixer.Sound('Audio2.mp3')

colours = ['Red','Blue','Green','Pink','Black', 'Yellow','Orange','White','Purple','gray','teal'] 
score = 0
timeleft = 30 
attempts = 0
counter1 = 0
mixer.init()
correct_answer_mp3 = mixer.Sound('Audio1.mp3')
wrong_anwer_mp3 = mixer.Sound('Audio2.mp3')
def startGame(event):
    global counter1
    startup = mixer.Sound('startaudio.mp3')
    if counter1 == 0:
        mixer.Sound.play(startup)
    global scorelabel
    
    if timeleft == 30:
        countdown()
    nextColour() 
    scoreLabel.place(relx=0.064,rely=0.22)
    counter1+=1
counter = 0
def nextColour():
    global score 
    global timeleft
    global attempts
    global x
    global y
    global lastLabel
    global counter
    
    if timeleft > 0:
        entry1.focus_set()
        if entry1.get().lower() == colours[1].lower():
            score += 1
            attempts +=1
            
            mixer.Sound.play(correct_answer_mp3)
        else:
            if counter > 1:
                
                attempts +=1
                mixer.Sound.play(wrong_answer_mp3)
            counter +=5
            
        entry1.delete(0, tkinter.END)
        random.shuffle(colours)
        label.configure(fg = str(colours[1]), text = str(colours[0]),bg='sky blue',borderwidth= 3,relief='solid')
        scoreLabel.configure(text = "Score: " + str(score),bg='sky blue',borderwidth= 2,relief='solid',padx =10,pady=10,width =12) 
        thelabel. configure(text = 'Attempts:  ' + str(attempts),bg = 'sky blue',borderwidth= 2,relief='solid',font = ('Helvetica', 30),padx =10,pady=10)
        

    if timeleft== 0:
        frame.tkraise()
        
        x -= 10
        y -=30
        z = ('x')

        a =(x/2)
        aa =round(a-15)
        b = ((y/2)-(3/2))
        
        
        screensize = (f'{x}{z}{y}+0+10')
        
        frame.place(x=0, y=0, relwidth=1.0, relheight=1.0)

        root.geometry(screensize)
        gameOverLabelWidth= GameOverLabel.winfo_reqwidth()
        
        
        Game_over_x = (x/2) -(gameOverLabelWidth/2)
        GameOverLabel.place(x=Game_over_x ,rely=0.5)
        


        scorelabel2 =tkinter.Label(frame,text = "Score: " + str(score),bg='sky blue',borderwidth= 2,relief='solid',font = ('ariel',25),width = 10)
        scorelabel2.place(relx= 0.32,rely = 0.37)
        w= 'Attemps: ' + str(attempts)
        thelabel2 =tkinter.Label(frame,bg = 'light blue',text = w,borderwidth= 2,relief='solid',font = ('ariel',25))
        thelabel2.place(relx= 0.58,rely = 0.37)
        
        
        xyz = (round(int(score)/int(attempts)*100))
        xyz1 = (str(xyz)+'%')
        xyz1.replace(' ','')
        lastLabel.configure(text =xyz1,bg = 'light blue',borderwidth= 2,relief='solid',font = ('ariel',50),padx =10,pady=10)
        PercentScore_width = lastLabel.winfo_reqwidth()
        PercentScore_x = (x/2)-(PercentScore_width/2)
        
        lastLabel.place(x = PercentScore_x, rely = 0.37)

        
def countdown():
    global timeleft
    if timeleft > 0:
        timeleft -= 1
        timeLabel.config(text = "Time left: "+ str(timeleft),bg='sky blue',borderwidth= 2,relief='solid')
        timeLabel.after(1000, countdown) 


root = tkinter.Tk() 
root.title("COLOR GAME") 

x= root.winfo_screenwidth()
y =root.winfo_screenheight()

x1 = round(x- (x*0.40))
y1= round(y- (y*0.40))

win_placmentx = round((x/2)-(x1/2))
win_placmenty = round((y/2)-(y1/2))


root.geometry(f'{x1}x{y1}+{win_placmentx}+{win_placmenty}') 

root.configure(bg = 'light blue')


instructions = tkinter.Label(root, text = "Type in the color of the words, and NOT the word!",font = ('ariel', 31),bg='sky blue',borderwidth= 2,relief='solid',width =40) 
instructions.pack(pady= 10)

scoreLabel = tkinter.Label(root, text = "Press enter to start", font = ('Helvetica', 30),bg='sky blue',borderwidth= 2,relief='solid',width =15,padx =10,pady=10) 
scoreLabel.pack(pady= 10,padx = 10)

thelabel = tkinter.Label(bg = 'light blue', font = ('Helvetica', 30),width =10,padx =10,pady=10)
thelabel.place(relx= 0.68,rely = 0.22)

timeLabel = tkinter.Label(root, text = "Time left: " +str(timeleft), font = ('Helvetica', 24),bg='sky blue',borderwidth= 2,relief='solid',padx =10,pady=10) 				
timeLabel.pack(pady= 20,padx = 20)

label = tkinter.Label(root, font = ('Helvetica', 70),bg = 'light blue',padx =30,pady=30,height = 1) 
label.pack(pady= 30,padx =30)

entry1 = tkinter.Entry(root,borderwidth= 3,relief='solid') 
root.bind('<Return>',startGame) 
entry1 = tkinter.Entry(justify='center',font = ('Helvetica', 60))
entry1.pack(pady=10)
entry1.insert(0,"Click Enter to Start",)

frame= tkinter.Frame(root, bg = 'red')
GameOverLabel = tkinter.Label(frame, text ='GAME OVER',height = 3,width = 30,font = ('Ariel',30),bg= 'dark red',fg ='White')


lastLabel= tkinter.Label(frame)

root.mainloop() 
