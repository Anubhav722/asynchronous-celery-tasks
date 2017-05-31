from django.db import models

# Create your models here.
class Photo(models.Model):
	created_on = models.DateTimeField("Created on", auto_now_add=True)
	updated_on = models.DateTimeField("Updated on", auto_now=True)
	title = models.CharField("Title", max_length=255)
	link = models.URLField("Photo Link", max_length=255, help_text="The URL to the image page")
	image_url = models.URLField("Image Url", max_length=255, help_text="The URL to the image file itself")
	description = models.TextField("Description")

	class Meta:
		verbose_name = "Photo"
		verbose_name_plural = "Photos"
		ordering = ['created_on', 'title']

	def __unicode__(self):
		return self.title