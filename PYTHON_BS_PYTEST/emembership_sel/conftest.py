"""
This module contains shared fixtures.
"""

import pytest
import time
import json
from pathlib import Path
import selenium.webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from pip._internal.utils import logging
from pytest_bdd import given, parsers
from pytest_bdd import when, parsers
from pytest_bdd import then, parsers
from pytest_bdd import feature, step, scenario, parsers
from functools import partial
from pages.common_for_all_pages import Common_Functions
from pages.candidate_WelcomePage import candidate_WelcomePage
from pages.login import loginPage
from pages.serviceNow_LoginPage import serviceNow_LoginPage
from pages.serviceNowPage import serviceNowPage
from pages.start_NewAppPage import start_NewAppPage
from pages.outlookPage import outlookPage
from pages.apply_VolunteerPage import apply_VolunteerPage
from pages.createProfilePage import createProfilePage
from pages.serviceNow_BrigadeReview_Page import serviceNow_BrigadeReview_Page
from pages.police_CheckPage import police_CheckPage
from pages.app_Submission_SuccessPage import app_Submission_SuccessPage
from pages.sapQasPage import sapQasPage
from selenium.common.exceptions import *
from selenium.webdriver.chrome.options import Options
from pages.createProfilePage import eMail
from browserstack.local import Local
from pages.common_for_all_pages import Common_Functions
import os
import random
import string
from selenium.webdriver.edge import options
from datetime import datetime
import logging
from pytest import mark
from Settings.config import bs_config, script_creds

#                  ___________:::::::::: CONFIGS STARTS HERE ::::::::::_____________

APP_NAME = 'Service Now'
RFS_ROLE_EXPLORER = 'https://nswrfsuat.service-now.com/rfsembr?id=embr_rfs_role_explorer'
LOGIN = 'https://nswrfsuat.service-now.com/rfsembr?id=embr_login'
SERVICENOW = 'https://nswrfsuat.service-now.com/'
SERVICENOW_EMAILS = 'https://nswrfsuat.service-now.com/sys_email_list.do'
SAP_QAS = 'https://sapqep.nswfire.nsw.gov.au/irj/portal?spnego=disabled'

"""
# ==========================================================
							#CODE FOR RECORDING - ON Testing
# ==========================================================
@pytest.fixture(scope="session")
def browser_recorder_fixture():
	# Create an instance of SeleniumBrowserRecorder
	recorder = SeleniumBrowserRecorder("./Videos", ".mp4")

	# Start the recording session at the beginning of the pytest session
	recorder.start_recording_session()

	yield recorder  # Provide the recorder as a fixture to the tests

	# Stop the recording session at the end of the pytest session
	recorder.stop_recording_session()
#----------------------------------------------------------------------------------------------------------------------------------------------------------------

																																	"""


@pytest.fixture(scope="session")
# the fixture is destroyed at the end of the test session
def test_config():
	# Read the file
	with open('test_config.json') as test_config_file:
		test_config = json.load(test_config_file)
	
	# Assert values are acceptable
	assert test_config['browser'] in ['Safari', 'Firefox', 'Chrome', 'Edge', 'Headless Chrome', 'Inco Edge']
	assert isinstance(test_config['implicit_wait'], int)
	assert test_config['implicit_wait'] > 0
	
	# Return test_config so it can be used
	return test_config


@pytest.fixture
def browser(test_config):
	if test_config['browserstack'] == 'No':
		# Initialize the Browser's Driver instance
		if test_config['browser'] == 'Firefox':
			driver = selenium.webdriver.Firefox()
		if test_config['browser'] == 'Edge':
			driver = selenium.webdriver.Edge()
		elif test_config['browser'] == 'Chrome':
			opts = Options()
			# opts.accept_insecure_certs()
			opts.add_argument("--incognito")
			opts.add_argument("--allow-running-insecure-content")
			opts.page_load_strategy = 'none'
			opts.accept_insecure_certs = True
			driver = selenium.webdriver.Chrome(options=opts)
			driver.maximize_window()
			driver.implicitly_wait(test_config['implicit_wait'])
		elif test_config['browser'] == 'Headless Chrome':
			opts = selenium.webdriver.ChromeOptions()
			opts.add_argument('headless')
			driver = selenium.webdriver.Chrome(options=opts)
		elif test_config['browser'] == 'Inco Edge':
			opts = selenium.webdriver.EdgeOptions()
			opts.add_argument('-inprivate')
			driver = selenium.webdriver.Edge(options=opts)
			driver.implicitly_wait(test_config['implicit_wait'])
		
		yield driver
	# driver.quit()
	
	else:
		# Other imports and desired_cap definition goes here
		username = script_creds['bs_user']['username']
		accessKey = script_creds['bs_user']['accesskey']
		
		if bs_config['platforms']['browserName'] == 'Chrome':
			# use desired cap or add to cap using options.set_cap
			chrome_options = Options()
			chrome_options.set_capability('bstack:options', bs_config['platforms'][1]['bstack:options'])
			chrome_options.add_experimental_option("prefs", {"profile.default_content_setting_values.geolocation": 1})
			desired_cap = chrome_options.to_capabilities()
			
			driver = selenium.webdriver.Remote(
				command_executor=script_creds['bs_user']['command_executor'],
				desired_capabilities=desired_cap
			)
			
			# Creates an instance of Local
			bs_local = Local()
			
			# You can also use the environment variable - "BROWSERSTACK_ACCESS_KEY".
			bs_local_args = {"key": accessKey}
			
			# Starts the Local instance with the required arguments
			bs_local.start(**bs_local_args)
			
			# Check if BrowserStack local instance is running
			print(bs_local.isRunning())
			# Return the WebDriver instance for the setup
			yield driver
			# Quit the WebDriver instance for the cleanup
			driver.quit()
			
			bs_local.stop()


