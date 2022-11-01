def win():
    if "_" not in clue:
        return True

def replace(indices):
    global answerlist 
    global cluelist
    for n in indices:
        cluelist[n]=answerlist[n]
    return cluelist

def lose(lives):
      if lives == 0:
            global e
            e.delete(0,END)
            e.insert(0, f'You Lose! The answer was {answer}.')
            e.config(state='disabled')
            return True


def prompt_fun(instruction):
    global prompt
    prompt=f'{instruction}'
   

def game_engine():
        global answerlist   
        global cluelist
        indices = [i.start() for i in finditer(guess, answer)]
        global clue_no_whitespace
        cluelist=list(clue_no_whitespace)
        answerlist=list(answer)
        replace(indices)
        clue=" ".join(cluelist)
        clue_no_whitespace=clue.replace(" ","")
        return clue, clue_no_whitespace
    
def image_display():
    display[lives].pack_forget()
    display[lives].pack(side=TOP, expand=YES, fill=BOTH)

def my_click(event):
    e.delete(0, END)


def my_click_away(event):
    e.delete(0, END)
    e.insert(0, "Guess a letter > ")

def function_call(event=None):
    global guess
    root.wait_variable(submit_var)
    guess=e.get().lower()
    e.delete(0,END)
    e.insert(0, 'Guess a letter > ')
    return guess

def endgame(option):
    global pop
    global root
    if option==True:
        pop.destroy()
        root.destroy()
        os.startfile(__file__)
    elif option==False:
        pop.destroy()
        root.destroy()


from ast import Lambda
from tkinter import *
from PIL import Image, ImageTk
#import sys
#import os

#if os.environ.get('DISPLAY','') == '':
    #os.environ.__setitem__('DISPLAY', ':0.0')
print(__file__)
root=Tk()
root.maxsize(325, 445)
root.minsize(325, 445)                                            
root.title("Hangman")
root.iconbitmap('C:\\Users\\Liam\\Pictures\\hangman.ico')
frame1=LabelFrame(root)
frame1.grid(row=0, column=0, sticky='news',padx=2, pady=2)
frame2=LabelFrame(root)
frame2.grid(row=1, column=0, sticky='news', padx=2, pady=2) 
frame3=LabelFrame(root)
frame3.grid(row=2, column=0, sticky='news', padx=2, pady=2)
frame4=LabelFrame(root)
frame4.grid(row=3, column=0, sticky='news', padx=2, pady=2)
frame5=LabelFrame(root)
frame5.grid(row=4, column=0, sticky='news', padx=2, pady=2)

lives=6
prompt='Lets play...'
lives_list=list(range(7))
display=list(range(7))
for i in range(7):
    lives_list[i]=ImageTk.PhotoImage(Image.open(f"C:\\Users\\Liam\\Pictures\\lives_{i}.png"))
    display[i]=Label(frame1, image=lives_list[i], anchor=CENTER)
display[lives].pack(side=TOP, expand=YES, fill=BOTH)
e=Entry(frame3, width=45, bg="white", fg="black", borderwidth=10)
e.grid(row= 2, column=0, columnspan=3, padx=10, pady=2)
message=Label(frame4, text=f'{prompt}', bd=1, anchor=CENTER)
message.grid(row=4, column=0, columnspan=3)
status=Label(frame5, text=f"You have {lives} lives remaining.", bd=1, relief=SUNKEN, anchor=E)
status.grid(row=3, column=0, columnspan=3, sticky=W+E)
e.insert(0, 'Guess a letter > ')
e.bind('<Button-1>', my_click)
e.bind('<FocusOut>', my_click_away)
submit_var=StringVar()
e.bind('<Return>', lambda e: submit_var.set(1))


# establish or import dictionary

from nltk.corpus import words
dictionary_1=words.words()
#print(type(dictionary_1))
#print(len(words.words()))
  
###dictionary_2={
# "1": "apple",
# "2": "boat",
# "3": "coaster",
# "4": "dance",
# "5": "elephant",
# "6": "forest"
# }
###
# select random answer from dictionary

