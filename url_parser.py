from os import path
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from settings import ROOT_DIR
import uuid

driver = webdriver.Chrome(path.join(ROOT_DIR, "chromedriver"))
url_list_path = path.join(ROOT_DIR, "character_and_creatures.txt")
with open(url_list_path, "r") as url_list:
    data = url_list.readlines()

for link in data[22:]:
    driver.get(link)
    author_name = driver.find_elements_by_class_name("username-wrapper")[0].text
    description = driver.find_elements_by_class_name("model-name__label")[0].text
    character_info = driver.find_elements_by_class_name("description-content, markdown-rendered-content")
    character_text_lines = character_info[0].find_elements_by_tag_name("p")

    user_id_generated = str(uuid.uuid4())[0:5]
    with open(f'captions/{author_name}_{user_id_generated}.txt', 'w') as caption:
        try:
            caption.writelines(link + '\n')
            caption.writelines(author_name + '\n')
            for text_row in character_text_lines:
                caption.writelines(text_row.text + '\n')
        except:
            pass

    print('on link')