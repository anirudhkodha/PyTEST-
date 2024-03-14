"""
This module contains service now page
"""

import time

from selenium.webdriver.common.keys import Keys
# import Alert
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from pyshadow.main import Shadow
from pages.locators import ServiceNow_BrigadeReview_Page

from pages.common_for_all_pages import Common_Functions


class serviceNow_BrigadeReview_Page(Common_Functions):
	URL = 'https://nswrfsuat.service-now.com/'
	
	def __init__(self, browser):
		self.browser = browser
	
	# Interaction Methods
	def load(self):
		self.browser.get(self.URL)
		WebDriverWait(self.browser, 7, poll_frequency=5).until(EC.visibility_of("div[data-original-title='Open Applications by Stage']"))
		WebDriverWait(self.browser, TimeoutError)
	
	def get_Iframe(self):
		self.browser.implicitly_wait(10)
		shadow0 = Shadow(self.browser)
		shadow0.set_implicit_wait(1)
		shadow0.find_element('sn-polaris-layout')
		self.browser.switch_to.frame(shadow0.find_element('iframe'))
	
	def click_Task(self, task):
		# time.sleep(10)
		self.get_Iframe()
		self.browser.find_element(*ServiceNow_BrigadeReview_Page.TAB_TASK).click()
		time.sleep(2)
		if task == "brigade":
			self.browser.find_element(*ServiceNow_BrigadeReview_Page.TASK_BRIGADEREVIEW).click()
			time.sleep(2)
			elem = self.browser.find_element(*ServiceNow_BrigadeReview_Page.email_Check)
			emailSubject = elem.text
			assert "task assigned to you" in emailSubject
		
		elif task == "health":
			self.browser.find_element(*ServiceNow_BrigadeReview_Page.TASK_HEALTHREVIEW).click()
			time.sleep(2)
			elem = self.browser.find_element(*ServiceNow_BrigadeReview_Page.email_Check)
			emailSubject = elem.text
			assert "task assigned to you" in emailSubject
		
		elif task == "district":
			self.browser.find_element(*ServiceNow_BrigadeReview_Page.TASK_DISTRICTREVIEW).click()
			time.sleep(2)
			elem = self.browser.find_element(*ServiceNow_BrigadeReview_Page.email_Check)
			emailSubject = elem.text
			assert "task assigned to you" in emailSubject
		
		elif task == "service check":
			self.browser.find_element(*ServiceNow_BrigadeReview_Page.TASK_SERVICECHECK).click()
			time.sleep(2)
			elem = self.browser.find_element(*ServiceNow_BrigadeReview_Page.email_Check)
			emailSubject = elem.text
			assert "task assigned to you" in emailSubject
		
		elif task == "special provision":
			self.browser.find_element(*ServiceNow_BrigadeReview_Page.TASK_SPECIALPROVISION).click()
			time.sleep(2)
			elem = self.browser.find_element(*ServiceNow_BrigadeReview_Page.email_Check)
			emailSubject = elem.text
			assert "task assigned to you" in emailSubject
		
		elif task == "police failed":
			self.browser.find_element(*ServiceNow_BrigadeReview_Page.TASK_POLICEFAILED).click()
		
		elif task == "reportable":
			self.browser.find_element(*ServiceNow_BrigadeReview_Page.TASK_REPORTABLE).click()
			time.sleep(2)
			elem = self.browser.find_element(*ServiceNow_BrigadeReview_Page.email_Check)
			emailSubject = elem.text
			assert "task assigned to you" in emailSubject
		
		elif task == "police check":
			self.browser.find_element(*ServiceNow_BrigadeReview_Page.TASK_POLICERESULTS).click()
		wait = WebDriverWait(self.browser, 10)
		wait.until(EC.title_contains("Task"))
		self.browser.switch_to.default_content()
	
	def click_PoliceCheck(self):
		# time.sleep(10)
		self.get_Iframe()
		self.browser.find_element(*ServiceNow_BrigadeReview_Page.TAB_POLICECHECK).click()
		wait = WebDriverWait(self.browser, 10)
		wait.until(EC.presence_of_element_located((By.XPATH, '//table[@id="x_nswr2_rfs_emembe_emembership_case.x_nswr2_rfs_emembe_police_check.u_case_number_table"]/tbody/tr')))
		self.browser.switch_to.default_content()
	
	def chk_PCStatus(self):
		self.get_Iframe()
		# el1 = self.browser.find_element(By.XPATH, '//a[contains(text(),"'+user+'")]/ancestor::tr')
		# status = el1.find_element(*self.PC_STATUS).text
		status = self.browser.find_element(*ServiceNow_BrigadeReview_Page.PC_STATUS).text
		self.browser.switch_to.default_content()
		return status
	
	def close_Task(self):
		self.get_Iframe()
		self.browser.find_element(*ServiceNow_BrigadeReview_Page.BTN_TASK_CLOSED).click()
		wait = WebDriverWait(self.browser, 10)
		wait.until(EC.alert_is_present())
		# create alert object
		alert = Alert(self.browser)
		# get alert text
		print(alert.text)
		# accept the alert
		alert.accept()
		time.sleep(2)
		self.browser.find_element(By.XPATH, "//button[@aria-label='Back']").click()
		wait.until(EC.title_contains("eMembership Case"))
		self.browser.find_element(By.XPATH, "//button[@aria-label='Back']").click()
		self.browser.refresh()
		wait.until(EC.title_contains("eMembership Case"))
		self.browser.switch_to.default_content()
	
	def close_ServiceCheckTask(self):
		self.get_Iframe()
		self.browser.find_element(*ServiceNow_BrigadeReview_Page.BTN_TASK_CLOSED).click()
		wait = WebDriverWait(self.browser, 10)
		wait.until(EC.alert_is_present())
		# create alert object
		alert = Alert(self.browser)
		# get alert text
		print(alert.text)
		# accept the alert
		alert.accept()
		self.browser.find_element(By.XPATH, "//button[@aria-label='Back']").click()
	
	def close_ServiceCheckTaskDual(self):
		
		self.get_Iframe()
		self.browser.find_element(*ServiceNow_BrigadeReview_Page.BTN_TASK_CLOSED).click()
		wait = WebDriverWait(self.browser, 10)
		wait.until(EC.alert_is_present())
		# create alert object
		alert = Alert(self.browser)
		# get alert text
		print(alert.text)
		# accept the alert
		alert.accept()
		wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@id='output_messages']/div[1]/div[1]")))
		wait.until(EC.visibility_of_element_located((By.XPATH, "//textarea[@id='sys_readonly.sn_customerservice_task.description']")))
		self.browser.find_element(By.XPATH, "//button[@aria-label='Back']").click()
	
	def click_Approver(self, approver, action):
		wait = WebDriverWait(self.browser, 20)
		self.get_Iframe()
		time.sleep(5)
		self.browser.find_element(*ServiceNow_BrigadeReview_Page.TAB_APPROVERS).click()
		self.browser.find_element(*ServiceNow_BrigadeReview_Page.BTN_SP).send_keys(approver, Keys.ENTER)
		time.sleep(5)
		self.browser.find_element(*ServiceNow_BrigadeReview_Page.state_tble).send_keys("Requested", Keys.ENTER)
		time.sleep(5)
		self.browser.find_element(*ServiceNow_BrigadeReview_Page.Srch_RES).click()
		wait.until(EC.title_contains(("Approval")))
		if action == "approval":
			self.browser.find_element(*ServiceNow_BrigadeReview_Page.BTN_APPROVED).click()
			self.browser.find_element(By.XPATH, "//button[@aria-label='Back']").click()
			wait.until(EC.title_contains("eMembership Cases"))
			self.browser.switch_to.default_content()
		elif action == "decline":
			self.browser.find_element(*ServiceNow_BrigadeReview_Page.txt_Comments).send_keys("Declining")
			self.browser.find_element(*ServiceNow_BrigadeReview_Page.btn_Post).click()
			self.browser.find_element(*ServiceNow_BrigadeReview_Page.BTN_REJECTED).click()
			self.browser.find_element(By.XPATH, "//button[@aria-label='Back']").click()
			wait.until(EC.title_contains("eMembership Cases"))
			self.browser.switch_to.default_content()
	
	def set_FormerID(self, memID):
		self.get_Iframe()
		self.browser.find_element(*ServiceNow_BrigadeReview_Page.TAB_MEMSHIPAPP).click()
		self.browser.find_element(*ServiceNow_BrigadeReview_Page.APP_TYPE).click()
		time.sleep(2)
		self.browser.execute_script(
			"document.querySelector(arguments[0],':before').click();", ServiceNow_BrigadeReview_Page.CHK_FORMERID)
		self.browser.find_element(*ServiceNow_BrigadeReview_Page.TXT_MEMID).send_keys(memID)
		self.browser.find_element(*ServiceNow_BrigadeReview_Page.BTN_UPDATE).click()
		self.browser.switch_to.default_content()