def pytest_configure(config):
	timestamp = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
	
	# Set the log file dynamically
	log_file = f"logs/log{timestamp}.txt"
	config.option.log_file = log_file


@pytest.fixture(scope='module')
def feature_status():
	status = {'failed': False}
	yield status
	if status['failed']:
		logging.info("Feature has failed tests")
		pytest.skip("Previous scenario in the feature failed")


@pytest.fixture(autouse=True)
def check_feature_status(feature_status):
	if feature_status['failed']:
		logging.info("Skipping due to a previous scenario failure in this feature.")
		pytest.skip("Skipped due to a previous scenario failure in this feature.")


def pytest_exception_interact(node, call, report):
	if report.failed:
		if "scenario" in node.keywords:
			logging.info("A scenario has failed. Setting feature to failed.")
			feature_status = node.funcargs['feature_status']
			feature_status['failed'] = True


# Shared Given Steps
EXTRA_TYPES = {
	'string': str,
}


#                 ___________:::::::::: COMMON STEPS FOR SCENARIOS STARTS FROM BELOW ::::::::::_____________


@given(parsers.cfparse('User is on "{pagename}" page'))
def page(pagename, browser):
	login_page = loginPage(browser)
	serviceNow_page = serviceNowPage(browser)
	sapQas_page = sapQasPage(browser)
	outlook_Page = outlookPage(browser)
	if pagename == 'login':
		login_page.load()
		time.sleep(5)
	elif pagename == 'rfsRoleExplorer':
		browser.get(RFS_ROLE_EXPLORER)
	elif pagename == 'Service Now':
		serviceNow_page.load()
	elif pagename == 'Service Now incognito':
		opts = selenium.webdriver.EdgeOptions()
		opts.add_argument('-inprivate')
		browser = selenium.webdriver.Edge(options=opts)
		browser.get(SERVICENOW)
	# serviceNow_page.load()
	elif pagename == 'outlookLogin':
		outlook_Page.load()
	elif pagename == 'Service Now - EMAILS':
		serviceNow_page.load_child_page()
		time.sleep(2)
	elif pagename == 'SAP_QAS':
		sapQas_page.load()


@then('user is displayed with message to verify email')
def email_verification(browser):
	create_profile = createProfilePage(browser)
	create_profile.email_Verification()


@then(parsers.cfparse('candidate is displayed with message about successful submission'))
def succes_verification(browser):
	app_sub_success = app_Submission_SuccessPage(browser)
	app_sub_success.verify_Success()


@then('User logs in service now portal for closing special provision task')
def serviceNow_Brigade(browser, read_JSON):
	ref = read_JSON('data/appRef.json')
	serviceNow_page = serviceNowPage(browser)
	serviceNow_page.navigate_AdminPortalDashboard("No")
	serviceNow_page.search_AppRef(ref["ref"])
	sn_Brigade_page = serviceNow_BrigadeReview_Page(browser)
	sn_Brigade_page.click_Task("special provision")
	sn_Brigade_page.close_Task()
	serviceNow_page.click_Unimpersonate_User()


# serviceNow_page.click_Logo()


@then('User logs in service now portal for health approval')
def serviceNow_Brigade(browser, read_JSON):
	ref = read_JSON('data/appRef.json')
	serviceNow_page = serviceNowPage(browser)
	serviceNow_page.navigate_AdminPortalDashboard("Yes")
	serviceNow_page.search_AppRef(ref["ref"])
	sn_Brigade_page = serviceNow_BrigadeReview_Page(browser)
	sn_Brigade_page.click_Task("health")
	sn_Brigade_page.close_Task()
	serviceNow_page.search_AppRef(ref["ref"])
	serviceNow_page.click_Unimpersonate_User()


@when(parsers.cfparse('Candidate enters credentials "{usr}" "{pwd}"'))
def user_Enters_Login_Det(browser, usr, pwd):
	login_page = loginPage(browser)
	login_page.enter_Creds(usr, pwd)


# login_page.enter_Creds(usr,pwd)   ##   >>> """THIS IS FOR DEBUG"""


@when(parsers.cfparse('User enters valid credentials "{user}" "{password}"'))
def user_Enters_Login_Det(browser, user, password):
	serviceNowLogin_page = serviceNow_LoginPage(browser)
	serviceNowLogin_page.enter_Credentials(user, password)


@when('user enters login details and logs in')
def login_user(browser, usr, pwd):
	create_profile = createProfilePage(browser)
	create_profile.logout_logi(eMail, pwd)


