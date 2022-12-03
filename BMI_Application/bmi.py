from tkinter import *
import customtkinter
from PIL import Image, ImageTk


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()

root.title('Cipher - BMI Calculator')
root.geometry("500x600")


def clear_screen():
    h_entry.delete(0, END)
    w_entry.delete(0, END)
    results.configure(text="")


def get_Bmi():
    # Calculate BMI
    #(weight_pounds/height_inches^2) * 703

    our_height = int(h_entry.get()) * int(h_entry.get())
    our_weight = int(w_entry.get())
    bmi = (our_weight/our_height)*703
    bmi_rounded = round(bmi, 1)

    results.configure(text=f"{str(bmi_rounded)}")

    # Logic
    if bmi_rounded < 18.5:
        results.configure(
            text=f"{str(bmi_rounded)}\nUnderweight", text_color="#54b1e1")
    elif bmi_rounded >= 18.5 and bmi_rounded <= 24.9:
        results.configure(
            text=f"{str(bmi_rounded)}\nNormal", text_color="#b3b686")
    elif bmi_rounded >= 25.0 and bmi_rounded <= 29.9:
        results.configure(
            text=f"{str(bmi_rounded)}\nOverweight", text_color="#fed429")
    elif bmi_rounded >= 30 and bmi_rounded <= 34.9:
        results.configure(
            text=f"{str(bmi_rounded)}\nObese", text_color="#fbaf42")
    elif bmi_rounded >= 35:
        results.configure(
            text=f"{str(bmi_rounded)}\nExtreme Obese", text_color="#f25356")

    # Define Entry Boxes


h_entry = customtkinter.CTkEntry(master=root, placeholder_text="Height in Inches",
                                 width=200, height=30, border_width=1, corner_radius=10)
h_entry.pack(pady=20)

w_entry = customtkinter.CTkEntry(master=root, placeholder_text="Width in Pounds",
                                 width=200, height=30, border_width=1, corner_radius=10)
w_entry.pack(pady=20)


# Buttons
button_1 = customtkinter.CTkButton(
    master=root, text="Calculate BMI", width=190, height=40, compound="top", command=get_Bmi)
button_1.pack(pady=20)

button_2 = customtkinter.CTkButton(
    master=root, text="Clear Screen", width=190, height=40, fg_color="#D35B58",
    hover_color="#C77C78", command=clear_screen)
button_2.pack(pady=20)

# Add Result Label

results = customtkinter.CTkLabel(
    master=root, text="", font=("Helvetica", 28))
results.pack(pady=50)

root.mainloop()
