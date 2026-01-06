import tkinter as tk

class CalculatorApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('My calculator')
        self.root.geometry('450x600')
        self.root.resizable(False,False)

        self.expression = tk.StringVar()

        self.entry = tk.Entry(
            self.root,
            textvariable=self.expression,
            font=('Arial', 30),
            justify='right'
        )
        self.entry.pack(fill='x', padx=10, pady=30)
        
        self.buttons_frame = tk.Frame(self.root)
        self.buttons_frame.pack()

        self.create_buttons()

    def create_buttons(self):
        buttons = [
            ('7', 0, 0), ('8', 0, 1), ('9', 0, 2), ('+', 0, 3),
            ('4', 1, 0), ('5', 1, 1), ('6', 1, 2), ('-', 1, 3),
            ('1', 2, 0), ('2', 2, 1), ('3', 2, 2), ('*', 2, 3),
            ('0', 3, 0), ('/', 3, 3),
            ('=', 3, 2),
        ]
        
        for text, row, col in buttons:
            if text == '=':
                btn = tk.Button(
                    self.buttons_frame,
                    text=text,
                    font=('Arial', 20),
                    width=5,
                    height=2,
                    command=self.calculate
                )
            else:
                btn = tk.Button(
                    self.buttons_frame,
                    text=text,
                    font=('Arial', 20),
                    width=5,
                    height=2,
                    command=lambda t=text: self.add_to_expression(t)
                )
                
            btn.grid(row=row, column=col, padx=8, pady=5)

    def add_to_expression(self, value):
        current = self.expression.get()
        self.expression.set(current+value)

    def calculate(self):
        try:
            result = eval(self.expression.get())
            self.expression.set(str(result))
        except:
            self.expression.set('Error')
    
    def run(self):
        self.root.mainloop()

if __name__ == '__main__':
    app = CalculatorApp()
    app.run()