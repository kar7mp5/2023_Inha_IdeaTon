"""
main.py

[Purpose]
iClass Anouncement Summary Program

[Order]
0. Crawling iClass anouncement
1. Parsing crawling data
2. Send converted data to email

[Used Library]
selenium : for opening website and login to crawling anounce data
bs4 & requests : scrap anounce data from iClass
"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests

from time import sleep
"""
[Database]
users' information dictionary
xpath dictionary
"""
# user's info dictionary
# key : id, pw
user_info = {
            "id" : "12234073",
            "pw" : "ms041005a@@"
            }
# xpath dictionary
# key : id_container, pw_container, anounce_button, detail_button
xpath_dict = {
                "id_container" : "/html/body/div[3]/div[2]/div/div/div/div/div[2]/div[1]/div[2]/form/div[1]/input[1]",
                "pw_container" : "/html/body/div[3]/div[2]/div/div/div/div/div[2]/div[1]/div[2]/form/div[1]/input[2]",
                "anounce_button" : "/html/body/div[3]/div[1]/nav/div/div[2]/ul/li[5]/a/div",
                "detail_button" : "/html/body/div[3]/div[1]/nav/div/div[2]/ul/li[5]/div[1]/div[2]/div[3]/a"
             }
# Open iClass login page
driver = webdriver.Chrome()
driver.get("https://learn.inha.ac.kr/login.php")
driver.implicitly_wait(time_to_wait=10)

# Login
driver.find_element(By.XPATH, xpath_dict["id_container"]).send_keys(user_info["id"])
driver.find_element(By.XPATH, xpath_dict["pw_container"]).send_keys(f'{user_info["pw"]}\n')
driver.implicitly_wait(time_to_wait=10)

# Move to announcement
driver.find_element(By.XPATH, xpath_dict["anounce_button"]).click()
driver.find_element(By.XPATH, xpath_dict["detail_button"]).click()
driver.implicitly_wait(time_to_wait=10)

html = driver.page_source

soup = BeautifulSoup(html, "lxml")
message_box = soup.find_all("div", {"class":"media"})
for message in message_box:
    print(message)
sleep(5)

driver.close()