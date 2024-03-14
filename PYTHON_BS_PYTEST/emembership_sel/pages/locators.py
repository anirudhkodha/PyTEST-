from selenium.webdriver.common.by import By


class App_Submission_SuccessPage:
	APP_REF = (By.XPATH, '//div[@class="sp-row-content article-content sb-xs row"]/div/span/div/dl/div[1]/dd')
	BTN_VIEW_APP = (By.XPATH, '//button[contains(text(),"View my application")]')
	BTN_LOGOUT = (By.XPATH, '//header/div[1]/div[1]/div[2]/a[1]')
	TXT_SUCCESS = (By.CSS_SELECTOR, "div[class='ng-binding ng-scope']>header>div>h1")
	logout_button = (By.XPATH, "//span[@class='header-nav-text']")


class Apply_VolunteerPage:
	BTN_CONT = (By.CSS_SELECTOR, "button[ng-click='remcover()']")
	LAB_SECTIONS = (By.XPATH, '//label[contains(text(),"Please complete all the following sections before ")]')
	BTN_SAVEVOLOP = (By.XPATH, "(//button[@class='btn btn-default save-and-continue btn-continue'][normalize-space()='Save & continue'])[1]")
	
	BTNS_SAVEANDCONT = (By.XPATH, '//button[contains(text(),"Save & continue")]')
	# How you'd like to volunteer section
	RADIO_FIREFIGHT = (By.XPATH, '//label[@class="radio-element"]/span[text()="Firefighting"]')
	RADIO_OPSUP = (By.XPATH, '//label[@class="radio-element"]/span[text()="Operational support"]')
	RADIO_COMSUP = (By.XPATH, '//label[@class="radio-element"]/span[text()="Community support"]')
	RADIO_BRIGADEAD = (By.XPATH, '//label[@class="radio-element"]/span[text()="Brigade administration"]')
	
	RADIO_CFU_NO = (By.CSS_SELECTOR, '#sp_formfield_vtype_cfu > div > div:nth-child(2) > label > input')
	RADIO_CFU_YES = (By.XPATH, '//label[@class="radio-element"]/span[text()="Community Fire Unit (CFU)"]')
	
	LAB_PREV = (By.XPATH, '//span[contains(text(),"Do you have previous experience working as a volunteer firefighter")]')
	RADIO_PREVEXP_NO = (By.CSS_SELECTOR, '#sp_formfield_vtype_prev_exp > div > div:nth-child(2) > label > input')
	RADIO_PREVEXP_YES = (By.CSS_SELECTOR, '#sp_formfield_vtype_prev_exp > div > div:nth-child(1) > label > input')
	
	# Your brigade section
	SEL_LOCAL_BRIG = (By.CSS_SELECTOR, 'div[id="s2id_sp_formfield_brig_preferred_or_local_brigade"]>a')
	DD_LOCAL_BRIG = (By.XPATH, '//div[@id="select2-drop"]')
	SEARCH_LOCAL_BRIG = (By.XPATH, '//input[@id="s2id_autogen11_search"]')
	Adaminaby = (By.XPATH, '//ul[@id="select2-results-11"]/li/div')
	LOCAL_BRIG_ADD = (By.ID, "sp_formfield_brig_address")
	RADIO_RFSA_YES = (By.CSS_SELECTOR, '#sp_formfield_brig_rfsa > div > div:nth-child(1) > label > input')
	RADIO_RFSA_NO = (By.CSS_SELECTOR, '#sp_formfield_brig_rfsa > div > div:nth-child(2) > label > input')
	
	# Medical History Locators
	RADIO_ROLEAGREE_YES = (By.CSS_SELECTOR, '#sp_formfield_medmen_firefighting_ability > div > div:nth-child(1) > label > input')
	RADIO_ROLEAGREE_NO = (By.CSS_SELECTOR, '#sp_formfield_medmen_firefighting_ability > div > div:nth-child(2) > label > input')
	RADIO_DIABETES_YES = (By.XPATH, '//fieldset[@id="sp_formfield_medical_diabetes"]/div/div/label/span[text()="Yes"]')
	RADIO_DIABETES_NO = (By.XPATH, '//fieldset[@id="sp_formfield_medical_diabetes"]/div/div/label/span[text()="No"]')
	
	RADIO_HRTCOND_YES = (By.XPATH, '//fieldset[@id="sp_formfield_medical_heart_condition"]/div/div/label/span[text()="Yes"]')
	RADIO_HRTCOND_NO = (By.XPATH, '//fieldset[@id="sp_formfield_medical_heart_condition"]/div/div/label/span[text()="No"]')
	
	RADIO_BLOODTHIN_YES = (By.XPATH, '//fieldset[@id="sp_formfield_medical_blood_thinning"]/div/div/label/span[text()="Yes"]')
	RADIO_BLOODTHIN_NO = (By.XPATH, '//fieldset[@id="sp_formfield_medical_blood_thinning"]/div/div/label/span[text()="No"]')
	
	RADIO_MEDVENTOLIN_YES = (By.XPATH, '//fieldset[@id="sp_formfield_medical_ventolin"]/div/div/label/span[text()="Yes"]')
	RADIO_MEDVENTOLIN_NO = (By.XPATH, '//fieldset[@id="sp_formfield_medical_ventolin"]/div/div/label/span[text()="No"]')
	
	RADIO_MEDSEIZURE_YES = (By.XPATH, '//fieldset[@id="sp_formfield_medical_seizure"]/div/div/label/span[text()="Yes"]')
	RADIO_MEDSEIZURE_NO = (By.XPATH, '//fieldset[@id="sp_formfield_medical_seizure"]/div/div/label/span[text()="No"]')
	
	RADIO_OTHERCOND_NO_JUN = (By.XPATH, '//fieldset[@id="sp_formfield_medical_other_conditions_junior"]/div/div/label/span[text()="No"]')
	RADIO_OTHERCOND_YES_JUN = (By.XPATH, '//fieldset[@id="sp_formfield_medical_other_conditions_junior"]/div/div/label/span[text()="Yes"]')
	
	RADIO_OTHRCOND_YES = (By.CSS_SELECTOR, '#sp_formfield_medical_other_conditions_firefighting > div > div:nth-child(1) > label > input')
	RADIO_OTHRCOND_NO = (By.CSS_SELECTOR, '#sp_formfield_medical_other_conditions_firefighting > div > div:nth-child(2) > label > input')
	RADIO_CSOTHER_YES = (By.CSS_SELECTOR, "#sp_formfield_medical_other_conditions_community > div > div:nth-child(1) > label > input")
	RADIO_CSOTHER_NO = (By.CSS_SELECTOR, "#sp_formfield_medical_other_conditions_community > div > div:nth-child(2) > label > input")
	RADIO_OPSOTHER_YES = (By.CSS_SELECTOR, "#sp_formfield_medical_other_conditions_operational > div > div:nth-child(1) > label > input")
	RADIO_OPSOTHER_NO = (By.CSS_SELECTOR, "#sp_formfield_medical_other_conditions_operational > div > div:nth-child(2) > label > input")
	
	RADIO_ADMIN_YES = (By.CSS_SELECTOR, 'body > div:nth-child(1) > section:nth-child(5) > main:nth-child(1) > div:nth-child(2) > div:nth-child(1) > sp-page-row:nth-child(1) > div:nth-child(1) > div:nth-child(1) > span:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > article:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > form:nth-child(2) > div:nth-child(1) > sp-variable-layout:nth-child(1) > fieldset:nth-child(5) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > sp-variable-layout:nth-child(1) > fieldset:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(13) > div:nth-child(1) > span:nth-child(2) > sp-radio-option:nth-child(1) > ng-include:nth-child(1) > fieldset:nth-child(1) > div:nth-child(2) > div:nth-child(1) > label:nth-child(1) > span:nth-child(2)')
	RADIO_ADMIN_NO = (By.CSS_SELECTOR, 'body > div:nth-child(1) > section:nth-child(5) > main:nth-child(1) > div:nth-child(2) > div:nth-child(1) > sp-page-row:nth-child(1) > div:nth-child(1) > div:nth-child(1) > span:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > article:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > form:nth-child(2) > div:nth-child(1) > sp-variable-layout:nth-child(1) > fieldset:nth-child(5) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > sp-variable-layout:nth-child(1) > fieldset:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(13) > div:nth-child(1) > span:nth-child(2) > sp-radio-option:nth-child(1) > ng-include:nth-child(1) > fieldset:nth-child(1) > div:nth-child(2) > div:nth-child(2) > label:nth-child(1) > span:nth-child(2)')
	RADIO_FFChallenge_Yes = (By.CSS_SELECTOR, "fieldset[id='sp_formfield_medmen_firefighting_ability']>div>div>label>input[value='all']")
	RADIO_FFChallenge_N0 = (By.CSS_SELECTOR, "fieldset[id='sp_formfield_medmen_firefighting_ability']>div>div>label>input[value='some']")
	RADIO_CSChallenge_Yes = (By.CSS_SELECTOR, "fieldset[id='sp_formfield_medmen_community_support_administrative_ability']>div>div>label>input[value='all']")
	RADIO_CSChallenge_No = (By.CSS_SELECTOR, "fieldset[id='sp_formfield_medmen_community_support_administrative_ability']>div>div>label>input[value='some']")
	RADIO_OPSChallenge_Yes = (By.CSS_SELECTOR, "fieldset[id='sp_formfield_medmen_operational_support_ability']>div>div>label>input[value='all']")
	RADIO_OPSChallenge_No = (By.CSS_SELECTOR, "fieldset[id='sp_formfield_medmen_operational_support_ability']>div>div>label>input[value='some']")
	RADIO_ADMINOTHER_Yes = (By.CSS_SELECTOR, "fieldset[id='sp_formfield_medical_other_conditions_brigade_administration']>div>div>label>input[value='yes']")
	RADIO_ADMINOTHER_NO = (By.CSS_SELECTOR, "fieldset[id='sp_formfield_medical_other_conditions_brigade_administration']>div>div:nth-child(2)>label>input")
	
	HEALTH_SAFETY_DD = (By.XPATH, '//span[contains(text(),"Health & safety")]')
	VOLUNTEER_OPTION = (By.XPATH, '//span[contains(text(),"like to volunteer")]')
	GUARDIAN_SECTION = (By.XPATH, '// span[contains(text(), "Legal guardian consent")]')
	BRIGADE_OPTION = (By.XPATH, '//span[contains(text(),"Your brigade")]')
	
	RADIO_PSYCHIATRIC_YES = (By.XPATH, '//fieldset[@id="sp_formfield_medical_psychiatric"]/div/div/label/span[text()="Yes"]')
	RADIO_PSYCHIATRIC_NO = (By.XPATH, '//fieldset[@id="sp_formfield_medical_psychiatric"]/div/div/label/span[text()="No"]')
	
	RADIO_MAINT_JUN_YES = (By.XPATH, '//fieldset[@id="sp_formfield_medmen_junior_volunteers"]/div/div/label/span[text()="Yes, I CAN fully undertake all of the above listed activities"]')
	
	RADIO_COVIDVAC_YES = (By.CSS_SELECTOR, '#sp_formfield_medical_covid > div > div:nth-child(1) > label > input')
	RADIO_COVID_EXEMPT = (By.CSS_SELECTOR, '#sp_formfield_medical_covid > div > div:nth-child(2) > label > input')
	RADIO_COVIDVAC_NO = (By.CSS_SELECTOR, '#sp_formfield_medical_covid > div > div:nth-child(3) > label > input')
	LAB_COVIDVAC = (By.CSS_SELECTOR, '#vf_vaccination_certificate_document_file>div>div>label>span:nth-child(2)')
	MSG_COVIDVAC_1 = (By.XPATH, '//*[@id="sp_formfield_medical_covid_fieldmsgs_container"]/div[1]')
	MSG_COVIDVAC_2 = (By.XPATH, '//*[@id="sp_formfield_medical_covid_fieldmsgs_container"]/div[2]')
	
	covid_vacc_upload = '#sp_formfield_vf_vaccination_certificate_document_file';
	UPLOAD_COVIDVAC = (By.XPATH, "//button[@aria-label='Upload Attachment for Click here to upload a copy of your Covid-19 Vaccination Certificate (optional) ']")
	UPLOAD_IDProof = (By.CSS_SELECTOR, "div[class='form-group ng-scope ng-isolate-scope']>span[class='type-sc_attachment field-actual question-width state-mandatory']>div>input[type='file']:nth-child(1)")
	UPLOAD_GUARDIANCONS = (By.CSS_SELECTOR, "div[class='form-group ng-scope ng-isolate-scope']>span[class='type-sc_attachment field-actual question-width state-mandatory']>div>input[type='file']:nth-child(1)")
	
	# Personal Details
	SEL_TITLE = (By.CSS_SELECTOR, 'div[id="s2id_sp_formfield_pdets_title"]>a')
	SEL_GENDER = (By.CSS_SELECTOR, '#s2id_sp_formfield_pdets_gender')
	DD_TITLE = (By.XPATH, '//div[@id="select2-drop"]')
	SEARCH_TITLE = (By.XPATH, '//input[@id="s2id_autogen1_search"]')
	SEARCH_GENDER = (By.XPATH, '//input[@id="s2id_autogen2_search"]')
	TXT_HOMEPHONE = (By.XPATH, '//input[@id="sp_formfield_pdets_home_phone"]')
	TXT_WRKPHONE = (By.XPATH, '//input[@id="sp_formfield_pdets_work_phone"]')
	
	TXT_STREET = (By.XPATH, '//input[@id="sp_formfield_pdets_street_and_house_number"]')
	TXT_SUBURB = (By.XPATH, '//input[@id="sp_formfield_pdets_suburb"]')
	TXT_POSTCODE = (By.XPATH, '//input[@id="sp_formfield_pdets_postcode"]')
	TXT_LIVED = (By.XPATH, '//input[@id="sp_formfield_pdets_lived_there_since"]')
	
	RADIO_POSTADD = (By.CSS_SELECTOR, "#sp_formfield_pdets_postal_address > div > div:nth-child(1) > label > input")
	RADIO_DIFFPOSTADD = (By.CSS_SELECTOR, "#sp_formfield_pdets_postal_address > div > div:nth-child(2) > label > input")
	
	RADIO_VOLORG_YES = (By.CSS_SELECTOR, "#sp_formfield_pdets_another_org > div > div:nth-child(1) > label > input")
	RADIO_VOLORG_NO = (By.CSS_SELECTOR, "#sp_formfield_pdets_another_org > div > div:nth-child(2) > label > input")
	RADIO_VOLORG_NOTTOSAY = (By.CSS_SELECTOR, "#sp_formfield_pdets_another_org > div > div:nth-child(3) > label > input")
	CHK_VOLORG = (By.CSS_SELECTOR, 'input[type="checkbox"]')
	
	# Emergency Contact
	TXT_EM_NAME = (By.XPATH, '//input[@id="sp_formfield_emer_name_of_contact"]')
	TXT_EM_HMEPHONE = (By.XPATH, '//input[@id="sp_formfield_emer_home_or_mobile_number"]')
	TXT_EM_WRKPHONE = (By.XPATH, '//input[@id="sp_formfield_emer_work_number"]')
	SEL_RELTOYOU = (By.XPATH, '//div[@id="s2id_sp_formfield_emer_relationship_to_you"]')
	DD_RELTOYOU = (By.XPATH, '//div[@id="select2-drop"]')
	SEARCH_RELTOYOU = (By.XPATH, '//input[@id="s2id_autogen7_search"]')
	
	# Guardian contact
	Txt_Guardian_Name = (By.XPATH, "//input[@id='sp_formfield_full_name']")
	Txt_Guardian_Email = (By.XPATH, "//input[@id='sp_formfield_email']")
	Txt_Guardian_Mobile = (By.XPATH, "//input[@id='sp_formfield_contact_number']")
	CHK_GUARDIAN_CONST = (By.CSS_SELECTOR, 'span[class="ng-scope"]>label>input[name="i_consent_and_agree_the_above"]')
	Txt_Guardain_Sign = (By.XPATH, "//input[@id='sp_formfield_g_full_name']")
	
	# Disclosures
	reportable_disclosure_text = '//span[contains(text(),"Reportable conduct disclosure")]'
	RADIO_REPORTABLE_YES = (By.CSS_SELECTOR, "#sp_formfield_pconduct_declaration > div > div:nth-child(1) > label > input")
	TXT_REPORTABLE_DET = (By.XPATH, '//textarea[@id="sp_formfield_pconduct_details"]')
	RADIO_REPORTABLE_NO = (By.CSS_SELECTOR, '#sp_formfield_pconduct_declaration > div > div:nth-child(2) > label > input')
	
	criminal_disclosure_text = '//span[contains(text(),"Criminal conduct disclosure")]'
	RADIO_CRIMINAL_YES = (By.CSS_SELECTOR, "#sp_formfield_pconduct_conviction > div > div:nth-child(1) > label > input")
	TXT_CRIMINAL_DET = (By.XPATH, '//textarea[@id="sp_formfield_pconduct_conviction_details"]')
	RADIO_CRIMINAL_NO = (By.CSS_SELECTOR, "#sp_formfield_pconduct_conviction > div > div:nth-child(2) > label > input")
	
	member_disclosure_text = '//span[contains(text(),"Membership conduct disclosure")]';
	RADIO_MEMBER_YES = (By.CSS_SELECTOR, "#sp_formfield_mem_info > div > div:nth-child(1) > label > input")
	RADIO_MEMBER_NO = (By.CSS_SELECTOR, "#sp_formfield_mem_info > div > div:nth-child(2) > label > input")
	
	# Demographical data elements
	identity_que_text = '//span[contains(text(),"Do you identify as an Aboriginal or Torres Strait Islander?")]';
	RADIO_ABORIGINAL = (By.CSS_SELECTOR, "#sp_formfield_demo_identity > div > div:nth-child(1) > label > input")
	RADIO_ISLANDER = (By.CSS_SELECTOR, "#sp_formfield_demo_identity > div > div:nth-child(2) > label > input")
	RADIO_ABO_ISLANDER = (By.CSS_SELECTOR, "#sp_formfield_demo_identity > div > div:nth-child(3) > label > input")
	RADIO_NEITHER = (By.CSS_SELECTOR, "#sp_formfield_demo_identity > div > div:nth-child(4) > label > input")
	
	ethnicity_que_text = '//span[contains(text(),"minority in Australian society")]';
	RADIO_ETHNICITY_YES = (By.CSS_SELECTOR, "#sp_formfield_demo_ethnicity > div > div:nth-child(1) > label > input")
	RADIO_ETHNICITY_NO = (By.CSS_SELECTOR, "#sp_formfield_demo_ethnicity > div > div:nth-child(2) > label > input")
	
	disability_que_text = '//span[contains(text(),"Are you a person with a disability")]';
	RADIO_DISABILITY_YES = (By.CSS_SELECTOR, "#sp_formfield_demo_pwd > div > div:nth-child(1) > label > input")
	RADIO_DISABILITY_NO = (By.CSS_SELECTOR, "#sp_formfield_demo_pwd > div > div:nth-child(2) > label > input")
	RADIO_DISABILITY_NOTTOSAY = (By.CSS_SELECTOR, "#sp_formfield_demo_pwd > div > div:nth-child(3) > label > input")
	
	# Decalartion elements
	CHKBOX_DECLARATION = (By.CSS_SELECTOR, '#sp_formfield_appd_declare')
	TXT_SIGN = (By.XPATH, '//input[@id="sp_formfield_appd_full_name"]')
	
	RADIO_SPECIALPROV = (By.CSS_SELECTOR, "span[class='ng-scope']>label>input[name='pc_pid_cannot_provide']")
	
	# Application Continue
	BTN_CONTINUETOPOLICECHK = (By.XPATH, '//*[@id="catItemTop"]/div[2]/div[2]/div/div[1]/div[2]/button[2]')
	
	BTN_JUN_CONTINUE = (By.CSS_SELECTOR, "div[class='form-group ng-scope']>button:nth-child(2)")
	MODAL_DIALOG = (By.CSS_SELECTOR, "div[class='modal fade ng-isolate-scope in']>div>div>div:nth-child(3)>button")


