import pandas as pd
import time

from selenium import webdriver

scroll_delay = 3
driver = webdriver.Chrome()

driver.get('https://www.leafly.com/explore')

# Click through the terms of use popup
tou_accept = driver.find_element_by_id('tou-continue')
tou_accept.click()

# Create set since we want unique links only
links = set()
strains = driver.find_elements_by_class_name("ga_Explore_Strain_Tile")
for strain in strains:
    link = strain.get_attribute("href")
    links.add(link)

last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # Find and click on load more button
    load_more = driver.find_element_by_css_selector("#main > div > section > div.explore-tiles > div > div > "
                                                    "div.l-grid.strain-tile--explore.trademarked > "
                                                    "div.copy--centered.padding-listItem > button")
    load_more.click()

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(scroll_delay)
    new_height = driver.execute_script("return document.body.scrollHeight")

    strains = driver.find_elements_by_class_name("ng-scope")
    for strain in strains:
        link = strain.get_attribute("href")
        links.add(link)

    if new_height == last_height:
        break
    last_height = new_height

df = pd.DataFrame({'links' : list(links)})
df.to_csv('Links/leafly_crawled_full.csv', header=False, index=False)

driver.quit()