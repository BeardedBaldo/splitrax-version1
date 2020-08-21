from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from .forms import TrackForm
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.contrib import messages
from .SpleeterCode import SpleeterRun
from .YoutubeDownload import YoutubeDownload
import shutil
import os
import datetime





def ModelFormsUpload(request):
    context = {}
    if request.method == "POST":
        try:
            UploadForm = TrackForm(request.POST, request.FILES) ## Get submit request
            if UploadForm.is_valid():
                UploadForm.save()  ## save file 

                Media_Root = getattr(settings, "MEDIA_ROOT", None) ## get location of media folder
                FileType = UploadForm.cleaned_data['OutputType']
                NStems = UploadForm.cleaned_data['NStems']

                if UploadForm.cleaned_data['YTLink'] is not None and UploadForm.cleaned_data['audio'] is None:
                    url = UploadForm.cleaned_data['YTLink']
                    
                    Filename = YoutubeDownload(url, Media_Root)
                    if Filename == "Error_code-42069":
                        context = {
                            "error_message": "Use a valid Youtube link, noob!",
                            "form": TrackForm()
                        }
                        return render(request, "upload_ModelForm.html", context)

                if UploadForm.cleaned_data['YTLink'] is None and UploadForm.cleaned_data['audio'] is not None:
                    Filename = UploadForm.cleaned_data['audio'].name.replace(" ", "_")

                MediaFile = os.path.join(Media_Root, Filename) ## get full file name

                #UploadForm.cleaned_data['audio'].name = UploadForm.cleaned_data['audio'].name.replace(" ", "_") ## replace spaces with strings in filenames
                #MediaFile = os.path.join(Media_Root, UploadForm.cleaned_data['audio'].name) ## get full file name                

                SpleeterRun(MediaFile, Media_Root, FileType, NStems) ## Run spleeter code

                FolderName = os.path.splitext(MediaFile)[0]
                ZippedFile = shutil.make_archive(FolderName, "zip", FolderName)


                Fl = open(ZippedFile, "r")
                response = HttpResponse(ZippedFile, content_type = "application/zip-download")
                response["Content-Disposition"] = "attachment; filename=%s" % ZippedFile
                return response
                # context["ZippedFile"] = ZippedFile
                # context["Filename"] = FolderName


                # return render(request, "SplitDone.html", context)

            else:
                context["error_message"] = UploadForm.non_field_errors().as_text()
                context["form"] = TrackForm()
                return render(request, "upload_ModelForm.html", context)

        except:
            
            context = {
                "error_message": UploadForm.non_field_errors().as_text(),
                "form": TrackForm()
            }
            return render(request, "upload_ModelForm.html", context)

    form = TrackForm()
    context = {
        "form": form
    }
    return render(request, "upload_ModelForm.html", context)



def simple_upload(request):
    if request.method == "POST":
        try:
            #UploadedFile = UploadTrack(request.POST, request.FILES)
            start = datetime.datetime.now()
            UploadedFile = request.FILES["track"]
            fs = FileSystemStorage()
            UploadedFile.name = UploadedFile.name.replace(" ", "_")
            fs.save(UploadedFile.name, UploadedFile)
            #UploadedFile.save()
            print(UploadedFile.name)
            print(UploadedFile.size)
            print(UploadedFile.content_type)
            Media_Root = getattr(settings, "MEDIA_ROOT", None)
            MediaFile = os.path.join(Media_Root, UploadedFile.name)
            FileType = "mp3"
            SpleeterRun(MediaFile, Media_Root, FileType)
            print(datetime.datetime.now() - start)
            return render(request, "upload_test.html")

        except(KeyError):
            context = {
                "error_message": "Upload a file, pleb!"
            }
            return render(request, "upload_test.html", context)

    return render(request, "upload_test.html")





# def simple_upload(request):
#     if request.method == "POST":
#         UploadedFile = request.FILES["document"]
#         fs = FileSystemStorage()
#         fs.save(UploadedFile.name, UploadedFile)
#     return render(request, "upload_test.html")


# def upload_file(request):
#     if request.method == 'POST':
#         form = UploadFileForm(request.POST, request.FILES)
#         if form.is_valid():
#             GetFileType(request.FILES['file'])
#             return HttpResponseRedirect('/success/url/')
#     else:
#         form = UploadFileForm()

#     context = {
# 		"form":form
# 	}

#     return render(request, 'upload.html', context)


# def simple_upload(request):
#     if request.method == 'POST' and request.FILES['myfile']:
#         myfile = request.FILES['myfile']
#         fs = FileSystemStorage()
#         filename = fs.save(myfile.name, myfile)
#         uploaded_file_url = fs.url(filename)
#         filetype = type(request.FILES['myfile'])
#         context = {
#         	'uploaded_file_url': uploaded_file_url,
#         	'filename': filename,
#         	'filetype': filetype
#         }
#         return render(request, 'upload.html', context)
#     return render(request, 'upload.html')