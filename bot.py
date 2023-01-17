from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
import os
from bs4 import BeautifulSoup
import time

FIRST_NAME = "first nam"
LAST_NAME = "last nam"
PHONE_NUM = "1234567890"
STUDENT_NUM = "123456789"
EMAIL = "email@gmail.com"
SERVICE_BTN_ID = "tt9000004114"

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

time.sleep(3)

try:
    closed_page = driver.find_element("id", "page_closed")
    while closed_page:
        time.sleep(30)
        driver.refresh()
        closed_page = driver.find_element("id", "page_closed")
except:
    pass

firstName = driver.find_element("id", "consumerfield_firstName")
lastName = driver.find_element("id", "consumerfield_lastName")
phoneNum = driver.find_element("id", "consumerfield_phone")
firstName.send_keys(FIRST_NAME)
lastName.send_keys(LAST_NAME)
phoneNum.send_keys(PHONE_NUM)

nextBtn = driver.find_element("id", "qBtnNext")
nextBtn.click()
time.sleep(1)

studentNum = driver.find_element("id", "customscreenfield_StudentID")
studentNum.send_keys(STUDENT_NUM)
nextBtn.click()
time.sleep(1)

select = Select(driver.find_element("id","customscreenfield_Interaction_0"))
select.select_by_visible_text('Telephone Call')

email = driver.find_element("id", "customscreenfield_Email_0")
email.send_keys(EMAIL)
nextBtn.click()
time.sleep(1)

serviceBtn = driver.find_element("id", SERVICE_BTN_ID)
serviceBtn.click()
time.sleep(1)

exitBtn = driver.find_element("id", "btnExit")
exitBtn.click()

while True:
    val = 1