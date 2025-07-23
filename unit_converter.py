import tkinter as tk

def convert():
    value = float(entry.get())
    unit = unit_var.get()
    
    if unit == "Kilometers to Miles":
        result.set(f"{round(value * 0.621371, 2)} Miles")
    elif unit == "Miles to Kilometers":
        result.set(f"{round(value / 0.621371, 2)} Kilometers")
    elif unit == "Celsius to Fahrenheit":
        result.set(f"{round((value * 9/5) + 32, 2)} °F")
    elif unit == "Fahrenheit to Celsius":
        result.set(f"{round((value - 32) * 5/9, 2)} °C")

root = tk.Tk()
root.title("Unit Converter")
root.geometry("300x200")

entry = tk.Entry(root)
entry.pack(pady=10)

unit_var = tk.StringVar()
unit_var.set("Kilometers to Miles")
options = [
    "Kilometers to Miles",
    "Miles to Kilometers",
    "Celsius to Fahrenheit",
    "Fahrenheit to Celsius"
    ]
tk.OptionMenu(root, unit_var, *options).pack()

tk.Button(root, text="Convert", command=convert).pack(pady=10)

result = tk.StringVar()
tk.Label(root, textvariable=result).pack()

root.mainloop()
