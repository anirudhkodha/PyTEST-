"""
This module contains candidate welcome page for volunteers
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from pages.locators import Candidate_WelcomePage
from selenium.webdriver.remote.webelement import *
from conftest import *


class candidate_WelcomePage(Common_Functions):
	URL = 'https://nswrfsuat.service-now.com/rfsembr?id=embr_login'
	
	def __init__(self, browser):
		self.browser = browser
	
	# Interaction Methods
	def load(self):
		self.browser.get(self.URL)
	
	def click_New_Cont_APP(self, btn):
		# time.sleep(5)
		self.browser.implicitly_wait(10)
		wait = WebDriverWait(self.browser, 10)
		
		## HANDLING THE POP UP FOR LOGIN +++++
		try:
			if self.browser.find_element(*Candidate_WelcomePage.pop_up).is_displayed():
				self.browser.find_element(*Candidate_WelcomePage.pop_up).send_keys(Keys.RETURN)
				self.browser.find_element(*Candidate_WelcomePage.pop_up).send_keys(Keys.RETURN)
			return True
		except Exception as e:
			print(f'Pop up not available after first login {e}')
			pass
		
		if btn == 'new':
			wait.until(EC.element_to_be_clickable(Candidate_WelcomePage.BTN_STRT_NEW_APP))
			self.browser.find_element(*Candidate_WelcomePage.BTN_STRT_NEW_APP).click()
		else:
			wait.until(EC.element_to_be_clickable(Candidate_WelcomePage.BTN_CONT_APP))
			self.browser.find_element(*Candidate_WelcomePage.BTN_CONT_APP).click()
	
	def click_New_Cont_APP_Rejoin(self, btn):
		# time.sleep(5)
		self.browser.implicitly_wait(10)
		wait = WebDriverWait(self.browser, 10)
		if btn == 'new':
			wait.until(EC.element_to_be_clickable(Candidate_WelcomePage.BTN_STRT_NEW_APP))
			self.browser.find_element(*Candidate_WelcomePage.BTN_STRT_NEW_APP).click()
		else:
			wait.until(EC.element_to_be_clickable(Candidate_WelcomePage.BTN_CONT_APP))
			self.browser.find_element(*Candidate_WelcomePage.BTN_CONT_APP).click()
	
	def verify_AppStatus(self, appRef):
		el1 = self.browser.find_element(By.XPATH, '//td[contains(text(),"' + appRef + '")]/ancestor::tr')
		status = el1.find_element(*Candidate_WelcomePage.APP_STATUS).text
		return status
