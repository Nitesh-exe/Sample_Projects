import tkinter as tk

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)

def delete_task():
    selected = listbox.curselection()
    if selected:
        listbox.delete(selected[0])

root = tk.Tk()
root.title("To-Do List")

entry = tk.Entry(root, width=25)
entry.pack(pady=5)

tk.Button(root, text="Add Task", command=add_task).pack()
tk.Button(root, text="Delete Task", command=delete_task).pack()

listbox = tk.Listbox(root, width=30, height=10)
listbox.pack(pady=5)

root.mainloop()