# @then(parsers.cfparse('candidate fills in junior volunteer details "{file}"'))
# def fill_volunteerDetails_Admin(browser,read_JSON,file):
#     data_dict = read_JSON(file)
#     apply_vol_page = apply_VolunteerPage(browser)
#     apply_vol_page.check_Junior_Role()
#     apply_vol_page.select_LocalBrigade(data_dict["Brigade"]["Name"])
#     apply_vol_page.select_RFSA(data_dict["Brigade"]["RFSA"])
#     # time.sleep(2)
#     apply_vol_page.saveAndCont(0)
#     # time.sleep(2)
#     apply_vol_page.check_Junior_HS()
#     apply_vol_page.select_Maint_Jun(data_dict["Admin"]["Option"])
#     # time.sleep(2)
#     apply_vol_page.select_Diabetes(data_dict["MedQues"]["Diabetes"])
#     # time.sleep(3)
#     apply_vol_page.select_Stroke(data_dict["MedQues"]["Stroke"])
#     # time.sleep(2)
#     apply_vol_page.select_BloodThinning(data_dict["MedQues"]["BloodThin"])
#     # time.sleep(2)
#     apply_vol_page.select_ReleiveMed(data_dict["MedQues"]["ReleiveMed"])
#     # time.sleep(2)
#     apply_vol_page.select_Seizure(data_dict["MedQues"]["Seizure"])
#     # time.sleep(2)
#     apply_vol_page.select_OtherMedCondJun(data_dict["MedQues"]["Other"])
#     # time.sleep(4)
#     apply_vol_page.select_Psychiatric(data_dict["MedQues"]["Psychiatric"])
#     filename = Path("data/sample.pdf")
#     apply_vol_page.select_COVID('NO','C:\Projects\WaridI\ServiceNow\emembership_sel\data\sample.pdf')
#     apply_vol_page.saveAndCont(1)
#     apply_vol_page.select_Title(data_dict["PersonalDetails"]["Title"])
#     apply_vol_page.select_Gender(data_dict["PersonalDetails"]["Gender"])
#     apply_vol_page.enter_HomePhone(data_dict["PersonalDetails"]["HomePhone"])
#     apply_vol_page.enter_WorkPhone(data_dict["PersonalDetails"]["WorkPhone"])
#     apply_vol_page.enter_HomeAdd(
#         data_dict["PersonalDetails"]["HomeAdd"]["street"], data_dict["PersonalDetails"]["HomeAdd"]["suburb"], data_dict["PersonalDetails"]["HomeAdd"]["postcode"])
#     apply_vol_page.enter_LivedSinceDate(data_dict["PersonalDetails"]["LivedSince"])
#     apply_vol_page.select_PostAdd(data_dict["PersonalDetails"]["PostalAdd"])
#     apply_vol_page.select_MemVolOrg(data_dict["PersonalDetails"]["Member"]["yn"], data_dict["PersonalDetails"]["Member"]["org"])
#     apply_vol_page.saveAndCont(2)
#     apply_vol_page.enter_EmContactName(data_dict["EmergencyContact"]["Name"])
#     apply_vol_page.select_RelToYou(data_dict["EmergencyContact"]["Relation"])
#     apply_vol_page.enter_EmHomePh(data_dict["EmergencyContact"]["HomePhone"])
#     apply_vol_page.enter_EmWorkPh(data_dict["EmergencyContact"]["WorkPhone"])
#     apply_vol_page.saveAndCont(3)
#     apply_vol_page.select_ReportableConduct(data_dict["Disclosure"]["Reportable"], data_dict["Disclosure"]["RepReason"])
#     apply_vol_page.select_CriminalConduct(data_dict["Disclosure"]["Criminal"],data_dict["Disclosure"]["CriminalReason"])
#     apply_vol_page.select_MembershipInfo(data_dict["Disclosure"]["MembershipInfo"])
#     apply_vol_page.saveAndCont(4)
#     apply_vol_page.select_Identity(data_dict["Demographics"]["Identity"])
#     apply_vol_page.select_Ethnicity(data_dict["Demographics"]["Ethnicity"])
#     apply_vol_page.select_Disability(data_dict["Demographics"]["Disability"])
#     apply_vol_page.saveAndCont(5)
#     apply_vol_page.check_Junior_Guardian()
#     # time.sleep(2)
#     apply_vol_page.enter_GuardianName(data_dict["Guardian"]["Name"])
#     #  time.sleep(2)
#     apply_vol_page.enter_GuardianEmail(data_dict["Guardian"]["Email"])
#     #  time.sleep(2)
#     apply_vol_page.enter_GuardianMobile(data_dict["Guardian"]["Contact"])
#     #  time.sleep(2)
#     apply_vol_page.select_IDProof('Yes', 'C:\Projects\WaridI\ServiceNow\emembership_sel\data\sample.pdf')
#     #  time.sleep(2)
#     apply_vol_page.select_GuardianProof('Yes', 'C:\Projects\WaridI\ServiceNow\emembership_sel\data\sample.pdf')
#     #  time.sleep(2)
#     apply_vol_page.chck_Guardian_Const('Guard')
#     apply_vol_page.saveAndCont(6)
#     time.sleep(5)
#     apply_vol_page.check_Declaration('Automation')
#     apply_vol_page.Juncontinue()

