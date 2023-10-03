import tkinter
import customtkinter
from pytube import YouTube

def startDownload():
    try:
        ytlink = link.get()
        ytObject = YouTube(ytlink, on_progress_callback=onProgress)
        video = ytObject.streams.get_highest_resolution()
        title.configure(text=ytObject.title, text_color="white")
        finishLabel.configure(text="")
        video.download()
        finishLabel.configure(text="Downloaded", text_color="green")
    except:
        finishLabel.configure(text="Download Error", text_color="red")

def onProgress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_compeletion = bytes_downloaded / total_size * 100
    per = str(int(percentage_of_compeletion))
    pPercentage.configure(text=per + '%')
    pPercentage.update()
    # update progressbar
    progressBar.set(float(percentage_of_compeletion) / 100)

# Settings System
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

#frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title("Youtube Downloader")

#Adding UI Elements
title = customtkinter.CTkLabel(app, text="Insert a youtube link")
title.pack(padx=10, pady=10)

#Link
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=300, height=40)
link.pack()

#Finish info
finishLabel = customtkinter.CTkLabel(app, text="")
finishLabel.pack()

#Progress bar
pPercentage = customtkinter.CTkLabel(app, text="0%")
pPercentage.pack()

progressBar = customtkinter.CTkProgressBar(app, width=400)
progressBar.set(0)
progressBar.pack(padx=10, pady=10)

#Download Button
download = customtkinter.CTkButton(app, text="Download", command=startDownload)
download.pack(padx=10, pady=10)

#Run
app.mainloop()
