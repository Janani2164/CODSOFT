
import tkinter as tk
from math import sqrt, pi, e, degrees, radians, factorial, sin, cos, tan, sinh, cosh, tanh, log, log10, log2, exp

class ScientificCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title('My Calculator')
        self.root.configure(bg='#D3D3D3')
        self.root.resizable(width=False, height=False)

        self.create_widgets()

    def create_widgets(self):
        self.entry_field = tk.Entry(self.root, bg='#FFFFFF', fg='#000000', font=('Arial', 20),
                                    borderwidth=5, justify="right")
        self.entry_field.grid(row=0, columnspan=5, padx=10, pady=10, sticky='nsew')
        self.entry_field.insert(0, '0')

        buttons_layout = [
            ('7', self.enter_num),
            ('8', self.enter_num),
            ('9', self.enter_num),
            ('/', self.standard_ops),
            ('CE', self.clear_entry),
            ('4', self.enter_num),
            ('5', self.enter_num),
            ('6', self.enter_num),
            ('*', self.standard_ops),
            ('sqrt', self.square_root),
            ('1', self.enter_num),
            ('2', self.enter_num),
            ('3', self.enter_num),
            ('-', self.standard_ops),
            ('pi', self.insert_constant, pi),
            ('0', self.enter_num),
            ('.', self.enter_num),
            ('+', self.standard_ops),
            ('=', self.calculate_result),
            ('e', self.insert_constant, e),
        ]

        row, col = 1, 0
        for button_text, command, *args in buttons_layout:
            button = tk.Button(self.root, text=button_text, font=('Arial', 15),
                               fg="#000000", width=5, height=2,
                               bg='#B0C4DE', command=lambda a=args: command(*a))
            button.grid(row=row, column=col, sticky='nsew', padx=5, pady=5)
            col += 1
            if col > 4:
                col = 0
                row += 1

    def enter_num(self, num):
        current = self.entry_field.get()
        if current == '0':
            self.entry_field.delete(0, 'end')
        self.entry_field.insert('end', num)

    def standard_ops(self, op):
        try:
            if op == '=':
                result = str(eval(self.entry_field.get()))
                self.entry_field.delete(0, 'end')
                self.entry_field.insert(0, result)
            else:
                current = self.entry_field.get() + op
                self.entry_field.delete(0, 'end')
                self.entry_field.insert(0, current)
        except (ValueError, SyntaxError):
            self.entry_field.delete(0, 'end')
            self.entry_field.insert(0, 'Error')

    def clear_entry(self):
        self.entry_field.delete(0, 'end')
        self.entry_field.insert(0, '0')

    def square_root(self):
        try:
            result = sqrt(float(self.entry_field.get()))
            self.entry_field.delete(0, 'end')
            self.entry_field.insert(0, result)
        except (ValueError, SyntaxError):
            self.entry_field.delete(0, 'end')
            self.entry_field.insert(0, 'Error')

    def insert_constant(self, constant):
        self.entry_field.insert('end', constant)

    def calculate_result(self):
        try:
            result = eval(self.entry_field.get())
            self.entry_field.delete(0, 'end')
            self.entry_field.insert(0, result)
        except (ValueError, SyntaxError):
            self.entry_field.delete(0, 'end')
            self.entry_field.insert(0, 'Error')


if __name__ == '__main__':
    root = tk.Tk()
    app = ScientificCalculator(root)
    root.mainloop()
