import tkinter as tk
from tkinter import messagebox, filedialog
from PIL import Image

def select_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png")])
    if file_path:
        compress_image(file_path)

def compress_image(file_path):
    try:
        #open image
        img = Image.open(file_path)
        #obtain image name without extension
        file_name = file_path.rsplit("/", 1)[-1].rsplit(".", 1)[0]
        save_path = filedialog.asksaveasfilename(defaultextension=".jpg", filetypes=[("JPEG files", "*.jpg")], initialfile=f"{file_name}_compressed.jpg")

        if save_path:
            #compress image
            img.save(save_path, "JPEG", quality=90) #adjust quality
            messagebox.showinfo("Done", f"Image saved in: {save_path}")
    except Exception as e:
        messagebox.showerror("Error", f"Compress failed: {e}")

#main window        
ventana = tk.Tk()
ventana.title("PY Image Compressor :O")

#methods to obtain screen dimensions
width_screen = ventana.winfo_screenwidth() # width
height_screen = ventana.winfo_screenheight() # height

# automatic window size
width_window = 300
height_window = 200
position_x = (width_screen - width_window) // 2
position_y = (height_screen - height_window) // 2

#window size
ventana.geometry(f"{width_window}x{height_window}+{position_x}+{position_y}")

#buttons
btn_select = tk.Button(ventana, text="Select Image", command=select_image)
btn_select.pack(pady=20)
ventana.mainloop()


