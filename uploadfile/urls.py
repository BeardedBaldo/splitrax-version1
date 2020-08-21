from django.urls import path
from .views import simple_upload, ModelFormsUpload

app_name = "uploadfile"

urlpatterns = [
    # path('', simple_upload, name = "Upload"),
    path('', ModelFormsUpload, name = "Upload"),
]