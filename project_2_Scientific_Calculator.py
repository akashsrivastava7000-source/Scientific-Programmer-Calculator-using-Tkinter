import tkinter as tk
import math

# ---------------- Window ----------------
root = tk.Tk()
root.title("Scientific Calculator")
root.geometry("640x520")
root.config(bg="#0f172a")  # dark navy

# ---------------- Frames ----------------
display_frame = tk.Frame(root, bg="#0f172a")
display_frame.pack(fill="x", pady=5)

main_frame = tk.Frame(root, bg="#0f172a")
main_frame.pack(pady=5)

button_frame = tk.Frame(main_frame, bg="#0f172a")
button_frame.grid(row=0, column=0, padx=10)

history_frame = tk.Frame(main_frame, bg="#111827")
history_frame.grid(row=0, column=1, padx=10)

# ---------------- Display ----------------
entry = tk.Entry(
    display_frame,
    font=("Segoe UI", 22, "bold"),
    bd=0,
    bg="#e2e8f0",
    fg="#0f172a",
    justify="right"
)
entry.pack(fill="x", padx=12, pady=10, ipady=10)

# ---------------- History ----------------
tk.Label(history_frame, text="History",
         bg="#111827", fg="white",
         font=("Segoe UI", 14, "bold")).pack(pady=5)

history_list = tk.Listbox(
    history_frame,
    height=22,
    width=28,
    font=("Consolas", 11),
    bg="#1f2937",
    fg="white",
    bd=0,
    highlightthickness=0
)
history_list.pack(padx=5, pady=5)

def add_history(text):
    history_list.insert(tk.END, text)

# ---------------- Functions ----------------
def click(value):
    entry.insert(tk.END, value)

def clear():
    entry.delete(0, tk.END)

def backspace():
    entry.delete(len(entry.get())-1, tk.END)

def calculate():
    try:
        exp = entry.get()
        result = eval(exp)
        entry.delete(0, tk.END)
        entry.insert(0, result)
        add_history(f"{exp} = {result}")
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Scientific
def sin_func():
    val = math.sin(math.radians(float(entry.get())))
    entry.delete(0, tk.END); entry.insert(0, val)
    add_history(f"sin = {val}")

def cos_func():
    val = math.cos(math.radians(float(entry.get())))
    entry.delete(0, tk.END); entry.insert(0, val)
    add_history(f"cos = {val}")

def tan_func():
    val = math.tan(math.radians(float(entry.get())))
    entry.delete(0, tk.END); entry.insert(0, val)
    add_history(f"tan = {val}")

def sqrt_func():
    val = math.sqrt(float(entry.get()))
    entry.delete(0, tk.END); entry.insert(0, val)
    add_history(f"√ = {val}")

def log_func():
    val = math.log10(float(entry.get()))
    entry.delete(0, tk.END); entry.insert(0, val)
    add_history(f"log = {val}")

def fact_func():
    val = math.factorial(int(entry.get()))
    entry.delete(0, tk.END); entry.insert(0, val)
    add_history(f"! = {val}")

# Programmer
def to_bin():
    val = bin(int(entry.get()))
    entry.delete(0, tk.END); entry.insert(0, val)
    add_history(f"BIN = {val}")

def to_hex():
    val = hex(int(entry.get()))
    entry.delete(0, tk.END); entry.insert(0, val)
    add_history(f"HEX = {val}")

def to_dec():
    val = entry.get()
    if val.startswith("0b"):
        res = int(val, 2)
    elif val.startswith("0x"):
        res = int(val, 16)
    else:
        res = int(val)
    entry.delete(0, tk.END); entry.insert(0, res)
    add_history(f"DEC = {res}")

# ---------------- Button Style ----------------
btn_style = {
    "width": 5,
    "height": 2,
    "font": ("Segoe UI", 11, "bold"),
    "bd": 0,
    "fg": "white",
    "bg": "#334155",
    "activebackground": "#475569",
    "activeforeground": "white"
}

# ---------------- Buttons ----------------
buttons = [
    ('7',1,0), ('8',1,1), ('9',1,2), ('/',1,3), ('C',1,4),
    ('4',2,0), ('5',2,1), ('6',2,2), ('*',2,3), ('⌫',2,4),
    ('1',3,0), ('2',3,1), ('3',3,2), ('-',3,3), ('(',3,4),
    ('0',4,0), ('.',4,1), ('=',4,2), ('+',4,3), (')',4,4),
    ('sin',5,0), ('cos',5,1), ('tan',5,2), ('log',5,3), ('√',5,4),
    ('x²',6,0), ('π',6,1), ('e',6,2), ('!',6,3), ('^',6,4),
    ('BIN',7,0), ('HEX',7,1), ('DEC',7,2)
]

for (text, row, col) in buttons:

    if text == 'C': action = clear
    elif text == '=': action = calculate
    elif text == '⌫': action = backspace
    elif text == 'sin': action = sin_func
    elif text == 'cos': action = cos_func
    elif text == 'tan': action = tan_func
    elif text == 'log': action = log_func
    elif text == '√': action = sqrt_func
    elif text == '!': action = fact_func
    elif text == 'π': action = lambda: click(str(math.pi))
    elif text == 'e': action = lambda: click(str(math.e))
    elif text == 'x²': action = lambda: click("**2")
    elif text == '^': action = lambda: click("**")
    elif text == 'BIN': action = to_bin
    elif text == 'HEX': action = to_hex
    elif text == 'DEC': action = to_dec
    else: action = lambda x=text: click(x)

    tk.Button(button_frame, text=text, command=action, **btn_style)\
        .grid(row=row, column=col, padx=4, pady=4)

root.mainloop()