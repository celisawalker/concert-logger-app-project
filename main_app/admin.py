from django.contrib import admin
from .models import Concert, Artist, Library
# Register your models here.

admin.site.register([Concert, Artist, Library])