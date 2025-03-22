import numpy as np
import tkinter as tk
from tkinter import messagebox, simpledialog

def input_matrix(name):
    rows = simpledialog.askinteger("Input", f"Enter rows for {name}:")
    cols = simpledialog.askinteger("Input", f"Enter columns for {name}:")
    matrix = []
    for i in range(rows):
        row = simpledialog.askstring("Input", f"Enter row {i + 1} of {name} (space-separated):")
        matrix.append(list(map(float, row.split())))
    return np.array(matrix)

def display_result(result):
    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, str(result))

def add_matrices():
    if matrix_A is not None and matrix_B is not None:
        if matrix_A.shape == matrix_B.shape:
            display_result(matrix_A + matrix_B)
        else:
            messagebox.showerror("Error", "Matrices must have the same dimensions for addition.")

def subtract_matrices():
    if matrix_A is not None and matrix_B is not None:
        if matrix_A.shape == matrix_B.shape:
            display_result(matrix_A - matrix_B)
        else:
            messagebox.showerror("Error", "Matrices must have the same dimensions for subtraction.")

def multiply_matrices():
    if matrix_A is not None and matrix_B is not None:
        if matrix_A.shape[1] == matrix_B.shape[0]:
            display_result(np.dot(matrix_A, matrix_B))
        else:
            messagebox.showerror("Error", "Columns of A must match rows of B for multiplication.")

def transpose(matrix, name):
    if matrix is not None:
        display_result(matrix.T)
    else:
        messagebox.showerror("Error", f"Please input {name} first.")

def determinant(matrix, name):
    if matrix is not None:
        if matrix.shape[0] == matrix.shape[1]:
            display_result(np.linalg.det(matrix))
        else:
            messagebox.showerror("Error", f"{name} must be square to calculate determinant.")
    else:
        messagebox.showerror("Error", f"Please input {name} first.")

# Initialize GUI
root = tk.Tk()
root.title("Matrix Operations Tool")
root.geometry("400x300")

# Matrix Input Buttons
matrix_A, matrix_B = None, None
tk.Button(root, text="Input Matrix A", command=lambda: globals().update(matrix_A=input_matrix("A"))).pack(pady=5)
tk.Button(root, text="Input Matrix B", command=lambda: globals().update(matrix_B=input_matrix("B"))).pack(pady=5)

# Operation Buttons
tk.Button(root, text="A + B", command=add_matrices).pack(pady=5)
tk.Button(root, text="A - B", command=subtract_matrices).pack(pady=5)
tk.Button(root, text="A * B", command=multiply_matrices).pack(pady=5)
tk.Button(root, text="Transpose A", command=lambda: transpose(matrix_A, "A")).pack(pady=5)
tk.Button(root, text="Transpose B", command=lambda: transpose(matrix_B, "B")).pack(pady=5)
tk.Button(root, text="Det(A)", command=lambda: determinant(matrix_A, "A")).pack(pady=5)
tk.Button(root, text="Det(B)", command=lambda: determinant(matrix_B, "B")).pack(pady=5)

# Result Display
result_text = tk.Text(root, height=5, width=40)
result_text.pack(pady=10)

root.mainloop()