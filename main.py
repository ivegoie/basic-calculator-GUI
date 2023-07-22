import tkinter as tk
from tkinter import font


class Calculator:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Basic Calculator")
        self.root.resizable(False, False)
        self.calculation = ""
        self.display_entry()
        self.display_buttons()
        self.disable_keyboard_input()

    def display_entry(self):
        result_frame = tk.Frame(self.root)
        result_frame.pack(padx=10, pady=10)

        self.text_result = tk.Text(result_frame, height=3, width=25, font=("Arial", 24))
        self.text_result.grid(columnspan=5)

    def display_buttons(self):
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=10)

        btn_1 = tk.Button(
            button_frame,
            text="1",
            command=lambda: self.add_to_calculation(symbol=1),
            width=5,
            height=2,
            font=("Arial", 14),
        )
        btn_1.grid(column=1, row=2)

        btn_2 = tk.Button(
            button_frame,
            text="2",
            command=lambda: self.add_to_calculation(symbol=2),
            width=5,
            height=2,
            font=("Arial", 14),
        )
        btn_2.grid(column=2, row=2)

        btn_3 = tk.Button(
            button_frame,
            text="3",
            command=lambda: self.add_to_calculation(3),
            width=5,
            height=2,
            font=("Arial", 14),
        )
        btn_3.grid(column=3, row=2)

        btn_4 = tk.Button(
            button_frame,
            text="4",
            command=lambda: self.add_to_calculation(4),
            width=5,
            height=2,
            font=("Arial", 14),
        )
        btn_4.grid(column=1, row=3)

        btn_5 = tk.Button(
            button_frame,
            text="5",
            command=lambda: self.add_to_calculation(5),
            width=5,
            height=2,
            font=("Arial", 14),
        )
        btn_5.grid(column=2, row=3)

        btn_6 = tk.Button(
            button_frame,
            text="6",
            command=lambda: self.add_to_calculation(6),
            width=5,
            height=2,
            font=("Arial", 14),
        )
        btn_6.grid(column=3, row=3)

        btn_7 = tk.Button(
            button_frame,
            text="7",
            command=lambda: self.add_to_calculation(7),
            width=5,
            height=2,
            font=("Arial", 14),
        )
        btn_7.grid(column=1, row=4)

        btn_8 = tk.Button(
            button_frame,
            text="8",
            command=lambda: self.add_to_calculation(8),
            width=5,
            height=2,
            font=("Arial", 14),
        )
        btn_8.grid(column=2, row=4)

        btn_9 = tk.Button(
            button_frame,
            text="9",
            command=lambda: self.add_to_calculation(9),
            width=5,
            height=2,
            font=("Arial", 14),
        )
        btn_9.grid(column=3, row=4)

        btn_0 = tk.Button(
            button_frame,
            text="0",
            command=lambda: self.add_to_calculation(0),
            width=5,
            height=2,
            font=("Arial", 14),
        )
        btn_0.grid(column=2, row=5)

        btn_plus = tk.Button(
            button_frame,
            text="+",
            command=lambda: self.add_to_calculation(symbol="+"),
            width=5,
            height=2,
            font=("Arial", 14),
        )
        btn_plus.grid(column=4, row=2)

        btn_minus = tk.Button(
            button_frame,
            text="-",
            command=lambda: self.add_to_calculation("-"),
            width=5,
            height=2,
            font=("Arial", 14),
        )
        btn_minus.grid(column=4, row=3)

        btn_mul = tk.Button(
            button_frame,
            text="*",
            command=lambda: self.add_to_calculation("*"),
            width=5,
            height=2,
            font=("Arial", 14),
        )
        btn_mul.grid(column=4, row=4)

        btn_div = tk.Button(
            button_frame,
            text="/",
            command=lambda: self.add_to_calculation("/"),
            width=5,
            height=2,
            font=("Arial", 14),
        )
        btn_div.grid(column=4, row=5)

        btn_open_p = tk.Button(
            button_frame,
            text="(",
            command=lambda: self.add_to_calculation("("),
            width=5,
            height=2,
            font=("Arial", 14),
        )
        btn_open_p.grid(column=1, row=5)

        btn_closed_p = tk.Button(
            button_frame,
            text=")",
            command=lambda: self.add_to_calculation(")"),
            width=5,
            height=2,
            font=("Arial", 14),
        )
        btn_closed_p.grid(column=3, row=5)

        btn_equals = tk.Button(
            button_frame,
            text="=",
            command=self.evaluate_calculation,
            width=15,
            height=2,
            font=("Arial", 14),
        )
        btn_equals.grid(column=3, row=6, columnspan=2)

        btn_clear = tk.Button(
            button_frame,
            text="C",
            command=self.clear_field,
            width=15,
            height=2,
            font=("Arial", 14),
        )
        btn_clear.grid(column=1, row=6, columnspan=2)

    def add_to_calculation(self, symbol):
        self.calculation += str(symbol)
        self.text_result.delete(1.0, tk.END)
        self.text_result.insert(1.0, self.calculation)

    def evaluate_calculation(self):
        try:
            calculation = str(eval(self.calculation))
            self.text_result.delete(1.0, tk.END)
            self.text_result.insert(1.0, calculation)
        except (ZeroDivisionError, SyntaxError) as err:
            self.clear_field()
            self.text_result.insert(1.0, "Error")
            print(err)

    def clear_field(self):
        self.calculation = ""
        self.text_result.delete(1.0, tk.END)

    def shortcut(self, event):
        if event.state == 4 and event.keysym == "Return":
            self.evaluate_calculation()

    def disable_keyboard_input(self):
        self.text_result.bind("<Key>", lambda e: "break")

    def mainloop(self):
        self.root.mainloop()


def main():
    app = Calculator()
    app.mainloop()


if __name__ == "__main__":
    main()
