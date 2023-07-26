import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime   

urls = [
    "https://khadmoneyacademy.com/course-category/development/",
    "https://khadmoneyacademy.com/course-category/design/"
]


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}


formations_info = []
today_date = datetime.today().strftime('%Y-%m-%d')

# Enregistrer les informations dans un fichier CSV
with open('KHadmoney.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['Catégorie','URL', 'Titre', 'Prix', 'Date']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader() 

    for index, url in enumerate(urls, 1):   
        response = requests.get(url, headers=headers)

        if response.status_code == 200: 
            soup = BeautifulSoup(response.text, 'html.parser')
            elements = soup.find_all('div', class_='tutor-card tutor-course-card')
            formations_info = []
            for element in elements:
                title_element = element.find('h3', class_='tutor-course-name')
                title = title_element.text.strip()
                ####################################################################################
                price_element = element.find('span', class_='woocommerce-Price-amount')
                price = price_element.text.strip()
                ######################################################################################
                formations_info.append({  'URL':url ,'Titre': title, 'Prix': price, 'Date': today_date})

    
            writer.writerow({'Catégorie': f'Catégorie {index}','URL': '', 'Titre': '', 'Prix': '', 'Date': ''})

            for formation in formations_info:
                formation_with_spaces = {key: f" {value.strip()} " for key, value in formation.items()}
                writer.writerow(formation_with_spaces)

            print(f"Les informations de la catégorie {index} ont été enregistrées dans KHadmoney.csv")
