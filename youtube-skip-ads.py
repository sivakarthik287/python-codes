from selenium import webdriver
import time
import selenium
import sys

#get URL
print("Enter the youtube URL to Start a browser : ")
url=input()


if not url:
    url="https://www.youtube.com/?feature=youtu.be"

options = webdriver.ChromeOptions()
options.add_argument('user-data-dir=C:/Users/sivak/AppData/Local/Google/Chrome/User Data/Default') 
driver = webdriver.Chrome("D:/python-practice/chromedriver_win32/chromedriver.exe", options=options)
driver.get(url)

while True:
    time.sleep(5)
    try:
        elements = driver.find_elements_by_class_name("ytp-ad-skip-button.ytp-button")
        elements[0].click()
    except:
        print("no ad(s) are played now or ad could not be skipped")
        try:
            _ = driver.window_handles
        except selenium.common.exceptions.WebDriverException as ex:
            print("browser session closed by user")
            sys.exit(0)
        except selenium.common.exceptions.InvalidSessionIdException as e:
            print("browser session closed by user")
            sys.exit(0)
        
