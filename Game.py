BY:Abraham Limon and Melvin Galicia Diaz
import tkinter 
import random 
from playsound import playsound
import pygame

#Creating the array of colors and basic variables that will be used
colours = ['Red','Blue','Green','Pink','Black', 'Yellow','Orange','White','Purple','gray','teal'] 
score = 0
timeleft = 30
attempts = 0
counter1 = 0


#This will be actived when the user presses enter or return on thier keybored therfore the 'event' argument
def startGame(event):
    global counter1
    global scorelabel
    #when the game starts this will call the coutdown function
    if timeleft == 30:
        countdown()

    #starts the next color function
    nextColor() 

    #places the label that tells the player what the color is
    scoreLabel.place(relx=0.064,rely=0.22)

    counter1+=1
counter = 0

# this function changes the label that that displayes the color and once the time has run out will raise the game over screen 
def nextColor():
    global score 
    global timeleft
    global attempts
    global x
    global y
    global lastLabel
    global counter
    
    #this determins if the correct answer matches with the answer given by the user and adds 1 to the score and wiether its wrong or not will add 1 to the number of attempts, 
    # also playes audio if answer is wrong or correct
    if timeleft > 0:
        entry1.focus_set()
        if entry1.get().lower() == colours[1].lower():
            score += 1
            attempts +=1
            playsound("Audio1.mp3")
        else:
            if counter > 1:
                playsound("Audio2.mp3")
                attempts +=1
            counter +=5
        # This delets the phrase "Press enter to start" so that the player can inout thier answer 
        entry1.delete(0, tkinter.END)

        #shuffles/randomized the list of all the colors
        random.shuffle(colours)

        # Tells the player what color they need to input for thier answer
        label.configure(fg = str(colours[1]), text = str(colours[0]),bg='sky blue',borderwidth= 3,relief='solid')

        #This will update the score and number of attempts taken by the user
        scoreLabel.configure(text = "Score: " + str(score),bg='sky blue',borderwidth= 2,relief='solid',padx =10,pady=10,width =12) 
        thelabel. configure(text = 'Attempts:  ' + str(attempts),bg = 'sky blue',borderwidth= 2,relief='solid',font = ('Helvetica', 30),padx =10,pady=10)
        
    #this will make the game over screen pop up once ther is no time left on the timer
    if timeleft== 0:

        #Raises the game over screen
        frame.tkraise()
        # x is the user screen width and y is the users screen height
        x -= 10
        y -=30

        #Variable with the string x 
        z = ('x')

        #calculates the size of the game over frame
        a =(x/2)
        aa =round(a-15)
        b = ((y/2)-(3/2))
        
        #turns the measurements made for the game over screen into a string with the foramt: ('widthxhieght+positionx+positiony')
        screensize = (f'{x}{z}{y}+0+10')
        
        #places the frame relative to the root already created
        frame.place(x=0, y=0, relwidth=1.0, relheight=1.0)

        #changes the size and location of the frame
        root.geometry(screensize)

        #to position the game over label, same method used to place the program in the center of the users screen
        gameOverLabelWidth= GameOverLabel.winfo_reqwidth()
        Game_over_x = (x/2) -(gameOverLabelWidth/2)
        GameOverLabel.place(x=Game_over_x ,rely=0.5)
        
        #This is another score label that will appear of the new frame and tells the user thier score
        scorelabel2 =tkinter.Label(frame,text = "Score: " + str(score),bg='sky blue',borderwidth= 2,relief='solid',font = ('ariel',25),width = 10)
        scorelabel2.place(relx= 0.32,rely = 0.37)

        #Creats a label for the attempts take by the player and places it on the new frame
        w= 'Attemps: ' + str(attempts)
        thelabel2 =tkinter.Label(frame,bg = 'light blue',text = w,borderwidth= 2,relief='solid',font = ('ariel',25))
        thelabel2.place(relx= 0.58,rely = 0.37)
        
        #This will display the percentage of the players score by dividing thier score by their attempts
        xyz = (round(int(score)/int(attempts)*100))
        xyz1 = (str(xyz)+'%')
        xyz1.replace(' ','')
        lastLabel.configure(text =xyz1,bg = 'light blue',borderwidth= 2,relief='solid',font = ('ariel',50),padx =10,pady=10)
        #calculates were this label will be placed, and places it
        PercentScore_width = lastLabel.winfo_reqwidth()
        PercentScore_x = (x/2)-(PercentScore_width/2)
        lastLabel.place(x = PercentScore_x, rely = 0.37)

        #Stops music
        pygame.mixer.music.stop()

  # this  function is changes the timeLabel  so that it is changeing the time left    
