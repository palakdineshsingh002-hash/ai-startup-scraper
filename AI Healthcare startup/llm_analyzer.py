# llm_analyzer.py
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from config import GEMINI_API_KEY

def analyze_startup_content(web_text, search_snippet):
    """
    Uses LangChain and Gemini API to extract targeted metrics from raw text.
    """
    # Initialize the Gemini model via LangChain
    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash", 
        google_api_key=GEMINI_API_KEY, 
        temperature=0 # Forced deterministic mapping
    )
    
    # Strictly define the layout rules required by the assignment
    prompt = ChatPromptTemplate.from_messages([
        ("system", """You are a precise market research AI agent.
        Review the provided data and format your output EXACTLY like the example below.
        Do not add generic introductory chat, summary remarks, markdown ticks, or markdown bold text headers.
        
        Template Format:
        Startup: [Exact corporate name]
        Website: [Clean homepage URL]
        Funding: [Current investment stage like Seed, Series A, Series B, etc., or 'Not available']
        Summary: [A concise, single-sentence summary detailing their core Indian AI healthcare product]
        """),
        ("user", "Analyze this collected web packet:\nSearch Context: {snippet}\nScraped Text: {body}")
    ])
    
    chain = prompt | llm | StrOutputParser()
    
    try:
        return chain.invoke({"snippet": search_snippet, "body": web_text})
    except Exception as e:
        return f"Error extracting info: {e}"