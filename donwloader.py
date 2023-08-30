import tkinter as tk
from pytube import YouTube
from tkinter import messagebox

def play_video():
    video_url = entry.get()
    try:
        yt = YouTube(video_url)
        stream = yt.streams.get_highest_resolution()
        stream.download()
        messagebox.showinfo("Téléchargement Terminé", "La vidéo a été téléchargée.")
    except Exception as e:
        messagebox.showerror("Erreur", "Une erreur est survenue : " + str(e))

app = tk.Tk()
app.title("Lecteur de Vidéo YouTube")

label = tk.Label(app, text="URL de la vidéo YouTube:")
label.pack(pady=10)

entry = tk.Entry(app)
entry.pack(pady=5)

button = tk.Button(app, text="Lire la Vidéo", command=play_video)
button.pack(pady=10)

app.mainloop()


# Created by Roméo Tonon @romz 2023 
 
