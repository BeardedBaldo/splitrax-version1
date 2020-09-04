from django.http import HttpResponseRedirect, HttpResponse, FileResponse
from django.shortcuts import render
from .forms import TrackForm
from .models import track
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.contrib import messages
from .SpleeterCodePy import SpleeterRun
from .YoutubeDownload import YoutubeDownload
import shutil
import os
from django.views.decorators.csrf import csrf_protect
import datetime




@csrf_protect
def ModelFormsUpload(request):
    context = {}
    print("reached level 1")
    if request.method == "POST":
        try:
            print("reached level 2")
            UploadForm = TrackForm(request.POST, request.FILES) ## Get submit request
            print(request.POST)
            ClassCheck = track(audio = request.FILES.get('audio'), YTLink = request.POST.get('YTLink'), NStems = request.POST.get('NStems'), OutputType = request.POST.get('OutputType') )
            print(ClassCheck.audio)
            print(ClassCheck.YTLink)
            print(ClassCheck.NStems)
            print(ClassCheck.OutputType)
            print(request.FILES)
            print(UploadForm.is_valid())
            print(TrackForm(request.POST, request.FILES))
            #print("uploadformnstems: --" + UploadForm.cleaned_data['Nstems'])
            #print("uploadformaudio: --" + UploadForm.cleaned_data['audio'])
            #print("isvalidcheck: --" + Upload.is_valid())
            print("reached level 3")
            if UploadForm.is_valid():
                UploadForm.save()  ## save file 
                print("reached level 4")
                Media_Root = getattr(settings, "MEDIA_ROOT", None) ## get location of media folder
                FileType = UploadForm.cleaned_data['OutputType']
                NStems = UploadForm.cleaned_data['NStems']
                print("reached level 5")
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


                Fl = open(ZippedFile, "rb")
                # response = HttpResponse(ZippedFile, content_type = "application/zip-download")
                # response["Content-Disposition"] = "attachment; filename=%s" % ZippedFile
                # return response
                return FileResponse(Fl, as_attachment = True)
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