@then(parsers.cfparse('User fills in U17 volunteer details "{file}"'))
def fill_volunteerDetails_Admin(browser, read_JSON, file):
	data_dict = read_JSON(file)
	apply_vol_page = apply_VolunteerPage(browser)
	apply_vol_page.check_Junior_Role()
	apply_vol_page.select_LocalBrigade(data_dict["Brigade"]["Name"])
	apply_vol_page.select_RFSA(data_dict["Brigade"]["RFSA"])
	#  time.sleep(2)
	apply_vol_page.saveAndCont(0)
	time.sleep(2)
	apply_vol_page.check_Junior_HS()
	apply_vol_page.select_Maint_Jun(data_dict["Admin"]["Option"])
	time.sleep(2)
	apply_vol_page.select_Diabetes(data_dict["MedQues"]["Diabetes"])
	time.sleep(3)
	apply_vol_page.select_Stroke(data_dict["MedQues"]["Stroke"])
	time.sleep(2)
	apply_vol_page.select_BloodThinning(data_dict["MedQues"]["BloodThin"])
	time.sleep(2)
	apply_vol_page.select_ReleiveMed(data_dict["MedQues"]["ReleiveMed"])
	time.sleep(2)
	apply_vol_page.select_Seizure(data_dict["MedQues"]["Seizure"])
	time.sleep(2)
	apply_vol_page.select_OtherMedCondJun(data_dict["MedQues"]["Other"])
	time.sleep(4)
	apply_vol_page.select_Psychiatric(data_dict["MedQues"]["Psychiatric"])
	filename = Path("data/sample.pdf")
	apply_vol_page.select_COVID('NO', 'C:\Projects\WaridI\ServiceNow\emembership_sel\data\sample.pdf')
	apply_vol_page.saveAndCont(1)
	apply_vol_page.select_Title(data_dict["PersonalDetails"]["Title"])
	apply_vol_page.select_Gender(data_dict["PersonalDetails"]["Gender"])
	apply_vol_page.enter_HomePhone(data_dict["PersonalDetails"]["HomePhone"])
	apply_vol_page.enter_WorkPhone(data_dict["PersonalDetails"]["WorkPhone"])
	apply_vol_page.enter_HomeAdd(
		data_dict["PersonalDetails"]["HomeAdd"]["street"], data_dict["PersonalDetails"]["HomeAdd"]["suburb"], data_dict["PersonalDetails"]["HomeAdd"]["postcode"])
	apply_vol_page.enter_LivedSinceDate(data_dict["PersonalDetails"]["LivedSince"])
	apply_vol_page.select_PostAdd(data_dict["PersonalDetails"]["PostalAdd"])
	apply_vol_page.select_MemVolOrg(data_dict["PersonalDetails"]["Member"]["yn"], data_dict["PersonalDetails"]["Member"]["org"])
	apply_vol_page.saveAndCont(2)
	apply_vol_page.enter_EmContactName(data_dict["EmergencyContact"]["Name"])
	apply_vol_page.select_RelToYou(data_dict["EmergencyContact"]["Relation"])
	apply_vol_page.enter_EmHomePh(data_dict["EmergencyContact"]["HomePhone"])
	apply_vol_page.enter_EmWorkPh(data_dict["EmergencyContact"]["WorkPhone"])
	apply_vol_page.saveAndCont(3)
	apply_vol_page.select_ReportableConduct(data_dict["Disclosure"]["Reportable"], data_dict["Disclosure"]["RepReason"])
	apply_vol_page.select_CriminalConduct(data_dict["Disclosure"]["Criminal"], data_dict["Disclosure"]["CriminalReason"])
	apply_vol_page.select_MembershipInfo(data_dict["Disclosure"]["MembershipInfo"])
	apply_vol_page.saveAndCont(4)
	apply_vol_page.select_Identity(data_dict["Demographics"]["Identity"])
	apply_vol_page.select_Ethnicity(data_dict["Demographics"]["Ethnicity"])
	apply_vol_page.select_Disability(data_dict["Demographics"]["Disability"])
	apply_vol_page.saveAndCont(5)
	apply_vol_page.check_Junior_Guardian()
	# time.sleep(2)
	apply_vol_page.enter_GuardianName(data_dict["Guardian"]["Name"])
	time.sleep(2)
	apply_vol_page.enter_GuardianEmail(data_dict["Guardian"]["Email"])
	time.sleep(2)
	apply_vol_page.enter_GuardianMobile(data_dict["Guardian"]["Contact"])
	time.sleep(2)
	apply_vol_page.select_IDProof('Yes', 'data\sample.pdf')
	time.sleep(2)
	apply_vol_page.select_GuardianProof('Yes', 'data\sample.pdf')
	time.sleep(2)
	apply_vol_page.chck_Guardian_Const('Guard')
	apply_vol_page.saveAndCont(6)
	time.sleep(5)
	apply_vol_page.check_Declaration('Automation')
	apply_vol_page.Juncontinue()


