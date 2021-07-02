import requests
from bs4 import BeautifulSoup
import re

def run():
    URL = 'https://covid19.min-saude.pt/pedido-de-agendamento/#error_msg'
    payload = {
        'f_dia': '1',
        'f_mes': '1',
        'f_ano': '2021' 
    }

    response = requests.post(URL, data=payload)

    soup = BeautifulSoup(response.text, features='html.parser')
    text = soup.find('span', attrs={'id': 'error_msg'}).text
    age =  re.findall(r'\d+', text)[0]

    return text, age