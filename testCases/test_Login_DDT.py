import time
import pytest
from selenium import webdriver
from pageObjects.LoginPage import Loginpage
from utilities.readProperties import Readconfig
from utilities.customLogger import LogGen
from utilities import XLUtils
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Test_002_Login_DDT:
    baseURL = Readconfig.getApplicationURL()
    path = "D:\\nopCommerceApp\\Testdata\\Logintest data.xlsx"
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_Login_DDT(self, setup):
        self.logger.info("********* Test_002_Login_DDT *********")
        self.logger.info("********* Verifing Login Test *********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = Loginpage(self.driver)

        self.rows = XLUtils.get_row_count(self.path, 'Sheet1')
        print("no of rows:", self.rows)

        list_status = []

        for r in range(2, self.rows+1):
            self.user = XLUtils.read_excel(self.path, 'Sheet1', r, 1)
            self.password = XLUtils.read_excel(self.path, 'Sheet1', r, 2)
            self.exp = XLUtils.read_excel(self.path, 'Sheet1', r, 3)

            self.lp.setUsername(self.user)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            WebDriverWait(self.driver, 10).until(EC.title_contains("Dashboard / nopCommerce administration"))

            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"
            time.sleep(20)
            if act_title == exp_title:
                if self.exp == "Pass":
                    self.logger.info("********* Login test passed*********")
                    self.lp.clickLogout()
                    list_status.append("PASS")

                elif self.exp == "Fail":
                    self.logger.info("********* Login test Failed*********")
                    self.lp.clickLogout()
                    list_status.append("FAIL")
            elif act_title != exp_title:
                if self.exp == "Pass":
                    list_status.append("FAIL")
                elif self.exp == "Fail":
                    list_status.append("PASS")

        if "FAIL" not in list_status:
            self.logger.info("********* Login test DDT Passed*********")
            self.driver.close()
            assert True
        else:
            self.logger.info("********* Login test DDT Failed*********")
            self.driver.close()
            assert False

