# scraper.py
import requests
from bs4 import BeautifulSoup

def extract_page_text(url):
    """
    Topic 1 & 3: Issues HTTP GET requests and breaks down the HTML DOM tree
    to pull out clean, raw readable text.
    """
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    try:
        # Topic 3: Send basic HTTP GET request with a strict safety timeout
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code != 200:
            return None
        
        # Topic 1: Parse DOM tree
        soup = BeautifulSoup(response.text, "html.parser")
        
        # Pull out and destroy visual design clutter and code blocks
        for element in soup(["script", "style", "nav", "footer", "header", "noscript"]):
            element.decompose()
            
        # Extract and format clean strings
        raw_text = soup.get_text(separator=" ")
        clean_text = " ".join(raw_text.split())
        
        # Constrain character depth to keep LLM context light
        return clean_text[:3500]
        
    except Exception:
        # If anti-bot security blocks us, return None to trigger our pipeline fallback
        return None