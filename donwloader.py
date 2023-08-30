import tkinter as tk
from pytube import YouTube
from tkinter import messagebox

def play_video():
    video_url = entry.get()
    try:
        yt = YouTube(video_url)
        stream = yt.streams.get_highest_resolution()
        stream.download()
        messagebox.showinfo("Download Completed", "Vidéo Downloaded")
    except Exception as e:
        messagebox.showerror("Error", "An Error has happened : " + str(e))

app = tk.Tk()
app.title("Youtube Downloader")

label = tk.Label(app, text="Youtube URL")
label.pack(pady=10)

entry = tk.Entry(app)
entry.pack(pady=5)

button = tk.Button(app, text="Download", command=play_video)
button.pack(pady=10)

app.mainloop()


# Created by Roméo Tonon @romz 2023 
 
