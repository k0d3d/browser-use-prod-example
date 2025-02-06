from typing import List
from pydantic import BaseModel

class SearchProspectsResult(BaseModel):
	author_handles: List[str]

class WebsiteAnalysisReq(BaseModel):
  tweet_url: str = ""
  tweet_content: str = ""
  profile_analysis: str = ""