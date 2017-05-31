from celery.decorators import task
from celery.utils.log import get_task_logger

from feedback.emails import send_feedback_email

@task(name='send_feedback_email_task')
def send_feedback_email_task(email, message):
	"""sends an email when feedback form is filled successfully"""
	logger.info("Sent feedback email")
	return send_feedback_email(email, message)	