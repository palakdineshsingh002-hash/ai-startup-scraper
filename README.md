# Startup Intelligence Scraper Agent 🤖

A smart Python AI agent that automatically searches the internet, crawls web pages, and uses Google Gemini to collect data on **20 AI healthcare startups in India**.

This project was built to demonstrate core web data extraction techniques like DOM parsing, HTTP handling, and Search Engine APIs.

---

## 📁 What Each File Does

The project is split into 5 simple files to keep the code clean and organized:

1. **`config.py`**: The settings room. It stores your API keys and target limits safely.
2. **`search_agent.py`**: The scout. It uses the **Tavily Search API** to search Google and gather the startup links.
3. **`scraper.py`**: The reader. It uses **BeautifulSoup** to open the websites, strip away junk code, and grab clean text.
4. **`llm_analyzer.py`**: The brain. It uses **LangChain** and **Google Gemini** to read the website text and summarize it.
5. **`main.py`**: The manager. It runs the entire loop automatically until it collects exactly 20 startups.

---

## 🛠️ How to Set It Up

### 1. Install Libraries
Open your terminal and run this command to install everything needed:
```bash
pip install requests beautifulsoup4 langchain langchain-core langchain-google-genai
