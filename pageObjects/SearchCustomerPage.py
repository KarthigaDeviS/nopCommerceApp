import time
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.common.by import By

class Searchcustomer:
    txtEmail_id = "SearchEmail"
    txtFirstname_id = "SearchFirstName"
    txtLastname_id = "SearchLastName"
    btnSearch_id = "search-customers"
    #tblsearch_xpath = ""
    table_xpath ="//table[@id = 'customers-grid']"
    tblrows_xpath = "//table[@id = 'customers-grid']/tbody/tr"
    tblcol_xpath = "//table[@id = 'customers-grid']/tbody/tr/td"

    def __init__(self, driver):
        self.driver = driver

    def setEmail(self, email):
        self.driver.find_element(By.ID, self.txtEmail_id).clear()
        self.driver.find_element(By.ID, self.txtEmail_id).send_keys(email)

    def setFirstname(self, firstname):
        self.driver.find_element(By.ID, self.txtFirstname_id).clear()
        self.driver.find_element(By.ID, self.txtFirstname_id).send_keys(firstname)

    def setLastname(self, lastname):
        self.driver.find_element(By.ID, self.txtLastname_id).clear()
        self.driver.find_element(By.ID, self.txtLastname_id).send_keys(lastname)

    def clickonSearch(self):
        self.driver.find_element(By.ID, self.btnSearch_id).click()

    def getnoofRows(self):
        return len(self.driver.find_elements(By.XPATH, self.tblrows_xpath))

    def getnoofColums(self):
        return len(self.driver.find_elements(By.XPATH, self.tblcol_xpath))

    def searchbyEmail(self, email):
        flag = False
        for r in range(1, self.getnoofRows()+1):
            table = self.driver.find_element(By.XPATH, self.table_xpath)
            emailid = table.find_element(By.XPATH,"//table[@id = 'customers-grid']/tbody/tr["+str(r)+"]/td[2]").text
            if emailid == email:
                flag = True
                break
        return flag

    def searchbyName(self, Name):
        flag = False
        for r in range(1, self.getnoofRows() + 1):
            table = self.driver.find_element(By.XPATH, self.table_xpath)
            name = table.find_element(By.XPATH, "//table[@id = 'customers-grid']/tbody/tr[" + str(r) + "]/td[3]").text
            if name == Name:
                flag = True
                break
        return flag



