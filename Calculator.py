import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")

        # Create display
        self.display = tk.Entry(master, width=35, borderwidth=5, font=('Arial', 16))
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        # Create buttons
        button_list = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '*'
        ]

        row = 1
        col = 0
        for button_text in button_list:
            button = tk.Button(master, text=button_text, width=5, height=2, font=('Arial', 14),
            command=lambda x=button_text: self.button_click(x))
            button.grid(row=row, column=col, padx=5, pady=5)
            if col > 3:
                col = 0
                row += 1

            # Bind keyboard keys
            self.master.bind('<Key>', self.key_press)

    def button_click(self, button):
        current = self.display.get()
        if button == 'C':
            self.display.delete(0, tk.END)
        elif button == '=':
            try:
                result = eval(current)
                self.display.delete(0, tk.END)
                self.display.insert(0, str(result))
            except SyntaxError:
                self.display.delete(0, tk.END)
                self.display.insert(0, "Error")
        else:
            self.display.delete(0, tk.END)
            self.display.insert(0, current + button)

    def key_press(self, event):
        key = event.char
        if key in '0123456789+-*/.':
            self.button_click(key)
        elif key == '\r':
            self.button_click('=')
        elif key == '\x1b': # Escape key
            self.display.delete(0, tk.END)

root = tk.Tk()
calculator = Calculator(root)
root.mainloop()