class Candidate_WelcomePage:
	BTN_STRT_NEW_APP = (By.XPATH, '//span[contains(text(),"Start a new application")]')
	BTN_CONT_APP = (By.XPATH, '//span[contains(text(),"Continue an application")]')
	APP_STATUS = (By.XPATH, '//tbody/tr[1]/td[3]')
	# pop_up = (By.XPATH, "//button[normalize-space()='Agree']")
	pop_up = (By.CSS_SELECTOR, "div[class='modal-dialog ']>div>div>div:nth-child(3)>button")


class CreateProfilePage:
	BTN_APPLY_TO_VOLUNTEER = (By.XPATH, '//a[contains(text(),"Apply to volunteer")]')
	BTN_HOW_TO_APPLY = (By.XPATH, '//a[contains(text(),"How to apply")]')
	BTN_CREATE_PROFILE = (By.XPATH, '//a[contains(text(),"Create a profile")]')
	BTN_LOGIN = (By.XPATH, '//a[contains(text(),"Login")]')
	TXT_FIRSTNAME = (By.XPATH, '//*[@id="first_name"]')
	TXT_PREFFEREDNAME = (By.XPATH, '//input[@id="preferred_name"]')
	TXT_LASTNAME = (By.XPATH, '//*[@id="last_name"]')
	TXT_EMAIL = (By.XPATH, '//*[@id="email"]')
	TXT_MOBILE = (By.XPATH, '//*[@id="rfsphone_number"]')
	TXT_DOB = (By.XPATH, '//input[@id="date_of_birth"]')
	TXT_PASSWORD = (By.XPATH, '//*[@id="password"]')
	TXT_CONFIRM_PASSWORD = (By.XPATH, '//*[@id="confirm_password"]')
	CHKBOX_RECAPTCHA = (By.XPATH, '//*[@id="recaptcha-anchor"]/div[4]')
	RADIO_MEM_NO = (By.CSS_SELECTOR, 'input[id="member-no"]')
	RADIO_MEM_YES = (By.XPATH, '//input[@id="member-yes"]')
	TXT_MEMID = (By.XPATH, "//input[@id='member_id']")
	TXT_ADD_MEMID = (By.XPATH, "//input[@id='additional_member_id']")
	TXT_PREV_BRIGADE = (By.XPATH, "//input[@id='prev_brigade']")
	CHKBOX_AGREE = (By.CSS_SELECTOR, 'input[id="checkbox_agree"]')
	BTN_CREATE_AND_START = (By.CSS_SELECTOR, 'button[type="submit"]')
	HDR_SUBMISSION = (By.XPATH, '//div[@class="article-content"]/h1')
	HDR_CREATEPROFILE = (By.XPATH, '//h1[text()="Create a profile"]')
	HDR_LOGIN = (By.XPATH, '//h1[text()="Log in"]')
	Confirm_mssg = (By.CSS_SELECTOR, 'div[class="article-content"]>h1')
	mail_search = (By.CSS_SELECTOR, 'input[type="search"]')
	mail_Results = (By.CSS_SELECTOR, '.datex.date-calendar')
	preview_mail = (By.XPATH, "//div[normalize-space()='Preview Email']")
	click_here = (By.XPATH, "//a[normalize-space()='click here']")
	logout_button = (By.XPATH, "//span[@class='header-nav-text']")
	EMAIL = (By.XPATH, '//input[@id="username"]')
	PASSWORD = (By.XPATH, '//input[@id="password"]')
	LOGIN_BTN = (By.XPATH, '//button[@type="submit"]')
	BTN_Logout = (By.CSS_SELECTOR, 'body[class="windows chrome ng-scope fixed-header fixed-footer"]>div>header>div>div>div:nth-child(2)>a')
	mssg_Welcome = (By.XPATH, '//div[@id="header-content"]>h1')


