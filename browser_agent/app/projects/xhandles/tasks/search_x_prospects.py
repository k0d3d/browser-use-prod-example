from app.celery import celery
import asyncio

from browser_agent.app.projects.xhandles.agents.search_x_prospects import create_twitter_prospects_agent
from browser_agent.app.projects.xhandles.types import SearchProspectsResult
from browser_agent.app.projects.xhandles.tasks.get_prospect_urls import get_prospect_urls




async def perform_search(agent):

  try:
      # await agent.run(max_steps=100)
      history = await agent.run(max_steps=100)

      result = history.final_result()
  except Exception as e:
      print(f"Error posting tweet: {str(e)}")

  return result

@celery.task(name="search.prospects", bind=True)
def search_prospects(self):
  # return result

  agent = create_twitter_prospects_agent()
  result = asyncio.run(perform_search(agent))
  if not result:
    return {'result': 'no results'}
  parsed = SearchProspectsResult.model_validate_json(result)
  get_prospect_urls.delay(parsed.author_handles,)
  return result