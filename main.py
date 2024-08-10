import os
import customtkinter as ctk
import sys
import subprocess

score = 0
sys.stdout = open("output.txt", "w")
root = ctk.CTk()
root.geometry("500x300")
root.title("Adaptive Test Bot (ATB)")
buttonpress = False
entry = ctk.CTkEntry(root, width=400)
label = ctk.CTkLabel(root, text=" ", wraplength=300)
def is_ready(cond):
    return(cond)
def main():
    global value
    global label
    global button
    global root
    global start
    start.destroy()
    label.configure(text="Welcome to the Adaptive Test Bot.\nthis bot will take your doubts and give questions with\n crystal clear explanations that can help alleviate\n and solve doubts in your mind.\nPlease enter your level(grade), and your subject/topic, separated by a space\n", require_redraw=True)

def main2():
    global start
    global label
    global question
    level = entry.get()
    global grade
    grade, subject = level.split(" ")
    question = subprocess.check_output(f"ollama run llama3.1 'give me an extremely hard multiple choice question for grade {grade} about {subject}, but dont provide the answer'", text=True, shell=True)
    label.configure(text=f"{question}")

def get_entry():
    global entry
    global grade
    global label
    value = entry.get()
    if value.lower() == "quit":
        root.destroy()
        quit()
    elif value.lower() == "answer":
        answer = subprocess.check_output(f"ollama run llama3.1 'give the answer for the question {question.replace("\n", " ")}, with an in-depth explanation suiting grade {grade} level.' ", text=True, shell=True)
        label.configure(text=answer)
    return value

command = ctk.CTkButton(root, width=100, text="Command", command=get_entry)
submit = ctk.CTkButton(root, width=100, text="Submit", command=main2)
start = ctk.CTkButton(root, text="start", command=main)
submit.place(x=400, y=270)
command.place(x=400, y=240)
entry.place(x=0, y=270)
start.place(x=190, y=150)
label.pack()
root.mainloop()
