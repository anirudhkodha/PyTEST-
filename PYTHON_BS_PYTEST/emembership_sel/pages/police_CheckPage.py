"""
This module contains police check page for volunteers
"""
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from pages.locators import Police_CheckPage


class police_CheckPage:

    URL = 'https://nswrfsuat.service-now.com/rfsembr?id=embr_login'

    def __init__(self, browser):
        self.browser = browser

      # Interaction Methods
    def load(self):
        self.browser.get(self.URL)


    def saveAndCont(self, i):
        saveNCont = self.browser.find_elements(*Police_CheckPage.BTNS_SAVEANDCONT)
        saveNCont[i].click()    

    def click_Cont_PoliceChk (self):
        self.browser.find_element(*Police_CheckPage.BTN_CONT_POLICECHK).click()


    def enter_OtherName(self, oname):
        self.browser.find_element(*Police_CheckPage.TXT_MNAME).send_keys(oname)

    def select_OtherName(self, yn):
        if yn == 'Yes':
            self.browser.execute_script(
                "document.querySelector(arguments[0],':before').click();", Police_CheckPage.RADIO_OTHERNAME_YES)
            wait = WebDriverWait(self.browser, 10)
            wait.until(EC.element_to_be_clickable(Police_CheckPage.BTN_OTHERNAME))
            self.click_Add_OtherName()
        else:
            self.browser.execute_script(
                "document.querySelector(arguments[0],':before').click();", Police_CheckPage.RADIO_OTHERNAME_NO)

    def click_Add_OtherName(self):   
        wait = WebDriverWait(self.browser, 10)
        self.browser.find_element(*Police_CheckPage.BTN_OTHERNAME).click()
        wait.until(EC.presence_of_element_located(*Police_CheckPage.MODAL))
    def add_OtherName(self, *argv):
        nameType = argv[0].lower()
        if nameType == 'past name':
            self.browser.execute_script(
                "document.querySelector(arguments[0],':before').click();", Police_CheckPage.RADIO_PASTNAME)
        elif nameType == 'maiden name':
            self.browser.execute_script(
                "document.querySelector(arguments[0],':before').click();", Police_CheckPage.RADIO_MAIDENNAME)
        elif nameType == 'alias':
            self.browser.execute_script(
                "document.querySelector(arguments[0],':before').click();", Police_CheckPage.RADIO_ALIAS)
        self.browser.find_element(*Police_CheckPage.TXT_OTHR_FNAME).send_keys(argv[1])
        self.browser.find_element(*Police_CheckPage.TXT_OTHR_ONAME).send_keys(argv[2])
        self.browser.find_element(*Police_CheckPage.TXT_OTHR_LNAME).send_keys(argv[3])
        self.browser.execute_script(
                "document.querySelector(arguments[0],':before').click();", Police_CheckPage.BTN_ADD)
        wait = WebDriverWait(self.browser, 10)
        wait.until(EC.presence_of_element_located((By.XPATH,'//div[@id="pc_pdets_onames"]')))
        assert self.browser.find_element(By.CSS_SELECTOR,'tr[class="ng-scope"]:nth-child(1)>th').text.lower() == nameType
        assert self.browser.find_element(By.CSS_SELECTOR,'tr[class="ng-scope"]:nth-child(1)>td[class="ng-binding"]').text.strip() == argv[1]+" "+argv[2]+" "+argv[3]

    def select_BirthCountry(self,cob):
        self.select_DD_Option(cob,Police_CheckPage.SEL_BCOUNTRY)

    def click_Add_OtherAdd(self):   
        wait = WebDriverWait(self.browser, 10)        
        wait.until(EC.element_to_be_clickable(Police_CheckPage.BTN_PREVADD))
        self.browser.find_element(*Police_CheckPage.BTN_PREVADD).click()
        wait.until(EC.presence_of_element_located(*Police_CheckPage.MODAL))

    def add_OtherAdd(self, *argv):
        #if Australia then pass the last argument as state
        self.browser.find_element(*Police_CheckPage.TXT_OTHR_STREET).send_keys(argv[0])
        self.browser.find_element(*Police_CheckPage.TXT_OTHR_SUBURB).send_keys(argv[1])
        Select(self.browser.find_element(*Police_CheckPage.DD_OTHR_COUNTRY)).select_by_visible_text(argv[2])
        if(argv[2]=='Australia'):
           Select(self.browser.find_element(self.locator.DD_OTHR_STATE)).select_by_visible_text(argv[6])
        self.browser.find_element(*Police_CheckPage.TXT_OTHR_POSTCODE).send_keys(argv[3])
        self.browser.find_element(*Police_CheckPage.TXT_OTHR_SINCE).send_keys(argv[4])
        self.browser.find_element(*Police_CheckPage.TXT_OTHR_UNTIL).send_keys(argv[5])
        self.browser.execute_script(
                "document.querySelector(arguments[0],':before').click();", self.locator.BTN_ADD)
        wait = WebDriverWait(self.browser, 10)
        wait.until(EC.presence_of_element_located((By.XPATH,'//div[@class="table-responsive ng-scope"]')))
        if(argv[2]=='Australia'):
            assert self.browser.find_element(By.CSS_SELECTOR,'#pc_resadd_past_addresses>div>span>div>div>div>table>tbody>tr:nth-child(1)>td:nth-child(1)').text.strip() == argv[0]+" "+argv[1]+" "+argv[6]+" "+argv[3]+" "+argv[2]
        else:
            assert self.browser.find_element(By.CSS_SELECTOR,'#pc_resadd_past_addresses>div>span>div>div>div>table>tbody>tr:nth-child(1)>td:nth-child(1)').text.strip() == argv[0]+" "+argv[1]+" "+argv[3]+" "+argv[2]
        assert self.browser.find_element(By.CSS_SELECTOR,'#pc_resadd_past_addresses>div>span>div>div>div>table>tbody>tr:nth-child(1)>td:nth-child(2)').get_attribute("innerHTML").strip() == argv[4]+" - "+argv[5]
       
    def provide_DL(self, *argv):        
        wait = WebDriverWait(self.browser, 10) 
        if argv[0] == 'Not Applicable': 
            wait.until(EC.invisibility_of_element_located(Police_CheckPage.TXT_DLNUM))
        else:
            self.select_DD_Option(argv[0],Police_CheckPage.SEL_DL_TYPE)
            self.browser.find_element(*Police_CheckPage.TXT_DLNUM).send_keys(argv[1])
            self.select_DD_Option(argv[2],Police_CheckPage.SEL_DL_STATE)
            self.upload_file(Police_CheckPage.UPLOPAD_DL, argv[3])
            time.sleep(10)

    def provide_FireArm_Lic(self, *argv):
        wait = WebDriverWait(self.browser, 10)
        if argv[0] == 'Not Applicable':
            self.browser.find_element(*Police_CheckPage.firearm_No).click()
            # wait.until(EC.invisibility_of_element_located((self.firearm_No)).click()
        else:
            self.select_DD_Option(argv[0],Police_CheckPage.SEL_FIREL_TYPE)
            self.browser.find_element(*Police_CheckPage.TXT_FIRELNUM).send_keys(argv[1])
            self.select_DD_Option(argv[2],Police_CheckPage.SEL_FIREL_STATE)
            self.upload_file(Police_CheckPage.UPLOAD_FIREL, argv[3])
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"#pc_licpass_firearm_file>div>span>div>a")))

    def provide_FireArm_Lic(self):
        wait = WebDriverWait(self.browser, 10)
        # if argv[0] == 'Not Applicable':
        self.browser.find_element(*Police_CheckPage.firearm_No).click()


    def passport_Details(self, *argv):
        wait = WebDriverWait(self.browser, 10) 
        if argv[0] == 'No':
            self.browser.execute_script(
                "document.querySelector(arguments[0],':before').click();", Police_CheckPage.RADIO_PASSPORT_NO)
            wait.until(EC.invisibility_of_element_located(*Police_CheckPage.TXT_PASSPORT_NUM))
        else:
            self.browser.execute_script(
                "document.querySelector(arguments[0],':before').click();", Police_CheckPage.RADIO_PASSPORT_YES)
            self.browser.find_element(*Police_CheckPage.TXT_PASSPORT_NUM).send_keys(argv[1])
            self.select_DD_Option(argv[2],Police_CheckPage.SEL_PASSPORT_COUNTRY)
            self.upload_file(Police_CheckPage.UPLOAD_PASSPORT,argv[3])
            wait = WebDriverWait(self.browser, 10)  
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"#pc_licpass_passport_file>div>span>div>a")))

    def commencement_Doc(self, *argv):
        wait = WebDriverWait(self.browser, 10)
        wait.until(EC.visibility_of_element_located((By.XPATH,"//label[contains(text(),'Commencement document')]")))
        self.select_DD_Option(argv[0],Police_CheckPage.SEL_COMM_DOC)
        self.browser.find_element(*Police_CheckPage.TXT_COMMDOC_NUM).send_keys(argv[1])
        self.upload_file(Police_CheckPage.UPLOAD_COMMDOC,argv[2])
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"#pc_pid_comm_document_file>div>span>div>a")))

    def primary_Doc(self, *argv):
        wait = WebDriverWait(self.browser, 10)
        self.select_DD_Option(argv[0],Police_CheckPage.SEL_PRIMARY_DOC)
        if argv[0] == 'Driver\'s licence' or 'Shooters or firearms licence':
            self.select_DD_Option(argv[1],Police_CheckPage.SEL_PDOC_STATE)
        elif argv[0] == 'Foreign passport':
            self.select_DD_Option(argv[1],Police_CheckPage.SEL_PDOC_COUNTRY)
        self.browser.find_element(*Police_CheckPage.TXT_PRIMARYDOC_NUM).send_keys(argv[2])
        self.upload_file(Police_CheckPage.UPLOAD_COMMDOC,argv[3])
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"#pc_pid_primary_document_file>div>span>div>a")))

    def secondary_Doc1(self, *argv):
        wait = WebDriverWait(self.browser, 10)
        self.select_DD_Option(argv[0],Police_CheckPage.SEL_SEC_DOC1)
        self.browser.find_element(*Police_CheckPage.TXT_SECDOC1_NUM).send_keys(argv[1])
        self.upload_file(Police_CheckPage.UPLOAD_SECDOC1,argv[2])
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"#pc_pid_secdoc1_document_file>div>span>div>a")))

    def secondary_Doc2(self, *argv):
        wait = WebDriverWait(self.browser, 10)
        self.select_DD_Option(argv[0],Police_CheckPage.SEL_SEC_DOC2)
        self.browser.find_element(*Police_CheckPage.TXT_SECDOC2_NUM).send_keys(argv[1])
        self.upload_file(Police_CheckPage.UPLOAD_SECDOC2,argv[2])
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"#pc_pid_secdoc2_document_file>div>span>div>a")))

    def select_DocFormerName(self):
        #keeping it fixed no as already too many options selected
        self.browser.execute_script(
                "document.querySelector(arguments[0],':before').click();", Police_CheckPage.RADIO_CHNGNAME_NO)

    def check_SpecialProvisions(self, yn):
        if yn == 'Yes':
             self.browser.execute_script(
                "document.querySelector(arguments[0],':before').click();", Police_CheckPage.CHKBOX_SPECIALPROV)
            # elem = self.browser.find_element(*self.CHKBOX_SPECIALPROV)
            # elem.click()
        else:
            None


    def check_Declaration(self, sign):
        self.browser.execute_script(
                "document.querySelector(arguments[0],':before').click();", Police_CheckPage.CHKBOX_DECLARATION)
        #self.browser.find_element(*self.TXT_SIGN).click()
        self.browser.find_element(*Police_CheckPage.TXT_SIGN).send_keys(sign)

    def chck_Guardian_Const(self, sign):
        self.browser.execute_script(
            "document.querySelector(arguments[0],':before').click();", Police_CheckPage.CHK_GUARDIAN_CONST)
        self.browser.find_element(*Police_CheckPage.Txt_Guardain_Sign).send_keys(sign)

    def check_Consent(self, sign):
        self.browser.execute_script(
                "document.querySelector(arguments[0],':before').click();", Police_CheckPage.CHKBOX_CONSENT)
        self.browser.find_element(*Police_CheckPage.TXT_CONSENT_FNAME).send_keys(sign)

    def check_Consent_U17(self, sign):
        self.browser.execute_script(
                "document.querySelector(arguments[0],':before').click();", Police_CheckPage.CHKBOX_CONSENT17)
        self.browser.find_element(*Police_CheckPage.TXT_CONSENTU17_FNAME).send_keys(sign)

    def click_Submit(self):
        self.browser.execute_script(
                "document.querySelector(arguments[0],':before').click();", Police_CheckPage.BTN_SUBMIT)
        #self.browser.find_element(*self.BTN_SUBMIT).click()
        print('h2')      
        wait = WebDriverWait(self.browser, 10)
        wait.until(EC.visibility_of_element_located(Police_CheckPage.HDR_SUBMITTED))
        assert "being reviewed" in self.browser.find_element(*Police_CheckPage.MSG_SUBMITTED).text

    #common Methods
    def select_DD_Option(self,*argv):        
        wait = WebDriverWait(self.browser, 10)
        self.browser.implicitly_wait(10)            
        wait.until(EC.element_to_be_clickable(argv[1]))
        self.browser.execute_script(
                "document.querySelector(arguments[0]).click();", argv[1])       
        self.browser.find_element(*argv[1]).click()
        wait.until(EC.visibility_of_element_located((By.XPATH,'//div[@id="select2-drop"]')))      
        self.browser.find_element(By.XPATH,'//div[@id="select2-drop"]/div/input').send_keys(argv[0]+Keys.RETURN)

    def enter_License_Num(self, num):
        self.browser.find_element(*Police_CheckPage.TXT_DLNUM).send_keys(num)

    def upload_file(self,*argv):
        self.browser.find_element(*argv[0]).send_keys(argv[1])