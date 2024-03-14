"""
This module contains create profile page
"""
from random import random
import string
import random
import json
from Settings.config import bs_config, script_creds
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import *
from faker.providers.person.en import Provider
from pages.locators import CreateProfilePage
from pages.common_for_all_pages import Common_Functions

# first_names = list(set(Provider.first_names))

from faker import Faker

faker = Faker()
fName = faker.first_name()
lName = faker.last_name()
first_names = list(set(Provider.first_names))

eMail = fName + "." + lName + "@test.com"


class createProfilePage(Common_Functions):
	URL = 'https://nswrfsuat.service-now.com/rfsembr?id=embr_rfs_role_explorer'
	RADIO_MEM_NO = (By.CSS_SELECTOR, 'input[id="member-no"]')
	
	def generate_rand_text(self, length):
		letters = string.ascii_letters + string.digits + string.punctuation + string.whitespace
		rand_text = ''.join(random.choice(letters) for _ in range(length))
		return rand_text
	
	def __init__(self, browser):
		self.browser = browser
	
	# Interaction Methods
	def load(self):
		self.browser.get(self.URL)
	
	def click_Option(self, option):
		
		if option == "ApplyToVolunteer":
			self.wait_for_element_click(*CreateProfilePage.BTN_APPLY_TO_VOLUNTEER)
			elem = self.browser.find_element(*CreateProfilePage.BTN_APPLY_TO_VOLUNTEER).click()
			# elem.click()
			self.wait_for_element_visible(*CreateProfilePage.BTN_CREATE_PROFILE)
		elif option == "HowToApply":
			self.browser.find_element(*CreateProfilePage.BTN_HOW_TO_APPLY).click()
			self.wait_for_title("eMBR RFS Triage Page - eMBR RFS Customer Service")
			assert self.browser.find_element(By.XPATH, '//header//h1').text == "How to join as a volunteer"
	
	def click_CreateOrLogin(self, option):
		if option == "CreateProfile":
			self.browser.find_element(*CreateProfilePage.BTN_CREATE_PROFILE).click()
			wait = WebDriverWait(self.browser, 10)
			wait.until(EC.visibility_of_element_located(CreateProfilePage.HDR_CREATEPROFILE))
		elif option == "Login":
			self.browser.find_element(*CreateProfilePage.BTN_LOGIN).click()
			wait = WebDriverWait(self.browser, 10)
			wait.until(EC.visibility_of_element_located(*CreateProfilePage.HDR_LOGIN))
	
	def save_user_details(self):
		Username = eMail
		Firstname = fName
		Lastname = lName
		
		with open("data/newProfileDetails.json", "r") as file:
			data = json.load(file)
			data["EMAIL"] = Username
			data["FNAME"] = Firstname
			data["LNAME"] = Lastname
			newdata = json.dumps(data)
		
		with open("data/newProfileDetails.json", "w") as file:
			file.write(newdata)
	
	def fill_ApplicantDetails(self, *args):
		self.wait_for_page_load(timeout=50)
		self.browser.find_element(*CreateProfilePage.TXT_FIRSTNAME).send_keys(fName)
		self.browser.find_element(*CreateProfilePage.TXT_PREFFEREDNAME).send_keys(args[1])
		self.browser.find_element(*CreateProfilePage.TXT_LASTNAME).send_keys(lName)
		Member_email_field = self.browser.find_element(*CreateProfilePage.TXT_EMAIL)
		EmaiL = Member_email_field.send_keys(eMail)
		self.browser.find_element(*CreateProfilePage.TXT_MOBILE).send_keys(args[4])
		self.browser.find_element(*CreateProfilePage.TXT_DOB).send_keys(args[5])
		self.browser.find_element(*CreateProfilePage.TXT_PASSWORD).send_keys(args[6])
		self.browser.find_element(*CreateProfilePage.TXT_CONFIRM_PASSWORD).send_keys(args[6])
	
	def sel_PreviousMembership(self, *args):
		if (args[0] != 'Yes'):
			self.browser.execute_script(
				"document.querySelector(arguments[0],':before').click();", CreateProfilePage.RADIO_MEM_NO)
		else:
			self.browser.find_element(*CreateProfilePage.RADIO_MEM_YES).click()
			wait = WebDriverWait(self.browser, 10)
			wait.until(EC.visibility_of_element_located(CreateProfilePage.TXT_MEMID))
			self.browser.find_element(*CreateProfilePage.TXT_MEMID).send_keys(args[1])
			self.browser.find_element(*CreateProfilePage.TXT_ADD_MEMID).send_keys(args[2])
			self.browser.find_element(*CreateProfilePage.TXT_PREV_BRIGADE).send_keys(args[3])
	
	def accept_Privacy(self):
		self.browser.execute_script(
			"document.querySelector(arguments[0],':before').click();", CreateProfilePage.CHKBOX_AGREE)
		wait = WebDriverWait(self.browser, 10)
		wait.until(EC.element_to_be_clickable(CreateProfilePage.BTN_CREATE_AND_START))
	
	def click_CreateProfile(self):
		wait = WebDriverWait(self.browser, 20)
		while True:
			try:
				# Attempt to click the element if it's already on the screen
				Create_Start = self.browser.find_element(*CreateProfilePage.BTN_CREATE_AND_START)
				if Create_Start.is_displayed():
					Create_Start.click()
					break  # Exit the loop once clicked
			except NoSuchElementException:
				pass  # Element not found yet, continue scrolling
			
			# Scroll down to load more content
			self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
	
	def logout_logi(self, usr, pwd):
		# self.browser.find_element(*self.logout_button).click()
		
		wait = WebDriverWait(self.browser, 20)
		self.browser.find_element(*CreateProfilePage.EMAIL).send_keys(usr)
		self.browser.find_element(*CreateProfilePage.PASSWORD).send_keys(script_creds['snow_user']['password'])
		self.browser.find_element(*CreateProfilePage.LOGIN_BTN).click()
		wait.until(EC.title_is("eMBR RFS Welcome Page - eMBR RFS Customer Service"))
	
	def logout_User(self):
		self.browser.find_element(*CreateProfilePage.BTN_Logout).click()
	
	def email_Verification(self):
		assert self.browser.find_element(*CreateProfilePage.Confirm_mssg).text == "Please check your email for RFS Email Verification that has now been sent."
