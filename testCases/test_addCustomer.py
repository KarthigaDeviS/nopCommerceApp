import time

import pytest
from selenium.webdriver.common.by import By
from pageObjects.AddCustomerPage import AddCustomer
from pageObjects.LoginPage import Loginpage
from utilities.customLogger import LogGen
from utilities.readProperties import Readconfig
import random
import string


class Test_003_AddCustomer:
    baseURL = Readconfig.getApplicationURL()
    username = Readconfig.getUsername()
    password = Readconfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_addCustomer(self, setup):
        self.logger.info("********** Test_003_AddCustomer ************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = Loginpage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("********** Login Successful ************")
        self.logger.info("********** Starting Add customer List ************")

        self.addcus = AddCustomer(self.driver)
        self.addcus.clickonCustomer()
        time.sleep(5)
        self.addcus.clickonCustomermenu()
        self.addcus.clickonAddnew()

        self.email = random_generator() + "@gmail.com"
        self.addcus.setEmail(self.email)
        self.addcus.setPassword("test123")
        self.addcus.setFirstname("Karthiga")
        self.addcus.setLastname("S")
        self.addcus.setGender("Female")
        self.addcus.setDOB("11/25/1996")
        self.addcus.setCompanyname("abc")
        self.addcus.setCustomerrole("Guests")
        time.sleep(5)
        self.addcus.setCustomerrole("Vendors")
        self.addcus.setManagerofVendor("1")
        self.addcus.setAdmincontent("testing")
        self.addcus.clickonSave()

        self.msg = self.driver.find_element(By.TAG_NAME, "body").text

        if "customer has been added successfully." in self.msg:
            self.logger.info("********** Add customer Test Passed ************")
            assert True == True

        else:
            self.driver.save_screenshot(".\\Screenshots\\test_addcustomer.png")
            self.logger.info("********** Add customer Test Failed ************")
            assert True == False



def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))
