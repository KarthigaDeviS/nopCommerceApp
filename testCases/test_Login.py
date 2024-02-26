import pytest
from selenium import webdriver
from pageObjects.LoginPage import Loginpage
from utilities.readProperties import Readconfig
from utilities.customLogger import LogGen

class Test_001_Login:
    baseURL = Readconfig.getApplicationURL()
    username = Readconfig.getUsername()
    password = Readconfig.getPassword()

    logger = LogGen.loggen()
    logger.info("**********Test_001_Login************")

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_homepageTitle(self, setup):
        self.logger.info("**********Test_001_Login************")
        self.logger.info("***********Verify homepage title****")
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title

        if act_title == "Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("********* Home page title test Passed*********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_homepageTitle.png")
            self.driver.close()
            self.logger.info("********* Home page title test Failed*********")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_Login(self, setup):
        self.logger.info("********* Verifing Login Test *********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = Loginpage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title

        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.driver.close()
            self.logger.info("********* Login test passed*********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_Login.png")
            self.driver.close()
            self.logger.info("********* Login test Failed*********")
            assert False