class Db_OverviewPage:
	DASHBOARD_HDR = (By.XPATH, '//div[@id="dashboardOverviewHeader"]/div[text()="Dashboards"]')


class LoginPage:
	LOGIN_TEXT = (By.XPATH, '//h1[contains(text(),"Log in")]')
	EMAIL = (By.XPATH, '//input[@id="username"]')
	PASSWORD = (By.XPATH, '//input[@id="password"]')
	LOGIN_BTN = (By.XPATH, '//button[@type="submit"]')
	analyics_Popup = (By.XPATH, '//body[1]/div[1]/div[1]/div[1]/div[1]/div[3]/button[1]')
	analytics_popup = (By.CSS_SELECTOR, 'div[class="modal-dialog "]>div>div>div:nth-child(3)>button')


class Police_CheckPage:
	BTN_CONT_POLICECHK = (By.XPATH, '//*[@id="article-footer"]/div/button')
	BTNS_SAVEANDCONT = (By.XPATH, '//button[contains(text(),"Save & continue")]')
	
	# Personal Details
	TXT_MNAME = (By.XPATH, '//input[@id="sp_formfield_pc_pdets_other_given_names"]')
	RADIO_OTHERNAME_YES = (
		By.CSS_SELECTOR, '#sp_formfield_pc_pdets_other_names > div > div:nth-child(1) > label > input')
	RADIO_OTHERNAME_NO = (
		By.CSS_SELECTOR, '#sp_formfield_pc_pdets_other_names > div > div:nth-child(2) > label > input')
	BTN_OTHERNAME = (By.XPATH, '//button[@class="nswrfs-button is-tertiary has-icon is-add"]')
	MODAL = (By.XPATH, '//div[@class="modal-content"]')
	SEL_BCOUNTRY = (By.CSS_SELECTOR, '#s2id_sp_formfield_pc_pdets_cob')
	DD_BCOUNTRY = (By.XPATH, '//div[@id="select2-drop"]')
	SEARCH_BCOUNTRY = (By.XPATH, '//div[@id="select2-drop"]/div/input')
	# Other Name Modal Window
	RADIO_PASTNAME = (By.CSS_SELECTOR, 'input[id="entry_tname-first"]')
	RADIO_MAIDENNAME = (By.CSS_SELECTOR, 'input[id="entry_tname-maiden"]')
	RADIO_ALIAS = (By.CSS_SELECTOR, 'input[id="entry_tname-alias"]')
	TXT_OTHR_FNAME = (By.XPATH, '//input[@id="entry_fname"]')
	TXT_OTHR_ONAME = (By.XPATH, '//input[@id="entry_oname"]')
	TXT_OTHR_LNAME = (By.XPATH, '//input[@id="entry_lname"]')
	BTN_ADD = (By.CSS_SELECTOR, 'button[class="btn btn-primary ng-scope"]')
	# Residential Address
	BTN_PREVADD = (By.XPATH, '//button[@class="nswrfs-button is-tertiary has-icon is-add m-b-lg"]')
	TXT_OTHR_STREET = (By.XPATH, '//input[@id="street-house-number"]')
	TXT_OTHR_SUBURB = (By.XPATH, '//input[@id="suburb-town"]')
	TXT_OTHR_POSTCODE = (By.CSS_SELECTOR, 'input[id="postcode"]')
	DD_OTHR_COUNTRY = (By.XPATH, '//select[@id="country"]')
	DD_OTHR_STATE = (By.CSS_SELECTOR, 'select[id="state"]')
	TXT_OTHR_SINCE = (By.CSS_SELECTOR, 'input[id="lived-since"]')
	TXT_OTHR_UNTIL = (By.CSS_SELECTOR, 'input[id="lived-until"]')
	# Licence & passprot
	select_input = '//div[@id="select2-drop"]/div/input';
	SEL_DL_TYPE = (By.CSS_SELECTOR, 'div[id="s2id_sp_formfield_pc_licpass_drivers_licence_type"]>a')
	DD_DL_TYPE = (By.XPATH, '//div[@id="select2-drop"]')
	SEARCH_DL_TYPE = (By.XPATH, '//div[@id="select2-drop"]/div/input')
	TXT_DLNUM = (By.XPATH, '//input[@id="sp_formfield_pc_licpass_drivers_licence_number"]')
	SEL_DL_STATE = (By.CSS_SELECTOR, 'div[id="s2id_sp_formfield_pc_licpass_drivers_state_issued"]>a')
	dlConturyIssued = '//div[@id="s2id_sp_formfield_pc_licpass_drivers_country_issued"]/a';
	UPLOPAD_DL = (By.XPATH,
	              '//div[@id="pc_licpass_drivers_file"]/div/span[@class="type-sc_attachment field-actual question-width state-mandatory"]/div/input[@type="file"]')
	
	SEL_FIREL_TYPE = (By.CSS_SELECTOR, 'div[id="s2id_sp_formfield_pc_licpass_firearm_licence_type"]>a')
	TXT_FIRELNUM = (By.XPATH, '//input[@id="sp_formfield_pc_licpass_firearm_licence_number"]')
	SEL_FIREL_STATE = (By.CSS_SELECTOR, 'div[id="s2id_sp_formfield_pc_licpass_firearm_state_issued"]>a')
	firelConturyIssued = '//div[@id="s2id_sp_formfield_pc_licpass_firearm_country_issued"]/a';
	UPLOAD_FIREL = (By.XPATH,
	                '//div[@id="pc_licpass_firearm_file"]/div/span[@class="type-sc_attachment field-actual question-width state-mandatory"]/div/input[@type="file"]')
	
	RADIO_PASSPORT_YES = (By.CSS_SELECTOR, '#sp_formfield_pc_licpass_passport > div > div:nth-child(1) > label > input')
	RADIO_PASSPORT_NO = (By.CSS_SELECTOR, '#sp_formfield_pc_licpass_passport > div > div:nth-child(2) > label > input')
	TXT_PASSPORT_NUM = (By.XPATH, '//input[@id="sp_formfield_pc_licpass_passport_number"]')
	SEL_PASSPORT_COUNTRY = (By.CSS_SELECTOR, 'div[id="s2id_sp_formfield_pc_licpass_passport_country_issued"]>a')
	UPLOAD_PASSPORT = (By.XPATH,
	                   '//div[@id="pc_licpass_passport_file"]/div/span[@class="type-sc_attachment field-actual question-width state-mandatory"]/div/input[@type="file"]')
	
	# Proof Of Indentity
	SEL_COMM_DOC = (By.CSS_SELECTOR, 'div[id="s2id_sp_formfield_pc_pid_comm_document_type"]>a')
	TXT_COMMDOC_NUM = (By.XPATH, '//input[@id="sp_formfield_pc_pid_comm_document_number"]')
	UPLOAD_COMMDOC = (By.XPATH,
	                  '//div[@id="pc_pid_comm_document_file"]/div/span[@class="type-sc_attachment field-actual question-width state-mandatory"]/div/input[@type="file"]')
	
	SEL_PRIMARY_DOC = (By.CSS_SELECTOR, 'div[id="s2id_sp_formfield_pc_pid_primary_document_type"]>a')
	TXT_PRIMARYDOC_NUM = (By.XPATH, '//*[@id="sp_formfield_pc_pid_primary_document_number"]')
	UPLOAD_PRIMARYDOC = (By.XPATH,
	                     '//div[@id="pc_pid_primary_document_file"]/div/span[@class="type-sc_attachment field-actual question-width state-mandatory"]/div/input[@type="file"]')
	SEL_PDOC_STATE = (By.CSS_SELECTOR, 'div[id="s2id_sp_formfield_proof_of_identity_drivers_state_issued"]>a')
	SEL_PDOC_COUNTRY = (By.CSS_SELECTOR, 'div[id="s2id_sp_formfield_proof_of_identity_country_issued"]>a')
	
	SEL_SEC_DOC1 = (By.CSS_SELECTOR, 'div[id="s2id_sp_formfield_pc_pid_secdoc1_document_type"]>a')
	TXT_SECDOC1_NUM = (By.XPATH, '//input[@id="sp_formfield_pc_pid_secdoc1_document_number"]')
	UPLOAD_SECDOC1 = (By.XPATH,
	                  '//div[@id="pc_pid_secdoc1_document_file"]/div/span[@class="type-sc_attachment field-actual question-width state-mandatory"]/div/input[@type="file"]')
	
	SEL_SEC_DOC2 = (By.CSS_SELECTOR, 'div[id="s2id_sp_formfield_pc_pid_secdoc2_document_type"]>a')
	TXT_SECDOC2_NUM = (By.XPATH, '//input[@id="sp_formfield_pc_pid_secdoc2_document_number"]')
	UPLOAD_SECDOC2 = (By.XPATH,
	                  '//div[@id="pc_pid_secdoc2_document_file"]/div/span[@class="type-sc_attachment field-actual question-width state-mandatory"]/div/input[@type="file"]')
	
	RADIO_CHNGNAME_YES = (
		By.CSS_SELECTOR, '#sp_formfield_pc_pid_document_former_name > div > div:nth-child(1) > label > input')
	RADIO_CHNGNAME_NO = (
		By.CSS_SELECTOR, '#sp_formfield_pc_pid_document_former_name > div > div:nth-child(2) > label > input')
	
	# CHKBOX_SPECIALPROV = (By.CSS_SELECTOR,'#sp_formfield_pc_pid_cannot_provide')
	# CHKBOX_SPECIALPROV =(By.XPATH, "//input[@id='sp_formfield_pc_pid_cannot_provide']")
	CHKBOX_SPECIALPROV = (By.CSS_SELECTOR,
	                      "sp-checkbox-group[class='checkbox-container ng-scope ng-isolate-scope']>fieldset>div>div>div>div>div>span>span>label>input[id='sp_formfield_pc_pid_cannot_provide']")
	# CHKBOX_SPECIALPROV=(By.XPATH, '//*[@id="sp_formfield_pc_pid_cannot_provide"]')
	firearm_No = (By.XPATH, "(//span[normalize-space()='No, I do not have a firearms licence'])[1]")
	
	# informed consent
	CHKBOX_CONSENT = (By.CSS_SELECTOR, '#sp_formfield_pc_ic_consent')
	# CHKBOX_CONSENT17 = (By.CSS_SELECTOR, "span[class='ng-scope']>label>input[name='i_consent_and_agree_the_above']")
	CHKBOX_CONSENT17 = (By.CSS_SELECTOR, "span[class ='ng-scope'] > label > input[name='pc_ic_parent_lg_consent']")
	TXT_CONSENT_FNAME = (By.XPATH, '//input[@id="sp_formfield_pc_ic_full_name"]')
	TXT_CONSENTU17_FNAME = (By.CSS_SELECTOR, "span[class='ng-scope']>input[name='pc_ic_full_name_parent']")
	
	BTN_SUBMIT = (By.XPATH, 'button[class="btn btn-primary ng-binding ng-scope"]')
	
	HDR_SUBMITTED = (By.XPATH, '//h1[contains(text(),"Application successfully submitted")]')
	MSG_SUBMITTED = (By.XPATH, '//div[@id="header-content"]/p')
	CHKBOX_DECLARATION = (By.CSS_SELECTOR, '#sp_formfield_pc_ic_consent')
	TXT_SIGN = (By.XPATH, '//input[@id="sp_formfield_pc_ic_full_name"]')
	CHK_GUARDIAN_CONST = (By.CSS_SELECTOR, '#sp_formfield_pc_ic_parent_lg_consent')
	Txt_Guardain_Sign = (By.XPATH, "//input[@id='sp_formfield_pc_ic_full_name_parent']")


