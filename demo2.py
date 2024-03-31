
import tkinter as tk
from PIL import Image, ImageTk
import time
import random

# Function to handle coin flipping logic
def tung(choice):
    result_label.config(text="......")  # Display "......" while flipping
    hieuung(5)  # Simulate coin flipping animation for 5 seconds

    # Randomly choose "Ngửa" (Heads) or "Sấp" (Tails)
    coin_side = random.choice(['Ngửa', 'Sấp'])

    # Determine the correct image based on player's choice and coin result
    kqhinhanh = anh7_photo if coin_side == 'Ngửa' and choice == 'Ngửa' else goat_photo
    kqhinhanh = goat_photo if coin_side == 'Sấp' and choice == 'Sấp' else anh7_photo

    # Display the result message and corresponding image
    hienthikq = "ANH 7 TAO LÀ SỐ 1." if coin_side == choice else "ANH 7 TAO MỘT MÌNH CHỐNG LẠI FIFA"
    image_label.config(image=kqhinhanh)
    result_label.config(text=hienthikq)

# Function to create the coin flipping animation
def hieuung(duration):
    start_time = time.time()
    while time.time() - start_time < duration:
        hienthi(anh7_photo, 0.1)  # Show front image for 0.1 seconds
        hienthi(goat_photo, 0.1)  # Show back image for 0.1 seconds

# Function to display the coin image
def hienthi(image, delay):  # tg_cho (delay) renamed for clarity
    image_label.config(image=image)
    root.update()
    time.sleep(delay)

# Create the main window
root = tk.Tk()
root.title("----Game sấp ngửa----")

# Window dimensions
window_width = 400
window_height = 540
# Calculate screen center coordinates (avoids negative values)
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
center_x = (screen_width - window_width) // 2
center_y = (screen_height - window_height) // 2

# Set window geometry with calculated center coordinates
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

# Display result label
result_label = tk.Label(root, text="Chọn mặt sấp hay ngửa", font=("bold"))
result_label.pack(pady=20)

# Load and resize coin images
anh7_image = Image.open('images/anh7.png')  # Ensure correct image paths
anh7_image = anh7_image.resize((300, 300), Image.LANCZOS)
anh7_photo = ImageTk.PhotoImage(anh7_image)

goat_image = Image.open('images/goat.png')
goat_image = goat_image.resize((300, 300), Image.LANCZOS)
goat_photo = ImageTk.PhotoImage(goat_image)

# Create image label (only one needed, update in `tung` function)
image_label = tk.Label(root)
image_label.pack(pady=20)

# Create button frame and buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

ngua_button = tk.Button(button_frame, text='Ngửa', bg='Gray', width=10, font=("bold"),
                         command=lambda: tung('Ngửa'))
ngua_button.pack(side=tk.LEFT, padx=10)

sap_button = tk.Button(button_frame, text='Sấp', bg='Gray', width=10, font=("bold"),
                        command=lambda: tung('Sấp'))
sap_button.pack(side=tk.RIGHT, padx=10)

root.mainloop()