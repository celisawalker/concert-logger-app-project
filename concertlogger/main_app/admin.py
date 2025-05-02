from django.contrib import admin
from .models import Concert, Artist
# Register your models here.

admin.site.register([Concert, Artist])