import os
import customtkinter as ctk
import subprocess
import pyttsx3
import sys

root = ctk.CTk()
root.geometry("500x300")
root.resizable(False, False)
root.title("Adaptive Test Bot (ATB)")
buttonpress = False
entry = ctk.CTkEntry(root, width=400)
label = ctk.CTkLabel(root, text=" ")

def is_ready(cond):
    if cond:
        return True
    else:
        return False
def main():
    global value
    global label
    global button
    global root
    global start
    label.configure(text="Welcome to the Adaptive Test Bot.\nthis bot will take your doubts and give questions with\n crystal clear explanations that can help alleviate\n and solve doubts in your mind.\nPlease enter your level(grade), and your subject, separated by a space\n", require_redraw=True)

def main2():
    global start
    global label
    start.destroy()
    level = entry.get()
    grade, subject = level.split(" ")
    question = subprocess.check_output(f"ollama run llama3.1 'give me an extremely hard multiple choice question for grade {grade} about {subject}, but dont provide the answer'", shell=True, text=True)
    label.configure(text=f"{question}")

def get_entry():
    global button
    global value
    global entry
    value = entry.get()
    button = True
    return value

submit = ctk.CTkButton(root, width=100, text="Submit", command=main2)
start = ctk.CTkButton(root, text="start", command=main)

submit.place(x=400, y=270)
entry.place(x=0, y=270)
start.place(x=250, y=220)
label.pack()
root.mainloop()