import os
import customtkinter as ctk
import pyttsx3

root = ctk.CTk()
root.geometry("500x300")
root.resizable(False, False)
root.title("Adaptive Test Bot (ATB)")
entry = ctk.CTkEntry(root, width=350)
submit = ctk.CTkButton(root, width=150, text="submit")

submit.place(x=350, y=270)
entry.place(x=0, y=270)
root.mainloop()