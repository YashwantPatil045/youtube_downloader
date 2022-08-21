from tkinter import *
from tkinter import filedialog
from pytube import YouTube
from pytube.exceptions import RegexMatchError, VideoUnavailable


def select_path():
    path = filedialog.askdirectory()
    path_label.config(text=path)
    download_confirm.config(text="")


def download_video():
    link = link_field.get()
    user_path = path_label.cget("text")
    try:
        YouTube(link)
    except RegexMatchError:
        download_confirm.config(text="Invalid URL!", foreground="red")
    except VideoUnavailable:
        download_confirm.config(text="Video is unavailable for some reason", foreground="red")
    finally:
        YouTube(link).streams.get_highest_resolution().download(user_path)
        link_field.delete(0, END)
        download_confirm.config(text="Video Downloaded Successfully !", foreground="green")


screen = Tk()
title = screen.title("Youtube Downloader")
canvas = Canvas(screen, width=500, height=500)
canvas.pack()

logo = PhotoImage(file="yt.png")
logo = logo.subsample(6, 6)

canvas.create_image(250, 100, image=logo)

link_field = Entry(screen, width=50)
link_label = Label(screen, text="Enter YouTube URL ", font=("Monospace", 18))
instruction = Label(screen, text="Press Ctrl + v to paste URL ", font=("Monospace", 10), foreground="gray")
canvas.create_window(250, 270, window=instruction)

path_label = Label(screen, text="Select Path", font=("Monospace", 14))
path_button = Button(screen, text="Select", command=select_path)
canvas.create_window(250, 320, window=path_label)
canvas.create_window(250, 360, window=path_button)

canvas.create_window(250, 210, window=link_label)
canvas.create_window(250, 250, window=link_field)

download_button = Button(screen, text="Download Video", command=download_video)
download_confirm = Label(screen, text="", font=("Monospace", 12), foreground="green")
canvas.create_window(250, 460, window=download_confirm)
canvas.create_window(250, 430, window=download_button)

screen.mainloop()
