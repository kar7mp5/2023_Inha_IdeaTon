"""
alert.py

[Purpose]
iClass Anouncement Summary Program

[Order]
0. Crawling iClass anouncement
1. Parsing crawling data
2. Send converted data to email

[Used Library]
selenium : for opening website and login to crawling anounce data
bs4 : scrap anounce data from iClass
smtplib : send message to email
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import smtplib

class AlertAnnouncement:
    def __init__(self):
        """
        [Database]
        users' information dictionary
        xpath dictionary
        """
        # user's info dictionary
        # key : id, pw
        self.user_info = {
                    "id" : "12234073",
                    "pw" : "ms041005a@@",
                    "FROM" : "tommy1005a@gmail.com",
                    "TO" : ["tommy1005a@gmail.com"],
                    "email_pw" : "hxzaewtcwtecnteq"
                    }
        # xpath dictionary
        # key : id_container, pw_container, anounce_button, detail_button
        self.xpath_dict = {
                        "id_container" : "/html/body/div[3]/div[2]/div/div/div/div/div[2]/div[1]/div[2]/form/div[1]/input[1]",
                        "pw_container" : "/html/body/div[3]/div[2]/div/div/div/div/div[2]/div[1]/div[2]/form/div[1]/input[2]",
                        "anounce_button" : "/html/body/div[3]/div[1]/nav/div/div[2]/ul/li[5]/a/div",
                        "detail_button" : "/html/body/div[3]/div[1]/nav/div/div[2]/ul/li[5]/div[1]/div[2]/div[3]/a"
                    }
        self.email_message = ""
    """
    Crawling report announcement from iClass
    """
    def crawling_announcement(self):
        # Load options
        options = webdriver.ChromeOptions()
        # Add hide window option
        options.add_argument("headless")
        # Open iClass login page
        driver = webdriver.Chrome(options=options)
        # Open iClass website
        driver.get("https://learn.inha.ac.kr/login.php")
        driver.implicitly_wait(time_to_wait=10)

        # Login
        driver.find_element(By.XPATH, self.xpath_dict["id_container"]).send_keys(self.user_info["id"])
        driver.find_element(By.XPATH, self.xpath_dict["pw_container"]).send_keys(f'{self.user_info["pw"]}\n')
        driver.implicitly_wait(time_to_wait=10)

        # Move to announcement
        driver.find_element(By.XPATH, self.xpath_dict["anounce_button"]).click()
        driver.find_element(By.XPATH, self.xpath_dict["detail_button"]).click()
        driver.implicitly_wait(time_to_wait=10)


        html = driver.page_source # load html from page
        driver.close()
        soup = BeautifulSoup(html, "lxml") # for fast speed to use lxml not html parser
        message_box = soup.find_all("div", "media") # <div class = "media"> report announcment tag information
        
        for message in message_box:
            # Parsing message
            text = message.text.split("일전") # split by "일전" to  
            self.email_message += f"{text[0][0:-1]}\n{text[1]}\n\n"
    """ 
    Send converted message by email
    """
    def send_mail(self):
        # Email message
        message = """\
From: %s
To: %s
Subject: %s
%s
        """ % (self.user_info["FROM"], ", ".join(self.user_info["TO"]), "과제 알림", self.email_message)

        # Send the mail
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(self.user_info["FROM"], self.user_info["email_pw"])
        server.sendmail(self.user_info["FROM"], self.user_info["TO"], message.encode("utf8"))

        server.quit()