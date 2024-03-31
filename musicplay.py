import tkinter as tk


def play_music():
    pygame.mixer.music.load("music/nhac.mp3")
    pygame.mixer.music.play(loops=0)

def stop_music():
    pygame.mixer.music.stop()

root = tk.Tk()
root.title("Music Player")

play_button = tk.Button(root, text="Play Music", command=play_music)
play_button.pack(pady=10)

stop_button = tk.Button(root, text="Stop Music", command=stop_music)
stop_button.pack(pady=10)

# Initialize Pygame mixer
pygame.mixer.init()

root.mainloop()