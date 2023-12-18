from selenium import webdriver
from selenium.webdriver.chrome.service import Service

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver_service = Service(executable_path='D:\Automation selenium\chromedriver/chromedriver.exe')
driver = webdriver.Chrome(options=options, service=driver_service)

driver.get("https://www.google.ro")
time.sleep(2)
driver.close()
