

from langchain_openai import ChatOpenAI
from browser_use import Agent, Controller, ActionResult

from browser_agent.app.browsers.browser import init_browser
from browser_agent.app.config import app_config
from browser_agent.app.projects.xhandles.types import SearchProspectsResult
from browser_agent.app.projects.xhandles.prompts.search import get_search_result_profiles 

controller = Controller()

# ============ Configuration Section ============



@controller.registry.action('Done with task', param_model=SearchProspectsResult)
async def done(params: SearchProspectsResult):
    result = ActionResult(is_done=True, extracted_content=params.model_dump_json())
    return result


def create_twitter_prospects_agent() -> Agent:
    # Customize these settings
    
    llm = ChatOpenAI(model=app_config.model, api_key=app_config.openai_api_key)

    # Create the agent with detailed instructions
    return Agent(
        task=get_search_result_profiles(
            url='https://x.com/search?q=(chatgpt%20OR%20is%20OR%20down%20OR%20frustrated%20OR%20cancelling)&src=typed_query',
            count=30
        ),
        llm=llm,
        controller=controller,
        # use_vision=True,
        browser=init_browser(),
    )
