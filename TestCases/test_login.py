import pytest
from selenium import webdriver
from PageObjects.LoginPage import LoginPage
from Utilities.readproperties import ReadConfig
from Utilities.CustomLogger import LogGen

class Test_login():
    baseURL =ReadConfig.getAppURL()
    email = ReadConfig.getUseremail()
    Passw = ReadConfig.getUserPass()

    logger = LogGen.loggen()

    def test_homepage(self,setup):
        self.logger.info("************Test_login************")
        self.logger.info("************test_homepage************")

        self.driver = setup
        self.driver.get(self.baseURL)
        Title = self.driver.title

        if Title == "Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("******************Test Homepage passed**************")
        else:
            self.driver.get_screenshot_as_file(r"C:\Users\Admin\PycharmProjects\Frameworkprac1\Screenshots\sshp.png")
            self.driver.close()
            self.logger.info("******************Test Homepage failed**************")
            assert False

    def test_login(self,setup):
        self.logger.info("******************Verifying test_login**************")
        self.driver =setup
        self.driver.get(self.baseURL)
        self.Logi = LoginPage(self.driver) #OBJECT OF LOGIN PAGE
        self.Logi.getEmail(self.email)
        self.Logi.getPassword(self.Passw)
        self.Logi.clickLogin().click()
        # self.Logi.clicklogout().click()


        if self.driver.title == "Dashboard / nopCommerce administration":
            self.driver.close()
            assert True
            self.logger.info("******************Test_login passed**************")
        else:
            self.driver.get_screenshot_as_file(r"C:\Users\Admin\PycharmProjects\Frameworkprac1\Screenshots\sslogin.png")
            self.driver.close()
            self.logger.error("******************Test_login failed**************")
            assert False









