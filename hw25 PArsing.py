import requests
from bs4 import BeautifulSoup
url = 'https://itstep.dp.ua/education-adults#c110'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
quotes = soup.find_all('p', class_="adult-educ-block__item-name")
print(quotes)
for quote in quotes:
    print(quote.text)
# ------------------------------------------------------------------------------------------------------------------------
url2 = 'https://itvdn.com/ru'
response2 = requests.get(url2)
soup2 = BeautifulSoup(response.text, 'lxml')
quotes2 = soup2.find_all('p', class_="spec-block__main_title")
print(quotes2)
#----------------------------------------------------------------------------------------------------
url3 = 'https://mate.academy/ru'
response3 = requests.get(url3)
soup3 = BeautifulSoup(response.text, 'lxml')
quotes3 = soup3.find_all('div', class_="sc-de4e2aba-0 sc-d7d524d6-1 geczXg")
print(quotes3)
