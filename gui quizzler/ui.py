
from quiz_brain import QuizBrain
from tkinter import *
THEME_COLOR = "#375362"
BG1="white"
class QuizInterface():
    def __init__(self,quiz_brain:QuizBrain):
        self.quizbrain=quiz_brain
        self.window=Tk()
        self.window.title("Quizzery")
        self.window.config(width=600,height=500,padx=20,pady=20,bg=THEME_COLOR)

        self.scorelabel=Label(text="Score:0", fg="white",bg=THEME_COLOR)
        self.scorelabel.grid(row=0,column=1)

        self.canvas=Canvas(width=300,height=250,bg=BG1)
        self.questiontxt=self.canvas.create_text(
            150,
            125,
            width=250,
            text="question",
            fill=THEME_COLOR,
            font=("Ariel",20,"italic")) 
        self.canvas.grid(row=1,column=0,columnspan=2,pady=50) 

        self.rightimg=PhotoImage(file="images/true.png")
        self.button1 = Button(image=self.rightimg, highlightthickness=0,command=self.true_pressed) 
        self.button1.grid(row=2,column=0)

        self.wrongimg=PhotoImage(file="images/false.png")
        self.button2 = Button(image=self.wrongimg, highlightthickness=0,command=self.false_pressed) 
        self.button2.grid(row=2,column=1)
       
        self.get_next_question()

        self.window.mainloop()
    
    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quizbrain.still_has_questions():
            self.scorelabel.config(text=f"Score: {self.quizbrain.score}")
            q_text = self.quizbrain.next_question()
            self.canvas.itemconfig(self.questiontxt, text=q_text)
        else:
            self.canvas.itemconfig(self.questiontxt, text="You've reached the end of the quiz.")
            self.button1.config(state="disabled")
            self.button2.config(state="disabled")

    def true_pressed(self):
        self.give_feedback(self.quizbrain.check_answer("True"))

    def false_pressed(self):
        is_right = self.quizbrain.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
            
        