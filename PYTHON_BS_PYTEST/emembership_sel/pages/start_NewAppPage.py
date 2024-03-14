"""
This module contains start new application page for volunteers
"""
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from pages.locators import Start_NewAppPage
from pages.common_for_all_pages import Common_Functions


class start_NewAppPage(Common_Functions):
	URL = 'https://nswrfsuat.service-now.com/rfsembr?id=embr_login'
	
	def __init__(self, browser):
		self.browser = browser
	
	# Interaction Methods
	def load(self):
		self.browser.get(self.URL)
	
	def verify_AppCards(self, usr_Cat):
		if usr_Cat == 'under16':
			cards = self.browser.find_elements(*Start_NewAppPage.APP_CARDS)
			assert len(cards) == 1
			print(cards[0].text)
			assert cards[0].text == 'Apply to be a junior member'
		elif usr_Cat == '16to17':
			cards = self.browser.find_elements(*Start_NewAppPage.APP_CARDS)
			assert len(cards) == 2
			assert cards[0].text == 'Apply to be a junior member'
			assert cards[1].text == 'Apply to be an ordinary member (under 18)'
		elif usr_Cat == 'adult':
			cards = self.browser.find_elements(*Start_NewAppPage.APP_CARDS)
			assert len(cards) == 1
			print(cards[0].text)
			assert cards[0].text == 'Apply to be a volunteer'
		elif usr_Cat == 'adultRejoin':
			cards = self.browser.find_elements(*Start_NewAppPage.APP_CARDS)
			assert len(cards) == 2
			assert cards[0].text == 'Apply for dual membership'
			assert cards[1].text == 'Transfer to another brigade'
	
	def click_Apply_Card(self, usr_cat):
		if usr_cat == 'U16':
			self.browser.find_element(*Start_NewAppPage.CARD_APPLY_VOLUNTEER).click()
			self.wait_for_page_load(timeout=50)
			
			wait = WebDriverWait(self.browser, 20)
			wait.until(EC.title_is('Apply to be a junior member - eMBR RFS Customer Service'))
			assert self.browser.title == 'Apply to be a junior member - eMBR RFS Customer Service'
			self.browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
		
		elif usr_cat == 'U17':
			self.browser.find_element(*Start_NewAppPage.CARD_APPLY_VOLUNTEER).click()
			self.wait_for_page_load(timeout=50)
			
			wait = WebDriverWait(self.browser, 20)
			wait.until(EC.title_is('Apply to be an ordinary member (under 18) - eMBR RFS Customer Service'))
			assert self.browser.title == 'Apply to be an ordinary member (under 18) - eMBR RFS Customer Service'
			self.browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
		
		elif usr_cat == "Adult":
			self.browser.find_element(*Start_NewAppPage.CARD_APPLY_VOLUNTEER).click()
			self.wait_for_page_load(timeout=50)
			
			wait = WebDriverWait(self.browser, 20)
			wait.until(EC.title_is('Apply to be a volunteer - eMBR RFS Customer Service'))
			assert self.browser.title == 'Apply to be a volunteer - eMBR RFS Customer Service'
			self.browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
	
	def click_Apply_Dual(self):
		# if argv == "Dual":
		self.browser.find_element(*Start_NewAppPage.CARD_APPLY_VOLUNTEER).click()
		wait = WebDriverWait(self.browser, 0)
		wait.until(EC.title_is('Apply for dual membership - eMBR RFS Customer Service'))
		self.browser.execute_script("window.scrollTo(0,document.body.scrollHeight);")
	
	def click_Apply_Transfer(self):
		self.browser.find_element(*Start_NewAppPage.CARD_APPLY_TRANSFER).click()
		wait = WebDriverWait(self.browser, 10)
		wait.until(EC.title_is('Transfer to another brigade - eMBR RFS Customer Service'))
		self.browser.execute_script("window.scrollTo(0,document.body.scrollHeight);")
	
	def click_Junior_Apply_Card(self, usr_cat):
		if usr_cat == 'U16':
			self.browser.find_element(*Start_NewAppPage.CARD_APPLY_VOLUNTEER).click()
			wait = WebDriverWait(self.browser, 10)
			wait.until(EC.title_is('Apply to be a junior member - eMBR RFS Customer Service'))
			self.browser.execute_script("window.scrollTo(0,document.body.scrollHeight);")
		elif usr_cat == 'U17':
			self.browser.find_element(*Start_NewAppPage.CARD_U17_ORD).click()
			wait = WebDriverWait(self.browser, 10)
			wait.until(EC.title_is('AApply to be an ordinary member (under 18) - eMBR RFS Customer Service'))
			self.browser.execute_script("window.scrollTo(0,document.body.scrollHeight);")
	
	def click_Transfer_card(self):
		self.browser.find_element(*Start_NewAppPage.CARD_APPLY_VOLUNTEER).click()
		wait = WebDriverWait(self.browser, 10)
		wait.until(EC.title_is('Transfer to another brigade - eMBR RFS Customer Service'))
		self.browser.execute_script("window.scrollTo(0,document.body.scrollHeight);")
