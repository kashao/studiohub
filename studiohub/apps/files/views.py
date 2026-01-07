from django.shortcuts import redirect, render

from .forms import UploadedFileForm
from .models import UploadedFile

def index(request):
    if request.method == "POST":
        form = UploadedFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("files-index")
    else:
        form = UploadedFileForm()

    files = UploadedFile.objects.order_by("-uploaded_at")
    return render(request, "files/index.html", {"form": form, "files": files})
