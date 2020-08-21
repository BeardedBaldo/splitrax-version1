import os
from django.conf import settings
from django.shortcuts import render


def UrlDownload():
	url = ""
	try:
		Command = "youtube-dl -x -o {} {}".format()
		os.system(Command)

	except:
		context = {
            "error_message": "Enter a valid Youtube URL, noob!",
            "TrackForm": TrackForm()
            }
        return render(request, "upload_ModelForm.html", context)
