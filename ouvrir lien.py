import csv
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from time import sleep

# Liste pour stocker les liens
liens = []

# Ouvrir le fichier CSV en mode lecture
with open('offres_stages.csv', 'r', newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    # Accéder directement à la 4e ligne
    for _ in range(3):  # On parcourt jusqu'à la 3ème ligne pour se positionner sur la 4ème
        next(reader)

    liens = next(reader)[1:]


# Initialisez le navigateur
driver = webdriver.Edge()


# Parcourir la liste des liens et remplir le formulaire pour chaque offre
for lien in liens:
    print(f"Ouverture de l'URL : {lien}")
    driver.get(lien)
    sleep(2)  # Laisser le temps à la page de charger

    try:
        refu_button = driver.find_element(By.CSS_SELECTOR, "button.eu-cookie-withdraw-button ")
        refu_button.click()
        sleep(1)
    except:
        print("arrive pas a appuyer sur le refu cookie")
        break
    # Appeler la fonction pour remplir le formulaire
    try:
        post_button = driver.find_element(By.CSS_SELECTOR, "a.c-btn.c-btn--primary-inverted.c-btn--full-width")
        post_button.click()
        sleep(1)
    except:
        print("arrive pas a postuler")
        break

    try:
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="didomi-notice-disagree-button"] and text()="Refuser"]'))).click()

    except:
        print("arrive pas a appuyer sur le refu")
        break
    sleep(30)
    # Trouvez l'élément <select> sur la page
    select_element = driver.find_element(By.CLASS_NAME,
        "ctl00_ctl00_corpsRoot_corps_formulairePJ_rptAttachedFile_ctl01_MultiPJAndSelection_SelectionPJ_DDLPj")

    # Créez une instance Select à partir de l'élément
    select = Select(select_element)

    # Sélectionnez l'option par son texte visible
    select.select_by_visible_text("CV 5A.PDF")


    # Trouvez l'élément <select> sur la page
    select_element = driver.find_element(By.ID,
        "ctl00_ctl00_corpsRoot_corps_formulairePJ_rptAttachedFile_ctl01_MultiPJAndSelection_SelectionPJ_DDLPj")

    # Créez une instance Select à partir de l'élément
    select = Select(select_element)

    # Sélectionnez l'option par son texte visible
    select.select_by_visible_text("LM_S_5A.PDF")

    # Trouvez le bouton sur la page à l'aide de son id
    try:
        sub_button = driver.find_element(By.CSS_SELECTOR, "ctl00_ctl00_corpsRoot_corps_bt_Preciser")
        sub_button.click()
        sleep(3)
    except:
        print("pas enregistrer")
        break
    sleep(2)
    # Fermer l'onglet actuel et passer au lien suivant
    driver.close()

# Fermer le navigateur
driver.quit()