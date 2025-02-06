

def get_search_result_profiles(url, count):
	return f"""Collect {count} user handles from the search results page 
        
        Here are the specific steps:

        1. Go to {url}. 
        2. Notice the user handle for each posts author profile 
        3. Collect {count} user handles or usernames.      
      
        """

def visit_analyze_profile_on_twitter(handle):
	return f"""
                Visit the profile page of https://x.com/{handle} on Twitter.
                Analyze the profile bio.
                Visit https://x.com/search?q=(crypto%20OR%20ai%20OR%20llm%20OR%20web3%20OR%20developer)%20(from%3A{handle})%20min_replies%3A5%20min_faves%3A10%20min_retweets%3A1&src=typed_query . 
                Analyze the top tweets and select a tweet you want to reply to that is related to Web3, AI or LLMs. 
                Click on the tweet and wait for the next page to load.
                Get the Url of the tweet.
      """