@then(parsers.cfparse('User fills in U17 volunteer details "{file}"'))
def fill_volunteerDetails_Admin(browser, read_JSON, file):
	data_dict = read_JSON(file)
	apply_vol_page = apply_VolunteerPage(browser)
	apply_vol_page.select_LocalBrigade(data_dict["Brigade"]["Name"])
	apply_vol_page.select_RFSA(data_dict["Brigade"]["RFSA"])
	# time.sleep(2)
	apply_vol_page.saveAndCont(0)
	# time.sleep(2)
	apply_vol_page.select_Maint_Jun(data_dict["Admin"]["Option"])
	# time.sleep(2)
	apply_vol_page.select_Diabetes(data_dict["MedQues"]["Diabetes"])
	# time.sleep(3)
	apply_vol_page.select_Stroke(data_dict["MedQues"]["Stroke"])
	# time.sleep(2)
	apply_vol_page.select_BloodThinning(data_dict["MedQues"]["BloodThin"])
	# time.sleep(2)
	apply_vol_page.select_ReleiveMed(data_dict["MedQues"]["ReleiveMed"])
	# time.sleep(2)
	apply_vol_page.select_Seizure(data_dict["MedQues"]["Seizure"])
	# time.sleep(2)
	apply_vol_page.select_OtherMedCondJun(data_dict["MedQues"]["Other"])
	# time.sleep(4)
	apply_vol_page.select_Psychiatric(data_dict["MedQues"]["Psychiatric"])
	filename = Path("data/sample.pdf")
	apply_vol_page.select_COVID('NO', 'C:\Projects\WaridI\ServiceNow\emembership_sel\data\sample.pdf')
	apply_vol_page.saveAndCont(1)
	apply_vol_page.select_Title(data_dict["PersonalDetails"]["Title"])
	apply_vol_page.select_Gender(data_dict["PersonalDetails"]["Gender"])
	apply_vol_page.enter_HomePhone(data_dict["PersonalDetails"]["HomePhone"])
	apply_vol_page.enter_WorkPhone(data_dict["PersonalDetails"]["WorkPhone"])
	apply_vol_page.enter_HomeAdd(
		data_dict["PersonalDetails"]["HomeAdd"]["street"], data_dict["PersonalDetails"]["HomeAdd"]["suburb"], data_dict["PersonalDetails"]["HomeAdd"]["postcode"])
	apply_vol_page.enter_LivedSinceDate(data_dict["PersonalDetails"]["LivedSince"])
	apply_vol_page.select_PostAdd(data_dict["PersonalDetails"]["PostalAdd"])
	apply_vol_page.select_MemVolOrg(data_dict["PersonalDetails"]["Member"]["yn"], data_dict["PersonalDetails"]["Member"]["org"])
	apply_vol_page.saveAndCont(2)
	apply_vol_page.enter_EmContactName(data_dict["EmergencyContact"]["Name"])
	apply_vol_page.select_RelToYou(data_dict["EmergencyContact"]["Relation"])
	apply_vol_page.enter_EmHomePh(data_dict["EmergencyContact"]["HomePhone"])
	apply_vol_page.enter_EmWorkPh(data_dict["EmergencyContact"]["WorkPhone"])
	apply_vol_page.saveAndCont(3)
	apply_vol_page.select_ReportableConduct(data_dict["Disclosure"]["Reportable"], data_dict["Disclosure"]["RepReason"])
	apply_vol_page.select_CriminalConduct(data_dict["Disclosure"]["Criminal"], data_dict["Disclosure"]["CriminalReason"])
	apply_vol_page.select_MembershipInfo(data_dict["Disclosure"]["MembershipInfo"])
	apply_vol_page.saveAndCont(4)
	apply_vol_page.select_Identity(data_dict["Demographics"]["Identity"])
	apply_vol_page.select_Ethnicity(data_dict["Demographics"]["Ethnicity"])
	apply_vol_page.select_Disability(data_dict["Demographics"]["Disability"])
	apply_vol_page.saveAndCont(5)
	# time.sleep(2)
	apply_vol_page.enter_GuardianName(data_dict["Guardian"]["Name"])
	# time.sleep(2)
	apply_vol_page.enter_GuardianEmail(data_dict["Guardian"]["Email"])
	# time.sleep(2)
	apply_vol_page.enter_GuardianMobile(data_dict["Guardian"]["Contact"])
	# time.sleep(2)
	apply_vol_page.select_IDProof('Yes', 'data/sample.pdf')
	# time.sleep(2)
	apply_vol_page.select_GuardianProof('Yes', 'data/sample.pdf')
	# time.sleep(2)
	apply_vol_page.chck_Guardian_Const('Guard')
	apply_vol_page.saveAndCont(6)
	time.sleep(5)
	apply_vol_page.check_Declaration('Automation')


@then('User can see staff admin portal dashboard')
def user_View_Admin_PortalDB(browser):
	serviceNow_page = serviceNowPage(browser)
	serviceNow_page.navigate_AdminPortalDashboard()


@then(parsers.cfparse('User click "{button}" application button'))
def user_Enters_Login_Det(browser, button):
	can_Wel_page = candidate_WelcomePage(browser)
	can_Wel_page.click_New_Cont_APP(button)


@then(parsers.cfparse('User then clicks "{opt}" button'))
def user_Selects_Create(browser, opt):
	create_profile = createProfilePage(browser)
	create_profile.click_CreateOrLogin(opt)
	create_profile.wait_for_page_load(timeout=60)


@then(parsers.cfparse('User Enter Details and Submit details to create profile "{file}"'))
def user_Selects_Create(browser, read_JSON, file):
	data = read_JSON(file)
	create_profile = createProfilePage(browser)
	create_profile.fill_ApplicantDetails(data["FNAME"], data["PNAME"],
	                                     data["LNAME"], data["EMAIL"], data["MOBILE"], data["DOB"], data["PWD"], data["PWD"])
	create_profile.sel_PreviousMembership(data["PREVMEM"])
	create_profile.save_user_details()
	create_profile.accept_Privacy()
	create_profile.click_CreateProfile()


@then('User searches for email and verifies')
def click_All(browser):
	serviceNow_page = serviceNowPage(browser)
	serviceNow_page.click_All()


@then(parsers.cfparse('user verifies the status of application "{file}" as "{status}"'))
def save_appJSON(browser, read_JSON, file, status):
	ref = read_JSON(file)
	can_Wel_page = candidate_WelcomePage(browser)
	status_retrieved = can_Wel_page.verify_AppStatus(ref["ref"])
	assert status in status_retrieved


@then(parsers.cfparse('Verify the forms displayed for "{usr_cat}"'))
def user_Enters_Login_Det(browser, usr_cat):
	strt_NewApp_page = start_NewAppPage(browser)
	strt_NewApp_page.verify_AppCards(usr_cat)


