# get urls
def get_urls(data):
    url_list = []
    for index, item in enumerate(data):
        url = item[index].find_elements_by_tag_name('meta')[5].get_attribute("content")
        url_list.append(url)
    return url_list

def save_urls(url_list):
    with open('url_list.txt', 'w') as file:
        for item in url_list:
            file.writelines(item + '\n')