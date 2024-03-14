"""
This module contains service now login page
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from pyshadow.main import Shadow
from pages.locators import Db_OverviewPage

"""
This module contains dashboard overview page
"""
class db_OverviewPage: 
    URL = 'https://nswrfsuat.service-now.com/'  


    def __init__(self, browser):
        self.browser = browser

      # Interaction Methods
    def load(self):
        self.browser.get(self.URL)
    
    def verify_DB(self, db):  
        shadow0 = Shadow(self.browser)
        shadow0.set_implicit_wait(1)
        shadow0.find_element('sn-polaris-layout') 
        self.browser.switch_to.frame(shadow0.find_element('iframe'))
        wait = WebDriverWait(self.browser, 10)        
        wait.until(EC.presence_of_element_located(Db_OverviewPage.DASHBOARD_HDR))
        self.browser.find_element(By.XPATH,'//div[text()="'+db+'"]').click()
        db_Text = self.browser.find_element(By.XPATH, '//div[@id="navbar"]/div[1]/span').text
        assert db_Text == db
        self.browser.switch_to.default_content()


        