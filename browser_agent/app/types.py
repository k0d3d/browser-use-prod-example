from typing import List, Optional
from pydantic import BaseModel

class SendPostReq(BaseModel):
  tweet_url: str = ""
  reply_content: str = ""

class RollerCoasterGlossaryPageResult(BaseModel):
	roller_coaster_urls: List[str]


class RollerCoasterElements(BaseModel):
    elementName: str = ""


class RollerCoaster(BaseModel):
    name: str = ""
    park: str = ""
    location: str = ""
    position: Optional[List[float]] = None
    status: str = ""
    openingYear: Optional[float] = None
    type: str = ""
    model: str = ""
    manufacturer: str = ""
    elements: List[RollerCoasterElements] = []
    design: str = ""
    trackLayout: str = ""
    scale: str = ""
    inversions: Optional[float] = None
    url: str = ""


class TwitterConfig(BaseModel):
	"""Configuration for Twitter posting"""

	openai_api_key: str = ""
	chrome_path: str = ""
	target_user: Optional[str] = None
	message: Optional[str] = None
	reply_url: Optional[str] = None
	headless: bool = False
	model: str = 'gpt-4o'
	base_url: str = 'https://x.com/home'

class AppConfig(BaseModel):
	"""Configuration for Twitter posting"""

	openai_api_key: str = ""
	chrome_path: str = ""
	headless: bool = False
	model: str = 'gpt-4o'
