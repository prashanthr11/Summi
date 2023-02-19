from rest_framework.decorators import api_view
from django.http import JsonResponse
from .models import UserUploadedFiles
from django.views.decorators.csrf import csrf_exempt
import logging
from .utils import *
from summI.settings import MEDIA_PATH

# logging
logger = logging.getLogger("django")


# Create your views here.
@csrf_exempt
@api_view(["POST"])
def UserUploadedFilesView(request):
    if request.method == "POST":
        try:
            user = request.user
            uploaded_file = request.FILES['uploaded_file']
            is_valid_file = True

            print(dir(uploaded_file))
            print(uploaded_file.name)
            is_valid_file = validate_file(uploaded_file.file)

            print("is_valid_file ", is_valid_file)

            if is_valid_file:
                return JsonResponse({
                    "status": 200,
                    "message": "file format supported",
                })

            file_name = strip_html(uploaded_file.name)
            uploaded_file_object = UserUploadedFiles.objects.create(
                user=user, file_name=file_name)
            file_path = os.path.join(
                MEDIA_PATH, str(uploaded_file_object.uuid))

            if create_dirs(file_path):
                file_path = os.path.join(file_path, file_name)
                with open(file_path, "wb") as f:
                    f.write(uploaded_file.file.read())

                uploaded_file_object.file_path = file_path
                uploaded_file_object.save()
            else:
                return JsonResponse({
                    "status": 400,
                    "message": "cannot able to create a dir in media"
                })

            return JsonResponse({
                "status": 200,
                "message": "success",
                "image_id": str(uploaded_file_object.uuid),
            })
        except Exception as e:
            logger.error(str(e))
            return JsonResponse({
                "status": 500,
                "message": str(e),
            })
