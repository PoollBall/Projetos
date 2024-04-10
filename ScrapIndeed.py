# install bs4
# install lxml
import os
import csv
import requests
from bs4 import BeautifulSoup
import time

# Definir o cabeçalho HTTP com um User-Agent genérico
headers = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Mobile Safari/537.36"
}

# Solicitar informações do usuário
skill = input('Enter your Skill: ').strip()
place = input('Enter the location: ').strip()
no_of_pages = int(input('Enter the #pages to scrape: '))

# Criar diretório principal
main_dir = os.getcwd() + '\\'
if not os.path.exists(main_dir):
    os.mkdir(main_dir)
    print('Base Directory Created Successfully.')

# Nome do arquivo CSV
file_name = skill.title() + '_' + place.title() + '_Jobs.csv'
file_path = main_dir + file_name

# Escrita no arquivo CSV
with open(file_path, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['JOB_NAME', 'COMPANY', 'LOCATION', 'POSTED', 'APPLY_LINK'])

    print(f'\nScraping in progress...\n')
    for page in range(no_of_pages):
        # Modificar a URL para apontar para a versão brasileira do Indeed
        url = f'https://www.indeed.com.br/jobs?q={skill}&l={place}&start={page * 10}'
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()  # Verificar se a requisição foi bem-sucedida
            soup = BeautifulSoup(response.text, 'html.parser')
            base_url = 'https://br.indeed.com/viewjob?jk='
            jobs = soup.find_all('a', class_='tapItem')

            for job in jobs:
                job_id = job['id'].split('_')[-1]
                job_title = job.find('span', title=True).text.strip()
                company = job.find('span', class_='companyName').text.strip()
                location = job.find('div', class_='companyLocation').text.strip()
                posted = job.find('span', class_='date').text.strip()
                job_link = base_url + job_id

                writer.writerow([job_title, company, location.title(), posted, job_link])
        except requests.RequestException as e:
            print(f"Error scraping page {page + 1}: {e}")

        # Adicionar um intervalo entre as requisições (2 segundos)
        time.sleep(2)

print(f'Jobs data written to <{file_name}> successfully.')

