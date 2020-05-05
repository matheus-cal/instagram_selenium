from selenium import webdriver
from time import sleep
from keys import username, password


driver = webdriver.Chrome()

def login():
    driver.get('https://www.instagram.com/')
    sleep(1)


    driver.find_element_by_xpath("//input[@name=\"username\"]").send_keys(username)
    driver.find_element_by_xpath("//input[@name=\"password\"]").send_keys(password)
    sleep(1)
    driver.find_element_by_xpath("//button[@type=\"submit\"]").click()
    sleep(3)

    try:
        driver.find_element_by_xpath("//button[contains(text(), 'Agora não')]").click()
        sleep(3)
    except:
        sleep(6)

    
def get_publications():
    driver.get(f'https://www.instagram.com/{username}')
    
    publications = driver.find_element_by_class_name("g47SY")
    publications = int(publications.text)

    return publications

def get_images():
    driver.find_element_by_xpath("/html/body/div/section/main/div/div/article/div/div/div/div").click()
    sleep(2)

def get_infos():
    description_list = []
    likes_list = []
    date_list = []    
    
    description = driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/article/div[2]/div[1]/ul/div/li/div/div/div[2]/span")
    likes = driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/article/div[2]/section[2]/div/div[2]/button/span")
    date = driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/article/div[2]/div[2]/a/time")

    description = description.text
    likes = int(likes.text)
    date = (date.text)

    description_list.append(description)
    likes_list.append(likes)
    date_list.append(date)

    driver.find_element_by_xpath("/html/body/div[4]/div[1]/div/div/a").click()

    i = 0

    sleep(3)

    while i < 6:
        try:
            description = driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/article/div[2]/div[1]/ul/div/li/div/div/div[2]/span")
            description = description.text
        except:
            description = 'Sem legenda'
        likes = driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/article/div[2]/section[2]/div/div[2]/button/span")
        date = driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/article/div[2]/div[2]/a/time")

        likes = int(likes.text)
        date = (date.text)
        
        description_list.append(description)    
        likes_list.append(likes)
        date_list.append(date)

        i =+ 1

        try:
            driver.find_element_by_xpath("/html/body/div[4]/div[1]/div/div/a[2]").click()
        except:
            break
        
        sleep(3)

    return {
        'descrição': description_list,
        'curtidas': likes_list,
        'data': date_list,
    }



if __name__ == '__main__':
    login()
    get_publications()
    get_images()
    print(get_infos())