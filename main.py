import os
import customtkinter as ctk
import pyttsx3
from time import sleep

root = ctk.CTk()
root.geometry("500x300")
root.resizable(False, False)
root.title("Adaptive Test Bot (ATB)")
entry = ctk.CTkEntry(root, width=400)
submit = ctk.CTkButton(root, width=100, text="Submit")
label = ctk.CTkLabel(root)
label.configure(text="Welcome to the Adaptive Test Bot.")
sleep(2)

submit.place(x=350, y=270)
entry.place(x=0, y=270)
root.mainloop()