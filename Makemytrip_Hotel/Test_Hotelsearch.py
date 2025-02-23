import time

import pytest

from selenium import webdriver

from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

from Pages.SearchPage import SearchPage
from Pages.SelectingHotelPage import SelectingHotelPage
from Pages.hotelSearchResultPage import hotelSearchResultPage
from Pages.hotelswindowpage import Windowshandling


# class Test_Hotelsearch(SearchPage,SelectingHotelPage):

    # def test_OpenAndClose1(self,url_Data):
    #     self.browser = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()))
    #     self.browser.maximize_window()
    #
    #     # self.browser.implicitly_wait(60)
    #     self.browser.get(url_Data)
    #     time.sleep(10)




@pytest.mark.usefixtures("url_Data")
class Test_Hotelsearch(SelectingHotelPage,hotelSearchResultPage,Windowshandling):

        def test_OpenAndClose1(self, url_Data,Hotelsearch ):

            self.browser = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()))
            self.browser.maximize_window()
            print("log in")
            # self.browser.implicitly_wait(60)
            self.browser.get(url_Data)
            self.ClickOnAddPopup(self.browser)
            self.ClickOnHotelmenu(self.browser)
            self.ClickOnCityDropdown(self.browser)
            self.SelectValueFromList(self.browser, Hotelsearch[0])
            self.SelectDate(self.browser,Hotelsearch[1])
            self.SelectDate(self.browser, Hotelsearch[2])
            self.SelectApplyButton(self.browser)
            self.SelectSearchButton(self.browser)

            parentWindow = self.GetWindowName(self.browser)
            time.sleep(15)
            self.SelectHotel(self.browser,"Ibis")
            time.sleep(5)
            self.Windowhand(self.browser,parentWindow)
            time.sleep(5)
            self.title(self.browser)
            time.sleep(10)
            self.FullnameLastnameMailID(self.browser)
            time.sleep(5)
            self.mobnumber(self.browser)
            time.sleep(5)
            #self.selectstate(self.browser)
            #time.sleep(5)
            self.lastpaybutton(self.browser)
            time.sleep(10)

            self.creditcardpaymentoption(self.browser)
            time.sleep(3)
            self.cardnumber(self.browser)
            time.sleep(5)
            self.paynowbutton(self.browser)
            time.sleep(5)
            self.errornotificaton(self.browser)
            time.sleep(3)



