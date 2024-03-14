"""
This module contains Apply to be a volunteer page for volunteers
"""
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from pages.locators import Apply_VolunteerPage
from pages.common_for_all_pages import Common_Functions
from selenium.common.exceptions import *


class apply_VolunteerPage(Common_Functions):
	URL = 'https://nswrfsuat.service-now.com/rfsembr?id=embr_login'
	
	def __init__(self, browser):
		self.browser = browser
	
	# Interaction Methods
	def load(self):
		self.browser.get(self.URL)
	
	def click_Continue(self):
		self.wait_for_page_load(timeout=20)
		while True:
			try:
				# Attempt to click the element if it's already on the screen
				Continue = self.browser.find_element(*Apply_VolunteerPage.BTN_CONT)
				if Continue.is_displayed():
					Continue.click()
					break  # Exit the loop once clicked
			except NoSuchElementException:
				pass  # Element not found yet, continue scrolling
			
			# Scroll down to load more content
			self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
	
	def select_VonteerOption(self, option):
		self.browser.execute_script("window.scrollTo(0,document.body.scrollHeight);")
		if option == "firefighting":
			self.browser.find_element(*Apply_VolunteerPage.RADIO_FIREFIGHT).click()
		elif option == "operational support":
			self.browser.find_element(*Apply_VolunteerPage.RADIO_OPSUP).click()
		elif option == "community support":
			self.browser.find_element(*Apply_VolunteerPage.RADIO_COMSUP).click()
		elif option == "CFU":
			self.browser.find_element(*Apply_VolunteerPage.RADIO_CFU_YES).click()
			time.sleep(1)
			self.browser.find_element(*Apply_VolunteerPage.MODAL_DIALOG).click()
		else:
			self.browser.find_element(*Apply_VolunteerPage.RADIO_BRIGADEAD).click()
	
	def select_OpSupport(self):
		self.browser.find_element(*Apply_VolunteerPage.RADIO_OPSUP).click()
	
	def select_ComSupport(self):
		self.browser.find_element(*Apply_VolunteerPage.RADIO_COMSUP).click()
	
	def select_CFU(self, yn):
		if yn == 'Yes':
			self.browser.execute_script(
				"document.querySelector(arguments[0],':before').click();", Apply_VolunteerPage.RADIO_CFU_YES)
			time.sleep(1)
			self.browser.find_element(*Apply_VolunteerPage.MODAL_DIALOG).click()
		else:
			None
	
	def select_PrevExp_FF(self, yn):
		if yn == 'Yes':
			self.browser.execute_script(
				"document.querySelector(arguments[0],':before').click();", Apply_VolunteerPage.RADIO_PREVEXP_YES)
		else:
			self.browser.execute_script(
				"document.querySelector(arguments[0],':before').click();", Apply_VolunteerPage.RADIO_PREVEXP_YES)
	
	def saveAndCont(self, i):
		while True:
			try:
				saveNCont = self.browser.find_elements(*Apply_VolunteerPage.BTNS_SAVEANDCONT)
				element = saveNCont[i]
				WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable(element))
				element.click()
				break
			except Exception as e:
				print(f"Click attempt failed: {e}")
				pass
			
			self.browser.execute_script("arguments[0].scrollIntoView(true);", element)
	
	def Juncontinue(self):
		self.browser.find_element(*Apply_VolunteerPage.BTN_JUN_CONTINUE).click()
	
	def select_LocalBrigade(self, brigade):
		wait = WebDriverWait(self.browser, 20)
		wait.until(EC.element_to_be_clickable(Apply_VolunteerPage.SEL_LOCAL_BRIG))
		self.browser.execute_script(
			"document.querySelector(arguments[0],':before').click();", Apply_VolunteerPage.SEL_LOCAL_BRIG)
		self.browser.find_element(*Apply_VolunteerPage.SEL_LOCAL_BRIG).click()
		wait.until(EC.visibility_of_element_located(Apply_VolunteerPage.DD_LOCAL_BRIG))
		self.browser.find_element(*Apply_VolunteerPage.SEARCH_LOCAL_BRIG).send_keys(brigade)
		wait.until(EC.element_to_be_clickable(Apply_VolunteerPage.Adaminaby))
		self.browser.find_element(*Apply_VolunteerPage.Adaminaby).click()
		Barigade_Address = self.browser.find_element(*Apply_VolunteerPage.LOCAL_BRIG_ADD)
	
	def select_RFSA(self, yn):
		if yn == 'Yes':
			self.browser.execute_script(
				"document.querySelector(arguments[0],':before').click();", Apply_VolunteerPage.RADIO_RFSA_YES)
		else:
			self.browser.execute_script(
				"document.querySelector(arguments[0],':before').click();", Apply_VolunteerPage.RADIO_RFSA_NO)
	
	def select_RoleAgree(self, yn):
		if yn == 'No':
			self.browser.execute_script(
				"document.querySelector(arguments[0],':before').click();", Apply_VolunteerPage.RADIO_ROLEAGREE_NO)
		else:
			self.browser.execute_script(
				"document.querySelector(arguments[0],':before').click();", Apply_VolunteerPage.RADIO_ROLEAGREE_YES)
	
	def check_Exists(self, role):
		if role == "firefighting" or role == "community" or role == "operational" or role == "CFU":
			# self.browser.find_element(*self.RADIO_FFChallenge_Yes).click()
			HS = self.browser.find_element(*Apply_VolunteerPage.HEALTH_SAFETY_DD)
			assert HS is not None
	
	def check_Junior_Role(self):
		roleOption = self.browser.find_element(*Apply_VolunteerPage.BRIGADE_OPTION)
		assert roleOption is not None
	
	def check_Junior_HS(self):
		healthSec = self.browser.find_element(*Apply_VolunteerPage.HEALTH_SAFETY_DD)
		assert healthSec is not None
	
	def check_Junior_Guardian(self):
		guardianSec = self.browser.find_element(*Apply_VolunteerPage.GUARDIAN_SECTION)
		assert guardianSec is not None
	
	def select_Challenge(self, yn, role):
		if role == "firefighting" and yn == 'Yes':
			self.browser.execute_script(
				"document.querySelector(arguments[0],':before').click();", Apply_VolunteerPage.RADIO_FFChallenge_Yes)
		elif role == "firefighting" and yn == 'No':
			# self.browser.find_element(*self.RADIO_FFChalenege_N0).click()
			self.browser.execute_script(
				"document.querySelector(arguments[0],':before').click();", Apply_VolunteerPage.RADIO_FFChallenge_N0)
		elif role == "community" and yn == 'Yes':
			self.browser.execute_script(
				"document.querySelector(arguments[0],':before').click();", Apply_VolunteerPage.RADIO_CSChallenge_Yes)
		elif role == "community" and yn == 'No':
			self.browser.execute_script(
				"document.querySelector(arguments[0],':before').click();", Apply_VolunteerPage.RADIO_CSChallenge_No)
		elif role == "operational" and yn == 'Yes':
			self.browser.execute_script(
				"document.querySelector(arguments[0],':before').click();", Apply_VolunteerPage.RADIO_OPSChallenge_Yes)
		elif role == "operational" and yn == 'No':
			self.browser.execute_script(
				"document.querySelector(arguments[0],':before').click();", Apply_VolunteerPage.RADIO_OPSChallenge_No)
		elif role == "admin" and yn == 'Yes':
			self.browser.execute_script(
				"document.querySelector(arguments[0],':before').click();", Apply_VolunteerPage.RADIO_CSChallenge_Yes)
		elif role == "admin" and yn == 'No':
			self.browser.execute_script(
				"document.querySelector(arguments[0],':before').click();", Apply_VolunteerPage.RADIO_CSChallenge_No)
		elif role != "Community" or "firefighting":
			None
	
	def select_Maint_Jun(self, yn):
		if yn == 'Yes':
			self.browser.find_element(*Apply_VolunteerPage.RADIO_MAINT_JUN_YES).click()
		else:
			self.browser.find_element(*Apply_VolunteerPage.RADIO_MAINT_JUN_No).click()
	
	def select_Diabetes(self, yn):
		wait = WebDriverWait(self.browser, 10)
		wait.until(EC.visibility_of_element_located(((By.XPATH, "//span[contains(text(),'Do you suffer from diabetes that requires injectio')]"))))
		if yn == 'Yes':
			self.browser.find_element(*Apply_VolunteerPage.RADIO_DIABETES_YES).click()
		else:
			self.browser.find_element(*Apply_VolunteerPage.RADIO_DIABETES_NO).click()
	
	def select_OtherMedCondJun(self, yn):
		wait = WebDriverWait(self.browser, 10)
		if yn == 'Yes':
			wait.until(EC.element_to_be_clickable((self.browser.find_element(*Apply_VolunteerPage.RADIO_OTHERCOND_YES_JUN)).click()))
		else:
			self.browser.find_element(*Apply_VolunteerPage.RADIO_OTHERCOND_NO_JUN).click()
	
	def select_Stroke(self, yn):
		if yn == 'Yes':
			self.browser.find_element(*Apply_VolunteerPage.RADIO_HRTCOND_YES).click()
		else:
			self.browser.find_element(*Apply_VolunteerPage.RADIO_HRTCOND_NO).click()
	
	def select_BloodThinning(self, yn):
		if yn == 'Yes':
			self.browser.find_element(*Apply_VolunteerPage.RADIO_BLOODTHIN_YES).click()
		else:
			self.browser.find_element(*Apply_VolunteerPage.RADIO_BLOODTHIN_NO).click()
	
	def select_ReleiveMed(self, yn):
		if yn == 'Yes':
			self.browser.find_element(*Apply_VolunteerPage.RADIO_MEDVENTOLIN_YES).click()
		else:
			self.browser.find_element(*Apply_VolunteerPage.RADIO_MEDVENTOLIN_NO).click()
	
	def select_Seizure(self, yn):
		if yn == 'Yes':
			self.browser.find_element(*Apply_VolunteerPage.RADIO_MEDSEIZURE_YES).click()
		else:
			self.browser.find_element(*Apply_VolunteerPage.RADIO_MEDSEIZURE_NO).click()
	
	def select_OtherMedCond(self, yn, role):
		wait = WebDriverWait(self.browser, 10)
		if role == "firefirgting" and yn == 'Yes':
			self.browser.find_element(*Apply_VolunteerPage.RADIO_OTHRCOND_YES).click()
		elif role == "firefirgting" and yn == 'No':
			self.browser.execute_script(
				"document.querySelector(arguments[0],':before').click();", Apply_VolunteerPage.RADIO_OTHRCOND_NO)
			# self.browser.find_element(*self.RADIO_OTHRCOND_NO).click()
		elif role == "community" and yn == 'Yes':
			self.browser.execute_script(
				"document.querySelector(arguments[0],':before').click();", Apply_VolunteerPage.RADIO_CSOTHER_YES)
		elif role == "community" and yn == 'No':
			self.browser.execute_script(
				"document.querySelector(arguments[0],':before').click();", Apply_VolunteerPage.RADIO_CSOTHER_NO)
		elif role == "operational" and yn == 'Yes':
			self.browser.execute_script(
				"document.querySelector(arguments[0],':before').click();", Apply_VolunteerPage.RADIO_OPSOTHER_YES)
		elif role == "operational" and yn == 'No':
			self.browser.execute_script(
				"document.querySelector(arguments[0],':before').click();", Apply_VolunteerPage.RADIO_OPSOTHER_NO)
		elif role == "admin" and yn == 'Yes':
			self.browser.execute_script(
				"document.querySelector(arguments[0],':before').click();", Apply_VolunteerPage.RADIO_ADMINOTHER_Yes)
		elif role == "admin" and yn == 'No':
			self.browser.execute_script(
				"document.querySelector(arguments[0],':before').click();", Apply_VolunteerPage.RADIO_ADMINOTHER_NO)
		
		elif role != "Community" or "firefighting":
			None
	
	def select_Psychiatric(self, yn):
		if yn == 'Yes':
			self.browser.find_element(*Apply_VolunteerPage.RADIO_PSYCHIATRIC_YES).click()
		else:
			self.browser.find_element(*Apply_VolunteerPage.RADIO_PSYCHIATRIC_NO).click()
	
	def select_COVID(self, *argv):
		wait = WebDriverWait(self.browser, 10)
		if argv[0] == 'Yes':
			self.browser.execute_script(
				"document.querySelector(arguments[0],':before').click();", Apply_VolunteerPage.RADIO_COVIDVAC_YES)
			wait.until(EC.visibility_of_element_located(Apply_VolunteerPage.LAB_COVIDVAC))
			label = self.browser.find_element(*Apply_VolunteerPage.LAB_COVIDVAC).text
			assert label == 'Click here to upload a copy of your Covid-19 Vaccination Certificate (optional)'
			self.upload_COVID(argv[1])
		
		elif argv[0] == 'Exempt':
			self.browser.execute_script(
				"document.querySelector(arguments[0],':before').click();", *Apply_VolunteerPage.RADIO_COVID_EXEMPT)
			wait.until(EC.visibility_of_element_located(Apply_VolunteerPage.LAB_COVIDVAC))
			label = self.browser.find_element(*Apply_VolunteerPage.LAB_COVIDVAC).text
			assert label == 'Please upload a copy of your Medical Exemption'
			self.upload_COVID(argv[1])
		else:
			self.browser.execute_script(
				"document.querySelector(arguments[0],':before').click();", Apply_VolunteerPage.RADIO_COVIDVAC_NO)
			# wait.until(EC.visibility_of_element_located(self.MSG_COVIDVAC_1))
			# wait.until(EC.visibility_of_element_located(self.MSG_COVIDVAC_2))
	
	def select_IDProof(self, *argv):
		wait = WebDriverWait(self.browser, 10)
		if argv[0] == 'Yes':
			self.upload_IDProof(argv[1])
	
	def select_GuardianProof(self, *argv):
		wait = WebDriverWait(self.browser, 10)
		if argv[0] == 'Yes':
			self.upload_GuardianProof(argv[1])
	
	def upload_COVID(self, path):
		self.browser.find_element(*Apply_VolunteerPage.UPLOAD_COVIDVAC).send_keys(path)
		time.sleep(10)
		wait = WebDriverWait(self.browser, 10)
		wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#vf_vaccination_certificate_document_file>div>span>div>a")))
	
	def upload_IDProof(self, path):
		self.browser.find_element(*Apply_VolunteerPage.UPLOAD_IDProof).send_keys(path)
		time.sleep(10)
		wait = WebDriverWait(self.browser, 10)
		wait.until(EC.visibility_of_element_located((By.XPATH, "//a[normalize-space()='sample.pdf']")))
	
	def upload_GuardianProof(self, path):
		self.browser.find_element(*Apply_VolunteerPage.UPLOAD_GUARDIANCONS).send_keys(path)
		time.sleep(10)
	
	def select_Title(self, title):
		wait = WebDriverWait(self.browser, 20)
		time.sleep(2)
		wait.until(EC.visibility_of_element_located((By.XPATH, '//label[contains(text(),"Please ensure your personal details are correct an")]')))
		wait.until(EC.element_to_be_clickable(Apply_VolunteerPage.SEL_TITLE))
		self.browser.execute_script(
			"document.querySelector(arguments[0]).click();", Apply_VolunteerPage.SEL_TITLE)
		self.browser.find_element(*Apply_VolunteerPage.SEL_TITLE).click()
		wait.until(EC.visibility_of_element_located(Apply_VolunteerPage.DD_TITLE))
		self.browser.find_element(*Apply_VolunteerPage.SEARCH_TITLE).send_keys(title)
		wait.until(EC.element_to_be_clickable(((By.XPATH, '//ul[@id="select2-results-1"]/li/div'))))
		self.browser.find_element(By.XPATH, '//ul[@id="select2-results-1"]/li/div').click()
	
	def select_Gender(self, sex):
		wait = WebDriverWait(self.browser, 10)
		self.browser.execute_script(
			"document.querySelector(arguments[0]).click();", Apply_VolunteerPage.SEL_GENDER)
		self.browser.find_element(*Apply_VolunteerPage.SEL_GENDER).click()
		wait.until(EC.visibility_of_element_located(Apply_VolunteerPage.DD_TITLE))
		self.browser.find_element(*Apply_VolunteerPage.SEARCH_GENDER).send_keys(sex)
		wait.until(EC.element_to_be_clickable(((By.XPATH, '//ul[@id="select2-results-2"]/li[1]/div'))))
		self.browser.find_element(By.XPATH, '//ul[@id="select2-results-2"]/li[1]/div').click()
	
	def enter_HomePhone(self, hPhone):
		self.browser.find_element(*Apply_VolunteerPage.TXT_HOMEPHONE).send_keys(hPhone)
	
	def enter_WorkPhone(self, wPhone):
		self.browser.find_element(*Apply_VolunteerPage.TXT_WRKPHONE).send_keys(wPhone)
	
	def enter_HomeAdd(self, *argv):
		self.browser.find_element(*Apply_VolunteerPage.TXT_STREET).send_keys(argv[0])
		self.browser.find_element(*Apply_VolunteerPage.TXT_SUBURB).send_keys(argv[1])
		self.browser.find_element(*Apply_VolunteerPage.TXT_POSTCODE).send_keys(argv[2])
	
	def enter_LivedSinceDate(self, date):
		self.browser.find_element(*Apply_VolunteerPage.TXT_LIVED).send_keys(date)
	
	def select_PostAdd(self, yn):
		if yn == 'Same as home address':
			self.browser.execute_script(
				"document.querySelector(arguments[0],':before').click();", Apply_VolunteerPage.RADIO_POSTADD)
		else:
			self.browser.execute_script(
				"document.querySelector(arguments[0],':before').click();", Apply_VolunteerPage.RADIO_DIFFPOSTADD)
			wait = WebDriverWait(self.browser, 10)
			wait.until(EC.visibility_of_element_located((By.XPATH, "//label[contains(text(),'Postal address')]")))
	
	def select_MemVolOrg(self, *argv):
		if argv[0] == 'Yes':
			self.browser.execute_script(
				"document.querySelector(arguments[0],':before').click();", Apply_VolunteerPage.RADIO_VOLORG_YES)
			wait = WebDriverWait(self.browser, 20)
			wait.until(EC.visibility_of_element_located((By.XPATH, '//label[@id="sp_grp_checkbox_pdets_all_that_apply_label"]')))
			
			try:
				for i in range(1, len(argv)):
					self.chk_VolOrg(argv[i])
			except:
				print("No Voluntary Organisations provided")
		
		elif argv[0] == 'No':
			self.browser.execute_script(
				"document.querySelector(arguments[0],':before').click();", Apply_VolunteerPage.RADIO_VOLORG_NO)
		elif argv[0] == 'Prefer not to say':
			self.browser.execute_script(
				"document.querySelector(arguments[0],':before').click();", Apply_VolunteerPage.RADIO_VOLORG_NOTTOSAY)
	
	def chk_VolOrg(self, volOrg):
		if volOrg == 'Emergency services':
			self.browser.execute_script(
				"(document.querySelectorAll(arguments[0]))[1].click();", Apply_VolunteerPage.CHK_VOLORG)
		elif volOrg == 'Religious':
			self.browser.execute_script(
				"(document.querySelectorAll(arguments[0]))[2].click();", Apply_VolunteerPage.CHK_VOLORG)
		elif volOrg == 'Parenting, children & youth':
			self.browser.execute_script(
				"(document.querySelectorAll(arguments[0]))[3].click();", Apply_VolunteerPage.CHK_VOLORG)
		elif volOrg == 'Education':
			self.browser.execute_script(
				"(document.querySelectorAll(arguments[0]))[4].click();", Apply_VolunteerPage.CHK_VOLORG)
		elif volOrg == 'Arts/heritage':
			self.browser.execute_script(
				"(document.querySelectorAll(arguments[0]))[5].click();", Apply_VolunteerPage.CHK_VOLORG)
		elif volOrg == 'Welfare/community':
			self.browser.execute_script(
				"(document.querySelectorAll(arguments[0]))[6].click();", Apply_VolunteerPage.CHK_VOLORG)
		elif volOrg == 'Sports & physical recreation':
			self.browser.execute_script(
				"(document.querySelectorAll(arguments[0]))[7].click();", Apply_VolunteerPage.CHK_VOLORG)
		else:
			self.browser.execute_script(
				"(document.querySelectorAll(arguments[0]))[8].click();", Apply_VolunteerPage.CHK_VOLORG)
	
	def enter_EmContactName(self, name):
		self.browser.find_element(*Apply_VolunteerPage.TXT_EM_NAME).send_keys(name)
	
	def enter_EmHomePh(self, hPhone):
		self.browser.find_element(*Apply_VolunteerPage.TXT_EM_HMEPHONE).send_keys(hPhone)
	
	def enter_EmWorkPh(self, wPhone):
		self.browser.find_element(*Apply_VolunteerPage.TXT_EM_WRKPHONE).send_keys(wPhone)
	
	def enter_GuardianName(self, name):
		self.browser.find_element(*Apply_VolunteerPage.Txt_Guardian_Name).send_keys(name)
	
	def enter_GuardianEmail(self, email):
		self.browser.find_element(*Apply_VolunteerPage.Txt_Guardian_Email).send_keys(email)
	
	def enter_GuardianMobile(self, mobile):
		self.browser.find_element(*Apply_VolunteerPage.Txt_Guardian_Mobile).send_keys(mobile)
	
	def select_RelToYou(self, rty):
		wait = WebDriverWait(self.browser, 10)
		wait.until(EC.element_to_be_clickable(Apply_VolunteerPage.SEL_RELTOYOU))
		self.browser.find_element(*Apply_VolunteerPage.SEL_RELTOYOU).click()
		wait.until(EC.visibility_of_element_located(Apply_VolunteerPage.DD_RELTOYOU))
		self.browser.find_element(*Apply_VolunteerPage.SEARCH_RELTOYOU).send_keys(rty)
		wait.until(EC.element_to_be_clickable(((By.XPATH, '//ul[@id="select2-results-7"]/li/div'))))
		self.browser.find_element(By.XPATH, '//ul[@id="select2-results-7"]/li/div').click()
	
	def select_ReportableConduct(self, yn, reason):
		if yn == 'No':
			self.browser.execute_script(
				"document.querySelector(arguments[0],':before').click();", Apply_VolunteerPage.RADIO_REPORTABLE_NO)
		else:
			self.browser.execute_script(
				"document.querySelector(arguments[0],':before').click();", Apply_VolunteerPage.RADIO_REPORTABLE_YES)
			wait = WebDriverWait(self.browser, 10)
			wait.until(EC.visibility_of_element_located(Apply_VolunteerPage.TXT_REPORTABLE_DET))
			self.browser.find_element(*Apply_VolunteerPage.TXT_REPORTABLE_DET).send_keys(reason)
	
	def select_CriminalConduct(self, yn, reason):
		if yn == 'No':
			self.browser.execute_script(
				"document.querySelector(arguments[0],':before').click();", Apply_VolunteerPage.RADIO_CRIMINAL_NO)
		else:
			self.browser.execute_script(
				"document.querySelector(arguments[0],':before').click();", Apply_VolunteerPage.RADIO_CRIMINAL_YES)
			wait = WebDriverWait(self.browser, 10)
			wait.until(EC.visibility_of_element_located(Apply_VolunteerPage.TXT_CRIMINAL_DET))
			self.browser.find_element(*Apply_VolunteerPage.TXT_CRIMINAL_DET).send_keys(reason)
	
	def select_MembershipInfo(self, yn):
		if yn == 'No':
			self.browser.execute_script(
				"document.querySelector(arguments[0],':before').click();", Apply_VolunteerPage.RADIO_REPORTABLE_NO)
		else:
			self.browser.execute_script(
				"document.querySelector(arguments[0],':before').click();", Apply_VolunteerPage.RADIO_REPORTABLE_YES)
	
	def chck_Guardian_Const(self, sign):
		# self.browser.find_element(*self.CHK_GUARDIAN_CONST).click()
		self.browser.execute_script(
			"document.querySelector(arguments[0],':before').click();", Apply_VolunteerPage.CHK_GUARDIAN_CONST)
		self.browser.find_element(*Apply_VolunteerPage.Txt_Guardain_Sign).send_keys(sign)
	
	def check_Declaration(self, sign):
		self.browser.execute_script(
			"document.querySelector(arguments[0],':before').click();", Apply_VolunteerPage.CHKBOX_DECLARATION)
		# self.browser.find_element(*self.TXT_SIGN).click()
		self.browser.find_element(*Apply_VolunteerPage.TXT_SIGN).send_keys(sign)
	
	def click_ContinutPoliceChk(self):
		self.browser.find_element(*Apply_VolunteerPage.BTN_CONTINUETOPOLICECHK).click()
		wait = WebDriverWait(self.browser, 10)
		wait.until(EC.visibility_of_element_located((By.XPATH, '//h1[contains(text(),"Police check application")]')))
	
	def select_Identity(self, identity):
		if identity == 'Aboriginal':
			self.browser.execute_script(
				"document.querySelector(arguments[0],':before').click();", Apply_VolunteerPage.RADIO_ABORIGINAL)
		elif identity == 'Islander':
			self.browser.execute_script(
				"document.querySelector(arguments[0],':before').click();", Apply_VolunteerPage.RADIO_ISLANDER)
		elif identity == 'Both':
			self.browser.execute_script(
				"document.querySelector(arguments[0],':before').click();", Apply_VolunteerPage.RADIO_ABO_ISLANDER)
		else:
			self.browser.execute_script(
				"document.querySelector(arguments[0],':before').click();", Apply_VolunteerPage.RADIO_NEITHER)
	
	def select_Ethnicity(self, yn):
		if yn == 'No':
			self.browser.execute_script(
				"document.querySelector(arguments[0],':before').click();", Apply_VolunteerPage.RADIO_ETHNICITY_NO)
		else:
			self.browser.execute_script(
				"document.querySelector(arguments[0],':before').click();", Apply_VolunteerPage.RADIO_ETHNICITY_YES)
	
	def select_Disability(self, op):
		if op == 'Yes':
			self.browser.execute_script(
				"document.querySelector(arguments[0],':before').click();", Apply_VolunteerPage.RADIO_DISABILITY_YES)
		elif op == 'No':
			self.browser.execute_script(
				"document.querySelector(arguments[0],':before').click();", Apply_VolunteerPage.RADIO_DISABILITY_NO)
		else:
			self.browser.execute_script(
				"document.querySelector(arguments[0],':before').click();", Apply_VolunteerPage.RADIO_DISABILITY_NOTTOSAY)
