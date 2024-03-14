"""
This module contains login page for volunteers,
the page object for the TL Consulting Home page.
"""

from selenium.webdriver.support.ui import WebDriverWait
from pages.locators import LoginPage
from Settings.config import bs_config, script_creds
from selenium.webdriver.support import expected_conditions as EC


class loginPage:
	URL = 'https://nswrfsuat.service-now.com/rfsembr?id=embr_login'
	
	def __init__(self, browser):
		self.browser = browser
		self.browser.maximize_window()
	
	# Interaction Methods
	def load(self):
		self.browser.get(self.URL)
	
	def enter_Creds(self, usr, pwd):
		wait = WebDriverWait(self.browser, 20)
		pwd = script_creds['candidate_user']['password']
		
		'''
		###ONLY FOR DEBUG###
		
		usr = "Angela.Melton@test.com"
		
		'''
		
		wait.until(EC.presence_of_element_located(LoginPage.EMAIL))
		if self.browser.find_element(*LoginPage.EMAIL).is_displayed() == True:
			Email_Input_Box = self.browser.find_element(*LoginPage.EMAIL)
			Email_Input_Box.send_keys(usr)
		self.browser.find_element(*LoginPage.PASSWORD).send_keys(pwd)
		self.browser.find_element(*LoginPage.LOGIN_BTN).click()
