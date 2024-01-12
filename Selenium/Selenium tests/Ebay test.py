from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver_service = Service(executable_path='D:\Automation python\Automation\Selenium\chromedriver.exe')
driver = webdriver.Chrome(options=options, service=driver_service)
driver.implicitly_wait(5)

driver.get("https://www.ebay.com/")


search = driver.find_element(By.CLASS_NAME, 'gh-tb ui-autocomplete-input')
search.send_keys('dress', Keys.ENTER)