from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import csv
from time import sleep

# Initialisez le navigateur
driver = webdriver.Edge()

# Allez sur la page d'accueil d'Indeed
driver.get('https://www.safran-group.com/fr/offres?countries%5B0%5D=1002-france&contracts%5B0%5D=42-stage&search=cfd')

# Attendre un peu pour que les résultats se chargent
sleep(5)

# Récupérez la liste des offres
offers = driver.find_elements(By.CLASS_NAME, 'result')

# Extrayez et affichez les informations pertinentes
# Pour chaque offre d'emploi :


titles = ["Titre"]
companies = ["Entreprise"]
locations = ["Lieu"]
links = ["Lien"]

while True:
    # Récupérez la liste des offres
    offers = driver.find_elements(By.CLASS_NAME, 'c-offer-item')

    # Pour chaque offre d'emploi :
    for offer in offers:
        try:
            title = offer.find_element(By.CSS_SELECTOR, 'a.c-offer-item__title.js-block-link--href').text
        except:
            title = "N/A"
        titles.append(title)

        try:
            company = offer.find_element(By.CSS_SELECTOR, 'span.c-offer-item__infos__item').text
        except:
            company = "N/A"
        companies.append(company)

        try:
            location = offer.find_elements(By.CSS_SELECTOR, 'span.c-offer-item__infos__item')[1].text
        except:
            location = "N/A"
        locations.append(location)

        try:
            link = offer.find_element(By.CSS_SELECTOR, 'a.c-offer-item__title.js-block-link--href').get_attribute(
                'href')
        except:
            link = "N/A"
        links.append(link)


    try:
        next_button = driver.find_element(By.CSS_SELECTOR, "a.pagination__nav-btn.pagination__nav-btn--next")
        next_button.click()
        sleep(5)
    except:
        print("Pagination terminée ou une erreur s'est produite.")
        break

# Écrire les données dans le fichier CSV
filename = "offres_stages.csv"
with open(filename, 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerows([titles, companies, locations, links])

# Fermez le navigateur
driver.quit()
