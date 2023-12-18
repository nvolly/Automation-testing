from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver_service = Service(executable_path='D:\python\Automation\Selenium tests\chromedriver.exe')
driver = webdriver.Chrome(options=options, service=driver_service)
driver.implicitly_wait(5)

driver.get("https://www.amazon.com/")


search = driver.find_element(By.ID, 'twotabsearchtextbox')
search.send_keys('dress', Keys.ENTER)

#$x("//span[@class='a-color-state a-text-bold']")

expected_text = '"dress"'
actual_text = driver.find_element(By.XPATH, "//span[@class='a-color-state a-text-bold']").text

assert expected_text == actual_text, f'Error. Exxpected text: {expected_text}, but actual text: {actual_text}'