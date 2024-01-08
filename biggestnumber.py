import customtkinter as ctk
import tkinter as tk
from tkinter import PhotoImage, Label

# Creating the main window

app = ctk.CTk()
app.title('What is the 3 numbers?')
app.geometry("500x250")
app.config(bg="#E1CFCF")
app.resizable(False, False)

# Entry widgets
entry1 = tk.Entry(app, width=10)
entry2 = tk.Entry(app, width=10)
entry3 = tk.Entry(app, width=10)

entry1.grid(row=0, column=0, pady=5)
entry2.grid(row=1, column=0, pady=5)
entry3.grid(row=2, column=0, pady=5)

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
