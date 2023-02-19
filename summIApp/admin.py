from django.contrib import admin
from .models import UserUploadedFiles

# Register your models here.
class UserUploadedFilesAdmin(admin.ModelAdmin):
    fields = ["user", "file_path", "uploaded_datetime"]

admin.site.register(UserUploadedFiles)
