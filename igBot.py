from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random


class InstagramBot:
    def __init__(self,username,password):
        self.username = username
        self.password = password
        self.driver = webdriver.Firefox(executable_path=r"./geckodriver.exe")

    def login(self):
        driver = self.driver
        driver.get('https://www.instagram.com/')
        time.sleep(3)
        user_element = driver.find_element_by_xpath('//input[@name="username"]')
        user_element.clear()
        #time.sleep(random.randint(4, 6))
        user_element.send_keys(self.username)
        #time.sleep(random.randint(4, 6))
        password_element = driver.find_element_by_xpath('//input[@name="password"]')
        password_element.clear()
        password_element.send_keys(self.password)
        password_element.send_keys(Keys.RETURN)
        time.sleep(5)
        self.comentario_hashtag('coding')

    @staticmethod
    def type_like_a_person(sentence, single_input_field):
        for letter in sentence:
            single_input_field.send_keys(letter)
            time.sleep(random.randint(1, 3) / 30)

    def comentario_hashtag(self,hashtag):
            driver = self.driver
            driver.get('https://www.instagram.com/explore/tags/'+ hashtag +'/')
            for i in range(1, 3):
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(3)
            hrefs = driver.find_elements_by_tag_name('a')
            pic_hrefs = [elem.get_attribute("href") for elem in hrefs]
            [href for href in pic_hrefs if hashtag in href]
            print(hashtag+ ' fotos ' + str(len(pic_hrefs)))

            for pic_href in pic_hrefs:
                driver.get(pic_href)
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                try:
                    comentarios = ["Que post irado!","Irado!","wow"]
                    driver.find_element_by_class_name("Ypffh").click()
                    campo_comentario = driver.find_element_by_class_name("Ypffh")
                    driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[1]/span[1]/button/div').click()
                    time.sleep(random.randint(2, 5))
                    self.type_like_a_person(random.choice(comentarios),campo_comentario)
                    time.sleep(random.randint(40,120))
                    driver.find_element_by_xpath("//button[contains(text(),'Publicar')]").click()
                    time.sleep(3)
                except Exception as e:
                    print(e)
                    time.sleep(5)

            




luanBot = InstagramBot('USUARIO','SENHA')
luanBot.login()