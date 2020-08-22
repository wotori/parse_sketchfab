from os import path
from settings import ROOT_DIR

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

from assist_functions import get_urls, save_urls

webdriver_path = path.join(ROOT_DIR, "chromedriver")
driver = webdriver.Chrome(webdriver_path)
driver.get('https://sketchfab.com/3d-models/categories/characters-creatures?date=week&sort_by=-likeCount')

button_next = driver.find_elements_by_css_selector(".load-next")[0]
# load page
for i in range(1):
    try:
        ActionChains(driver).move_to_element(button_next).perform()
        button_next.click()
        print('next clicked', i, "of 400")
        sleep(5)
    except:
        data = driver.find_elements_by_class_name("card-model, card")
        get_urls(driver)
        save_urls()
        sleep(5)
        continue

data = driver.find_elements_by_class_name("card-model, card")
url_list = get_urls(data)
save_urls(url_list)

print(len(url_list), 'urls saved', sep=":")
