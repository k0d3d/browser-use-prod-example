import os
from celery import Celery
from dotenv import load_dotenv

load_dotenv()

# celery broker and backend urls
CELERY_BROKER_URL = os.getenv("REDISSERVER", "redis://localhost:6379")
CELERY_RESULT_BACKEND = os.getenv("REDISSERVER", "redis://localhost:6379")


# create celery application
celery = Celery(
	'tasks',
	backend=CELERY_BROKER_URL,
	broker=CELERY_RESULT_BACKEND,
	include=[
		'tasks.projects.xhandles.tasks.search_prospects',
		'tasks.projects.xhandles.tasks.get_prospect_urls',
		'tasks.projects.xhandles.tasks.visit_profile',
	],
)

if __name__ == '__main__':
	celery.start()