import time

import pytest

from pageObjects.AddCustomerPage import AddCustomer
from pageObjects.LoginPage import Loginpage
from pageObjects.SearchCustomerPage import Searchcustomer
from utilities.customLogger import LogGen
from utilities.readProperties import Readconfig


class Test_004_SearchCustomerbyEmail:
    baseURL = Readconfig.getApplicationURL()
    username = Readconfig.getUsername()
    password = Readconfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_searchCustomerbyEmail(self, setup):
        self.logger.info("********** Test_004_SearchCustomerby Email ************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = Loginpage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        self.logger.info("********** Login Successful ************")
        self.logger.info("********** Starting Search customer test ************")
        self.addcus = AddCustomer(self.driver)
        self.addcus.clickonCustomer()
        self.addcus.clickonCustomermenu()
        self.logger.info("********** Starting Search customer By Email ************")
        searchcus = Searchcustomer(self.driver)
        searchcus.setEmail("steve_gates@nopCommerce.com")
        searchcus.clickonSearch()
        time.sleep(5)
        status = searchcus.searchbyEmail("steve_gates@nopCommerce.com")
        assert True == status
        self.driver.save_screenshot(".\\Screenshots\\test_Searchcustomer.png")
        self.logger.info("********** End Search customer By Email ************")
        self.driver.close()


