import time
from logging import exception

from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

from Commons.CommonElements import CommonElements


class SearchPage(CommonElements):

    def ClickOnAddPopup(self,browser):
        try:
            #self.ElementToBeClickable(browser,"//*[@data-cy='closeModal']")
            time.sleep(3)
            #WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@data-cy='closeModal']")))
            browser.find_element(by=By.XPATH, value="//*[@data-cy='closeModal']").click()
        except Exception as e:
            print(e)
            pass

    def ClickOnFromCityDropdown(self,browser):
        try:
            self.ElementToBeClickable(browser,"//*[@for='fromCity']")
            #WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@for='fromCity']")))
            browser.find_element(by=By.XPATH, value="//*[@for='fromCity']").click()
        except Exception as e:
            print(e)
            pass

    def ClickOnToCityDropdown(self,browser):
        self.ElementToBeClickable(browser, "//*[@for='toCity']")
        #WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@for='toCity']")))
        browser.find_element(by=By.XPATH, value="//*[@for='toCity']").click()

    def SelectValueFromList(self, browser, expectedCountry):
        WebDriverWait(browser, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='react-autowhatever-1']//ul//li[last()]")))
        allElements = browser.find_elements(by=By.XPATH, value="//*[@id='react-autowhatever-1']//ul//li")
        for eachelement in range(1, len(allElements) + 1):
            actualCountry = browser.find_element(by=By.XPATH,
                                                      value="//*[@id='react-autowhatever-1']//ul//li[" + str(
                                                          eachelement) + "]//div[starts-with(@class,'font14')]").text
            print(actualCountry)
            if expectedCountry == actualCountry:
                browser.find_element(by=By.XPATH, value="//*[@id='react-autowhatever-1']//ul//li[" + str(
                    eachelement) + "]").click()
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
                                          eachelement) + "]//*[@class='DayPicker-Day']["+str(eachcolumn)+"]//p[1]").text
                print(actualDate)
                if expectedDate == actualDate:
                    browser.find_element(by=By.XPATH,
                                         value="//*[@class='DayPicker-Month'][last()]//div[@class='DayPicker-Week'][" + str(
                                             eachelement) + "]//*[@class='DayPicker-Day'][" + str(
                                             eachcolumn) + "]").click()
                    return


    def ClickOnSearchButton(self,browser):
        self.ElementToBeClickable(browser, "//*[@data-cy='submit']")
        #WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@data-cy='submit']")))
        browser.find_element(by=By.XPATH, value="//*[@data-cy='submit']").click()


    def ClickOnToCityDropdown(self,browser):
        self.ElementToBeClickable(browser, "//*[@for='toCity']")
        #WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@for='toCity']")))
        browser.find_element(by=By.XPATH, value="//*[@for='toCity']").click()