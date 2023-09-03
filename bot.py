import sys
import logging
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time

log_filename = "bot_log.txt"
logging.basicConfig(
    filename=log_filename,
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s]: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

def main():
    try:
        if len(sys.argv) != 7:
            logging.error("Usage: python3 bot.py FIRST_NAME LAST_NAME PHONE_NUM STUDENT_NUM EMAIL SERVICE_BTN_ID")
            sys.exit(1)

        FIRST_NAME = sys.argv[1]
        LAST_NAME = sys.argv[2]
        PHONE_NUM = sys.argv[3]
        STUDENT_NUM = sys.argv[4]
        EMAIL = sys.argv[5]
        SERVICE_BTN_ID = sys.argv[6]

        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument('--headless=new')

        link = "https://kiosk.ca1.qless.com/kiosk/app/home/19713"

        driver = webdriver.Chrome(
            options=chrome_options
        )

        driver.get(link)

        content = driver.page_source
        soup = BeautifulSoup(content, "html.parser")

        time.sleep(5)

        try:
            closed_page = driver.find_element("id", "page_closed")
            while closed_page:
                logging.info("Queue is closed")
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

        logging.info("Starting bot")
        nextBtn = driver.find_element("id", "qBtnNext")
        nextBtn.click()
        time.sleep(1)

        studentNum = driver.find_element("id", "customscreenfield_StudentID")
        studentNum.send_keys(STUDENT_NUM)
        nextBtn.click()
        time.sleep(1)

        select = Select(driver.find_element("id", "customscreenfield_Interaction_0"))
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

        driver.quit()

        logging.info("Script completed")
        
    except Exception as e:
        logging.exception("An error occurred:")
        raise

if __name__ == "__main__":
    main()
