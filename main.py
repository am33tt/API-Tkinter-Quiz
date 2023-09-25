from tkinter import *
import requests
import random
from urllib.parse import unquote
from tkinter import messagebox



window = Tk()
window.title('Quiz')
window.config(padx=50, pady=50, background='#CEDEBD')

data = None
quest = None
answ = None
score = 0
list = []


     

def rest_question():
    global data
    response = requests.get(url='https://opentdb.com/api.php?amount=50&type=boolean&encode=url3986')
    data = response.json()


def read():
        global quest, answ, list
        question = random.choice(data['results'])
        quest = question['question']
        quest = unquote(quest)
        if quest in list:
            question = random.choice(data['results'])
            quest = question['question']
            quest = unquote(quest) 
             
        answ = question ['correct_answer']

def start():
    new_ques()

def new_ques():
      canvas.config(bg='white')
      read()
      canvas.itemconfig(text, text=f'{quest}')

def right():
    global answ, score
    if answ == "True":
        canvas.config(bg='green')
        canvas.after(1000, new_ques)
        score += 1
        score_label.config(text=f'Score: {score}')
        list.append(quest)
    else:
        canvas.config(bg='red')
        canvas.after(1000, new_ques)

def wrong(): 
    global answ, score
    if answ == "False":
        canvas.config(bg='green')
        canvas.after(1000, new_ques)
        score += 1
        score_label.config(text=f'Score: {score}')
        list.append(quest)
    else:
        canvas.config(bg='red')
        canvas.after(1000, new_ques)



response = requests.get(url='https://opentdb.com/api.php?amount=50&type=boolean&encode=url3986')
data = response.json()


score_label = Label(text=f'Score: {score}', font=('arial', 8, 'bold'), bg='#CEDEBD')
score_label.grid(column=2, row=0, pady=10,)

canvas = Canvas(window, height=300, width=400, bg='White')
canvas.grid(column=0, row=1, columnspan=3)

right1 = Button(text='✅', font=('arial',20,'bold'), command=right)
right1.grid(row=2, column=0, pady=20)

wrong1 = Button(text='❌', font=('arial',20,'bold'), command=wrong)
wrong1.grid(row=2, column=2)

quiz_start = Button(text='Start', font=('arial', 10, 'bold'), command=start)
quiz_start.grid(column=1, row=2)

new_q = Button(text='Refresh Questions', font=('arial', 10, 'bold'), command=rest_question)
new_q.grid(column=0, row=3, columnspan=3)


text = canvas.create_text(200,150,font=('arial', 15, ' bold italic'),text='Welcome to the\nQUIZZZ App', width=370)


window.mainloop()