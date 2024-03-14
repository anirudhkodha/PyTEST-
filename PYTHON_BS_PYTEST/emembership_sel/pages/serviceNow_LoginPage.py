"""
This module contains service now login page
"""
import time

# import TimeUnit as

import yaml
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.expected_conditions import any_of
from selenium.webdriver.support.ui import WebDriverWait
from pages.locators import ServiceNow_LoginPage
from Settings.config import script_creds, bs_config
from selenium.common.exceptions import NoSuchAttributeException


class serviceNow_LoginPage:
	
	def __init__(self, browser):
		assert isinstance(browser, object)
		self.browser = browser
	
	# Interaction Method
	def load(self):
		self.browser.get(self.URL)
		time.sleep(5)
	
	def is_Login_UsrPwd(self):
		self.browser.find_element(*ServiceNow_LoginPage.USERNAME)
	
	def enter_Credentials(self, usr, pwd):
		usr = script_creds['snow_user']['username']
		pwd = script_creds['snow_user']['password']
		title_condition_1 = EC.title_contains('Membership Services Dashboard')
		title_condition_2 = EC.title_contains('Emails | NSW RFS Service Now')
		
		wait = WebDriverWait(self.browser, 50)
		# self.browser.implicitly_wait(40)
		wait.until(EC.presence_of_element_located(ServiceNow_LoginPage.OKTALOGINCONTAINER))
		
		if self.browser.find_element(By.XPATH, '//h2[contains(text(),"Sign In")]'):
			
			user_field = self.browser.find_element(*ServiceNow_LoginPage.USERNAME_STANDLONE)
			user_field.clear()
			user_field.send_keys(usr)
			self.browser.find_element(*ServiceNow_LoginPage.NEXT_BTN).click()
			self.browser.find_element(*ServiceNow_LoginPage.PASSWORD_STANDALONE).send_keys(pwd)
			self.browser.find_element(*ServiceNow_LoginPage.VERIFY_BTN).click()
			
			wait.until(any_of(title_condition_1, title_condition_2))
		
		elif self.browser.find_element(By.XPATH, '//div[contains(text(),"Windows Authentication")]').is_displayed():
			self.browser.find_element(*ServiceNow_LoginPage.NOTACCT).click()
			self.browser.find_element(*ServiceNow_LoginPage.USERNAME).send_keys(usr)
			self.browser.find_element(*ServiceNow_LoginPage.PASSWORD).send_keys(pwd)
			self.browser.find_element(*ServiceNow_LoginPage.LOGIN_BTN).click()
			
			wait.until(any_of(title_condition_1, title_condition_2))
		
		
		elif self.browser.find_element(By.XPATH, '//p[contains(text(),"Please enter your corporate credentials")]').is_displayed():
			self.browser.find_element(*ServiceNow_LoginPage.USERNAME).send_keys(usr)
			self.browser.find_element(*ServiddceNow_LoginPage.PASSWORD).send_keys(pwd)
			self.browser.find_element(*ServiceNow_LoginPage.LOGIN_BTN).click()
			
			wait.until(any_of(title_condition_1, title_condition_2))
