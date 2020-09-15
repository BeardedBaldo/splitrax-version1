from django.urls import path
from .views import ModelFormsUpload, ContactView, AboutView, FaqView, TermsView

app_name = "uploadfile"

urlpatterns = [
    # path('', simple_upload, name = "Upload"),
    path('', ModelFormsUpload, name = "Upload"),
    path('contact/', ContactView, name = "Contact"),
    path('about/', AboutView, name = "About"),
    path('faq/', FaqView, name = "Faq"),
    path('terms/', TermsView, name = "Terms")


]