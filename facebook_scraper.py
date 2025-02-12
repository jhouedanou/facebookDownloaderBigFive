from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def extraire_urls_facebook():
    # Configuration du navigateur
    driver = webdriver.Chrome()
    driver.get("https://www.facebook.com/dinor.ci/photos")
    
    # Attendre la connexion manuelle
    print("Veuillez vous connecter à Facebook et appuyez sur Entrée...")
    input()
    
    # Faire défiler la page pour charger toutes les images
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

    # Récupérer tous les liens d'images
    images = driver.find_elements(By.CSS_SELECTOR, "a[href*='photo']")
    urls = []
    
    for img in images:
        url = img.get_attribute('href')
        if url and 'photo' in url:
            urls.append(url)

    # Enregistrer les URLs dans un fichier
    with open('facebook_urls.txt', 'w') as f:
        for url in urls:
            f.write(url + '\n')

    driver.quit()
    print(f"{len(urls)} URLs ont été enregistrées dans facebook_urls.txt")

if __name__ == "__main__":
    extraire_urls_facebook()
