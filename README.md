# asynchronous-celery-tasks

### Fire up redis server: $ redis-server

### Test redis is working or not: $ redis-cli ping
The server should reply with PONG!

### Test that celery worker is ready to receive tasks: $ celery -A picha worker -l info

### Test that celery task scheduler is ready for action: $ celery -A picha beat -l info

After every 15 mins an image is fetched from Flickr
