import os
from uuid import uuid4
from django.db import models
from django.db import models
from django.conf import settings
from django.utils import timezone


def upload_to_func(instance, filename):
    prefix = timezone.now().strftime("%Y/%m/%d")
    file_name = uuid4().hex
    extension = os.path.splitext(filename)[-1].lower() # 확장자 추출
    return "/".join(
        [prefix, file_name, extension,]
    )



# Create your models here.
class Photo(models.Model):
    image = models.ImageField(upload_to = upload_to_func) # 어디로 업로드 할지 지정