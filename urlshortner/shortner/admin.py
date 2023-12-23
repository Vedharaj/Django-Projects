from django.contrib import admin
from .models import Url

# Register your models here.
class UrlDisplay(admin.ModelAdmin):
    list_display = ("link", "uuid")

admin.site.register(Url, UrlDisplay)