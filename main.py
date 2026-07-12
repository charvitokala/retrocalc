import customtkinter as ctk
ctk.set_appearance_mode("system")
ctk.set_default_color_theme("blue")
app = ctk.CTk()
app.configure(fg_color="#FF006E")
app.title("retrocalc")
app.geometry("450x700")
display = ctk.CTkEntry(
   app,
   width=389,
   height=134,
   fg_color="#FFD60A",  
   text_color="black",     
   corner_radius=20,     
   border_width=1,        
   font=("Pixelify Sans", 83),     
   justify="right"         
)
display.pack(pady=40)


button_frame = ctk.CTkFrame(
   app,
   fg_color="transparent"
)


button_frame.pack(pady=5)


current_expression = ""
def button_click(value):
   global current_expression


   current_expression += value
   update_display()

def calculate():
    global current_expression

    try:
        current_expression = str(eval(current_expression))
        update_display()

    except:
        current_expression = "Error"
        update_display()

def clear():
   global current_expression
   current_expression = ""
   update_display()
  
def erase():
   global current_expression
   current_expression = current_expression[:-1]
   update_display()


def update_display():
   display.delete(0, "end")          # Clear what's currently in the display
   display.insert(0, current_expression)  # Insert the updated expression


buttonc = ctk.CTkButton(
   button_frame,
   text="C",
   command=clear,
   font=("Pixelify Sans", 40),
   fg_color="#FFD60A",
   text_color="black",
   border_width=1,
   width=78,
   height=70
)


buttonc.grid(row=0, column=0, padx=10, pady=10)


buttone = ctk.CTkButton(
   button_frame,
   text="E",
   command=erase,
   font=("Pixelify Sans", 40),
   fg_color="#FFD60A",
   text_color="black",
   border_width=1,
   width=78,
   height=70
)


buttone.grid(row=0, column=1, padx=10, pady=10)


buttona = ctk.CTkButton(
   button_frame,
   text="+",
   command=lambda: button_click("+"),
   font=("Pixelify Sans", 40),
   fg_color="#FFD60A",
   text_color="black",
   border_width=1,
   width=78,
   height=70
)


buttona.grid(row=0, column=2, padx=10, pady=10)


buttonm = ctk.CTkButton(
   button_frame,
   text="x",
   command=lambda: button_click("*"),
   font=("Pixelify Sans", 40),
   fg_color="#FFD60A",
   text_color="black",
   border_width=1,
   width=78,
   height=70
)


buttonm.grid(row=0, column=3, padx=10, pady=10)




button7 = ctk.CTkButton(
   button_frame,
   text="7",
   command=lambda: button_click("7"),
   font=("Pixelify Sans", 40),
   fg_color="#FFD60A",
   text_color="black",
   border_width=1,
   width=78,
   height=70
)


button7.grid(row=1, column=0, padx=10, pady=10)


button8 = ctk.CTkButton(
   button_frame,
   text="8",
   command=lambda: button_click("8"),
   font=("Pixelify Sans", 40),
   fg_color="#FFD60A",
   text_color="black",
   border_width=1,
   width=78,
   height=70
)


button8.grid(row=1, column=1, padx=10, pady=10)


button9 = ctk.CTkButton(
   button_frame,
   text="9",
   command=lambda: button_click("9"),
   font=("Pixelify Sans", 40),
   fg_color="#FFD60A",
   text_color="black",
   border_width=1,
   width=78,
   height=70
)


button9.grid(row=1, column=2, padx=10, pady=10)


buttond = ctk.CTkButton(
   button_frame,
   text="/",
    command=lambda: button_click("/"),
   font=("Pixelify Sans", 40),
   fg_color="#FFD60A",
   text_color="black",
   border_width=1,
   width=78,
   height=70
)


buttond.grid(row=1, column=3, padx=10, pady=10)


button4 = ctk.CTkButton(
   button_frame,
   text="4",
   command=lambda: button_click("4"),
   font=("Pixelify Sans", 40),
   fg_color="#FFD60A",
   text_color="black",
   border_width=1,
   width=78,
   height=70
)


button4.grid(row=2, column=0, padx=10, pady=10)


button5 = ctk.CTkButton(
   button_frame,
   text="5",
   command=lambda: button_click("5"),
   font=("Pixelify Sans", 40),
   fg_color="#FFD60A",
   text_color="black",
   border_width=1,
   width=78,
   height=70
)


button5.grid(row=2, column=1, padx=10, pady=10)


button6 = ctk.CTkButton(
   button_frame,
   text="6",
   command=lambda: button_click("6"),
   font=("Pixelify Sans", 40),
   fg_color="#FFD60A",
   text_color="black",
   border_width=1,
   width=78,
   height=70
)


button6.grid(row=2, column=2, padx=10, pady=10)


buttons = ctk.CTkButton(
   button_frame,
   text="-",
    command=lambda: button_click("-"),
   font=("Pixelify Sans", 40),
   fg_color="#FFD60A",
   text_color="black",
   border_width=1,
   width=78,
   height=70
)


buttons.grid(row=2, column=3, padx=10, pady=10)


button1 = ctk.CTkButton(
   button_frame,
   text="1",
   command=lambda: button_click("1"),
   font=("Pixelify Sans", 40),
   fg_color="#FFD60A",
   text_color="black",
   border_width=1,
   width=78,
   height=70
)


button1.grid(row=3, column=0, padx=10, pady=10)


button2 = ctk.CTkButton(
   button_frame,
   text="2",
   command=lambda: button_click("2"),
   font=("Pixelify Sans", 40),
   fg_color="#FFD60A",
   text_color="black",
   border_width=1,
   width=78,
   height=70
)


button2.grid(row=3, column=1, padx=10, pady=10)


button3 = ctk.CTkButton(
   button_frame,
   text="3",
   command=lambda: button_click("3"),
   font=("Pixelify Sans", 40),
   fg_color="#FFD60A",
   text_color="black",
   border_width=1,
   width=78,
   height=70
)


button3.grid(row=3, column=2, padx=10, pady=10)


buttonx = ctk.CTkButton(
   button_frame,
   text="=",
   command=calculate,
   font=("Pixelify Sans", 40),
   fg_color="#FFD60A",
   text_color="black",
   border_width=1,
   width=78,
   height=70
)


buttonx.grid(
   row=3,
   column=3,
   rowspan=2,
   padx=10,
   pady=10,
   sticky="nsew"
)


button0 = ctk.CTkButton(
   button_frame,
   text="0",
   command=lambda: button_click("0"),
   font=("Pixelify Sans", 40),
   fg_color="#FFD60A",
   text_color="black",
   border_width=1,
   width=78,
   height=70
)


button0.grid(
   row=4,
   column=0,
   columnspan=2,
   padx=10,
   pady=10,
   sticky="nsew"
)


buttonp = ctk.CTkButton(
   button_frame,
   text=".",
    command=lambda: button_click("."),
   font=("Pixelify Sans", 40),
   fg_color="#FFD60A",
   text_color="black",
   border_width=1,
   width=78,
   height=70
)


buttonp.grid(row=4, column=2, padx=10, pady=10)


app.mainloop()



