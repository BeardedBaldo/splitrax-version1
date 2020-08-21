import youtube_dl
import os
from .forms import TrackForm
from django.shortcuts import render

url = "https://www.youtube.com/watch?v=e_hfh2k8p6o"
OutputPath = "/Volumes/Data/Adithya/ML_for_Audio_processing/Codes/"


import youtube_dl
import os

url = "https://www.youtube.com/watch?v=e_hfh2k8p6o"
OutputPath = "/Volumes/Data/Adithya/ML_for_Audio_processing/Codes/"


def YoutubeDownload(url, OutputPath):
	try:
		ydl_opts = {
			'format': 'bestaudio/best',
			'restrictfilenames': True,
			'outtmpl': os.path.join(OutputPath, '%(id)s.%(ext)s'),
			'noplaylist': True,
			'postprocessors': [{
		            'key': 'FFmpegExtractAudio',
		            'preferredcodec': 'mp3',
		        },
		        	{'key': 'FFmpegMetadata'},

		        ]
		}

		with youtube_dl.YoutubeDL(ydl_opts) as ydl:
		    id = ydl.extract_info(url, download = True)['id']
		    Filename = id + ".mp3"
		    return Filename

	except:
		return "Error_code-42069"


if __name__ == "__main__":
	Filename = YoutubeDownload(url, OutputPath)
	print(Filename)
	
	


