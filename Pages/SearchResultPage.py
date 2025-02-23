from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

class SearchResultPage():
    def GetValidationText(self, browser):
        WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.XPATH, "//*[@class='error-title']")))
        return browser.find_element(by=By.XPATH, value="//*[@class='error-title']").text

