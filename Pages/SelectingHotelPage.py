import time

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

from Commons.CommonElements import CommonElements

class SelectingHotelPage(CommonElements):


    def ClickOnAddPopup(self,browser):
        self.ElementToBeClickable(browser,"//*[@data-cy='closeModal']")
        #WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@data-cy='closeModal']")))
        browser.find_element(by=By.XPATH, value="//*[@data-cy='closeModal']").click()

    def ClickOnHotelmenu(self,browser):
        self.ElementToBeClickable(browser,"//*[@data-cy='menu_Hotels']")
        #WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@for='fromCity']")))
        browser.find_element(by=By.XPATH, value="//*[@data-cy='menu_Hotels']").click()

    def ClickOnCityDropdown(self,browser):
        self.ElementToBeClickable(browser,"//*[@for='city']")
        #WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@for='fromCity']")))
        browser.find_element(by=By.XPATH, value="//*[@for='city']").click()

    def SelectValueFromList(self, browser, expectedHotel):
        WebDriverWait(browser, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@title='Where do you want to stay?']")))
        browser.find_element(by=By.XPATH, value="//*[@title='Where do you want to stay?']").click()
        allElements = browser.find_elements(by=By.XPATH, value="//ul[@role='listbox']//li//span[@class='blackText']")
        for eachelement in allElements:
            print(eachelement)
            actualHotel = eachelement.text
            if expectedHotel == actualHotel:
                eachelement.click()
                break

    def SelectDate(self, browser, expectedDate):
        WebDriverWait(browser, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@class='DayPicker-Month'][last()]//div[@class='DayPicker-Week']")))
        allRows = browser.find_elements(by=By.XPATH, value="//*[@class='DayPicker-Month'][last()]//div[@class='DayPicker-Week']")
        for eachelement in range(1, len(allRows) + 1):
            allcolumns = browser.find_elements(by=By.XPATH,
                                                      value="//*[@class='DayPicker-Month'][last()]//div[@class='DayPicker-Week'][" + str(
                                                          eachelement) + "]//*[@class='DayPicker-Day']")
            for eachcolumn in range(1, len(allcolumns) + 1):
                actualDate = browser.find_element(by=By.XPATH,
                                      value="//*[@class='DayPicker-Month'][last()]//div[@class='DayPicker-Week'][" + str(
                                          eachelement) + "]//*[@class='DayPicker-Day']["+str(eachcolumn)+"]").text
                print(actualDate)
                if expectedDate == actualDate:
                    browser.find_element(by=By.XPATH,
                                         value="//*[@class='DayPicker-Month'][last()]//div[@class='DayPicker-Week'][" + str(
                                             eachelement) + "]//*[@class='DayPicker-Day'][" + str(
                                             eachcolumn) + "]").click()
                    return

    def SelectApplyButton(self,browser):
        time.sleep(2)
        self.ElementToBeClickable(browser, "//button[text()='Apply']")
        # WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@data-cy='submit']")))
        browser.find_element(by=By.XPATH, value="//button[text()='Apply']").click()

    def SelectSearchButton(self,browser):
        self.ElementToBeClickable(browser, "//*[@id='hsw_search_button']")
        # WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@data-cy='submit']")))
        browser.find_element(by=By.XPATH, value="//*[@id='hsw_search_button']").click()


    def SelectingITC(self,browser):
        self.ElementToBeClickable(browser,"//div[@id='RECENTLY_VIEWED_HOTELS']")
        browser.find_element(by=By.XPATH,value="//div[@id='RECENTLY_VIEWED_HOTELS']").click()

    def GetWindowName(self,browser):
        return browser.current_window_handle

