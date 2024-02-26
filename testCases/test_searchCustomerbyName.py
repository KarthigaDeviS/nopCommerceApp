import time

import pytest

from pageObjects.AddCustomerPage import AddCustomer
from pageObjects.LoginPage import Loginpage
from pageObjects.SearchCustomerPage import Searchcustomer
from utilities.customLogger import LogGen
from utilities.readProperties import Readconfig


class Test_005_SearchCustomerbyName:
    baseURL = Readconfig.getApplicationURL()
    username = Readconfig.getUsername()
    password = Readconfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_searchCustomerbyName(self, setup):
        self.logger.info("********** Test_005_SearchCustomerby Name ************")
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
        time.sleep(5)
        self.addcus.clickonCustomermenu()
        self.logger.info("********** Starting Search customer By Name ************")
        searchcus = Searchcustomer(self.driver)
        searchcus.setFirstname("Virat")
        searchcus.setLastname("Kohli")
        searchcus.clickonSearch()
        time.sleep(5)
        status = searchcus.searchbyName("Virat Kohli")
        assert True == status
        self.driver.save_screenshot(".\\Screenshots\\test_Searchbyname.png")
        self.logger.info("********** End Search customer By Name ************")
        self.driver.close()