def countdown():
    global timeleft
    if timeleft > 0:
        timeleft -= 1
        timeLabel.config(text = "Time left: "+ str(timeleft),bg='sky blue',borderwidth= 2,relief='solid')
        timeLabel.after(1000, countdown) 

#creating a window with the title 'Color Game'
root = tkinter.Tk() 
root.title("COLOR GAME") 

#Finds the size of the users screen
x= root.winfo_screenwidth()
y= root.winfo_screenheight()

#Takes 40% of the users screen size
x1 = round(x- (x*0.40))
y1= round(y- (y*0.40))

#using the new window size(40% of the users screen size) this will help center the window in the geomtry function
win_placmentx = round((x/2)-(x1/2))
win_placmenty = round((y/2)-(y1/2))

#placing the window in the center of the users screen
root.geometry(f'{x1}x{y1}+{win_placmentx}+{win_placmenty}') 

#making the background of the window light blue
root.configure(bg = 'light blue')

#Instructions label
instructions = tkinter.Label(root, text = "Type in the color of the words, and NOT the word!",font = ('ariel', 31),bg='sky blue',borderwidth= 2,relief='solid',width =40) 
instructions.pack(pady= 10)

#Will display the number of correct answers the user has made
scoreLabel = tkinter.Label(root, text = "Press enter to start", font = ('Helvetica', 30),bg='sky blue',borderwidth= 2,relief='solid',width =15,padx =10,pady=10) 
scoreLabel.pack(pady= 10,padx = 10)

#Label that will display the number of attempts the player has made
thelabel = tkinter.Label(bg = 'light blue', font = ('Helvetica', 30),width =10,padx =10,pady=10)
thelabel.place(relx= 0.68,rely = 0.22)

# This label will show how much time is left
timeLabel = tkinter.Label(root, text = "Time left: " +str(timeleft), font = ('Helvetica', 24),bg='sky blue',borderwidth= 2,relief='solid',padx =10,pady=10) 				
timeLabel.pack(pady= 20,padx = 20)

#Label that will show the words once the game has started
label = tkinter.Label(root, font = ('Helvetica', 70),bg = 'light blue',padx =30,pady=30,height = 1) 
label.pack(pady= 30,padx =30)

#Entry Box
entry1 = tkinter.Entry(root,borderwidth= 3,relief='solid') 
entry1 = tkinter.Entry(justify='center',font = ('Helvetica', 60))
entry1.pack(pady=10)
entry1.insert(0,"Click Enter to Start",)

#Creating another frame for the game over screen
frame= tkinter.Frame(root, bg = 'red')

#Game over label thats on the new frame
GameOverLabel = tkinter.Label(frame, text ='GAME OVER',height = 3,width = 30,font = ('Ariel',30),bg= 'dark red',fg ='White')

#This label is on the game over frame and will display the percentage of the correct answer / the attempts made
lastLabel= tkinter.Label(frame)

#Makes it so that once this python get started up by the mainmenue.py it is focused on this prgoram
root.after(1, lambda: root.focus_force())

#Makes the Enter or return button on the keybored start the 'startgame' function
root.bind('<Return>',startGame) 

root.mainloop() 
