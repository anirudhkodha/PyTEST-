from pytest_bdd import scenarios, parsers, given, when, then
from pages.apply_VolunteerPage import apply_VolunteerPage
import time
import pathlib

scenarios('../features/U16_E2E.feature')


@then(parsers.cfparse('candidate fills in junior volunteer details "{file}"'))
def fill_volunteerDetails_Admin(browser, read_JSON, file):
	data_dict = read_JSON(file)
	apply_vol_page = apply_VolunteerPage(browser)
	apply_vol_page.check_Junior_Role()
	apply_vol_page.select_LocalBrigade(data_dict["Brigade"]["Name"])
	apply_vol_page.select_RFSA(data_dict["Brigade"]["RFSA"])
	time.sleep(2)
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
	apply_vol_page.select_COVID('NO', 'C:\Pytest servicenow\ServiceNow\emembership_sel\data\sample.pdf')
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
	apply_vol_page.select_IDProof('data/sample.pdf')
	time.sleep(2)
	apply_vol_page.select_GuardianProof('Yes', 'data/sample.pdf')
	time.sleep(2)
	apply_vol_page.chck_Guardian_Const('Guard')
	apply_vol_page.saveAndCont(6)
	time.sleep(5)
	apply_vol_page.check_Declaration('Automation')
	apply_vol_page.Juncontinue()
