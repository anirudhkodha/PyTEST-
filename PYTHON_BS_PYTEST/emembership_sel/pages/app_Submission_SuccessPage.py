"""
This module contains application succesful submission page for volunteers
"""
import json
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from pages.locators import App_Submission_SuccessPage





class app_Submission_SuccessPage:

    URL = 'https://nswrfsuat.service-now.com/rfsembr?id=embr_login'


    def __init__(self, browser):
        self.browser = browser

        # Interaction Methods
    def load(self):
        self.browser.get(self.URL)

    def click_ViewApp(self):
        self.browser.find_element(*App_Submission_SuccessPage.BTN_VIEW_APP).click()
        wait = WebDriverWait(self.browser, 10)
        wait.until(EC.visibility_of_element_located(App_Submission_SuccessPage.APP_REF))
        ref = self.get_AppRef()
        file_name = ref + ".png"
        self.browser.save_screenshot('data/Screenshots/' + file_name)

    def app_logout(self):
        self.browser.find_element(*App_Submission_SuccessPage.logout_button).click()

    def get_AppRef(self):
        return self.browser.find_element(*App_Submission_SuccessPage.APP_REF).text

    def save_Appref_JSON(self):        
        ref = self.get_AppRef()
        file ={
            "ref": ref
        }        
        with open("data/appRef.json", "w") as outfile:
            json.dump(file, outfile)

    def verify_Success(self):
        assert self.browser.find_element(*App_Submission_SuccessPage.TXT_SUCCESS).text == "Application successfully submitted"
        
    def logout(self):
        self.browser.find_element(*App_Submission_SuccessPage.BTN_LOGOUT).click()
        wait = WebDriverWait(self.browser, 10)
        wait.until(EC.title_is(("eMBR RFS CSM Login - eMBR RFS Customer Service")))