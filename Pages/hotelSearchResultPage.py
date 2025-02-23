from selenium.webdriver.common.by import By

from Commons.CommonElements import CommonElements


class hotelSearchResultPage(CommonElements):

    def SelectHotel(self,browser,expectedhotel):
        self.ElementToBeVisible(browser, "(//div[starts-with(@class,'listingRowOuter')])[last()]")
        totalHotels = browser.find_elements(by=By.XPATH, value="(//div[starts-with(@class,'listingRowOuter')])")
        for eachvalue in range(1,len(totalHotels)+1):
            atcualhotel = browser.find_element(by=By.XPATH, value="(//div[starts-with(@class,'listingRowOuter')])["+str(eachvalue)+"]//p[@id='hlistpg_hotel_name']//*[starts-with(@class,'word')]").text
            print(atcualhotel)
            if expectedhotel.upper() in atcualhotel.upper() :
                browser.find_element(by=By.XPATH, value="(//div[starts-with(@class,'listingRowOuter')])[" + str(
                    eachvalue) + "]//div[starts-with(@class,'listingRow')]").click()
                break