# @then(parsers.cfparse('User fills in volunteer details for "{role}" "{file}"'))
# def fill_volunteerDetails(browser,read_JSON,file, role):
#     data_dict = read_JSON(file)
#     apply_vol_page = apply_VolunteerPage(browser)
#     apply_vol_page.select_VonteerOption(data_dict["VolunteerOpt"]["Option"])
#     # apply_vol_page.select_CFU(data_dict["VolunteerOpt"]["CFU"])
#     apply_vol_page.select_PrevExp_FF(data_dict["VolunteerOpt"]["PrevExp"])
#     apply_vol_page.saveAndCont(0)
#     apply_vol_page.select_LocalBrigade(data_dict["Brigade"]["Name"])
#     apply_vol_page.select_RFSA(data_dict["Brigade"]["RFSA"])
#     apply_vol_page.saveAndCont(1)
#     apply_vol_page.select_RoleAgree('Yes')
#     apply_vol_page.check_Exists(role)
#    #  time.sleep(2)
#     apply_vol_page.select_Challenge(data_dict["Admin"]["Option"], role)
#    #  time.sleep(2)
#     apply_vol_page.select_Diabetes(data_dict["MedQues"]["Diabetes"])
#    #  time.sleep(2)
#     apply_vol_page.select_Stroke(data_dict["MedQues"]["Stroke"])
#    #  time.sleep(2)
#     apply_vol_page.select_BloodThinning(data_dict["MedQues"]["BloodThin"])
#    #  time.sleep(2)
#     apply_vol_page.select_ReleiveMed(data_dict["MedQues"]["ReleiveMed"])
#     # time.sleep(2)
#     apply_vol_page.select_Seizure(data_dict["MedQues"]["Seizure"])
#     time.sleep(10)
#     apply_vol_page.select_OtherMedCond(data_dict["MedQues"]["Other"], role)
#    #  time.sleep(2)
#     apply_vol_page.select_Psychiatric(data_dict["MedQues"]["Psychiatric"])
#     filename = Path("data/sample.pdf")
#     apply_vol_page.select_COVID('NO','C:\Projects\WaridI\ServiceNow\emembership_sel\data\sample.pdf')
#     apply_vol_page.saveAndCont(2)
#     apply_vol_page.select_Title(data_dict["PersonalDetails"]["Title"])
#     apply_vol_page.select_Gender(data_dict["PersonalDetails"]["Gender"])
#     apply_vol_page.enter_HomePhone(data_dict["PersonalDetails"]["HomePhone"])
#     apply_vol_page.enter_WorkPhone(data_dict["PersonalDetails"]["WorkPhone"])
#     apply_vol_page.enter_HomeAdd(
#         data_dict["PersonalDetails"]["HomeAdd"]["street"], data_dict["PersonalDetails"]["HomeAdd"]["suburb"], data_dict["PersonalDetails"]["HomeAdd"]["postcode"])
#     apply_vol_page.enter_LivedSinceDate(data_dict["PersonalDetails"]["LivedSince"])
#     apply_vol_page.select_PostAdd(data_dict["PersonalDetails"]["PostalAdd"])
#     apply_vol_page.select_MemVolOrg(data_dict["PersonalDetails"]["Member"]["yn"], data_dict["PersonalDetails"]["Member"]["org"])
#     apply_vol_page.saveAndCont(3)
#     apply_vol_page.enter_EmContactName(data_dict["EmergencyContact"]["Name"])
#     apply_vol_page.select_RelToYou(data_dict["EmergencyContact"]["Relation"])
#     apply_vol_page.enter_EmHomePh(data_dict["EmergencyContact"]["HomePhone"])
#     apply_vol_page.enter_EmWorkPh(data_dict["EmergencyContact"]["WorkPhone"])
#     apply_vol_page.saveAndCont(4)
#     apply_vol_page.select_ReportableConduct(data_dict["Disclosure"]["Reportable"], data_dict["Disclosure"]["RepReason"])
#     apply_vol_page.select_CriminalConduct(data_dict["Disclosure"]["Criminal"],data_dict["Disclosure"]["CriminalReason"])
#     apply_vol_page.select_MembershipInfo(data_dict["Disclosure"]["MembershipInfo"])
#     apply_vol_page.saveAndCont(5)
#     apply_vol_page.select_Identity(data_dict["Demographics"]["Identity"])
#     apply_vol_page.select_Ethnicity(data_dict["Demographics"]["Ethnicity"])
#     apply_vol_page.select_Disability(data_dict["Demographics"]["Disability"])
#     apply_vol_page.saveAndCont(6)
#     apply_vol_page.check_Declaration('Automation')


@when(parsers.cfparse('candidate clicks the apply volunteer card for "{usr_cat}"'))
def user_Click_ApplyCard(browser, usr_cat):
	strt_NewApp_page = start_NewAppPage(browser)
	strt_NewApp_page.click_Apply_Card(usr_cat)


@when('clicks continue')
def user_Click_Cont(browser):
	apply_vol_page = apply_VolunteerPage(browser)
	apply_vol_page.click_Continue()


@then('User continues to police check')
def fill_volunteerDetails(browser):
	apply_vol_page = apply_VolunteerPage(browser)
	police_chk_page = police_CheckPage(browser)
	apply_vol_page.click_ContinutPoliceChk()


# police_chk_page.click_Cont_PoliceChk()


@then('User saves app ref to JSON file')
def save_appJSON(browser):
	app_sub_success = app_Submission_SuccessPage(browser)
	app_sub_success.click_ViewApp()
	app_sub_success.save_Appref_JSON()
	app_sub_success.app_logout()


