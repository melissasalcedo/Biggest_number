import customtkinter as ctk
import tkinter as tk
from tkinter import Label

# Ask user for input
def find_the_biggest_number():
    try:
        number1 = int(entry1.get())
        number2 = int(entry2.get())
        number3 = int(entry3.get())

        if number1 > number2 and number1 > number3:
            biggest_number = number1
        elif number2 > number1 and number2 > number3:
            biggest_number = number2
         
    

        
        # Display the result in window
        if number1 == number2 == number3:
            result_label.configure(text=f"There is no highest, \nAll numbers are equal")
        else:
            result_label.configure(text=f"The biggest number is: \n{biggest_number}")
        
    except ValueError:
        result_label.configure(text=f"Please enter \nvalid numbers.")

# Creating the main window
app = ctk.CTk()
app.title('What are the 3 numbers?')
app.geometry("350x400")
app.config(bg="#E1CFCF")
app.resizable(False, False)

# Fonts
font1 =  ('Plantagenet Cherokee', 28, 'italic', 'bold')
font2 = ('Franklin Gothic Book', 19, 'bold')

# Message frame
mess_frame = ctk.CTkEntry(app, width=250, height=50, fg_color="#AD6E8C", bg_color="#E1CFCF", corner_radius=30)
mess_frame.place(relx=0.150, rely=0.11)

# Message label
mess_label = ctk.CTkLabel(app, text="Type 3 Numbers", bg_color='#AD6E8C', text_color='#403F3F', font=font1)
mess_label.place(relx=0.20, rely=0.13)

# Entry widgets
entry1 = ctk.CTkEntry(app, text_color="#000000", bg_color="#E1CFCF", fg_color="#FFF5F7", width=85)
entry1.place(relx=0.075, rely=0.35)
entry2 = ctk.CTkEntry(app, text_color="#000000", bg_color="#E1CFCF", fg_color="#FFF5F7", width=85)
entry2.place(relx=0.385, rely=0.35)
entry3 = ctk.CTkEntry(app, text_color="#000000", bg_color="#E1CFCF", fg_color="#FFF5F7", width=85)
entry3.place(relx=0.7, rely=0.35)

# Enter Button
Enter_button = ctk.CTkButton(app,command=find_the_biggest_number, text="Enter", font=font2, text_color= "#545454", fg_color="#C4A5B8", bg_color="#E1CFCF", hover_color="#DFBCD2", corner_radius=20, cursor="hand2", width=110)
Enter_button.place(relx=0.350, rely=0.48)

# Result Frame
Result_frame = ctk.CTkFrame(app, width=275, height=140, fg_color="#AD6E8C", bg_color="#E1CFCF", corner_radius=30)
Result_frame.place(relx=0.115, rely=0.58)
Result_frame.pack_propagate(False) 

# Result Label
result_label = Label(Result_frame, text="", font=font2, bg='#AD6E8C', fg='#FFFFFF')
result_label.pack(pady=50)

app.mainloop()
