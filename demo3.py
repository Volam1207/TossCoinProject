import tkinter as tk
from PIL import Image, ImageTk
import time 
import random
import pygame


# Hàm tạo nhạc nền 
def play_music():
    pygame.mixer.music.load("music/nhac.mp3")
    pygame.mixer.music.play(loops=0)

# Hàm tạo nhạc khi bắt đầu game
def start_game_music():
    pygame.mixer.music.load("music/nhacig.mp3")
    pygame.mixer.music.play(loops=0)

# Hàm tạo nhạc khi kết thúc game
def end_game_music():
    pygame.mixer.music.load("music/nhacog.mp3")
    pygame.mixer.music.play(loops=0)

# Hàm tung đồng xu 
def tung(chon):
    result_label.config(text=" ... Đang tung đồng xu ...")
    start_game_music()  # Bắt đầu nhạc khi tung đồng xu
    hieuung(5) # Chuyển động trong 5s
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
    end_game_music()  # Phát nhạc kết thúc game
    pygame.mixer.music.set_endevent(pygame.USEREVENT)  # Xác định sự kiện kết thúc nhạc
    pygame.event.clear()  # Xóa các sự kiện trước đó
    


    # Load background music again
    play_music()

# Hàm hiệu ứng tung đồng xu
def hieuung(g):
    gio_batdau = time.time()
    while time.time() - gio_batdau < g:
        hienthi(anh7_photo, 0.10) # Hiển thị mặt trước trong 0.10s
        hienthi(goat_photo, 0.10) # Hiển thị mặt sau trong 0.10s

# Hàm hiển thị đồng xu đang tung
def hienthi(hinh, tg): # tg chờ
    image_label.config(image=hinh)
    root.update() # Cập nhật thay đổi
    time.sleep(tg)

root = tk.Tk()
root.title("----Game sấp ngửa----")

# Kích thước cửa sổ
window_width = 400
window_height = 540

# Tính toán tọa độ trung tâm của màn hình
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
center_x = (screen_width - window_width) // 2
center_y = (screen_height - window_height) // 2

# Thiết lập kích thước cửa sổ ở tọa độ trung tâm tính toán
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

result_label = tk.Label(root, text="Chọn mặt sấp hay ngửa", font=("bold"))
result_label.pack(pady=20)

# Ảnh mặt trước
anh7_image = Image.open('images/anh7.png').resize((300, 300), Image.LANCZOS)
anh7_photo = ImageTk.PhotoImage(anh7_image)

# Ảnh mặt sau
goat_image = Image.open('images/goat.png').resize((300, 300), Image.LANCZOS)
goat_photo = ImageTk.PhotoImage(goat_image)

image_label = tk.Label(root, image=anh7_photo)
image_label.pack(pady=20)

# Khởi tạo bộ trộn âm thanh của Pygame
pygame.mixer.init()

# Phát nhạc khi chương trình bắt đầu
play_music()

# Tạo nút sấp ngửa 
button = tk.Frame(root)
button.pack(pady=10)

# Nút sấp
ngua = tk.Button(button, text='Ngửa', bg='Gray', width=10, font=("bold"), command=lambda: tung('Ngửa'))
ngua.pack(side=tk.LEFT, padx=10)

# Nút ngửa
sap = tk.Button(button, text='Sấp', bg='Gray', width=10, font=("bold"), command=lambda: tung('Sấp'))
sap.pack(side=tk.RIGHT, padx=10)

# Dừng nhạc khi thoát chương trình
root.protocol("WM_DELETE_WINDOW", lambda: [pygame.mixer.music.stop(), root.destroy()])

root.mainloop()