import pytest
from selenium import webdriver
from PageObjects.LoginPage import LoginPage
from Utilities.readproperties import ReadConfig
from Utilities.CustomLogger import LogGen
from Utilities import XLUtilis
import time

class Test_login2_DDT():
    baseURL = ReadConfig.getAppURL()
    path = ".//Testdata/Logindata.xlsx"

    logger = LogGen.loggen()

    def test_login(self,setup):
        self.logger.info("******************Test_login2_DDT**************")
        self.logger.info("******************Verifying test_loginDD**************")
        self.driver =setup
        self.driver.get(self.baseURL)
        self.Logi = LoginPage(self.driver) #OBJECT OF LOGIN PAGE

        self.rows = XLUtilis.getRowCount(self.path,'Sheet1')
        print("Number of rows in excel :",self.rows)

        list =[]  #will use entry variable

        for r in range(2, self.rows+1):
            self.user = XLUtilis.readData(self.path,'Sheet1', r, 1)
            self.passw = XLUtilis.readData(self.path,'Sheet1', r, 2)
            self.exp = XLUtilis.readData(self.path, 'Sheet1',  r, 3)

            self.Logi.getEmail(self.user)
            self.Logi.getPassword(self.passw)
        self.Logi.clickLogin().click()
            # time.sleep(5)

        # self.Logi.clicklogout().click()

        act_title = self.driver.title
        exp_title = "Dashboard / nopCommerce administration"
        if act_title == exp_title:
            if self.exp == "Pass":
                self.logger.info("**Pass*")
                self.Logi.clicklogout().click()
                list.append("Pass")
            elif self.exp == "Fail":
                self.logger.info("**fail*")
                self.Logi.clicklogout().click()
                list.append("Fail")
        elif act_title != exp_title:
            if self.exp== "Pass":
                self.logger.info("**fail*")
                list.append("Fail")
            elif self.exp == "Fail":
                self.logger.info("**Pass*")
                list.append("Pass")

        if "Fail" not in list:
            self.logger.info("Login DDT test passed")
            self.driver.close()
            assert True
        else:
            self.logger.info("Login DDT test failed")
            self.driver.close()
            assert False


        self.logger.info("Login DDT test END")

        # pytest -rA --html=myHTMLReport.html







