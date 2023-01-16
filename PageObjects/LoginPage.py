from selenium.webdriver.common.by import By

class LoginPage():
    Email = (By.ID, "Email")
    Password = (By.ID, "Password")
    LoginButton = (By.XPATH, "/html/body/div[6]/div/div/div/div/div[2]/div[1]/div/form/div[3]/button")
    LogoutText = (By.XPATH, "//*[@id='navbarText']/ul/li[3]/a")

    def __init__(self,driver):
        self.driver = driver

    def getEmail(self,email):
        self.driver.find_element(*LoginPage.Email).clear()
        return self.driver.find_element(*LoginPage.Email).send_keys(email)

    def getPassword(self,Passw):
        self.driver.find_element(*LoginPage.Password).clear()
        return self.driver.find_element(*LoginPage.Password).send_keys(Passw)

    def clickLogin(self):
        return self.driver.find_element(*LoginPage.LoginButton)

    def clicklogout(self):
        return self.driver.find_element(*LoginPage.LogoutText)