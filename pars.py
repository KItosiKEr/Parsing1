import requests
from bs4 import BeautifulSoup

# url = 'https://www.nbkr.kg/index1.jsp?item=1562&lang=RUS'

# response = requests.get(url)
# soup = BeautifulSoup(response.text, 'lxml')
# r = soup.find_all('td', class_='stat-left')
# rt = soup.find_all('td', class_='stat-right')

# for rtt in rt:
#     for rr in r:   
# print(f'{rr.text} -  {rtt.text}')


class Parsing:
    def pars(self):
        url = 'https://www.nbkr.kg/index1.jsp?item=1562&lang=RUS&valuta_id=15&beg_day=05&beg_month=08&beg_year=2021&end_day=05&end_month=08&end_year=2022'
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
        r = soup.find('td', class_='stat-center')
        rt = soup.find('td', class_='stat-right')
        print('Доллар к Сому')
        print(r.text, rt.text)
a = Parsing()
a.pars()
class parsing:
    def pars(self):
        url = 'https://www.nbkr.kg/index1.jsp?item=1562&lang=RUS&valuta_id=20&beg_day=05&beg_month=08&beg_year=2021&end_day=05&end_month=08&end_year=2022'
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
        r = soup.find('td', class_='stat-center')
        rt = soup.find('td', class_='stat-right')
        print('Евро к Сому')
        print(r.text, rt.text)
a = parsing()
a.pars()
class parsing_r:
    def pars(self):
        url = 'https://www.nbkr.kg/index1.jsp?item=1562&lang=RUS&valuta_id=44&beg_day=05&beg_month=08&beg_year=2021&end_day=05&end_month=08&end_year=2022'
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
        r = soup.find('td', class_='stat-center')
        rt = soup.find('td', class_='stat-right')
        print('Рубль к Сому')
        print(r.text, rt.text)
a = parsing_r()
a.pars()
