import time
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.common.by import By


class AddCustomer:
    lnkCustomers_xpath = "//a[@href='#']//p[contains(text(),'Customers')]"
    lnkCustomers_menuitem_xpath = "//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]"
    lnkAddcus_xpath = "//a[@class='btn btn-primary']"
    txtEmail_xpath = "//input[@id = 'Email']"
    txtPassword_id = "Password"
    txtFirstname_id = "FirstName"
    txtLastname_id = "LastName"
    rdbtn_GenderMale_id = "Gender_Male"
    rdbtn_GenderFemale_id = "Gender_Female"
    txt_DOB_id = "DateOfBirth"
    txt_Companyname_id = "Company"
    chk_istax_id = "IsTaxExempt"
    lst_Customerrole_xpath = "// input[ @ aria-describedby = 'SelectedCustomerRoleIds_taglist']"
    lst_Customerrole_Admin_xpath = "//li[contains(text(),'Administrators')]"
    lst_Customerrole_Forum_xpath = "//li[contains(text(),'Forum Moderators')]"
    lst_Customerrole_Guests_xpath = "//li[contains(text(),'Guests')]"
    lst_Customerrole_Registered_xpath = "//li[contains(text(),'Registered')]"
    lst_Customerrole_Vendors_xpath = "//li[contains(text(),'Vendors')]"
    lst_mgrofVendor_xpath = "//select[@id='VendorId']"
    chk_active_id = "Active"
    txt_Admincmt_id = "AdminComment"
    btn_save_xpath = "//*[@name='save']"


    def __init__(self, driver):
        self.driver = driver

    def clickonCustomer(self):
        self.driver.find_element(By.XPATH, self.lnkCustomers_xpath).click()

    def clickonCustomermenu(self):
        self.driver.find_element(By.XPATH, self.lnkCustomers_menuitem_xpath).click()

    def clickonAddnew(self):
        self.driver.find_element(By.XPATH, self.lnkAddcus_xpath).click()

    def setEmail(self, email):
        self.driver.find_element(By.XPATH, self.txtEmail_xpath).send_keys(email)

    def setPassword(self, password):
        self.driver.find_element(By.ID, self.txtPassword_id).send_keys(password)

    def setFirstname(self, firstname):
        self.driver.find_element(By.ID, self.txtFirstname_id).send_keys(firstname)

    def setLastname(self, lastname):
        self.driver.find_element(By.ID, self.txtLastname_id).send_keys(lastname)

    def setGender(self, gender):
        if gender == "Male":
            self.driver.find_element(By.ID, self.rdbtn_GenderMale_id).click()
        elif gender == "Female":
            self.driver.find_element(By.ID, self.rdbtn_GenderFemale_id).click()
        else:
            self.driver.find_element(By.ID, self.rdbtn_GenderMale_id).click()

    def setDOB(self, dob):
        self.driver.find_element(By.ID, self.txt_DOB_id).send_keys(dob)

    def setCompanyname(self, nameofcompany):
        self.driver.find_element(By.ID, self.txt_Companyname_id).send_keys(nameofcompany)

    def setTaxExempt(self):
        self.driver.find_element(By.ID, self.chk_istax_id).click()

    def setCustomerrole(self, role):
        self.driver.find_element(By.XPATH, self.lst_Customerrole_xpath).click()
        time.sleep(5)
        #self.listitem = self.driver.find_element(By.XPATH, self.lst_Customerrole_Registered_xpath)
        #drop.select_by_value(val)
        if role == "Registered":
            self.listitem = self.driver.find_element(By.XPATH, self.lst_Customerrole_Registered_xpath)
        elif role == "Administrators":
            self.listitem = self.driver.find_element(By.XPATH, self.lst_Customerrole_Admin_xpath)
        elif role == "Guests":
            self.driver.find_element(By.XPATH, "//span[@title='delete']").click()
            self.driver.find_element(By.XPATH, self.lst_Customerrole_xpath).click()
            self.listitem = self.driver.find_element(By.XPATH, self.lst_Customerrole_Guests_xpath)
        elif role == "Registered":
            self.listitem = self.driver.find_element(By.XPATH, self.lst_Customerrole_Registered_xpath)
        elif role == "Forum Moderators":
            self.listitem = self.driver.find_element(By.XPATH, self.lst_Customerrole_Forum_xpath)
        elif role == "Vendors":
            self.listitem = self.driver.find_element(By.XPATH, self.lst_Customerrole_Vendors_xpath)
        else:
            self.listitem = self.driver.find_element(By.XPATH, self.lst_Customerrole_Guests_xpath)

        time.sleep(10)
        self.driver.execute_script("arguments[0].click();", self.listitem)

    def setManagerofVendor(self, val):
        drp = Select(self.driver.find_element(By.XPATH, self.lst_mgrofVendor_xpath))
        drp.select_by_value(val)

    def setAdmincontent(self, content):
        self.driver.find_element(By.ID, self.txt_Admincmt_id).send_keys(content)

    def clickonSave(self):
        self.driver.find_element(By.XPATH, self.btn_save_xpath).click()








