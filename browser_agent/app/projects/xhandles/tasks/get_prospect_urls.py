from typing import List
from browser_agent.app.celery import celery
from browser_agent.app.projects.xhandles.tasks.visit_x_profile import visit_x_profile

@celery.task(name="get.prospect.urls", bind=True)
def get_prospect_urls(self, result: List[str]):
  # loop over result.author_handles
  for handle in result:
    visit_x_profile.delay(handle, )

  return True