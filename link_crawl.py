from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://www.leafly.com/explore')

strains = driver.find_elements_by_class_name('ga_Explore_Strain_Tile')
for strain in strains:
    print(strain.get_attribute('href'))