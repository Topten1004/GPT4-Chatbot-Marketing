## If running in windows command shell then run this command - chcp 65001

import sys

from lxml import html  
import csv,os,json
import requests
from time import sleep
import re 
from pprint import pprint
from bs4 import BeautifulSoup
from bs4 import BeautifulSoup as Soup, Tag
import requests


def bingAdExtractor(url):
    response = requests.get(url, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.120 Safari/537.36'})
    
    try:
       
        soup = BeautifulSoup(response.content,'lxml')

        print('\n')
        print('Adds on right section: ')
        
        ad_ol_right = soup.find("ol", {"id": "b_context"})
        ad_li_right = ad_ol_right.find("li", {"class": "b_ad"})    
        
        for item_right in ad_li_right.findAll('div', {"class": "sb_add sb_adTA"}):
            ad_h2 = item_right.find("h2")
            ad_sb_desc = item_right.find('p', {"class": "sb_addesc"})
            ad_sb_cite = item_right.find('cite')
            print('\n')
            try:
                print('Header: '+(ad_h2.text))
                print('Desc: '+(ad_sb_desc.text))
                print('Site: '+(ad_sb_cite.text))
            except Exception as e:
                print(e)

        print('\n')        
        print('-----------------------------------')
        print('\n')
        
        print('Adds on main section: ')
                
        ad_ol_main = soup.find("ol", {"id": "b_results"})
        ad_li_main = ad_ol_main.find("li", {"class": "b_ad"})    
        
        
        for item_main in ad_li_main.findAll('div', {"class": "sb_add sb_adTA"}):
            ad_h2 = item_main.find("h2")
            ad_sb_desc = item_main.find('p', {"class": "sb_addesc"})
            ad_sb_cite = item_main.find('cite')
            print('\n')
            try:
                print('Header: '+(ad_h2.text))
                print('Desc: '+(ad_sb_desc.text))
                print('Site: '+(ad_sb_cite.text))
            except Exception as e:
                print(e)                
                
            
    except Exception as e:
            print(e)

if __name__ == "__main__":
    if len(sys.argv) != 2:
       print('Check arguments entered!!!')
       print('Arguments should be entered as --> xxx.py "Iphone 7"')
    else:
        try:
            url = "http://www.bing.com/search?q="+(str(sys.argv[1]).replace(" ","+")).lower()
            #print(()
            print('URL Created : '+url)
            bingAdExtractor(url)     
        except Exception as e:
            print(e)
    