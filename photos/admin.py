from django.contrib import admin

from photos.models import Photo
# Register your models here.

class PhotoAdmin(admin.ModelAdmin):
	pass

admin.site.register(Photo, PhotoAdmin)