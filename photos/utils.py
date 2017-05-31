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

