import customtkinter as ctk
import tkinter as tk
from tkinter import PhotoImage, Label

# Creating the main window

app = ctk.CTk()
app.title('What is the 3 numbers?')
app.geometry("350x400")
app.config(bg="#E1CFCF")
app.resizable(False, False)

# Entry widgets
entry1 = ctk.CTkEntry(app, text_color="#000000", bg_color="#E1CFCF", fg_color="#FFF5F7", width=85)
entry1.place(relx=0.075, rely=0.4)
entry2 = ctk.CTkEntry(app, text_color="#000000", bg_color="#E1CFCF", fg_color="#FFF5F7", width=85)
entry2.place(relx=0.385, rely=0.4)
entry3 = ctk.CTkEntry(app, text_color="#000000", bg_color="#E1CFCF", fg_color="#FFF5F7", width=85)
entry3.place(relx=0.7, rely=0.4)


# Ask user for input
def find_the_biggest_number():
    try:
        number1 = int(entry1.get())
        number2 = int(entry2.get())
        number3 = int(entry3.get())

        # Find the highest number
        biggest_number = max(number1, number2, number3)
        
        # Display the result in window
        if number1 == number2 == number3:
            print("There is no highest, All numbers are equal")
        else:
            print(f"The biggest number is: {biggest_number}")
        
    except ValueError:
        result_label.config(text="Please enter valid numbers.")

result_label = tk.Label(app, text="Result will be displayed here.")


    
app.mainloop()
