# main.py
import time
import config
from search_agent import get_startup_links
from scraper import extract_page_text
from llm_analyzer import analyze_startup_content

def run_agent_pipeline():
    print("="*60)
    print(f" Agent Initiated: Hunting for '{config.TARGET_INDUSTRY}'")
    print("="*60)
    
    # Step 1: Discover potential leads using Tavily
    print("\n Step 1: Running Tavily Search Engine API Extraction...")
    discovered_leads = get_startup_links(config.TARGET_INDUSTRY)
    print(f" Search complete. Discovered {len(discovered_leads)} target references.\n")
    
    successful_count = 0
    
    # Step 2: Pipeline Loop Execution
    print(f" Step 2: Driving Scraping and AI Summary Loop (Target: {config.REQUIRED_ENTRIES})...\n")
    print("-" * 50)
    
    for lead in discovered_leads:
        if successful_count >= config.REQUIRED_ENTRIES:
            break
            
        url = lead["link"]
        snippet = lead["snippet"]
        
        print(f" [{successful_count + 1}/{config.REQUIRED_ENTRIES}] Processing Target: {url}")
        
        # Step 2a: Scrape live web page DOM content
        page_text = extract_page_text(url)
        
        # Topic 2 Resiliency Fallback: If scraper fails/is blocked, fall back to Tavily's pre-parsed context
        if not page_text or len(page_text) < 150:
            print(" Live scraping restricted. Utilizing Tavily context fallback packet.")
            page_text = f"Context: {snippet}"
            
        # Step 2b: Send data package to Gemini via LangChain
        print(" Invoking Gemini AI parsing layer...")
        structured_profile = analyze_startup_content(page_text, snippet)
        
        # Step 2c: Validate and output formatting block
        if "Startup:" in structured_profile:
            print("\n" + structured_profile)
            print("-" * 50 + "\n")
            successful_count += 1
            
        # Topic 2: Polite crawl sleep interval between calls
        time.sleep(1.5)

    print("="*60)
    print(f" Mission Accomplished! Generated {successful_count} verified profiles.")
    print("="*60)

if __name__ == "__main__":
    run_agent_pipeline()