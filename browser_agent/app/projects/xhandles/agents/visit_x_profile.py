from langchain_openai import ChatOpenAI
from browser_use import Agent, Controller, ActionResult
from browser_use.browser.context import BrowserContext

from browser_agent.app.projects.xhandles.prompts.search import visit_analyze_profile_on_twitter
from browser_agent.app.browsers.browser import main_browser
from browser_agent.app.config import app_config
from browser_agent.app.projects.xhandles.types import WebsiteAnalysisReq

controller = Controller()

@controller.registry.action('Done with task', param_model=WebsiteAnalysisReq)
async def done(params: WebsiteAnalysisReq):
	result = ActionResult(is_done=True, extracted_content=params.model_dump_json())
	return result

@controller.registry.action('Get Post Url')
async def get_post_url(browser: BrowserContext):
	page = await browser.get_current_page()
	return ActionResult(extracted_content=page.url)

def create_visit_x_profile_agent(handle) -> Agent:

  llm = ChatOpenAI(model=app_config.model, api_key=app_config.openai_api_key)



  # Create the agent with detailed instructions
  return Agent(
    task=visit_analyze_profile_on_twitter(
      handle,
    ),
    llm=llm,
    controller=controller,
    # use_vision=True,
    browser=main_browser,
  )
