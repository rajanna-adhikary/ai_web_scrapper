# import selenium
# import selenium.webdriver as webdriver
# from selenium.webdriver.chrome.service import Service
# import time
# #function to grab the content using selenuim


# def scrape_website(website):
#     print("launching chrome browser....")

#     chrome_driver_path= "./chromedriver.exe"
#     options= webdriver.ChromeOptions()
#     driver=webdriver.Chrome(service=Service(chrome_driver_path),options=options)

#     try:
#         driver.get(website)
#         print("page loaded....")
#         html= driver.page_source
#         time.sleep(10)

#         return html
#     finally:
#         driver.quit()
#This is the same code as above, which uses the regular Chrome driver. But the code below uses Bright Data to solve problems like accessing websites such as Amazon. These sites often detect bots trying to scrape them and respond with login CAPTCHAs and other challenges.
#so we will use bright data
from selenium.webdriver import Remote, ChromeOptions
from selenium.webdriver.chromium.remote_connection import ChromiumRemoteConnection
from bs4 import BeautifulSoup
# This link connects your Python code to a browser running in the cloud (not on your computer). It’s like saying:
# “Hey Bright Data, spin up a Chrome browser for me, and I’ll control it from here.”
SBR_WEBDRIVER = 'https://brd-customer-hl_498b1d91-zone-ai_scraper:k3f5n1yysax2@brd.superproxy.io:9515'

# you don’t need to know the internal code of Bright Data’s browser. But you should understand what it’s doing at a high level:
# It runs a remote browser (like Chrome in the cloud).
# It solves CAPTCHAs using its own backend tools.
# It returns the final HTML after the page is fully loaded.
def scrape_website(website):
    print(f'→ Connecting to Browser API for: {website}')

    # Normalize the URL
    website = website.strip()
    if not website.startswith(('http://', 'https://')):
        website = 'https://' + website

    sbr_connection = ChromiumRemoteConnection(SBR_WEBDRIVER, 'goog', 'chrome')
    with Remote(sbr_connection, options=ChromeOptions()) as driver:
        print(f'→ Navigating to: {website}')
        #tells the browswer to go to the website
        driver.get(website)

        # Try solving CAPTCHA if present
        try:
            print('→ Checking for CAPTCHA...')
            solve_res = driver.execute('executeCdpCommand', {
                'cmd': 'Captcha.waitForSolve',
                'params': {'detectTimeout': 10000},
            })
            print('→ CAPTCHA solve status:', solve_res['value']['status'])
        except Exception as e:
            print('⚠️ CAPTCHA solve skipped or failed:', e)

        print('→ Page loaded. Extracting HTML...')
        html = driver.page_source
        return html

# def scrape_website(website):
#     print('Connecting to Browser API...')
#     sbr_connection = ChromiumRemoteConnection(SBR_WEBDRIVER, 'goog', 'chrome')
#     with Remote(sbr_connection, options=ChromeOptions()) as driver:
#         print('Connected! Navigating to https://example.com...')
#         driver.get(website)
#         # CAPTCHA handling: If you're expecting a CAPTCHA on the target page, use the following code snippet to check the status of Browser API's automatic CAPTCHA solver
#         print('Waiting captcha to solve...')
#         # solve_res = driver.execute('executeCdpCommand', {
#         #     'cmd': 'Captcha.waitForSolve',
#         #     'params': {'detectTimeout': 10000},
#         # })
#         # print('Captcha solve status:', solve_res['value']['status'])
#         print('Navigated! Scraping page content...')
#         html = driver.page_source
#         print(html)
#         return html
    #till now unnessessary html tage and all are being scraped; we will not pass that to our llms in order to save the tokens so
#only text extract 
#from that  html content only the boddy part is extracted
def  extract_body_content(html_content):
    soup=BeautifulSoup(html_content, "html.parser")
    body_content= soup.body
    if body_content:
        return str(body_content)
    return ""

#now using beautiful soup hum bekar ke scripts and styles ko hataenge basicaaly saaf kar rah hai
#removes the script and style tags from the main body content
def clean_body_content(body_content):
    soup = BeautifulSoup(body_content, "html.parser")

    for script_or_style in soup(["script", "style"]):
        script_or_style.extract()
    cleaned_content=soup.get_text(separator="\n")
    cleaned_content = "\n".join(
        line.strip() for line in cleaned_content.splitlines() if line.strip()
    )

    return cleaned_content
# Initially, the value of i is set to 0. Then, the first 6000 characters are extracted (from index 0 to 6000). After that, i is updated to 6000, and the next 6000 characters are extracted. This process continues until we reach the end of the DOM content.
def split_dom_content(dom_content, max_length=6000):
    return[
        dom_content[i :i + max_length] for i in range(0,len(dom_content),max_length)
    ]
