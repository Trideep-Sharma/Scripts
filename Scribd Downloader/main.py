import PyPDF2
from scrape_lib import get_proxies , get_all_pages , download_image
import os
import sys
from random import randint
import urllib.request
import re
from fpdf import FPDF

if __name__ == '__main__':
    pdf = FPDF()
    id = '335563290/Digital-Signal-Processing-by-S-Salivahanan-pdf'
    #proxies = list()
    #while len(proxies) < 5:
    #    proxies = get_proxies()
    #proxy = proxies[randint(0, len(proxies) - 1)]
    pages = get_all_pages(id,'35.189.86.114:3128')
    for i in range(len(pages)):
        page = pages[i]
        page[2:-2]
        page = re.findall('(.*)(pages)(.*)',page)
        page = page[0][0][1::]+'images'+page[0][2]
        x=download_image(page,i)
        pdf.add_page()
        print(i)
        pdf.image(str(i)+'.jpg', 0 , 0 , 210 , 295)
    pdf.output('salivahan.pdf','F')