class ServiceNow_BrigadeReview_Page:
	TAB_TASK = (By.XPATH, '//div[@id="tabs2_list"]/span[1]/span[1]')
	TAB_POLICECHECK = (By.XPATH, '//div[@id="tabs2_list"]/span[4]/span[1]')
	TAB_MEMSHIPAPP = (By.XPATH, '//div[@id="tabs2_list"]/span[3]/span[1]')
	CHK_FORMERID = (By.CSS_SELECTOR, "span[class='input-group-checkbox']>input[id='ni.x_nswr2_rfs_emembe_emembership_application.former_member']")
	TXT_MEMID = (By.CSS_SELECTOR, "div[class='col-xs-10 col-sm-9 col-md-6 col-lg-5 form-field input_controls']>input[id='x_nswr2_rfs_emembe_emembership_application.member_id']")
	APP_TYPE = (By.XPATH, '//table[@id="x_nswr2_rfs_emembe_emembership_case.x_nswr2_rfs_emembe_emembership_application.case_number_table"]/tbody/tr/td[3]//a')
	BTN_UPDATE = (By.CSS_SELECTOR, "div[class='form_action_button_container']>button[id='sysverb_update_bottom']")
	TASK_BRIGADEREVIEW = (By.XPATH, '//a[contains(text(),"Brigade Review")]')
	TASK_HEALTHREVIEW = (By.XPATH, '//a[contains(text(),"Health and Safety Review")]')
	TASK_REPORTABLE = (By.XPATH, '//a[contains(text(),"Reportable Conduct Review")]')
	TASK_DISTRICTREVIEW = (By.XPATH, '//a[contains(text(),"District Review")]')
	TASK_SERVICECHECK = (By.XPATH, '//a[contains(text(),"Service Check")]')
	TASK_SPECIALPROVISION = (By.XPATH, '//a[contains(text(),"Review Special Provision")]')
	TASK_POLICEFAILED = (By.XPATH, '//a[contains(text(),"eMembership Application related police check submi")]')
	TASK_POLICERESULTS = (By.XPATH, '//a[contains(text(),"Review police check results task")]')
	BTN_TASK_CLOSED = (By.XPATH, '//button[@id="sn_customerservice_task_closed_bottom"]')
	TAB_APPROVERS = (By.XPATH, '//div[@id="tabs2_list"]/span[2]/span[1]')
	BTN_SEARCH_APPROVER = (By.XPATH, '//thead/tr[@id="hdr_x_nswr2_rfs_emembe_emembership_case.sysapproval_approver.sysapproval"]/th[2]/div[1]/button[1]')
	DIV_APPROVER = (By.XPATH, '//a[contains(text(),"Jim Darrant")]/ancestor::tr')
	APPROVER = (By.XPATH, '//table[@id="x_nswr2_rfs_emembe_emembership_case.sysapproval_approver.sysapproval_table"]/tbody/tr/td[3]/a[contains(text(),"Requested")]')
	BTN_APPROVED = (By.XPATH, '//button[@id="approve_bottom"]')
	BTN_REJECTED = (By.XPATH, '//button[@id="reject_bottom"]')
	PC_STATUS = (By.XPATH, '//table[@id="x_nswr2_rfs_emembe_emembership_case.x_nswr2_rfs_emembe_police_check.u_case_number_table"]/tbody/tr/td[6]')
	BTN_SRCHAPP = (By.XPATH, '//*[@id="x_nswr2_rfs_emembe_emembership_case.sysapproval_approver.sysapproval_hide_searchinput"]/div/div/input[@type ="search"]')
	BTN_SP = (By.XPATH, '//div[@id="x_nswr2_rfs_emembe_emembership_case.sysapproval_approver.sysapproval_list"]/span/div[2]/div/div/span/div/div/input')
	Srch_RES = (By.XPATH, '//table[@id="x_nswr2_rfs_emembe_emembership_case.sysapproval_approver.sysapproval_table"]/tbody/tr[1]/td[3]/a')
	icon_Filter = (By.XPATH, '//div[@id="x_nswr2_rfs_emembe_emembership_case.sysapproval_approver.sysapproval_list"]/span/div[2]/div/div/div/a')
	choose_Field = (By.XPATH, '//table[@id="x_nswr2_rfs_emembe_emembership_case.sysapproval_approver.sysapprovalfilters_table"]/tbody/tr/td/table/tbody/tr[3]/td/table/tbody/tr/td[2]/div')
	input_filterFieldApp = (By.XPATH, '//div[@class="select2-search"]/input')
	input_filterAppValue = (By.XPATH, '//table[@class="sn-filter-clause sn-animate-filter-clause"]/tbody/tr[3]/td/table/tbody/tr/td[4]/input[2]')
	btn_filterAdd = (By.XPATH, '//table[@class="sn-filter-clause sn-animate-filter-clause"]/tbody/tr[3]/td/table/tbody/tr/td[5]/button')
	input_filterFieldApp2 = (By.XPATH, '//div[@id="select2-drop"]/div/input')
	state_tble = (By.XPATH, '//table[@id="x_nswr2_rfs_emembe_emembership_case.sysapproval_approver.sysapproval_table"]/thead/tr[2]/td[3]/div/div/div/input')
	pc_Status = (By.XPATH, '//table[@id="x_nswr2_rfs_emembe_emembership_case.x_nswr2_rfs_emembe_police_check.u_case_number_table"]/tbody/tr/td[6]')
	txt_Comments = (By.CSS_SELECTOR, "#activity-stream-textarea")
	btn_Post = (By.XPATH, "//button[normalize-space()='Post']")
	email_Check = (By.CSS_SELECTOR, "div[id='sn_form_inline_stream_container']>div>ul>li:nth-child(1)>div:nth-child(3)>div>ul>li:nth-child(2)>span:nth-child(2)")


