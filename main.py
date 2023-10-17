import tkinter as tk
from tkinter import filedialog, messagebox
import sys
from file_organizer import organize_files
def execute_program(source_path, destination_path):
    destination_path1=destination_path.replace("\\", "/")
    source_path1=source_path.replace("\\", "/")
    organize_files(source_path1,destination_path1)
    
def browse_source_path():
    source_path = filedialog.askdirectory()
    source_path_var.set(source_path)

def browse_destination_path():
    destination_path = filedialog.askdirectory()
    destination_path_var.set(destination_path)

def on_convert_button_click():
    source_path = source_path_var.get()
    destination_path = destination_path_var.get()

    if source_path and destination_path:
        execute_program(source_path, destination_path)
        messagebox.showwarning("Note","Operation is completed successfully.")
        sys.exit()
    elif not source_path and destination_path:
        messagebox.showwarning("Warning", "Please select a source path.")
    elif not destination_path and source_path:
        messagebox.showwarning("Warning", "Please select a destination path.")
    elif not source_path and not destination_path:
        messagebox.showwarning("Warning", "Please select source and destination paths.")

root = tk.Tk()
root.title("My Desktop App")

source_path_var = tk.StringVar()
destination_path_var = tk.StringVar()

# Widgets
source_label = tk.Label(root, text="Source Path:")
source_entry = tk.Entry(root, textvariable=source_path_var)
source_button = tk.Button(root, text="Browse", command=browse_source_path)

destination_label = tk.Label(root, text="Destination Path:")
destination_entry = tk.Entry(root, textvariable=destination_path_var)
destination_button = tk.Button(root, text="Browse", command=browse_destination_path)
convert_button = tk.Button(root, text="Convert", command=on_convert_button_click)

# Layout
source_label.grid(row=0, column=0, padx=10, pady=5, sticky=tk.E)
source_entry.grid(row=0, column=1, padx=10, pady=5, sticky=tk.W)
source_button.grid(row=0, column=2, padx=5, pady=5)

destination_label.grid(row=1, column=0, padx=10, pady=5, sticky=tk.E)
destination_entry.grid(row=1, column=1, padx=10, pady=5, sticky=tk.W)
destination_button.grid(row=1, column=2, padx=5, pady=5)

convert_button.grid(row=2, column=0, columnspan=3, pady=10)

root.mainloop()
