from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pytest

class TestAmazon:
    search_words = ('dress', 'shoes', 'toys')

    driver = ''

    def setup_method(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        driver_service = Service(executable_path='D:\python\Automation\chromedriver-win64\chromedriver.exe')
        self.driver = webdriver.Chrome(options=options, service=driver_service)
        self.driver.implicitly_wait(5)
        self.driver.get("https://www.amazon.com/")
        time.sleep(10)

    @pytest.mark.parametrize("search_query", search_words)
    def test_Amazon_search_dress(self, search_query):
        search = self.driver.find_element(By.ID, 'twotabsearchtextbox')
        search.send_keys(search_query, Keys.ENTER)

        # $x("//span[@class='a-color-state a-text-bold']")

        expected_text = f'\"{search_query}\"' #dress / "dress"
        actual_text = self.driver.find_element(By.XPATH, "//span[@class='a-color-state a-text-bold']").text

        assert expected_text == actual_text, f'Error. Expected text: {expected_text}, but actual text: {actual_text}'

    def teardown_method(self):
        self.driver.quit()
