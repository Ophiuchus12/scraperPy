import selenium.webdriver as webdriver  
# Importe le module WebDriver de Selenium, utilisé pour automatiser le contrôle des navigateurs.

from selenium.webdriver.chrome.service import Service  
# Importe la classe `Service`, qui permet de gérer l'exécution de ChromeDriver en arrière-plan.

from bs4 import BeautifulSoup

import time


def scrape_website(website):
    print("lauching the browser")

    chrome_driver_path = "./chromedriver"
    options = webdriver.ChromeOptions()
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")  
    # Définit un User-Agent personnalisé pour faire croire au site que la requête vient d'un vrai navigateur Chrome sur Windows 10.  
    # Utile pour éviter que le site détecte Selenium et bloque l'accès.  

    options.add_argument("--headless=new")  
    # Active le mode "headless" (sans interface graphique), ce qui permet d'exécuter Chrome en arrière-plan.  
    # Améliore la performance et permet d'exécuter le script sur un serveur sans interface graphique.  

    options.add_argument("--disable-blink-features=AutomationControlled")  
    # Désactive la fonctionnalité "AutomationControlled" qui signale que le navigateur est contrôlé par Selenium.  
    # Permet de masquer l'utilisation de Selenium et de réduire les chances d'être détecté comme un bot.  

    driver = webdriver.Chrome(service=Service(chrome_driver_path), options=options)

    try:
        driver.get(website)
        print("page loaded...")
        html = driver.page_source
        time.sleep(10)

        return html
    finally:
        driver.quit()

def extract_body_content(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    body_content = soup.find("body")
    if body_content : 
        return str(body_content)
    return ""

def cleaned_body_content(body_content):
    soup = BeautifulSoup(body_content, "html.parser")

    for script_style in soup(["script", "style"]):
        script_style.extract()

    cleaned_content = soup.get_text(separator="\n")
    cleaned_content = "\n".join(line.strip() for line in cleaned_content.splitlines() if line.strip())

    return cleaned_content

def split_dom_content(dom_content, max_length= 6000):
    return [
        dom_content[i: i + max_length] for i in range (0, len(dom_content), max_length)
    ]