class ServiceNowPage:
	DASHBOARD_HDR = (By.XPATH, '//div[@id="dashboardOverviewHeader"]/div[text()="Dashboards"]')
	BTN_DB_OVERVIEW = (By.CSS_SELECTOR, 'button[data-original-title="Dashboards Overview"]')
	TXT_APPNO_SEARCH = (By.XPATH, '//input[@id="x_nswr2_rfs_emembe_emembership_case_table_header_search_control"]')
	SEARCH_RES = (By.XPATH, '//table[@id="x_nswr2_rfs_emembe_emembership_case_table"]/tbody/tr[1]/td[3]/a')
	BTN_Search = (By.CSS_SELECTOR, 'body > div:nth-child(2) > div:nth-child(3) > span:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > span:nth-child(2) > div:nth-child(2) > div:nth-child(1) > input:nth-child(3)')
	choice_Dropdown = (By.CSS_SELECTOR, 'body > div:nth-child(2) > div:nth-child(3) > span:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > span:nth-child(2) div:nth-child(2) > div:nth-child(1)  >span > span > select')
	Open_App = (By.CSS_SELECTOR, "div[data-original-title='Open Applications by Stage']")
	mail_search = (By.CSS_SELECTOR, 'input[type="search"]')
	open_Task = By.XPATH, "//div[contains(text(),'Open Tasks')]"
	mail_Results = (By.CSS_SELECTOR, '.datex.date-calendar')
	preview_mail = (By.XPATH, "//div[normalize-space()='Preview Email']")
	click_here = (By.XPATH, "//a[normalize-space()='click here']")
	logout_button = (By.XPATH, "//span[@class='header-nav-text']")
	dropdown_subject = (By.CSS_SELECTOR, "select[role='listbox']")
	txt_Recepients = (By.CSS_SELECTOR, "input[id='sys_email_table_header_search_control']")
	nsw_Logo = (By.CSS_SELECTOR, '#header-logo-image')
	txt_Subject = (By.CSS_SELECTOR, "input[aria-label='Search column: subject']")
	txt_subjectSearch = (By.CSS_SELECTOR, "div[class='container-fluid ']>span>div>div>input")
	filter_item = (By.CSS_SELECTOR, "div[id='x_nswr2_rfs_emembe_emembership_case_list']>span>div>div>div>div>a")
	cross_Button = (By.CSS_SELECTOR, "div[class='filterContainer']>table>tbody>tr:nth-child(2)>td>table>tbody>tr>td>table>tbody>tr:nth-child(3)>td>table>tbody>tr>td:nth-child(6)>button")
	run_Button = (By.CSS_SELECTOR, "div[class='filterToolbar']>button")


