from tkinter import *


class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")

        

        # Create a text box for displaying the result
        self.result = Entry(master, width=100, borderwidth=5)
        self.result.grid(row=0, column=0, columnspan=4, padx=4, pady=8)

        # Define buttons for the calculator
        self.buttons = [
            {"text": "1", "command": lambda: self.button_click(1)},
            {"text": "2", "command": lambda: self.button_click(2)},
            {"text": "3", "command": lambda: self.button_click(3)},
            {"text": "Del", "command": self.delete},
            {"text": "4", "command": lambda: self.button_click(4)},
            {"text": "5", "command": lambda: self.button_click(5)},
            {"text": "6", "command": lambda: self.button_click(6)},
            {"text": "+", "command": lambda: self.button_click("+")},
            {"text": "7", "command": lambda: self.button_click(7)},
            {"text": "8", "command": lambda: self.button_click(8)},
            {"text": "9", "command": lambda: self.button_click(9)},
            {"text": "-", "command": lambda: self.button_click("-")},
            {"text": "0", "command": lambda: self.button_click(0)},
            {"text": "*", "command": lambda: self.button_click("*")},
            {"text": "/", "command": lambda: self.button_click("/")},
            {"text": ".", "command": lambda: self.button_click(".")},
            {"text": "C", "command": self.clear},
            {"text": "=", "command": self.calculate},
        ]

        # Add buttons to the calculator
        for i, button in enumerate(self.buttons):
            row = (i // 4) + 1
            col = i % 4
            btn = Button(master, text=button["text"], padx=10, pady=10, width=20, height=4, background='pink', command=button["command"])
            btn.grid(row=row, column=col)


            

    def button_click(self, number):
        current = self.result.get()
        self.result.delete(0, END)
        self.result.insert(0, str(current) + str(number))

    def clear(self):
        self.result.delete(0, END)

    def calculate(self):
        equation = self.result.get()
        try:
            result = eval(equation)
            self.result.delete(0, END)
            self.result.insert(0, round(result, 5))
        except:
            self.result.delete(0, END)
            self.result.insert(0, "Error")
    
    def delete(self):
        current = self.result.get()
        self.result.delete(0, END)
        self.result.insert(0, current[:-1])

# Create a Tkinter window and start the calculator
root = Tk()
calc = Calculator(root)
root.mainloop()