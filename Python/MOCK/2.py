import tkinter as tk

class Calculator:
    def __init__(self):
        self.total = 0
        self.current = ""
        self.new_num = True
        self.op_pending = False
        self.op = ""

    def clear(self):
        self.__init__()

    def num_press(self, num):
        if self.new_num:
            self.current = str(num)
            self.new_num = False
        else:
            self.current += str(num)
        self.update_display()

    def calc_total(self):
        if self.op == "+":
            self.total += float(self.current)
        elif self.op == "-":
            self.total -= float(self.current)
        elif self.op == "*":
            self.total *= float(self.current)
        elif self.op == "/":
            self.total /= float(self.current)
        self.current = str(self.total)
        self.update_display()

    def operation(self, op):
        if not self.op_pending:
            if op == "+":
                self.total = float(self.current)
            elif op == "-":
                self.total = float(self.current)
            elif op == "*":
                self.total = float(self.current)
            elif op == "/":
                self.total = float(self.current)
            self.new_num = True
        else:
            self.calc_total()
        self.op = op
        self.op_pending = True

    def equals(self):
        if not self.op_pending:
            return
        self.calc_total()
        self.op_pending = False

    def update_display(self):
        self.display.delete(0, tk.END)
        self.display.insert(0, self.current)

class CalculatorUI:
    def __init__(self, master):
        self.master = master
        self.calc = Calculator()

        # Create the display screen
        self.display = tk.Entry(master, width=30, font=('Helvetica', 16))
        self.display.grid(row=0, column=0, columnspan=4, pady=5)
        self.display.insert(0, "0")

        # Create the buttons
        buttons = [
            ("1", "2", "3", "/"),
            ("4", "5", "6", "*"),
            ("7", "8", "9", "-"),
            ("C", "0", "=", "+")
        ]

        # Add the buttons to the GUI
        for row_idx, row in enumerate(buttons):
            for col_idx, val in enumerate(row):
                button = tk.Button(master, text=val, width=5, height=2, font=('Helvetica', 12))
                button.grid(row=row_idx+1, column=col_idx, padx=3, pady=3)
                if val.isdigit():
                    button.configure(command=lambda x=val: self.calc.num_press(x))
                elif val in ["+", "-", "*", "/"]:
                    button.configure(command=lambda x=val: self.calc.operation(x))
                elif val == "C":
                    button.configure(command=lambda: self.clear_display())
                elif val == "=":
                    button.configure(command=lambda: self.calc.equals())

    def clear_display(self):
        self.calc.clear()
        self.display.delete(0, tk.END)
        self.display.insert(0, "0")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Calculator")
    calc_gui = CalculatorUI(root)
    root.mainloop()
