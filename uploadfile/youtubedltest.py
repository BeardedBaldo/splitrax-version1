import youtube_dl
import os

ydl_opts = {}

print(os.getcwd())
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download(['https://www.youtube.com/watch?v=e_hfh2k8p6o'])