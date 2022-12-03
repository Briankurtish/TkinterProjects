from tkinter import *
import customtkinter
from PIL import Image, ImageTk


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()

root.title('Cipher - BMI Calculator')
root.geometry("500x600")

# Define Entry Boxes

h_entry = customtkinter.CTkEntry(master=root, placeholder_text="Height in Inches",
                                 width=200, height=30, border_width=1, corner_radius=10)
h_entry.pack(pady=20)

w_entry = customtkinter.CTkEntry(master=root, placeholder_text="Width in Pounds",
                                 width=200, height=30, border_width=1, corner_radius=10)
w_entry.pack(pady=20)


# Buttons
button_1 = customtkinter.CTkButton(
    master=root, text="Calculate BMI", width=190, height=40, compound="top")
button_1.pack(pady=20)

button_2 = customtkinter.CTkButton(
    master=root, text="Clear Screen", width=190, height=40, fg_color="#D35B58", hover_color="#C77C78")
button_2.pack(pady=20)

# Add Result Label

results = customtkinter.CTkLabel(
    master=root, text="", font=("Helvetica", 28))
results.pack(pady=50)

root.mainloop()
