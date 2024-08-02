from pytube import YouTube
from pytube import Playlist
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import os

#Functions to decide what to download

def download_video(): 
    try:
        url_ = eee.get()
        yt = YouTube(url_)
    except:
        messagebox.showerror(message="Enter a valid URL!")
        exit()

    try:
        print("Now downloading "+yt.title+" to folder "+outpath)
        yt.streams.get_highest_resolution().download(outpath)
        print("Successfully downloaded "+yt.title)
        messagebox.showinfo(message="Video file "+yt.title+" downloaded.")
    except:
        print("Error occured whilst trying to download video file " + yt.title)
        messagebox.showerror(message="Error occured whilst trying to download video file "+yt.title)
        exit()

def download_audio():
    try:
        url_ = eee.get()
        yt = YouTube(url_)
    except:
        messagebox.showerror(message="Enter a valid URL!")
        exit()
   
    try:
        print("Now downloading audio of "+yt.title+" to folder "+outpath)
        out_file = yt.streams.get_highest_resolution().download(outpath)
        base, ext = os.path.splitext(out_file) 
        new_file = base + '.mp3'
        os.rename(out_file, new_file) 
        print("Successfully downloaded audio of "+yt.title)
        messagebox.showinfo(message="Audio file "+yt.title+" downloaded.")
    except:
        print("Error occured whilst trying to download audio file " + yt.title)
        messagebox.showerror(message="Error occured whilst trying to download audio file "+yt.title)
        exit()

def download_list():
    try:
        pid = eee.get()
        t = selected.get()
        p = Playlist('https://www.youtube.com/playlist?list=' + pid)
    except:
        messagebox.showerror(message="Enter a valid Playlist ID!")
        exit()
    
    if t == 'vaa':
        for video in p.videos:
            try:
                print("Downloading " + video.title)
                video.streams.get_highest_resolution().download(outpath)
                print(video.title + " downloaded.")
            except:
                print("All videos downloaded or an error occured.")
                messagebox.showinfo(message="All videos are downloaded or error occured.")
                exit()
    elif t == 'oa':
        for video in p.videos:
            try:
                print("Downloading " + video.title)
                out_file = video.streams.get_highest_resolution().download(outpath)
                base, ext = os.path.splitext(out_file) 
                new_file = base + '.mp3'
                os.rename(out_file, new_file) 
                print(video.title + " downloaded.")
            except:
                print("All audios downloaded or an error occured.")
                messagebox.showinfo(message="All audios are downloaded or error occured.")
                exit()
    else:
        messagebox.showerror(message="Enter option what to download!")
        exit()

def select_outpath():
    global outpath
    outpath = filedialog.askdirectory(title="Choose saving directory")
    

root = Tk()
root.title('DownPlay - by CHVILI')

eee = StringVar()
url_ = ""
selected = StringVar()

notebook = ttk.Notebook(root)
notebook.pack()

# create frames
frame1 = ttk.Frame(notebook, width=400, height=280)
frame2 = ttk.Frame(notebook, width=400, height=280)
frame3 = ttk.Frame(notebook, width=400, height=280)

frame1.pack(fill='both', expand=True)
frame2.pack(fill='both', expand=True)
frame3.pack(fill='both', expand=True)


# add frames to notebook

notebook.add(frame1, text='Video')
notebook.add(frame2, text='Audio')
notebook.add(frame3, text='Playlist')

Label(frame1, text='Video Downloader').pack()
Label(frame1, text='Enter Video URL:').pack()
Entry(frame1, textvariable=eee, width=50).pack()
Button(frame1, text='Download', command=download_video).pack()
Button(root,text="Select save directory",command=select_outpath).pack()

Label(frame2, text='Audio Downloader').pack()
Label(frame2, text='Enter Video URL to extract audio:').pack()
Entry(frame2, textvariable=eee, width=50).pack()
Button(frame2, text='Download', command=download_audio).pack()

Label(frame3, text='PlayList Downloader').pack()
Label(frame3, text='Enter Playlist ID:').pack()
Entry(frame3, textvariable=eee, width=50).pack()
Label(frame3, text='Options').pack()
r1 = ttk.Radiobutton(frame3, text='Download Video & Audio', value='vaa', variable=selected).pack()
r2 = ttk.Radiobutton(frame3, text='Download Only Audio', value='oa', variable=selected).pack()
Button(frame3, text='Download', command=download_list).pack()

root.mainloop()