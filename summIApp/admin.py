from django.contrib import admin
from .models import UserUploadedFiles

# Register your models here.
class UserUploadedFilesAdmin(admin.ModelAdmin):
    ordering = ["-uploaded_datetime"]
    list_display = ["uuid", "user", "uploaded_datetime", "file_path"]

admin.site.register(UserUploadedFiles, UserUploadedFilesAdmin)
