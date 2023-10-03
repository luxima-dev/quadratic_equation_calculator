# IMPORT #

import tkinter as tk
from tkinter import messagebox

def get_coefficients():
    a = entry_a.get()
    b = entry_b.get()
    c = entry_c.get()
    return a, b, c

def check_coefficients(a, b, c):
    if not a or not b or not c:
        messagebox.showerror("Ошибка", "Введите значения всех коэффициентов")
        return False
    try:
        a = float(a)
        b = float(b)
        c = float(c)
    except ValueError:
        messagebox.showerror("Ошибка", "Некорректный ввод. Введите числа")
        return False
    return a, b, c


def solve_equation(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return "Нет решения."
    elif discriminant == 0:
        x = -b / (2*a)
        return f"Один корень: x={x}"
    else:
        x1 = round((-b + discriminant**0.5) / (2*a), 3)
        x2 = round((-b - discriminant**0.5) / (2*a), 3)
        return f"Два корня: x1={x1}, x2={x2}"


def update_solution(solution):
    label_solution.configure(text=solution)

# Функция для решения квадратного уравнения
def solve():
    a, b, c = get_coefficients()
    result = check_coefficients(a, b, c)
    if result:
        a, b, c = result
        solution = solve_equation(a, b, c)
        update_solution(solution)


# MAIN WINDOW %
root = tk.Tk()
root.title("Квадратное уравнение")
root.geometry("1000x300")

# TITLE #
label_title = tk.Label(root, text="Решение квадратного уравнения", font=("Arial", 18))
label_title.pack(pady=10)

# INPUT FRAME
frame_input = tk.Frame(root, bg="#FFFFFF")
frame_input.pack(pady=10)

# INPUT A #
label_a = tk.Label(frame_input, text="a:", font=("Arial", 14))
label_a.pack(side="left")
entry_a = tk.Entry(frame_input, font=("Arial", 14))
entry_a.pack(side="left")

# INPUT B #
label_b = tk.Label(frame_input, text="b:", font=("Arial", 14))
label_b.pack(side="left")
entry_b = tk.Entry(frame_input, font=("Arial", 14))
entry_b.pack(side="left")

# INPUT C #
label_c = tk.Label(frame_input, text="c:", font=("Arial", 14))
label_c.pack(side="left")
entry_c = tk.Entry(frame_input, font=("Arial", 14))
entry_c.pack(side="left")

# BUTTON SOLVE #
button_solve = tk.Button(root, text="Решить", font=("Arial", 14), command=solve)
button_solve.pack(pady=10)

# RESULT #
label_solution = tk.Label(root, text="", font=("Arial", 12))
label_solution.pack()

# DESIGN #
root.configure(bg="#FFFFFF")
label_title.configure(fg="#000000")
label_a.configure(bg="#FFFFFF", fg="#000000")
label_b.configure(bg="#FFFFFF", fg="#000000")
label_c.configure(bg="#FFFFFF", fg="#000000")
entry_a.configure(bg="#FFFFFF", fg="#000000")
entry_b.configure(bg="#FFFFFF", fg="#000000")
entry_c.configure(bg="#FFFFFF", fg="#000000")
button_solve.configure(bg="#4CAF50", fg="#FFFFFF")
label_solution.configure(bg="#FFFFFF", fg="#000000")

# INSTRUCTION #
label_instruction = tk.Label(root, text="Введите коэффициенты уравнения в соответствующие поля ввода и нажмите кнопку 'Решить'.", font=("Arial", 12))
label_instruction.pack(pady=10)

# ABOUT #
label_about = tk.Label(root, text="Эта программа решает квадратное уравнение вида ax^2 + bx + c = 0", font=("Arial", 10))
label_about.pack(side="bottom", padx=10, pady=10)

# RUN! #
root.mainloop()