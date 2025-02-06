import asyncio
from app.celery import celery
from app.types import WebsiteAnalysisReq
from app.projects.xhandles.agents.visit_x_profile import create_visit_x_profile_agent

async def perform_analysis(agent):
	try:
		# await agent.run(max_steps=100)
		history = await agent.run(max_steps=100)

		result = history.final_result()
	except Exception as e:
		print(f'Error posting tweet: {str(e)}')

	return result

@celery.task(name="visit.profile", bind=True, rate_limit="2/m")
def visit_x_profile(self, handle: str):
	agent = create_visit_x_profile_agent(handle)
	result = asyncio.run(perform_analysis(agent))
	if not result:
		return {'result': 'no results'}
	analysisReq = WebsiteAnalysisReq.model_validate_json(result)

	return {
    'profile_analysis': analysisReq.profile_analysis,
    'tweet_url': analysisReq.tweet_url,
    'tweet_content': analysisReq.tweet_content
  }