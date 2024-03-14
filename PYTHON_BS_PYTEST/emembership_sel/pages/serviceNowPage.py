"""
This module contains service now page
"""

import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from pyshadow.main import Shadow
from selenium.webdriver.support.wait import WebDriverWait
from pages.createProfilePage import eMail
from pages.locators import ServiceNowPage
from selenium.common.exceptions import *
from pages.common_for_all_pages import Common_Functions


class serviceNowPage(Common_Functions):
	URL = 'https://nswrfsuat.service-now.com/'
	URL_EMAILS = 'https://nswrfsuat.service-now.com/sys_email_list.do'
	
	def __init__(self, browser):
		self.browser = browser
	
	# Interaction Methods
	def load(self):
		self.browser.get(self.URL)
	
	def load_child_page(self):
		self.browser.get(self.URL_EMAILS)
		self.wait_for_page_load(timeout=50)
	
	# This is used to verify the status of application
	def app_status(self, ref):
		shadow0 = Shadow(self.browser)
		self.browser.switch_to.frame(shadow0.find_element('iframe'))
		self.browser.find_element(*ServiceNowPage.filter_item).click()
		self.browser.find_element(*ServiceNowPage.cross_Button).click()
		self.browser.find_element(*ServiceNowPage.run_Button).click()
		self.browser.find_element(*ServiceNowPage.BTN_Search).send_keys(ref)
		self.browser.find_element(*ServiceNowPage.BTN_Search).send_keys(Keys.ENTER)
		time.sleep(2)
		file_name = ref + "_Applicationstatus.png"
		self.browser.save_screenshot('data/Screenshots/' + file_name)
	
	# This is used to click on All option in SNOW home page and to search for the candidate verification emails
	def click_All(self):
		# time.sleep(10)
		wait = WebDriverWait(self.browser, 60)
		# shadow0 = Shadow(self.browser)
		# shadow0.find_element('sn-polaris-layout')
		# shadow1 = Shadow(self.browser)
		# shadow1.set_implicit_wait(2)
		# shadow1.find_element('sn-polaris-header')
		# shadow2 = Shadow(self.browser)
		# shadow2.set_implicit_wait(1)
		# shadow2.find_element('#d6e462a5c3533010cbd77096e940dd8c').click()
		# shadow2.find_element('#filter').send_keys("Sent")
		# shadow2.find_element('.label').click()
		# # time.sleep(2)
		# self.browser.implicitly_wait(20)
		shadow0 = Shadow(self.browser)
		shadow0.set_implicit_wait(1)
		shadow0.find_element('sn-polaris-layout')
		self.browser.switch_to.frame(shadow0.find_element('iframe'))
		# time.sleep(100)
		self.browser.find_element(*ServiceNowPage.mail_search).send_keys(eMail)
		time.sleep(2)
		dd = Select(self.browser.find_element(*ServiceNowPage.dropdown_subject))
		dd.select_by_value("recipients")
		self.browser.find_element(*ServiceNowPage.mail_search).send_keys(Keys.ENTER)
		actions = ActionChains(self.browser)
		elem = self.browser.find_element(*ServiceNowPage.mail_Results)
		actions.context_click(elem).perform()
		self.browser.find_element(*ServiceNowPage.preview_mail).click()
		self.browser.switch_to.frame(shadow0.find_element('iframe'))
		self.browser.find_element(*ServiceNowPage.click_here).click()
		original_window = self.browser.current_window_handle
		time.sleep(10)
		for window_handle in self.browser.window_handles:
			if window_handle != original_window:
				self.browser.switch_to.window(window_handle)
				time.sleep(10)
				wait.until(EC.visibility_of_element_located(ServiceNowPage.logout_button))
				self.browser.find_element(*ServiceNowPage.logout_button).click()
	
	def navigate_AdminPortalDashboard(self, impersonation):
		time.sleep(10)
		self.browser.implicitly_wait(30)
		shadow0 = Shadow(self.browser)
		shadow0.find_element('sn-polaris-layout')
		shadow1 = Shadow(self.browser)
		shadow1.set_implicit_wait(2)
		shadow1.find_element('sn-polaris-header')
		shadow2 = Shadow(self.browser)
		shadow2.set_implicit_wait(1)
		shadow2.find_element('#d6e462a5c3533010cbd77096e940dd8c').click()
		shadow2.set_implicit_wait(2)
		if (impersonation != 'Yes'):
			shadow2.find_element('nav>div[class="polaris-header can-animate polaris-enabled"]')
		else:
			shadow2.find_element('nav>div[class="polaris-header is-impersonating can-animate polaris-enabled"]')
		shadow4 = Shadow(self.browser)
		shadow4.find_element('sn-collapsible-list')
		shadow5 = Shadow(self.browser)
		shadow5.find_element('sn-collapsible-list[class="nested-item"]')
		shadow6 = Shadow(self.browser)
		all_app = shadow6.find_element('a[aria-label="All Applications"]')
		all_app.click()
		wait = WebDriverWait(self.browser, 10)
		wait.until(EC.title_contains('eMembership Cases | NSW RFS Service Now'))
		self.browser.switch_to.default_content()
	
	# This is used to open a new tab
	def open_newTab(self):
		time.sleep(10)
		self.browser.implicitly_wait(30)
		self.browser.execute_script("window.open('about:blank', 'secondtab')")
		self.browser.switch_to.window("secondtab")
		self.browser.get('https://nswrfsuat.service-now.com/rfsembr?id=embr_login')
	
	# This function is used to verify the emails of approvals and the application submitted email
	def email_Verification(self, read_JSON, approval):
		ref = read_JSON('data/appRef.json')
		wait = WebDriverWait(self.browser, 60)
		self.browser.implicitly_wait(10)
		wait.until(EC.title_contains('eMembership Cases | NSW RFS Service Now'))
		shadow0 = Shadow(self.browser)
		shadow0.find_element('sn-polaris-layout')
		shadow1 = Shadow(self.browser)
		shadow1.set_implicit_wait(2)
		shadow1.find_element('sn-polaris-header')
		shadow2 = Shadow(self.browser)
		shadow2.set_implicit_wait(1)
		shadow2.find_element('#d6e462a5c3533010cbd77096e940dd8c').click()
		shadow2.find_element('#filter').send_keys("Sent")
		shadow2.find_element('.label').click()
		self.browser.implicitly_wait(20)
		shadow0 = Shadow(self.browser)
		shadow0.set_implicit_wait(1)
		shadow0.find_element('sn-polaris-layout')
		self.browser.switch_to.frame(shadow0.find_element('iframe'))
		if approval == "application":
			searchSubject = "We have received your RFS eMembership application " + ref["ref"]
			dd = Select(self.browser.find_element(*ServiceNowPage.dropdown_subject))
			dd.select_by_value("subject")
			self.browser.find_element(*ServiceNowPage.mail_search).send_keys(searchSubject)
			time.sleep(10)
			self.browser.find_element(*ServiceNowPage.mail_search).send_keys(Keys.ENTER)
			actions = ActionChains(self.browser)
			elem = self.browser.find_element(*ServiceNowPage.mail_Results)
			actions.context_click(elem).perform()
			self.browser.find_element(*ServiceNowPage.preview_mail).click()
			file_name = ref["ref"] + "_User" + ".png"
			self.browser.save_screenshot('data/Screenshots/' + file_name)
			self.browser.switch_to.frame(shadow0.find_element('iframe'))
			file_name = ref["ref"] + "_Email" + ".png"
			self.browser.save_screenshot('data/Screenshots/' + file_name)
			time.sleep(1)
			actions.send_keys(Keys.ESCAPE).perform()
		
		elif approval == "brigade":
			searchSubject1 = "eMembership application " + ref["ref"]
			searchSubjectFinal = searchSubject1 + ": Brigade Captain endorsement"
			dd = Select(self.browser.find_element(*ServiceNowPage.dropdown_subject))
			dd.select_by_value("subject")
			self.browser.find_element(*ServiceNowPage.txt_subjectSearch).send_keys(searchSubject1)
			self.browser.find_element(*ServiceNowPage.txt_subjectSearch).send_keys(Keys.ENTER)
			time.sleep(2)
			self.browser.find_element(*ServiceNowPage.txt_Subject).send_keys(searchSubjectFinal)
			time.sleep(8)
			self.browser.find_element(*ServiceNowPage.txt_Subject).send_keys(Keys.ENTER)
			actions = ActionChains(self.browser)
			elem = self.browser.find_element(*ServiceNowPage.mail_Results)
			actions.context_click(elem).perform()
			self.browser.find_element(*ServiceNowPage.preview_mail).click()
			self.browser.switch_to.frame(shadow0.find_element('iframe'))
			file_name = ref["ref"] + "_BrigadeEndorsement" + ".png"
			self.browser.save_screenshot('data/Screenshots/' + file_name)
			actions.send_keys(Keys.ESCAPE).perform()
		
		elif approval == "district":
			searchSubject1 = "eMembership application " + ref["ref"]
			searchSubjectFinal = searchSubject1 + ": District endorsement"
			dd = Select(self.browser.find_element(*ServiceNowPage.dropdown_subject))
			dd.select_by_value("subject")
			self.browser.find_element(*ServiceNowPage.txt_subjectSearch).send_keys(searchSubject1)
			self.browser.find_element(*ServiceNowPage.txt_subjectSearch).send_keys(Keys.ENTER)
			time.sleep(2)
			self.browser.find_element(*ServiceNowPage.txt_Subject).send_keys(searchSubjectFinal)
			time.sleep(10)
			self.browser.find_element(*ServiceNowPage.txt_Subject).send_keys(Keys.ENTER)
			actions = ActionChains(self.browser)
			elem = self.browser.find_element(*ServiceNowPage.mail_Results)
			actions.context_click(elem).perform()
			self.browser.find_element(*ServiceNowPage.preview_mail).click()
			self.browser.switch_to.frame(shadow0.find_element('iframe'))
			file_name = ref["ref"] + "_DistrictEndorsement" + ".png"
			self.browser.save_screenshot('data/Screenshots/' + file_name)
			actions.send_keys(Keys.ESCAPE).perform()
		shadow0 = Shadow(self.browser)
		shadow0.find_element('sn-polaris-layout')
		shadow1 = Shadow(self.browser)
		shadow1.set_implicit_wait(2)
		shadow1.find_element('#header-logo-image').click()
	
	def click_impersonate_User(self):
		# time.sleep(15)
		self.browser.implicitly_wait(50)
		wait = WebDriverWait(self.browser, 60)
		# self.browser.implicitly_wait(50)
		wait.until(EC.title_is("Membership Services Dashboard | ServiceNow | NSW RFS Service Now"))
		shadow0 = Shadow(self.browser)
		shadow0.set_implicit_wait(2)
		shadow0.find_element('sn-polaris-layout')
		shadow1 = Shadow(self.browser)
		shadow1.find_element('sn-polaris-header')
		shadow2 = Shadow(self.browser)
		shadow2.find_element('div[class="header-avatar-button contextual-zone-button user-menu"').click()
		shadow2.set_implicit_wait(1)
		impersonate_User = shadow2.find_element('button[class="user-menu-button impersonateUser keyboard-navigatable polaris-enabled"]>div')
		impersonate_User.click()
	
	def impersonate_user(self, email):
		shadow0 = Shadow(self.browser)
		shadow0.set_implicit_wait(1)
		shadow0.find_element('sn-polaris-layout')
		shadow1 = Shadow(self.browser)
		shadow0.set_implicit_wait(1)
		shadow1.find_element('sn-impersonation')
		shadow2 = Shadow(self.browser)
		shadow2.find_element('now-typeahead[placeholder="Search for a user"]')
		shadow3 = Shadow(self.browser)
		search_usr = shadow3.find_element('input[class="now-typeahead-native-input"]')
		search_usr.clear()
		search_usr.click()
		search_usr.send_keys(email)
		self.browser.switch_to.default_content()
		self.browser.find_element(By.CSS_SELECTOR, 'seismic-hoist')
		shadow1_1 = Shadow(self.browser)
		shadow1_1.set_implicit_wait(1)
		shadow1_1.find_element('div[class="now-dropdown-list"]>div>div[role="option"]').click()
		shadow2.find_element('now-modal')
		shadow1_2 = Shadow(self.browser)
		shadow1_2.find_element('now-button:nth-child(2)')
		shadow1_3 = Shadow(self.browser)
		shadow1_3.find_element('button[class="now-button -primary -md"]').click()
		self.browser.switch_to.default_content()
		wait = WebDriverWait(self.browser, 10)
		wait.until(EC.title_contains('ServiceNow | NSW RFS Service Now'))
	
	def click_overviewDB(self):
		shadow0 = Shadow(self.browser)
		shadow0.set_implicit_wait(1)
		shadow0.find_element('sn-polaris-layout')
		self.browser.switch_to.frame(shadow0.find_element('iframe'))
		self.browser.find_element(*ServiceNowPage.BTN_DB_OVERVIEW).click()
		self.browser.switch_to.default_content()
	
	def click_Unimpersonate_User(self):
		wait = WebDriverWait(self.browser, 50)
		self.browser.implicitly_wait(10)
		# wait.until(EC.title_is("Membership Services Dashboard | ServiceNow | NSW RFS Service Now"))
		shadow0 = Shadow(self.browser)
		shadow0.set_implicit_wait(1)
		shadow0.find_element('sn-polaris-layout')
		shadow1 = Shadow(self.browser)
		shadow1.find_element('sn-polaris-header')
		shadow2 = Shadow(self.browser)
		shadow2.find_element('now-avatar[class="is-impersonating"]').click()
		shadow2.set_implicit_wait(1)
		unimpersonate_User = shadow2.find_element('button[class="user-menu-button unimpersonate keyboard-navigatable polaris-enabled"]>div')
		unimpersonate_User.click()
		wait = WebDriverWait(self.browser, 10)
		# wait.until(EC.title_is("Membership Services Dashboard | ServiceNow | NSW RFS Service Now"))
		wait.until(EC.title_contains('Membership Services Dashboard'))
	
	def search_AppRef(self, ref):
		shadow0 = Shadow(self.browser)
		shadow0.set_implicit_wait(1)
		shadow0.find_element('sn-polaris-layout')
		self.browser.switch_to.frame(shadow0.find_element('iframe'))
		self.browser.find_element(*ServiceNowPage.BTN_Search).send_keys(ref)
		self.browser.find_element(*ServiceNowPage.BTN_Search).send_keys(Keys.ENTER)
		shadow0.set_implicit_wait(2)
		self.browser.find_element(*ServiceNowPage.SEARCH_RES).click()
		shadow0.set_implicit_wait(1)
		self.browser.switch_to.default_content()
	
	def logout_User(self):
		self.browser.find_element(*ServiceNowPage.BTN_Logout).click()
	
	def click_Logo(self):
		self.browser.find_element(*ServiceNowPage.nsw_Logo).click()
