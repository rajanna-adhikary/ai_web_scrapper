#  AI Web Scraper

This is a Streamlit-based AI-powered web scraper that extracts and parses content from websites—even those protected by CAPTCHAs like Amazon. It uses Bright Data’s remote browser to bypass bot detection, cleans the HTML using BeautifulSoup, and parses structured information using LangChain + Ollama.

##  Features

- Scrapes websites using Bright Data’s CAPTCHA-solving browser
- Extracts and cleans visible text from the DOM
- Splits large content into manageable chunks
- Uses LLMs to parse specific information based on user input
- Simple Streamlit interface for interaction

## Tech Stack

- Python
- Streamlit
- Selenium (with Bright Data)
- BeautifulSoup
- LangChain + Ollama

##  Project Structure
ai-web-scraper/
├── main.py          
├── Scrape.py        
├── parse.py         
├── requirements.txt 
├── .gitignore       
└── README.md        


