# -*- coding: utf-8 -*-
"""
Created on Sun Oct 21 19:30:01 2018

@author: Mihai
"""

from urllib.request import urlopen
from urllib.parse import urlparse
from bs4 import BeautifulSoup

url = "https://www.leafly.com/indica/bubba-og"
path = urlparse(url)[2].split("/")[1]

html = urlopen(url)
soup = BeautifulSoup(html, "html.parser")

for flavour in soup.find_all("div",{"class":"l-square-content"}):
    print(flavour.find("span").text[3:])

review_count = soup.find("span", {"itemprop":"reviewCount"}).text
rating_value = soup.find("span", {"class":"rating-number"}).text