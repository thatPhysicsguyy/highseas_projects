import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from datetime import datetime
import random

# Create root window
root = tk.Tk()
root.title("Todo Helper")
root.geometry("500x600")  # Adjusted for better layout

# Load the background image
background_image_path = ""  # Replace with the path to your image
try:
    bg_image = Image.open(background_image_path)
    bg_photo = ImageTk.PhotoImage(bg_image.resize((500, 600)))  # Resize image to fit the window
except Exception as e:
    messagebox.showerror("Error", f"Failed to load background image: {e}")
    bg_photo = None

# Create a canvas for the background image
canvas = tk.Canvas(root, width=500, height=600)
canvas.pack(fill="both", expand=True)
if bg_photo:
    canvas.create_image(0, 0, image=bg_photo, anchor="nw")

# Tasks dictionary
tasks = {}

# Function to update the listbox with color-coded tasks
def update_listbox():
    lb_tasks.delete(0, "end")
    today = datetime.today()
    for i, (task, date) in enumerate(tasks.items()):
        try:
            due_date = datetime.strptime(date, "%Y-%m-%d")
            delta = (due_date - today).days

            if delta < 0:
                color = "red"  # Overdue
            elif delta <= 3:
                color = "orange"  # Due soon
            else:
                color = "green"  # Distant due date

            lb_tasks.insert("end", f"{task} (Due: {date})")
            lb_tasks.itemconfig(i, fg=color)
        except ValueError:
            messagebox.showerror("Invalid Date", f"Invalid date format for task '{task}'.")

def add_task(event=None):
    task = txt_task.get()
    date = txt_date.get()
    if task and date:
        try:
            datetime.strptime(date, "%Y-%m-%d")  # Validate date format
            tasks[task] = date
            update_listbox()
            lbl_display.config(text="Task Added!", fg="green")
            root.after(2000, lambda: lbl_display.config(text=""))  # Clear message after 2 seconds
        except ValueError:
            messagebox.showerror("Invalid Date", "Please enter the date in YYYY-MM-DD format.")
    else:
        messagebox.showwarning("Incomplete Input", "Please enter both a task and a date.")
    txt_task.delete(0, "end")
    txt_date.delete(0, "end")

def delete_task():
    selected = lb_tasks.get("active")
    if selected:
        task = selected.split(" (Due:")[0]
        if task in tasks:
            confirm = messagebox.askyesno("Confirm Deletion", f"Delete task: '{task}'?")
            if confirm:
                del tasks[task]
                update_listbox()
                lbl_display.config(text="Task Deleted!", fg="red")
                root.after(2000, lambda: lbl_display.config(text=""))  # Clear message
    else:
        messagebox.showwarning("No Selection", "Please select a task to delete.")

def delete_all():
    confirm = messagebox.askyesno("Delete All", "Are you sure you want to delete all tasks?")
    if confirm:
        tasks.clear()
        update_listbox()

def sort_by_date():
    global tasks
    tasks = dict(sorted(tasks.items(), key=lambda item: item[1]))
    update_listbox()

def random_task():
    if tasks:
        task = random.choice(list(tasks.items()))
        lbl_display["text"] = f"Random Task: {task[0]} (Due: {task[1]})"
    else:
        lbl_display["text"] = "No tasks available!"

def exit_program():
    confirm = messagebox.askyesno("Exit", "Are you sure you want to exit?")
    if confirm:
        root.quit()

# Task Input Frame
frame_input = tk.Frame(canvas, bg="#FFFFFF", relief="ridge", bd=2)
frame_input.place(x=50, y=50, width=400, height=150)

lbl_title = tk.Label(frame_input, text="Add a New Task", font=("Arial", 16, "bold"), bg="#FFFFFF")
lbl_title.pack(pady=5)

lbl_task = tk.Label(frame_input, text="Task Name:", bg="#FFFFFF", anchor="w")
lbl_task.pack(fill="x", padx=10)
txt_task = tk.Entry(frame_input)
txt_task.pack(fill="x", padx=10, pady=5)

lbl_date = tk.Label(frame_input, text="Due Date (YYYY-MM-DD):", bg="#FFFFFF", anchor="w")
lbl_date.pack(fill="x", padx=10)
txt_date = tk.Entry(frame_input)
txt_date.pack(fill="x", padx=10, pady=5)

# Task List Frame
frame_list = tk.Frame(canvas, bg="#F8F8F8", relief="ridge", bd=2)
frame_list.place(x=50, y=220, width=400, height=250)

lb_tasks = tk.Listbox(frame_list, width=50, height=12)
lb_tasks.pack(padx=10, pady=10)

# Display Label
lbl_display = tk.Label(canvas, text="", bg="#FFFFFF", font=("Arial", 12))
lbl_display.place(x=50, y=480, width=400, height=30)

# Buttons Frame
frame_buttons = tk.Frame(canvas, bg="#FFFFFF")
frame_buttons.place(x=50, y=520, width=400, height=70)

btn_add_task = tk.Button(frame_buttons, text="Add Task", bg="#4CAF50", fg="white", command=add_task)
btn_add_task.grid(row=0, column=0, padx=5, pady=5)

btn_delete_task = tk.Button(frame_buttons, text="Delete Task", bg="#FF5722", fg="white", command=delete_task)
btn_delete_task.grid(row=0, column=1, padx=5, pady=5)

btn_delete_all = tk.Button(frame_buttons, text="Delete All", bg="#FF5722", fg="white", command=delete_all)
btn_delete_all.grid(row=0, column=2, padx=5, pady=5)

btn_sort_date = tk.Button(frame_buttons, text="Sort by Date", bg="#2196F3", fg="white", command=sort_by_date)
btn_sort_date.grid(row=1, column=0, padx=5, pady=5)

btn_random_task = tk.Button(frame_buttons, text="Random Task", bg="#FFC107", fg="black", command=random_task)
btn_random_task.grid(row=1, column=1, padx=5, pady=5)

btn_exit = tk.Button(frame_buttons, text="Exit", bg="#9E9E9E", fg="white", command=exit_program)
btn_exit.grid(row=1, column=2, padx=5, pady=5)

root.mainloop()
