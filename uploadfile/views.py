from django.http import HttpResponseRedirect, HttpResponse, FileResponse
from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import render
from .forms import TrackForm, ContactForm
from .models import FaqModel
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

    if request.method == "POST":
        try:
            UploadForm = TrackForm(request.POST, request.FILES) ## Get submit request
            
            if UploadForm.is_valid():
                UploadForm.save()  ## save file 

                Media_Root = getattr(settings, "MEDIA_ROOT", None) ## get location of media folder
                FileType = UploadForm.cleaned_data['OutputType'] ## get Output type
                NStems = UploadForm.cleaned_data['NStems'] ## get number of stems requried 
                
                if UploadForm.cleaned_data['YTLink'] is not None and UploadForm.cleaned_data['audio'] is None:
                    url = UploadForm.cleaned_data['YTLink']  ## get url
                    
                    Filename = YoutubeDownload(url, Media_Root)
                    if Filename == "Error_code-42069":
                        context = {
                            "error_message": "Use a valid Youtube link, please!",
                            "form": TrackForm()
                        }
                        return render(request, "upload_ModelForm.html", context)

                if UploadForm.cleaned_data['YTLink'] is None and UploadForm.cleaned_data['audio'] is not None:
                    Filename = UploadForm.cleaned_data['audio'].name.replace(" ", "_")   ## replace spaces with underscores

                MediaFile = os.path.join(Media_Root, Filename) ## get full file name

                
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


@csrf_protect 
def ContactView(request):
    context = {}
    form = ContactForm()
    context["form"] = form
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            form.save()

            FromEmail = form.cleaned_data["FromEmail"]
            Subject = form.cleaned_data["Subject"]
            Message = form.cleaned_data["Message"]
            RecipientList = ['adithya.ajith05@gmail.com']

            try:
                send_mail(subject = Subject, message = Message, from_email = FromEmail, recipient_list = RecipientList)
                context["SuccessMessage"] = "Mail was sent!"
                form = ContactForm()
                context["form"] = form

                return render(request, 'contact.html', context)

            except BadHeaderError:
                return HttpResponse('Invalid Header Found. Try Again.')

    return render(request, 'contact.html', context)


def AboutView(request):
    return render(request, "about.html")


def FaqView(request):
    FaqList = FaqModel.objects.all()
    context = {
        "FaqList": FaqList
    }
    print(FaqList)
    return render(request, "faq.html", context)


def TermsView(request):
    return render(request, "terms.html")



# def simple_upload(request):
#     if request.method == "POST":
#         try:
#             #UploadedFile = UploadTrack(request.POST, request.FILES)
#             start = datetime.datetime.now()
#             UploadedFile = request.FILES["track"]
#             fs = FileSystemStorage()
#             UploadedFile.name = UploadedFile.name.replace(" ", "_")
#             fs.save(UploadedFile.name, UploadedFile)
#             #UploadedFile.save()
#             print(UploadedFile.name)
#             print(UploadedFile.size)
#             print(UploadedFile.content_type)
#             Media_Root = getattr(settings, "MEDIA_ROOT", None)
#             MediaFile = os.path.join(Media_Root, UploadedFile.name)
#             FileType = "mp3"
#             SpleeterRun(MediaFile, Media_Root, FileType)
#             print(datetime.datetime.now() - start)
#             return render(request, "upload_test.html")

#         except(KeyError):
#             context = {
#                 "error_message": "Upload a file, pleb!"
#             }
#             return render(request, "upload_test.html", context)

#     return render(request, "upload_test.html")


