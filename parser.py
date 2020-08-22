from os import path
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from settings import ROOT_DIR

driver = webdriver.Chrome(path.join(ROOT_DIR, "chromedriver"))
driver.get('https://sketchfab.com/3d-models/categories/characters-creatures?date=week&sort_by=-likeCount')

button_next = driver.find_elements_by_css_selector(".load-next")[0]
# load page
for i in range(10):
    ActionChains(driver).move_to_element(button_next).perform()
    button_next.click()
    sleep(10)

# get urls
data = driver.find_elements_by_class_name("card-model, card")
url_list = []
for index, item in enumerate(data):
    url = data[index].find_elements_by_tag_name('meta')[5].get_attribute("content")
    url_list.append(url)

with open('url_list.txt', 'w') as file:
    for item in url_list:
        file.writelines(item + '\n')

print('Connected')
