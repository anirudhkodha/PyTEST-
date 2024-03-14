import time
from selenium import *
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from pyshadow.main import Shadow
from selenium.webdriver.support.wait import WebDriverWait
from pages.locators import SAP_LoginPage
from selenium.common.exceptions import *
from pages.common_for_all_pages import Common_Functions
from Settings.config import bs_config, script_creds


class sapQasPage(Common_Functions):
	URL = script_creds['web_pages']['sap_qas']
	
	def __init__(self, browser):
		self.browser = browser
	
	# Interaction Methods
	def load(self):
		self.browser.get(self.URL)
	
	def login_sap(self, usr, pwd):
		usr = script_creds['sap_user']['username']
		pwd = script_creds['sap_user']['password']
		self.wait_for_element_present(*SAP_LoginPage.LOGON_BOX)
		self.browser.find_element(*SAP_LoginPage.USER).send_keys(usr)
		self.browser.find_element(*SAP_LoginPage.PASS).send_keys(pwd)
		self.browser.find_element(*SAP_LoginPage.BTN_LOGON).click()
		self.wait_for_page_load(50)
	
	def sap_homepage(self):
		TItle = 'Self Service Portal'
		self.wait_for_title(title=TItle)
		assert self.browser.title == TItle
