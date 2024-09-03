from django.contrib import admin

from app_book_app.models import *


class ProfileAdmin(admin.ModelAdmin):
    pass

admin.site.register(Profile, ProfileAdmin)
