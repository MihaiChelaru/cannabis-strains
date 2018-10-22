# -*- coding: utf-8 -*-
"""
Created on Sun Oct 21 20:38:10 2018

@author: Mihai
"""

from urllib.request import urlopen
from urllib.parse import urlparse
from bs4 import BeautifulSoup
from urllib.error import HTTPError
import pandas as pd
from datetime import date, datetime
import gevent
from gevent.pool import Pool
from gevent import monkey

monkey.patch_all()

def rip_strains(url):
    try:
        html = urlopen(url)
        soup = BeautifulSoup(html, "html.parser")
        print(str(datetime.now()).split('.')[0], "Now scraping:", url)

        # Get species (indica, sativa, hybrid) by parsing url
        name = soup.find("meta",{"name":"sailthru.title"}).attrs['content']
        species = urlparse(url)[2].split("/")[1]

        i = 2
        # Strain name, 3 flavours, 30 columns of attribute: value
        strain_info = [name, species, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "",
                 "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]

        for flavour in soup.find_all("div",{"class":"l-square-content"}):
            strain_info[i] = flavour.find("span").text[3:]
            i += 1
        # Set i = 4 in case less than 3 flavours
        i = 5
        for bar in soup.find_all("div",{"class":"m-histogram-item-wrapper"}):
            strain_info[i] = bar.find("div").string
            i += 1
            amount = bar.find("div",{"class":"m-attr-bar"}).attrs['style']
            strain_info[i] = amount[6:(len(amount)-1)]
            i += 1
        results.append(pd.DataFrame([strain_info], columns=cols))
    except HTTPError as e:
        print("",end="")
    except AttributeError as f:
        print("Warning: "+ url +" not found",end="")


links = pd.read_csv("Links/leafly_unique_links.csv", delimiter=',', engine='c',
                    header=None, low_memory=False, na_filter=False)

results = []

cols = ['strain_name', 'species', 'Pain', 'Euphoric', 'Fatigue', 'Paranoid',
        'Focused', 'Spasticity', 'Nausea', 'Tingly', 'Headache', 'Dry Mouth', 'Aroused', 'Happy', 'Muscle Spasms',
        'Uplifted', 'Anxious', 'Energetic', 'Headaches', 'Depression', 'Giggly', 'Talkative', 'Dizzy', 'Insomnia',
        'Inflammation', 'Stress', 'Relaxed', 'Seizures', 'Cramps', 'Sleepy', 'Hungry', 'Lack of Appetite', 'Dry Eyes',
        'Creative', 'Eye Pressure', 'Orange', 'Violet', 'Mint', 'Peach', 'Chestnut', 'Rose', 'Coffee', 'Citrus',
        'Lime', 'Plum', 'Sage', 'Pine', 'Pungent', 'Pear', 'Tar', 'Tree Fruit', 'Berry', 'Vanilla', 'Pepper',
        'Chemical', 'Tea', 'Ammonia', 'Apple', 'Skunk', 'Pineapple', 'Grapefruit', 'Honey', 'Earthy', 'Cheese',
        'Blue Cheese', 'Tropical', 'Grape', 'Lemon', 'Flowery', 'Strawberry', 'Butter', 'Tobacco', 'Spicy/Herbal',
        'Woody', 'Blueberry', 'Sweet', 'Lavender', 'Nutty', 'Apricot', 'Diesel', 'Menthol', 'Mango']

pool = Pool(500)

pool.map(rip_strains, links[0])

df = pd.concat(results, ignore_index=True)

df.to_csv("Results/StrainScrape_full_"+date.today().isoformat()+".csv", index=False)

print("Finished running.")