class ServiceNow_LoginPage:
	SERVICENOW_HDR_TXT = (By.XPATH, '//div[contains(text(),"nswrfsuat.service-now.com")]')
	NOTACCT = (By.LINK_TEXT, "Not your account?")
	USERNAME = (By.CSS_SELECTOR, 'input[name="username"]')
	PASSWORD = (By.CSS_SELECTOR, 'input[name="password"]')
	LOGIN_BTN = (By.CSS_SELECTOR, 'button[type="submit"][name="submit"]')
	DSHBRD = (By.XPATH, "//button[normalize-space()='Create a dashboard']")
	
	USERNAME_STANDLONE = (By.CSS_SELECTOR, "input[type='text']")
	PASSWORD_STANDALONE = (By.CSS_SELECTOR, "input[type='password']")
	NEXT_BTN = (By.CSS_SELECTOR, "input[value='Next']")
	VERIFY_BTN = (By.CSS_SELECTOR, "input[value='Verify']")
	DSHBRD = (By.XPATH, "//button[normalize-space()='Create a dashboard']")
	OKTALOGINCONTAINER = (By.ID, "signin-container")


class Start_NewAppPage:
	APP_CARDS = (By.CSS_SELECTOR, '.h4.card-heading')
	CARD_APPLY_VOLUNTEER = (By.XPATH, '//article[@class="nswrfs-card is-plain is-compact has-icon"]')
	# CARD_APPLY_TRANSFER = (By.XPATH, "//a[contains(text(), 'Transfer to another brigade')]")
	CARD_APPLY_TRANSFER = (By.XPATH, '(//article[@class="nswrfs-card is-plain is-compact has-icon"])[2]')
	CARD_U17_ORD = (By.XPATH, '(//article[@class="nswrfs-card is-plain is-compact has-icon"])[2]')


class SAP_LoginPage:
	LOGON_BOX = (By.CSS_SELECTOR, 'table[id="tblInnerCnt"]')
	USER = (By.CSS_SELECTOR, '#logonuidfield')
	PASS = (By.CSS_SELECTOR, '#logonpassfield')
	BTN_LOGON = (By.CSS_SELECTOR, 'input[type="submit"][value="Log On"]')
