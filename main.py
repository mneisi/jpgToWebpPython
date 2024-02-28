import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image
import os

def select_images():
    file_paths = filedialog.askopenfilenames(title="Select JPG Images", filetypes=[("JPG Images", "*.jpg")])
    if not file_paths:
        return
    file_list.delete(0, tk.END)
    for path in file_paths:
        file_list.insert(tk.END, path)

def convert_to_webp():
    target_size = size_entry.get()
    try:
        width, height = map(int, target_size.split('x'))
    except ValueError:
        messagebox.showerror("Error", "Size must be in format WIDTHxHEIGHT (e.g., 800x600).")
        return
    
    for idx in range(file_list.size()):
        file_path = file_list.get(idx)
        image = Image.open(file_path)
        resized_image = image.resize((width, height))
        output_path = os.path.splitext(file_path)[0] + '.webp'
        resized_image.save(output_path, 'WEBP')
    
    messagebox.showinfo("Success", "Images converted and resized successfully.")

app = tk.Tk()
app.title("JPG to WebP Converter")

frame = tk.Frame(app)
frame.pack(pady=20)

select_button = tk.Button(frame, text="Select Images", command=select_images)
select_button.pack(side=tk.LEFT, padx=10)

convert_button = tk.Button(frame, text="Convert to WebP", command=convert_to_webp)
convert_button.pack(side=tk.LEFT, padx=10)

size_label = tk.Label(frame, text="Size (WIDTHxHEIGHT):")
size_label.pack(side=tk.LEFT, padx=10)

size_entry = tk.Entry(frame)
size_entry.pack(side=tk.LEFT, padx=10)
size_entry.insert(0, "800x600")

file_list = tk.Listbox(app, width=50, height=10)
file_list.pack(pady=20)

app.mainloop()
