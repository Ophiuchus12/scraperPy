import selenium.webdriver as webdriver  
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time  
from scrape import extract_body_content

def google_search_results (query):

    print("lauching the browser")

    chrome_driver_path = "./chromedriver"
    options = webdriver.ChromeOptions()
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.6943.53 Safari/537.36")  
    options.add_argument("--headless")
    options.add_argument("--disable-blink-features=AutomationControlled")  
   

    driver = webdriver.Chrome(service=Service(chrome_driver_path), options=options)

    links = []

    try: 
        driver.get("https://www.google.com/search?q="+query)
        print("page loaded...")

        

        html = driver.page_source
        time.sleep(10)


        soup = BeautifulSoup(html, "html.parser")
        body_content = soup.find("body")

        results = body_content.find_all("div", class_="g")
        for result in results:
            link = result.find("a", href=True)  
            #print (link)
            if link :
                links.append(link['href'])
        print (links)
        return links

    finally:
        driver.quit()

    
        


if __name__ == "__main__":
    google_search_results("python")

 