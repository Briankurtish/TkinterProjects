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


root.mainloop()
