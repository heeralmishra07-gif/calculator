import tkinter as tk
from src.calculator import evaluate_expression
class CalculatorApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Python Calculator")
        self.geometry("320x450")
        self.resizable(False, False)
        self.configure(bg="#22252d")
        self.expression = "0"
        self._create_widgets()

    def _create_widgets(self):
        self.display = tk.Label(
            self,
            text=self.expression,
            font=("Segoe UI", 24, "bold"),
            bg="#292d36",
            fg="#ffffff",
            anchor="e",
            padx=15,
            pady=15,
        )
        self.display.pack(expand=True, fill="both", padx=15, pady=(15, 10))
        frame = tk.Frame(self, bg="#22252d")
        frame.pack(expand=True, fill="both", padx=10, pady=10)

        buttons = [
            ("AC", 0, 0, "#26e7a6", self.clear),
            ("DEL", 0, 1, "#26e7a6", self.delete_last),
            ("%", 0, 2, "#ff605c", lambda: self.append_op("/100")),
            ("/", 0, 3, "#ff605c", lambda: self.append_op("/")),
            ("7", 1, 0, "#ffffff", lambda: self.append_num("7")),
            ("8", 1, 1, "#ffffff", lambda: self.append_num("8")),
            ("9", 1, 2, "#ffffff", lambda: self.append_num("9")),
            ("*", 1, 3, "#ff605c", lambda: self.append_op("*")),
            ("4", 2, 0, "#ffffff", lambda: self.append_num("4")),
            ("5", 2, 1, "#ffffff", lambda: self.append_num("5")),
            ("6", 2, 2, "#ffffff", lambda: self.append_num("6")),
            ("-", 2, 3, "#ff605c", lambda: self.append_op("-")),
            ("1", 3, 0, "#ffffff", lambda: self.append_num("1")),
            ("2", 3, 1, "#ffffff", lambda: self.append_num("2")),
            ("3", 3, 2, "#ffffff", lambda: self.append_num("3")),
            ("+", 3, 3, "#ff605c", lambda: self.append_op("+")),
            ("0", 4, 0, "#ffffff", lambda: self.append_num("0")),
            (".", 4, 1, "#ffffff", lambda: self.append_num(".")),
            ("=", 4, 2, "#ffffff", self.calculate),
        ]

        for text, row, col, fg_color, cmd in buttons:
            colspan = 2 if text == "=" else 1
            btn = tk.Button(
                frame,
                text=text,
                font=("Segoe UI", 14, "bold"),
                bg="#292d36",
                fg=fg_color,
                bd=0,
                activebackground="#333842",
                activeforeground=fg_color,
                command=cmd,
            )
            btn.grid(row=row, column=col, columnspan=colspan, sticky="nsew", padx=5, pady=5)
        for i in range(5):
            frame.rowconfigure(i, weight=1)
        for j in range(4):
            frame.columnconfigure(j, weight=1)

    def update_display(self):
        self.display.config(text=self.expression)

    def append_num(self, num):
        if self.expression == "0" and num != ".":
            self.expression = num
        else:
            self.expression += num
        self.update_display()

    def append_op(self, op):
        if self.expression[-1:] in ["+", "-", "*", "/"]:
            self.expression = self.expression[:-1] + op
        else:
            self.expression += op
        self.update_display()

    def clear(self):
        self.expression = "0"
        self.update_display()

    def delete_last(self):
        self.expression = self.expression[:-1] if len(self.expression) > 1 else "0"
        self.update_display()

    def calculate(self):
        self.expression = evaluate_expression(self.expression)
        self.update_display()
