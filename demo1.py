import tkinter as tk
from PIL import Image, ImageTk
import time 
import random
import threading

# Tạo biến để kiểm soát việc nhấp nháy
blinking = True

# Tạo hàm tung đồng xu 
def tung(chon):
    result_label.config(text="......")
    hieuung(5)  # Chuyển động trong 5 giây
    ngaunhien = random.choice(['Ngửa', 'Sấp'])
    kqhinhanh = None
    if ngaunhien == "Ngửa":
        kqhinhanh = anh7_photo
    else:
        kqhinhanh = goat_photo
    hienthikq = None
    if ngaunhien == chon:
        hienthikq = " Vamos! bạn đã đoán đúng."
    else: 
        hienthikq = " Tiếc quá! Bạn sai rồi! "
    image_label.config(image=kqhinhanh)
    result_label.config(text=hienthikq)
    # Dừng nhấp nháy dòng text khi ra kết quả
    global blinking
    blinking = False

# Tạo hiệu ứng tung đồng xu
def hieuung(g):
    gio_batdau = time.time()
    while time.time() - gio_batdau < g :
        hienthi(anh7_photo, 0.10)  # Hiển thị mặt trước trong 0.10 giây
        hienthi(goat_photo, 0.10)  # Hiển thị mặt sau trong 0.10 giây

# Hàm hiển thị đồng xu đang tung
def hienthi(hinh, tg):  # tg chờ
    image_label.config(image=hinh)
    root.update()  # Cập nhật thay đổi
    time.sleep(tg)

# Hàm để làm nhấp nháy dòng text
def blink_text():
    while blinking:  # Chỉ nhấp nháy khi biến blinking là True
        result_label.config(text="......")
        time.sleep(0.5)
        result_label.config(text="Vui lòng đợi...")
        time.sleep(0.5)

root = tk.Tk()
root.title("----Game sấp ngửa----")

# Cửa sổ chiều rộng và cao
window_width = 400
window_height = 540

# Tính toán tọa độ trung tâm của màn hình (tránh giá trị âm)
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
center_x = (screen_width - window_width) // 2
center_y = (screen_height - window_height) // 2

# Thiết lập kích thước cửa sổ với tọa độ trung tâm tính toán
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

# Chỉnh màu nền của cửa sổ là màu xanh lam
root.configure(bg='blue')

# Hiển thị
result_label = tk.Label(root, text="Chọn mặt sấp hay ngửa", font=("bold"))
result_label.pack(pady=20)

# Hình ảnh mặt trước 
anh7_image = Image.open('images/anh7.png').resize((300, 300), Image.LANCZOS)
anh7_photo = ImageTk.PhotoImage(anh7_image)

# Hình ảnh mặt sau 
goat_image = Image.open('images/goat.png').resize((300, 300), Image.LANCZOS)
goat_photo = ImageTk.PhotoImage(goat_image)

# Label
image_label = tk.Label(root, image=anh7_photo)
image_label.pack(pady=20)

# Tạo nút sấp ngửa 
button = tk.Frame(root)
button.pack(pady=10)

# Nút sấp
ngua = tk.Button(button, text='Ngửa', bg='Gray', width=10, font=("bold"), command=lambda: tung('Ngửa'))
ngua.pack(side=tk.LEFT, padx=10)

# Nút ngửa
sap = tk.Button(button, text='Sấp', bg='Gray', width=10, font=("bold"), command=lambda: tung('Sấp'))
sap.pack(side=tk.RIGHT, padx=10)

# Tạo một luồng riêng để làm nhấp nháy dòng text
blink_thread = threading.Thread(target=blink_text)
blink_thread.daemon = True
blink_thread.start()

root.mainloop()