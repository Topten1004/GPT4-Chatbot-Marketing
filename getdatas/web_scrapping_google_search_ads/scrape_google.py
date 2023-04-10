import requests
from bs4 import BeautifulSoup as bsoup
import pandas as pd
from datetime import datetime

def scrap_g_search_ads_section():

    text = 'samsung mobile'
    text = text.replace(' ', '+')
    url = 'https://google.com/search?q=' + text
    USER_AGENT = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}
    

    data = requests.get(url, headers=USER_AGENT)
    

    data_html = bsoup(data.content, 'lxml')
    
    ads_info = {'serial_no' : [],
           'model_name': [],
           'url' : [],
           'price' : [],
           'from' : []}
    serial_no = 0
    result = data_html.find('div', attrs={'class':'pla-unit-container'})
    for i in range(len(data_html.find_all('div', attrs={'class':'pla-unit-container'}))):
        try:
            serial_no += 1
            ads_info['serial_no'].append(serial_no)
            ads_info['model_name'].append(result.find('span').find_next('span').get_text())
            ads_info['url'].append(result.find('a', class_="plantl").get('href'))
            ads_info['price'].append(result.find('div', class_="e10twf T4OwTb").get_text())
            ads_info['from'].append(result.find('div', class_="LbUacb").get_text())
            result = result.find_next('div', attrs={'class':'pla-unit-container'})
        except:
            continue
     
    for i in ads_info['model_name']:
        if i == 'View all':
            ads_info['model_name'].pop()
            ads_info['serial_no'].pop()

    df = pd.DataFrame()
    df['serial_no'] = ads_info['serial_no']
    df['model_name'] = ads_info['model_name']
    df['url'] = ads_info['url']
    df['price'] = ads_info['price']
    df['from'] = ads_info['from']
    
    
    df.to_csv('samsung_mobile_ads_{}.csv'.format(datetime.now().strftime("%Y_%m_%d_%H_%M_%S")),index= False)
    return
