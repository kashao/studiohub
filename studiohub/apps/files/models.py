from django.core.validators import FileExtensionValidator
from django.db import models


class UploadedFile(models.Model):
    file = models.FileField(
        upload_to="files/",
        validators=[FileExtensionValidator(["txt"])],
    )
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.file.name