@then(parsers.cfparse('User fills in police check details "{file}"'))
def fill_volunteerDetails(browser, read_JSON, file):
	data_dict = read_JSON(file)
	police_chk_page = police_CheckPage(browser)
	police_chk_page.enter_OtherName(data_dict["PersonalDetails"]["OtherGivenName"])
	police_chk_page.select_OtherName(data_dict["PersonalDetails"]["OtherNameOpt"])
	police_chk_page.select_BirthCountry(data_dict["PersonalDetails"]["BirthCountry"])
	police_chk_page.saveAndCont(0)
	#  time.sleep(2)
	police_chk_page.saveAndCont(1)
	police_chk_page.provide_DL(
		data_dict["DrivingLicense"]["Country"], data_dict["DrivingLicense"]["Number"], data_dict["DrivingLicense"]["State"],
		'data/NSW_Drivers_Licence.png')
	police_chk_page.provide_FireArm_Lic()
	police_chk_page.passport_Details(data_dict["Passport"]["yn"], data_dict["Passport"]["Number"], data_dict["Passport"]["Country"],
	                                 'data/passport.png')
	police_chk_page.saveAndCont(2)
	police_chk_page.commencement_Doc(data_dict["CommenceDoc"]["Type"], data_dict["CommenceDoc"]["Number"],
	                                 'data/citizen.jpg')
	police_chk_page.secondary_Doc1(data_dict["SecDoc1"]["Type"], data_dict["SecDoc1"]["Number"],
	                               'data/transcript.jpg')
	police_chk_page.secondary_Doc2(data_dict["SecDoc2"]["Type"], data_dict["SecDoc2"]["Number"],
	                               'data/certificateID.png')
	police_chk_page.select_DocFormerName()
	police_chk_page.check_SpecialProvisions(data_dict["SpecialProv"]["yn"])
	police_chk_page.saveAndCont(3)
	police_chk_page.check_Consent('Automation')
	police_chk_page.click_Submit()


@then(parsers.cfparse('User fills in police check details for u17 "{file}"'))
def fill_volunteerDetails(browser, read_JSON, file):
	data_dict = read_JSON(file)
	police_chk_page = police_CheckPage(browser)
	police_chk_page.enter_OtherName(data_dict["PersonalDetails"]["OtherGivenName"])
	police_chk_page.select_OtherName(data_dict["PersonalDetails"]["OtherNameOpt"])
	police_chk_page.select_BirthCountry(data_dict["PersonalDetails"]["BirthCountry"])
	police_chk_page.saveAndCont(0)
	#  time.sleep(2)
	police_chk_page.saveAndCont(1)
	police_chk_page.provide_DL(
		data_dict["DrivingLicense"]["Country"], data_dict["DrivingLicense"]["Number"], data_dict["DrivingLicense"]["State"],
		'data/NSW_Drivers_Licence.png')
	police_chk_page.provide_FireArm_Lic()
	police_chk_page.passport_Details(
		data_dict["Passport"]["yn"], data_dict["Passport"]["Number"], data_dict["Passport"]["Country"],
		'data/passport.png')
	police_chk_page.saveAndCont(2)
	police_chk_page.commencement_Doc(data_dict["CommenceDoc"]["Type"], data_dict["CommenceDoc"]["Number"],
	                                 'data/citizen.jpg')
	police_chk_page.secondary_Doc1(data_dict["SecDoc1"]["Type"], data_dict["SecDoc1"]["Number"],
	                               'data/transcript.jpg')
	police_chk_page.secondary_Doc2(data_dict["SecDoc2"]["Type"], data_dict["SecDoc2"]["Number"],
	                               'data/certificateID.png')
	police_chk_page.select_DocFormerName()
	police_chk_page.check_SpecialProvisions(data_dict["SpecialProv"]["yn"])
	police_chk_page.saveAndCont(3)
	police_chk_page.check_Declaration('Automation')
	police_chk_page.chck_Guardian_Const('Guard')
	police_chk_page.click_Submit()


@then('User clicks on user profile and select impersonate user')
def user_impersonate(browser):
	serviceNow_page = serviceNowPage(browser)
	serviceNow_page.click_impersonate_User()


@then('User logs in service now portal for closing policeCheck task')
def serviceNow_Brigade(browser, read_JSON):
	ref = read_JSON('data/appRef.json')
	serviceNow_page = serviceNowPage(browser)
	serviceNow_page.navigate_AdminPortalDashboard("No")
	serviceNow_page.search_AppRef(ref["ref"])
	sn_Brigade_page = serviceNow_BrigadeReview_Page(browser)
	sn_Brigade_page.click_PoliceCheck()
	res_PC = sn_Brigade_page.chk_PCStatus()
	if res_PC == 'Error':
		sn_Brigade_page.click_Task("police failed")
		sn_Brigade_page.close_Task()
		time.sleep(10)
		serviceNow_page.search_AppRef(ref["ref"])
	elif res_PC == 'NoDisclosableCourtOutcomes':
		logging.log("Police check successful, Application approved!!")


# sn_Brigade_page.click_Task("police check")
# sn_Brigade_page.close_Task()


@then(parsers.cfparse('User clicks "{opt}" button'))
def user_Enters_Login_Det(browser, opt):
	create_profile = createProfilePage(browser)
	create_profile.click_Option(opt)