import os
from random import choice
from re import L, finditer

# number_of_keys=len(dictionary_2)
# range=range(1, number_of_keys+1)
# n=choice(range)
# answer=dictionary_2[str(n)]

number_of_keys=len(dictionary_1)
range=range(1, number_of_keys+1)
n=choice(range)
answer=dictionary_1[n]
while len(answer)>8:
    n=choice(range)
    answer=dictionary_1[n]

# show clue and prompt input

number_of_letters=len(answer)
nn=[1]*number_of_letters
clue=""
for i in nn:
    clue+=("_ ") 
clue_no_whitespace=clue.replace(" ","")
clue_bar=Label(frame2, text=f"{clue}", bg='black', fg='green', font=('comic sans', 32), borderwidth=2, relief=SOLID, anchor=CENTER)
clue_bar.pack(side=TOP, expand=YES, fill=BOTH)
function_call()

while '_' in clue:
    # function to replace '_' in clue with chosen letter
    if guess in answer and len(guess)==1:
       clue, clue_no_whitespace= game_engine()
       clue_bar.config(text=f'{clue}')
       clue_bar.pack(side=TOP, expand=YES, fill=BOTH)
       flag=win()
       if flag==True:
            prompt_fun(f"You win!")
            message.grid_forget()
            message=Label(frame4, text=f'{prompt}', bd=1, anchor=CENTER)
            message.grid(row=4, column=0, columnspan=3)
            e.config(state='disabled')
            break
       prompt_fun(f"Nice! Guess again...")
       message.grid_forget()
       message=Label(frame4, text=f'{prompt}', bd=1, anchor=CENTER)
       message.grid(row=4, column=0, columnspan=3)
       function_call()
                               
    # funtion to take life away from player if guess is incorrect
    elif guess not in answer and len(guess)==1 and guess.isdigit()==False:
        display[lives].pack_forget()
        status.grid_forget()
        lives-=1
        display[lives].pack(side=TOP, expand=YES, fill=BOTH)
        status=Label(frame5, text=f"You have {lives} lives remaining.", bd=1, relief=SUNKEN, anchor=E)
        status.grid(row=3, column=0, columnspan=3, sticky=W+E)
        if lose(lives)==True:
            prompt_fun(f"You lose!")
            message.grid_forget()
            message=Label(frame4, text=f'{prompt}', bd=1, anchor=CENTER)
            message.grid(row=4, column=0, columnspan=3)
            break
        prompt_fun(f"Incorrect! Guess again...")
        message.grid_forget()
        message=Label(frame4, text=f'{prompt}', bd=1, anchor=CENTER)
        message.grid(row=4, column=0, columnspan=3)
        function_call()

    # for game syntax errors
    elif len(guess)!=1:
        prompt_fun('Guess one letter at a time.')
        message.grid_forget()
        message=Label(frame4, text=f'{prompt}', bd=1, anchor=CENTER)
        message.grid(row=4, column=0, columnspan=3)
        function_call()
    elif guess.isdigit()==True:
        prompt_fun('You can only guess letters.')
        message.grid_forget()
        message=Label(frame4, text=f'{prompt}', bd=1, anchor=CENTER)
        message.grid(row=4, column=0, columnspan=3)
        function_call()   


pop=Toplevel(root)
pop.title("Hangman")
pop.maxsize(250, 150)
pop.minsize(250, 150)
play_again=Label(pop, text=' Play again?', font=('comic sans', 32),anchor=CENTER)
play_again.grid(row=0, column=0, columnspan=2)
endgame_var=StringVar()
yes=Button(pop, text="Yes", font=('comic sans', 16),  command=lambda: endgame(True))
yes.grid(row=1, column=0, padx=10, pady=50)
no=Button(pop, text="No", font=('comic sans', 16), command=lambda: endgame(False))
no.grid(row=1, column=1, padx=10, pady=50)


root.mainloop() 