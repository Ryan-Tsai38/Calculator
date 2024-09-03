import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
from tkinter import messagebox

class Calculator:
    def __init__(self):
        self.expression = ""

    def add_to_expression(self, value):
        self.expression += str(value)

    def clear_expression(self):
        self.expression = ""

    def evaluate_expression(self):
        try:
            result = eval(self.expression)
            return result
        except Exception as e:
            return "Error: " + str(e)

class Grapher:
    def __init__(self):
        pass

    def plot_function(self, func, x_range):
        x = np.linspace(x_range[0], x_range[1], 400)
        y = eval(func)
        plt.plot(x, y)
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title(f'Graph of {func}')
        plt.grid(True)
        plt.show()

class GraphingCalculatorApp:
    def __init__(self, master):
        self.master = master
        master.title("Graphing Calculator")

        self.calculator = Calculator()
        self.grapher = Grapher()

        self.display = tk.Entry(master, width=40, borderwidth=5)
        self.display.grid(row=0, column=0, columnspan=5)

        self.create_buttons()

    def create_buttons(self):
        buttons = [
            '7', '8', '9', '/', 'Clear',
            '4', '5', '6', '*', 'Plot',
            '1', '2', '3', '-', '(',
            '0', '.', '=', '+', ')'
        ]

        row_val = 1
        col_val = 0

        for button_text in buttons:
            action = lambda x=button_text: self.click_event(x)
            tk.Button(self.master, text=button_text, width=9, height=3, command=action).grid(row=row_val, column=col_val)
            col_val += 1
            if col_val > 4:
                col_val = 0
                row_val += 1

    def click_event(self, key):
        if key == "Clear":
            self.calculator.clear_expression()
            self.update_display()
        elif key == "=":
            result = self.calculator.evaluate_expression()
            self.update_display(result)
        elif key == "Plot":
            try:
                func = self.display.get()
                self.grapher.plot_function(f"np.{func}", (-10, 10))
            except Exception as e:
                messagebox.showerror("Error", str(e))
        else:
            self.calculator.add_to_expression(key)
            self.update_display()

    def update_display(self, value=None):
        if value is None:
            value = self.calculator.expression
        self.display.delete(0, tk.END)
        self.display.insert(0, value)

if __name__ == "__main__":
    root = tk.Tk()
    app = GraphingCalculatorApp(root)
    root.mainloop()