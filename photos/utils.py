import json
import requests

from photos.models import Photo
from django.conf import settings

def get_latest_flickr_image():
	"""
	Grabs the latest image from the flick public image feed
	"""
	url = settings.FLICKR_JSON_FEED_URL
	r = requests.get(url)
	page_content = r.text

	# It turns out flickr escapes single quotes (')
	# and apparently this isn't allowed and makes the json invalid
	# we use String.replace to get around this.

	probably_json = page_content.replace("\\'", "'")
	# now we load json

	feed = json.loads(probably_json)
	images = feed['items']
	return images[0]

def save_latest_flickr_image():
	"""
	We get the lastest image and save it to flickr model
	"""
	flickr_image = get_latest_flickr_image()
	# make sure we don't save the image more than once
	# assuming each flickr image has a unique link
	if not Photo.objects.filter(link=flickr_image['link']).exists():
		photo = Photo(
				title = flickr_image['title'],
				link = flickr_image['link'],
				image_url = flickr_image['media']['m'],
				description = flickr_image['description'],
			)
		photo.save()