from django import forms
from django.core.exceptions import ValidationError

from .models import UploadedFile


class UploadedFileForm(forms.ModelForm):
    class Meta:
        model = UploadedFile
        fields = ["file"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["file"].widget.attrs.update({"class": "form-control"})

    def clean_file(self):
        uploaded_file = self.cleaned_data["file"]
        filename = uploaded_file.name.lower()
        if not filename.endswith(".txt"):
            raise ValidationError("僅允許上傳 .txt 檔案。")
        return uploaded_file
