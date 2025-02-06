
import os
from browser_agent.app.types import AppConfig


app_config = AppConfig(
		openai_api_key=os.getenv('OPENAI_API_KEY'),
		chrome_path='/opt/brave.com/brave/brave',
		headless=False,
	)