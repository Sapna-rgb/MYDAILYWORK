import tkinter as tk
from tkinter import messagebox

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Simple Calculator")

        # Entry widget to display calculations
        self.entry = tk.Entry(master, width=16, font=('Arial', 24), borderwidth=2, relief='ridge')
        self.entry.grid(row=0, column=0, columnspan=4)

        # Button layout
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3)
        ]

        for (text, row, column) in buttons:
            self.create_button(text, row, column)

    def create_button(self, text, row, column):
        button = tk.Button(self.master, text=text, width=5, height=2, font=('Arial', 18),
                           command=lambda: self.on_button_click(text))
        button.grid(row=row, column=column)

    def on_button_click(self, char):
        if char == 'C':
            self.entry.delete(0, tk.END)  # Clear the entry
        elif char == '=':
            try:
                result = eval(self.entry.get())  # Evaluate the expression
                self.entry.delete(0, tk.END)  # Clear the entry
                self.entry.insert(0, str(result))  # Display the result
            except Exception as e:
                messagebox.showerror("Error", "Invalid input")
                self.entry.delete(0, tk.END)  # Clear the entry
        else:
            current_text = self.entry.get()
            self.entry.delete(0, tk.END)
            self.entry.insert(0, current_text + char)  # Append the clicked button's text

if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()