@then(parsers.cfparse('User logs in service now portal for "{approval}" "{action}"'))
def serviceNow_Brigade(browser, read_JSON, approval, action):
	ref = read_JSON('data/appRef.json')
	serviceNow_page = serviceNowPage(browser)
	serviceNow_page.navigate_AdminPortalDashboard("Yes")
	serviceNow_page.search_AppRef(ref["ref"])
	sn_Brigade_page = serviceNow_BrigadeReview_Page(browser)
	if approval == "brigade":
		sn_Brigade_page.click_Task("brigade")
		sn_Brigade_page.close_Task()
		serviceNow_page.search_AppRef(ref["ref"])
		time.sleep(2)
		sn_Brigade_page.click_Approver("Drew Butters", action)
		serviceNow_page.click_Unimpersonate_User()
	# serviceNow_page.approvals_email_Verification(read_JSON, approval)
	elif approval == "district":
		sn_Brigade_page.click_Task("district")
		sn_Brigade_page.close_Task()
		serviceNow_page.search_AppRef(ref["ref"])
		#  time.sleep(2)
		sn_Brigade_page.click_Approver("Jim Darrant", action)
		serviceNow_page.click_Unimpersonate_User()


# serviceNow_page.approvals_email_Verification(read_JSON, approval)


@then(parsers.cfparse('user search for confirmation email for "{approval}"'))
def approval_Email(browser, read_JSON, approval):
	serviceNow_page = serviceNowPage(browser)
	serviceNow_page.navigate_AdminPortalDashboard("Yes")
	serviceNow_page.email_Verification(read_JSON, approval)
	serviceNow_page.click_Unimpersonate_User()


@then('the status of the application is verified')
def app_status(browser, read_JSON):
	ref = read_JSON('data/appRef.json')
	serviceNow_page = serviceNowPage(browser)
	serviceNow_page.navigate_AdminPortalDashboard("Yes")
	serviceNow_page.app_status(ref["ref"])


@then(parsers.cfparse('User search for "{email}"'))
def user_Enters_Login_Det(browser, email):
	serviceNow_page = serviceNowPage(browser)
	serviceNow_page.impersonate_user(email)


@then('User logs in service now portal')
def serviceNow_Brigade(browser):
	app_sub_success = app_Submission_SuccessPage(browser)
	app_sub_success.click_ViewApp()
	appRef = app_sub_success.get_AppRef()
	app_sub_success.logout()
	serviceNowLogin_page = serviceNow_LoginPage(browser)
	serviceNowLogin_page.load()
	serviceNowLogin_page.enter_Credentials("MuhammadK", "Atifrfs22-1!")
	serviceNow_page = serviceNowPage(browser)
	serviceNow_page.navigate_AdminPortalDashboard()
	serviceNow_page.search_AppRef(appRef)


@then('User logs in service now portal for closing serviceCheck task')
def serviceNow_Brigade(browser, read_JSON):
	ref = read_JSON('data/appRef.json')
	serviceNow_page = serviceNowPage(browser)
	serviceNow_page.navigate_AdminPortalDashboard("No")
	serviceNow_page.search_AppRef(ref["ref"])
	sn_Brigade_page = serviceNow_BrigadeReview_Page(browser)
	sn_Brigade_page.click_Task("service check")
	# sn_Brigade_page.close_ServiceCheckTask()
	sn_Brigade_page.close_Task()
	# serviceNow_page.click_Unimpersonate_User()
	time.sleep(5)


@then('User logs in service now portal for reportable conduct approval')
def serviceNow_Brigade(browser, read_JSON):
	ref = read_JSON('data/appRef.json')
	serviceNow_page = serviceNowPage(browser)
	serviceNow_page.navigate_AdminPortalDashboard("No")
	serviceNow_page.search_AppRef(ref["ref"])
	sn_Brigade_page = serviceNow_BrigadeReview_Page(browser)
	sn_Brigade_page.click_Task("reportable")
	sn_Brigade_page.close_Task()


# serviceNow_page.search_AppRef(ref["ref"])
# time.sleep(5)


# Hooks to start and stop the recording session at the beginning and end of the pytest session
def pytest_sessionstart(session):
	print('PYTEST SESSION STARTED')
	pass


def pytest_sessionfinish(session, exitstatus):
	print('PYTEST SESSION CLOSED')
	pass


@pytest.fixture
# This fixture is for file upload
def upload(self, path):
	self.browser.find_element(*self.UPLOAD_COVIDVAC).send_keys(path)


@pytest.fixture
# This fixture is for file upload
def read_JSON(*args):
	"""Loads data from JSON file"""
	
	def _loader(filename):
		with open(filename, 'r') as f:
			print(filename)
			data = json.load(f)
		return data
	
	return _loader


def save_screenshot(self, fileName):
	browser.save_screenshot(f'emembership_sel/data/Screenshots/{fileName}.png')


@pytest.fixture
def generate_random_letter():
	return random.choice(string.ascii_letters)


"""
# ==========================================================
							#Report_CONFIG - CODE [ANALYSIS STAGE]
# ==========================================================
# def pytest_html_report_title(report):
#     timestamp = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
#
#
#     report.title = f"report{timestamp}"

# # Set the HTML report file dynamically
# html_report = f"assets/assets/report{timestamp}.html"
# if config.getoption('--html'):
#     config.option.re('--html') : html_report
#---------------------------------------------------------------------------------------------------------------------------------------------

# ==========================================================
							#CODE FOR RECORDING - ON Testing
# ==========================================================
@pytest.fixture(scope="session")
def browser_recorder_fixture():
	# Create an instance of SeleniumBrowserRecorder
	recorder = SeleniumBrowserRecorder("./Videos", ".mp4")

	# Start the recording session at the beginning of the pytest session
	recorder.start_recording_session()

	yield recorder  # Provide the recorder as a fixture to the tests

	# Stop the recording session at the end of the pytest session
	recorder.stop_recording_session()
#----------------------------------------------------------------------------------------------------------------------------------------------
																																				"""
