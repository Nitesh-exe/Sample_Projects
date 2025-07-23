import tkinter as tk

def calculate_bmi():
    height = float(height_entry.get())
    weight = float(weight_entry.get())
    bmi = weight / (height ** 2)
    result.set(f"BMI: {round(bmi, 2)}")

root = tk.Tk()
root.title("BMI Calculator")
root.geometry("250x200")

tk.Label(root, text="Height (m):").pack()
height_entry = tk.Entry(root)
height_entry.pack()

tk.Label(root, text="Weight (kg):").pack()
weight_entry = tk.Entry(root)
weight_entry.pack()

result = tk.StringVar()
tk.Button(root, text="Calculate BMI", command=calculate_bmi).pack(pady=10)
tk.Label(root, textvariable=result).pack()

root.mainloop()