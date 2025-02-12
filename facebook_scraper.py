from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.chrome.options import Options

def extraire_urls_facebook():
    # Configuration pour utiliser Chrome déjà ouvert
    chrome_options = Options()
    chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
    driver = webdriver.Chrome(options=chrome_options)
    
    # Aller à l'URL de la première photo
    driver.get("https://www.facebook.com/photo.php?fbid=948871760758622&set=pb.100069074211251.-2207520000&type=3")
    
    urls = []
    
    # Boucle pour parcourir les photos
    while True:
        try:
            time.sleep(2)
            
            current_url = driver.current_url
            if current_url not in urls:
                urls.append(current_url)
            
            next_button = driver.find_element(By.CSS_SELECTOR, "div[aria-label='Photo suivante']")
            next_button.click()
            
            time.sleep(1)
            
        except Exception as e:
            print("Fin de l'album ou erreur rencontrée")
            break

    # Enregistrer les URLs dans un fichier
    with open('facebook_urls.txt', 'w') as f:
        for url in urls:
            f.write(url + '\n')

    print(f"{len(urls)} URLs ont été enregistrées dans facebook_urls.txt")

if __name__ == "__main__":
    extraire_urls_facebook()
