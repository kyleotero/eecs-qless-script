from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import os
from bs4 import BeautifulSoup
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")

link = "https://kiosk.ca1.qless.com/kiosk/app/home/19713"

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()), options=chrome_options
)

driver.get(link)

content = driver.page_source
soup = BeautifulSoup(content, "html.parser")

time.sleep(5)

firstName = driver.find_element("id", "consumerfield_firstName")
lastName = driver.find_element("id", "consumerfield_lastName")
phoneNum = driver.find_element("id", "consumerfield_phone")
firstName.send_keys("first name")
lastName.send_keys("last name")
phoneNum.send_keys("phone number")

nextBtn = driver.find_element("id", "qBtnNext")
nextBtn.click()

while True:
    val = 1
