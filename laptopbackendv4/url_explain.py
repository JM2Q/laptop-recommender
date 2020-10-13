# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 11:42:32 2020

@author: 77433
"""
import re
from bs4 import BeautifulSoup
import requests
import json
from bs4 import SoupStrainer
# request_headers={
#  'User - Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36', 
#  'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
#  ,'referer': 'https://www.iss.nus.edu.sg/',
#  'upgrade-insecure-requests': '1',
#  'cookie': '_ga=GA1.3.1788786153.1573902624; visid_incap_1988262=iz9zv9QVSQqWlivfVz4sayIxy14AAAAAQUIPAAAAAACvmgAl4gFEp+EEZ+DGwz7H; visid_incap_2246921=Y3bjKLAOTZOdT2LnQFXlbTkxy14AAAAAQUIPAAAAAACXwMHwr5B8IxCziasMP3KH; visid_incap_1750112=fdHRlakxSjeD5AMQe1A60nd91F4AAAAAQUIPAAAAAABiTfHVOJPJ+qUMVKenfsS3; visid_incap_1988269=2htganRCS9yQyCBcuxxj2Way1F4AAAAAQUIPAAAAAABIg55D5UCNCHtDqGKxSU4Y; visid_incap_2324509=RtTiJZjNTuaL3OkE6hV4Y7vM8l4AAAAAQUIPAAAAAABahbY24x5HYlZjaAuix3Ic; visid_incap_2023966=dW6giSURT72DGC0LhRp0whduBV8AAAAAQUIPAAAAAAB6RWUI/yGox/uVe7supjx4; visid_incap_787926=/x5xCTnkR1GLTp1SuB2GbqH6IF8AAAAAQUIPAAAAAADxhkXCM8UyVYQA7EWmzdg1; _gcl_au=1.1.2144378240.1595996858; permutive-id=abec8bb3-48ba-43dd-ae09-cf767a847d37; Hm_lvt_eaa57ca47dacb4ad4f5a257001a3457c=1599573970; ASP.NET_SessionId=op0kichc314wotlgusqwj2as; _gid=GA1.3.2041822699.1600747688; _subscribe=1; Hm_lvt_eaa57ca47dacb4ad4f5a257001a3457c=1599573970; incap_ses_164_787926=mpCDY2SyETWkSQh3WaVGAnexaV8AAAAAepjSmUz3CSGkYyrK1PI62w==; permutive-session=%7B%22session_id%22%3A%22efbe22e0-6ea1-45eb-a385-dfdc47bd009b%22%2C%22last_updated%22%3A%222020-09-22T08%3A26%3A32.950Z%22%7D; Hm_lpvt_eaa57ca47dacb4ad4f5a257001a3457c=1600763198'
#  ,'accept-encoding': 'gzip, deflate, br',
#  'accept-language': 'en,zh-CN;q=0.9,zh;q=0.8',
#  'sec-fetch-dest': 'document',
# 'sec-fetch-mode': 'navigate',
# 'sec-fetch-site': 'same-origin',
# 'sec-fetch-user': '?1',
# 'upgrade-insecure-requests': '1'
#  }

request_headers={'User - Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'
    }

url = 'https://www.ea.com/games/battlefield/battlefield-5/buy/pc-system-requirements'


# html_file=open("htmldoc.txt",'r',encoding ='utf-8')
# html_doc=html_file.read()
# html_file.close()
# testsoup=BeautifulSoup(html_doc,'html.parser')
# soup1 = testsoup.find('p',class_ = 'title')
# for c in soup1.children:
#     print (c)


# html = requests.get(url,request_headers)
# html_doc = html.text
# soup = BeautifulSoup(html_doc,'html.parser')
# only_a_tags = SoupStrainer("ul")
# soup_ul = soup.find_all(only_a_tags)
# recommendation = BeautifulSoup(str(soup_ul[2]),'html.parser')
# for i in recommendation.text.splitlines():
#     print (i)
#     print(' ')
    
dic = {'ram':0,'gpu_memory':6,'price':6000,'cpu_rank':5}
def detect(text):
    if 'RAM' in text:
        pattern  = re.compile(r'\d+')
        s = re.search(pattern,text)
        t = s.group(0)
        t = int (t)
        dic['ram']=t
    if 'NVIDIA' in text:
        pattern  = re.compile(r'\d+GB')
        s = re.search(pattern,text)
        t = s.group(0)
        t = int (t[:-2])
        dic['gpu_memory']=t
    if "Intel" in text :
        pattern  = re.compile(r'i\d')
        s = re.search(pattern,text)
        t = s.group(0)
        t = int (t[1:])
        dic['cpu_rank']=t
        
def explain(url):
    html = requests.get(url,request_headers)
    html_doc = html.text
    soup = BeautifulSoup(html_doc,'html.parser')
    only_a_tags = SoupStrainer("ul")
    soup_ul = soup.find_all(only_a_tags)
    recommendation = BeautifulSoup(str(soup_ul[2]),'html.parser')
    for i in recommendation.text.splitlines():
        detect(i)
   
    return 0


def main_op(url):
    explain(url)
    return dic

if __name__ == '__main__':
    print(main_op(url))
