from django.urls import path
from . import views

urlpatterns = [
    path("upload-file/", views.UserUploadedFilesView, name="UserUploadedFilesView"),
]
