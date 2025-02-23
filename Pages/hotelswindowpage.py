import time

import self
from outcome import Value
from selenium.webdriver.common.by import By

from selenium.webdriver.remote.webelement import WebElement
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from weblib.selenium_tools import send_keys

from Commons.CommonElements import CommonElements


class Windowshandling(CommonElements):

    def Windowhand(self,browser,parent_window):
        allwindows = browser.window_handles  # get all windows name
        for eachWindow in allwindows:  # iterate in to all windows
            if parent_window != eachWindow:
                browser.switch_to.window(eachWindow)  # switching in to respective  window
                elementExist = browser.find_elements(by=By.XPATH, value="//button[text()='BOOK THIS NOW']")
                if len(elementExist) > 0:  # ensuring the element exist in the respective window
                    browser.find_element(by=By.XPATH, value="//button[text()='BOOK THIS NOW']").click()
                    break;



    def title(self,browser):
        startbutton = browser.find_element(by=By.XPATH, value="//select[@id='title']")
        browser.execute_script("arguments[0].scrollIntoView();", startbutton)  #for scrolling the selected id
        automation_Tool = Select(browser.find_element(by=By.XPATH, value="//select[@id='title']"))
        automation_Tool.select_by_index(1)
        #self.browser.find_element(by=By.XPATH, value="//select[@id='title']").click()

    def FullnameLastnameMailID(self,browser):
        browser.find_element(by=By.XPATH, value="//input[@name='fName']").send_keys("Anand")
        browser.find_element(by=By.XPATH, value="//input[@name='lName']").send_keys("Venkatesh")
        browser.find_element(by=By.XPATH, value="//input[@name='email']").send_keys("anandavenkatesh103@gmail.com")

    def mobnumber(self,browser):
        browser.find_element(by=By.XPATH, value="//input[@name='mNo']").send_keys("7358277404")

        #self.browser.find_element(by=By.XPATH, value="//select[@id='title']").click()

    def selectstate(self,browser):
        automation_Tool = Select(browser.find_element(by=By.XPATH, value="//input[@value='Tamil Nadu']"))
        automation_Tool.select_by_index(0)
        #self.browser.find_element(by=By.XPATH, value="//select[@id='title']").click()

    def lastpaybutton(self,browser):
        #elementExist = browser.find_elements(by=By.XPATH, value="//a[text()='Pay Now']")
        self.ElementToBeClickable(browser,"//a[text()='Pay Now']")
        browser.find_element(by=By.XPATH, value="//a[text()='Pay Now']").click()


    def creditcardpaymentoption(self,browser):
        self.ElementToBeClickable(browser, "//span[text()='Credit & Debit Cards']//ancestor::li[contains(@class,'paymode')]")
        browser.find_element(by=By.XPATH, value="//span[text()='Credit & Debit Cards']//ancestor::li[contains(@class,'paymode')]").click()

    def cardnumber(self,browser):
        browser.find_element(by=By.XPATH, value="//input[@id='cardNumber']").send_keys("4585460020783735")
        browser.find_element(by=By.XPATH, value="//input[@id='nameOnCard']").send_keys("ANANDAVENKATESH")
        time.sleep(5)
        selectmonth = Select(self.browser.find_element(by=By.NAME, value="expiryMonth")) #//*[@class='month__select__wrap']//select[@name='expiryMonth']
        selectmonth.select_by_index(1)
        time.sleep(2)
        selectmonth.select_by_visible_text("February (02)")
        time.sleep(2)

        selectyear = Select(self.browser.find_element(by=By.NAME,
                                                       value="Year"))  # //*[@class='month__select__wrap']//select[@name='Year']
        selectyear.select_by_index(1)
        time.sleep(2)
        selectyear.select_by_visible_text("2025")
        time.sleep(2)
        browser.find_element(by=By.XPATH, value="//input[@id='cardCvv']").send_keys("458")
        time.sleep(3)

    def paynowbutton(self,browser):
        #elementExist = browser.find_elements(by=By.XPATH, value="//a[text()='Pay Now']")
        self.ElementToBeClickable(browser,"//span[text()='pay now']")
        browser.find_element(by=By.XPATH, value="//span[text()='pay now']").click()

    def errornotificaton(self,browser):
        self.ElementToBeClickable(browser, "//span[@class='white-text flex-one']")
        print(browser.find_element(by=By.XPATH, value="//span[@class='white-text flex-one']").text)

        assert browser.find_element(by=By.XPATH, value="//span[@class='white-text flex-one']").text == "We encountered a technical issue at network's end while processing your card.Please retry with another card or payment method."
        time.sleep(3)





