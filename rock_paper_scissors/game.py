#Simple python program for Rock paper scissors game using Tkinter 

import random
import tkinter
from tkinter import *    # imports everything from tkinter module


throw = " "
result = " "
def winner(call):
    global throw
    global result
    if random.random() <=(1/3):
        throw="rock"
    elif (1/3)< random.random()<= (2/3):
        throw ="paper"
    else:
        throw="scissors"
    
    if (throw == "rock" and call == "paper") or (throw == "paper" and call == "scissors")or (throw == "scissors" and call == "rock"):
        result= "You Won!"
        print(result)
    elif throw == call:
        
        
        result ="It's a Draw"
        print(result)
    else:
        
        result = "You Lose!"
        print(result)
    
    out = tkinter.Label(win, width = 20, fg = "red", text = "Result: ")
    out.pack(side = "left")
    out.config(text='Computer did : '+ throw + "\n" + result) #output_console

global output



def pass_r():
	winner("rock")
	
	
def pass_p():
	winner("paper")
	
def pass_s():
	winner("scissors")
	


win = tkinter.Tk()   #creates a window

#initialising icons for rock,paper,and scissors
photo_r = PhotoImage(file = r"rock_1.png")
photo_p = PhotoImage(file = r"paper_1.png")
photo_s = PhotoImage(file = r"scissor.png")



#initialising buttons for rock,paper,scissors
rock = tkinter.Button(win, text ='Rock' ,image= photo_r, command=pass_r,background ="red")
paper = tkinter.Button(win, text ='Paper' ,image= photo_p, command=pass_p,background ="blue")
scissors = tkinter.Button(win, text ='Scissors',image= photo_s,  command=pass_s,background ="green")
rock.pack(side = "left")
paper.pack(side = "left")
scissors.pack(side = "left")


output = tkinter.Label(win, width = 20, fg = "red", text = "What's your call?")
output.pack(side = "left")


win.mainloop()  # infinite loop used to run the application, It waits for an event to occur and process the event as long as the window is not closed.