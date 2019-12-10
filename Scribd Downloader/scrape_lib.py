import sys
import requests
import pandas as pd
from time import sleep
from random import randint
from bs4 import BeautifulSoup
import re
import urllib.request
from user_agent import generate_user_agent

def get_proxies():
    """This function gets all proxies from the provided webpage"""

    proxy_list = list()
    page = requests.get('https://www.us-proxy.org/')
    soup = BeautifulSoup(page.text, 'html.parser')
    proxy_table = soup.find(id='proxylisttable').tbody
    for row in proxy_table.find_all('tr'):
        proxy = row.find_all('td')
        if proxy[4] != 'transparent' and proxy[6] != 'no':
            proxy_list.append(proxy[0].text + ":" + proxy[1].text)
    return proxy_list


#Function to get reviews
def get_all_pages(id, proxy):
    count = 0
    image_list = list()  # Create an empty list
    base_url = "http://www.scribd.com/document/" + id
    header = {'User-Agent': generate_user_agent(device_type="desktop", os=('linux'))}
    html_page = requests.get(base_url, headers=header, proxies = {'https':proxy})
    if html_page.status_code == 404:  # Return -1 if page not found
        return -1

    image_list = re.findall('pageParams.contentUrl = (.*)jsonp',html_page.text)
    return image_list

def download_image(url, i):
    r = requests.get(url+'jpg')
    with open(str(i)+'.jpg', 'wb') as f:
        f.write(r.content)
    return r.content

if __name__ == '__main__':
    pass
