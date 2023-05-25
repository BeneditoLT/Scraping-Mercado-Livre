import requests 
from bs4 import BeautifulSoup
from requests.api import get

def scrap():
        for item in range(0,int(j)):
                
                vendas = ''
                vendas = ""
                url2 = link[item].get('href')
                site = requests.get(url2, headers=headers)
                soup = BeautifulSoup(site.content, 'html.parser') 
                titulo = soup.find('h1', class_='ui-pdp-title').get_text()
                valor = soup.find('span', class_='andes-money-amount__fraction').get_text()  
                vendas = soup.find('span', class_='ui-pdp-subtitle').get_text()
                nun_vendas = vendas[7:-9]
                url2 = str(url2)
                linha = titulo+','+ valor+','+nun_vendas
               
                print(linha)
                f.write(linha)
                f.write('\n')
                

url = 'https://lista.mercadolivre.com.br/_CustId_84594669 '

headers = {
        'User-Agent' : "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"}

site = requests.get(url, headers=headers)
soup = BeautifulSoup(site.content, 'html.parser')  

link = soup.find_all( 'a',class_='ui-search-item__group__element shops__items-group-details ui-search-link') 
pagina= soup.find('li', class_='andes-pagination__page-count')  
pagina = pagina.get_text()
pagina = int(pagina[3:])
print(pagina)


item = 0
j = len(link) 
with open ('stm.csv', 'a', newline ='', encoding= 'UTF-8') as f:
         
       scrap()
       while pagina > 1:
                urlp = soup.find('a', class_='andes-pagination__link shops__pagination-link ui-search-link')
                urlp = urlp.get('href')
                site = requests.get(urlp, headers=headers)
                soup = BeautifulSoup(site.content, 'html.parser')  
                link = soup.find_all('a', class_='ui-search-item__group__element shops__items-group-details ui-search-link')
                j = len(link) 
                scrap()
                print("teste")
                pagina = pagina -1 
