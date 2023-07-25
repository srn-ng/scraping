import requests
from bs4 import BeautifulSoup
import csv
import json
from datetime import datetime   
url = "https://gomycode.com/dz/web-development/"
response = requests.get(url)

if response.status_code == 200: 
    soup = BeautifulSoup(response.text, 'html.parser')
    elements = soup.find_all('div', class_='course-loop-info')

    formations_info = []

    today_date = datetime.today().strftime('%Y-%m-%d')

    for element in elements:

        title_element = element.find('h2', class_='course-loop-title-collapse-2-rows')
        title = title_element.text.strip()
        ########################################################################################
        price_element = element.find('span', class_='woocommerce-Price-amount amount')
        price = price_element.text.strip()
        #######################################################################################

        formations_info.append({'URL': url, 'Titre': title, 'Prix': price, 'Date': today_date})

    # Enregistrer les informations dans un fichier CSV
    with open('GoMyCode.csv', 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['URL', 'Titre', 'Prix', 'Date']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()  # Écrire les en-têtes (noms des colonnes)

        for formation in formations_info:
            # Ajouter des espaces avant et après chaque virgule dans les valeurs du fichier CSV
            formation_with_spaces = {key: f" {value.strip()} " for key, value in formation.items()}
            writer.writerow(formation_with_spaces)

    print("Les informations ont été enregistrées dans formations.csv")




