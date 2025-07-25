# 🧠 AI Web Scraper

A powerful and adaptive Streamlit-based web scraping tool enhanced with AI. It extracts and parses content from websites—including those protected by CAPTCHAs like Amazon—using Bright Data’s remote browser. Clean HTML processing, chunked text handling, and LLM-powered parsing make this a seamless experience for automated data collection and analysis.

---

## 🚀 Features

- ✅ Bypasses CAPTCHAs using Bright Data’s stealth browser  
- 🧼 Cleans and extracts visible text from the DOM  
- 📦 Automatically splits lengthy content into digestible chunks  
- 🧠 Parses targeted information using LangChain + Ollama (LLM-powered)  
- 🎛️ Intuitive Streamlit interface for user-friendly interaction  

---

## 🛠 Tech Stack

| Tool/Library            | Purpose                                |
|------------------------|----------------------------------------|
| Python                 | Core scripting language                |
| Streamlit              | Web interface and interaction          |
| Selenium + Bright Data | Dynamic scraping with CAPTCHA bypass   |
| BeautifulSoup          | HTML parsing and cleaning              |
| LangChain + Ollama     | AI-based contextual parsing            |

---

## 📁 Project Structure

```bash
ai-web-scraper/
├── main.py           # Streamlit app entry point
├── Scrape.py         # Web scraping logic
├── parse.py          # LLM-based parsing utilities
├── requirements.txt  # Python dependencies
├── .gitignore        # Git exclusions
└── README.md         # Project documentation
