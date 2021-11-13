
from sys import version
from bs4 import BeautifulSoup
import requests
from requests_html import HTMLSession
import pandas as pd
import json
from bs4 import SoupStrainer
url ='https://condos.ca/property-management/firstservice-residential'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'}
r = requests.get(url,headers=headers)
soup  = BeautifulSoup(r.text,'html.parser')
# csv = pd.DataFrame(main_list)
# csv.to_csv('data.csv',index=False)
main_list = []
links = []
main_urls = soup.find_all('a',{'class':'styles___BuildingPreview-sc-xn4y80-0 dsAqai'})
for main_url in main_urls:
    links.append('https://condos.ca/'+main_url['href'])

# print(links[0])
c = 0
for x in links:
    if c == 20:
        break
    c= c+1
    print('product',c)
    r = requests.get(x,headers=headers)
    soup  = BeautifulSoup(r.text,'html.parser')
    try:
        name = soup.find('h2',{'class':'styles___Title-sc-rxqpm4-8 gxpaEL'}).text
        # print(name)/
        prices = soup.find_all('div',class_="styles___ValueDiv-sc-r1n1mk-4 exHguF")[0].text
        area = soup.find_all('div',class_="styles___BlurCont-sc-qq1hs5-0 styles___InfoRowValue-sc-r1n1mk-3 iwveiX")[1].text
        size = soup.find_all('div',class_="styles___ValueDiv-sc-r1n1mk-4 exHguF")[1].text
        year_bluding  = soup.find_all('div',class_="styles___ValueDiv-sc-r1n1mk-4 exHguF")[2].text
        img = soup.find('img',class_="noLazy")['src']
        description = soup.find('div',class_='styles___BodyHtml-sc-1gxkqh1-2 dBZHLr').text
        
    except:
        pass
    main_dir = {
        'property_name':name,
        'property_price':prices,
        'property_area':area,
        'property_size':size,
        'property_img':img,
        'property_des':description,
        'property_year_bulding':year_bluding,
    }
    main_list.append(main_dir)
    


csv = pd.DataFrame(main_list)
csv.to_csv('property.csv',index=False)
    
