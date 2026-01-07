import os

from .base import *  # noqa: F403,F401

DEBUG = True

ALLOWED_HOSTS = ["127.0.0.1", "localhost"]

if "DJANGO_SECRET_KEY" in os.environ:
    SECRET_KEY = os.environ["DJANGO_SECRET_KEY"]
