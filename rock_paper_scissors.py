import random    #random module to select a random variable
import tkinter as tk
from tkinter import*

window=tk.Tk()   #creating a tk window
window.geometry("655x570")  #geometry of the window (width x height)
window.config(bg="light green") #colour of the window
window.title("Rock Paper Scissors Game....")  #title of the window

frame=tk.Frame(master=window) #a frame organize widgets and master represents the parent window.

your_score=0 #your intial score is 0
comp_score=0 #computer's intial score is 0

#RPS is Rock Paper Scissors
your_choice=""  #initial choice RPS is null
comp_choice=""  #initial choice RPS is null

#defining a user define function choice to number to count the score
def choice_to_number(choice): #def1

    x={"ROCK":0,"PAPER":1,"SCISSORS":2}  #dict is used were key is rock and value is 0
    return x[choice]

#defining a user define function number to choice to compare the your and computer choices
def number_to_choice(number): #def2
    x={0:"ROCK",1:"PAPER",2:"SCISSORS"}
    return x[number]

#defining a user define function for comp to choice 
def random_comp_choice():  #def3
    return random.choice(["ROCK","PAPER","SCISSORS"]) #giving random choices to the computer

def result(human_choice,comp_choice): #def4
    global your_score   #global is used to create a global variable and make changes to the variable in a local context
    global comp_score   

    you=choice_to_number(human_choice)  #from def1
    comp=choice_to_number(comp_choice)  #from def1

    if(you==comp):
        print("Tt was Tie!!!!")
    elif((you-comp)%3==1):
        print("You win!!!")
        your_score+=1   #your_score=your_score+1
    else:
        print("Computer Wins!!!")
        comp_score+=1   #comp_score=comp_score+1 
    text_area = tk.Text(master=window,height=16,width=47,font=("Algerian",18),bg="lavender")  #colour of the text area in the window (bg is background)
    answer ="\n                                 Your Choice: {uc} \n                                Computer Choice: {cc} \n\n                                Your Score : {u} \n\n                                Computer Score : {c} \n\n\n                   So Let's PLAY ROCK PAPER SCISSORS✂!!!".format(uc=your_choice,cc=comp_choice,u=your_score,c=comp_score)
    text_area.insert(tk.END,answer)  # .insert() insert a string and tk.END ....
    text_area.place(x=0,y=278) #here x and y are the point on the axis which are in pixels
    
    
rock_img=PhotoImage(file=r"C:\Users\sahil\Desktop\django web dev\RockPaperScissors\RockPaperScissors\rock.png")  #location of the image rock
paper_img=PhotoImage(file=r"C:\Users\sahil\Desktop\django web dev\RockPaperScissors\RockPaperScissors\paper.png")  #location of the image paper
scissors_img=PhotoImage(file=r"C:\Users\sahil\Desktop\django web dev\RockPaperScissors\RockPaperScissors\scissors.png")  #location of the image scissors
def ROCK():
    global your_choice   #global variable to make changes to the variable in a local context
    global comp_choice
    your_choice="ROCK"
    comp_choice=random_comp_choice() #def3
    result(your_choice,comp_choice)

def PAPER():
    global your_choice   #global variable to make changes to the variable in a local context
    global comp_choice
    your_choice="PAPER"
    comp_choice=random_comp_choice()  #def3
    result(your_choice,comp_choice)

def SCISSORS():
    global your_choice
    global comp_choice
    your_choice="SCISSORS"
    comp_choice=random_comp_choice()  #def3
    result(your_choice,comp_choice)

#creating button for rock
button1=tk.Button(image=rock_img,text="Choose ROCK!",font="Algerian",fg="dark orange",height=270,width=220,command=ROCK,compound=TOP)  #button is used to display button on window 
button1.place(x=0,y=1)    # place() set the widgets by placing them in a specific position in the parent widget.
                          # x, y − Horizontal and vertical offset in pixels.

#creating button for paper
button2=tk.Button(image=paper_img,text="Choose PAPER!",font="Algerian",fg="red",height=270,width=220,command=PAPER,compound=TOP) #button is used to display button on window
button2.place(x=200,y=1)  # place() set the widgets by placing them in a specific position in the parent widget.
                          # x, y − Horizontal and vertical offset in pixels.

#creating button for scissors
button3=tk.Button(image=scissors_img,text="Choose SCISSORS!",font="Algerian",fg="green",height=270,width=226,command=SCISSORS,compound=TOP)  #button is used to display button on window
button3.place(x=420,y=1)  # place() set the widgets by placing them in a specific position in the parent widget.
                          # x, y − Horizontal and vertical offset in pixels.
#window.mainloop() tells Python to run the Tkinter event loop.
#(this method listens for events i.e, button clicks  or keypresses)
window.mainloop()
