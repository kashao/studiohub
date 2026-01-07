import re

from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_POST


PUNCTUATION_PATTERN = re.compile(
    r"[，。！？、；：「」『』（）《》【】…—,.!?;:'\"()\[\]{}<>]"
)


def clean_message(message: str) -> str:
    return PUNCTUATION_PATTERN.sub("", message).strip()


def index(request):
    return render(request, "chat/index.html")


@require_POST
def process_message(request):
    user_text = request.POST.get("usertext", "")
    cleaned_text = clean_message(user_text)
    return JsonResponse({"result": cleaned_text})
