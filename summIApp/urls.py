from django.urls import path
from . import views

urlpatterns = [
    path("upload-file/", views.UserUploadedFilesView, name="UserUploadedFilesView"),
    # path("get-file/<uuid:image_id>", views.GetUserUploadedFileView, name="GetUserUploadedFileView"),
    path("summarise-text/",  views.GetSummarisedTextView, name="GetSummarisedTextView"),
    path("process-image-url/", views.ProcessImageURLView, name="ProcessImageURLView"),
]
