import tkinter as tk

def evaluate_expression(expr):
    try:
        return str(eval(expr))
    except:
        return "Error"

def on_button_click(val):
    current_text = text_var.get()
    if val == '=':
        result = evaluate_expression(current_text)
        text_var.set(result)
    elif val == 'C':
        text_var.set("")
    else:
        text_var.set(current_text + val)

root = tk.Tk()
root.title("Simple Calculator")

text_var = tk.StringVar()
entry = tk.Entry(root, textvariable=text_var, font=('Arial', 24), justify='right')
entry.grid(row=0, column=0, columnspan=4, sticky='nsew', padx=10, pady=10)

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
    ('C', 5, 0, 3)  
]

for (text, row, col, *options) in buttons:
    col_span = options[0] if options else 1
    btn = tk.Button(root, text=text, font=('Arial', 18), width=4, height=2,
                    command=lambda val=text: on_button_click(val))
    btn.grid(row=row, column=col, sticky='nsew', padx=5, pady=5, columnspan=col_span)

for i in range(4):
    root.grid_columnconfigure(i, weight=1)
for i in range(1, 6):
    root.grid_rowconfigure(i, weight=1)

root.mainloop()
