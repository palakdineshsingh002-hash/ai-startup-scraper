# search_agent.py
import requests
import config

def get_startup_links(query):
    """
    Topic 4 & Tool 1: Queries Tavily Search to identify startup candidates.
    Filters out massive consumer directories.
    """
    url = "https://api.tavily.com/search"
    payload = {
        "api_key": config.TAVILY_API_KEY,
        "query": query,
        "search_depth": "advanced",
        "max_results": 35 # Fetch extra results to secure 20 high-quality hits
    }
    
    try:
        response = requests.post(url, json=payload)
        results = response.json()
        
        filtered_results = []
        if "results" in results:
            for item in results["results"]:
                link = item.get("url", "")
                
                # Filter out generic platforms
                blacklist = ["wikipedia.org", "linkedin.com", "youtube.com", "facebook.com", "twitter.com"]
                if any(domain in link.lower() for domain in blacklist):
                    continue
                    
                filtered_results.append({
                    "title": item.get("title"),
                    "link": link,
                    "snippet": item.get("content") # Pre-compiled context from Tavily
                })
        return filtered_results
    except Exception as e:
        print(f"❌ Error connecting to Tavily Search API: {e}")
        return []