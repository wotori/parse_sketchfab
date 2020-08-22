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
for i in range(1000):
    try:
        ActionChains(driver).move_to_element(button_next).perform()
        button_next.click()
        print(f"Iter #{i} of 1000")
        sleep(3)
    except:
        break

# get urls
data = driver.find_elements_by_class_name("card-model, card")
url_list = []
for item in data:
    url = item.find_elements_by_tag_name('meta')[5].get_attribute("content")
    url_list.append(url)

# save result
with open('character_and_creatures.txt.txt', 'w') as file:
    for item in url_list:
        file.writelines(item + '\n')

print('Process finished')
