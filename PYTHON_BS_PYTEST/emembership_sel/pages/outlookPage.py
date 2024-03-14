"""
This module contains login page for volunteers,
the page object for the TL Consulting Home page.
"""
from operator import contains
import time
import pytest
import os.path
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.alert import Alert



class outlookPage:

    URL = 'https://outlook.office365.com/'
    count = 0

    TXT_EMAIL= (By.XPATH, '//input[@type="email"]')
    BTN_NEXT = (By.XPATH,'//input[@type="submit"]')
    TXT_USERNAME = (By.XPATH, '//input[@id="username"]')
    TXT_PASSWORD = (By.XPATH,'//input[@type="password"]')
    TXT_EML = (By.XPATH,'//input[@type="text"]')
    BTN_PROFILE = (By.XPATH,'//*[@id="O365_MainLink_MePhoto"]')
    LINK_MAILBOX = (By.XPATH, '//*[@id="mectrl_OwaOpenTargetMailboxLink"]')
    TXT_COMBOBOX = (By.XPATH, '//input[@role="combobox"]')
    BTN_SIGNIN = (By.XPATH, '//span[contains(text(),"Sign in")]')
    TXT_EMAIL_SEARCH = (By.XPATH, '//input[@aria-label="Search email and people, type your search term then press enter to search."]')

    def __init__(self, browser):
        self.browser = browser        
        self.browser.maximize_window()
      # Interaction Methods
    def load(self):
        self.browser.get(self.URL)

    # def enter_Creds (self, usr, pwd):
    #     wait = WebDriverWait(self.browser, 10)
    #     self.browser.find_element(*self.TXT_EMAIL).send_keys(usr)
    #     self.browser.find_element(*self.BTN_NEXT).click()
    #     wait.until(EC.visibility_of_element_located(self.TXT_EML))
    #     self.browser.find_element(*self.BTN_NEXT).click()
    #     wait.until(EC.visibility_of_element_located(self.TXT_PASSWORD))
    #     self.browser.find_element(*self.TXT_PASSWORD).send_keys(pwd)
    #     self.browser.find_element(*self.BTN_NEXT).click()
    #     if self.is_staySignedin_prompt():
    #         wait.until(EC.visibility_of_element_located((By.XPATH,'//div[contains(text(),"Stay signed in?")]')))
    #     self.browser.find_element(By.XPATH,"//input[@type='button'and @value='No']").click()
    #     wait.until(EC.title_contains("Email"))

    def is_staySignedin_prompt(self):
        try:
            self.browser.find_element(By.XPATH, '//div[contains(text(),"Stay signed in?")]')
            return True
        except:
            return False 
    
    def open_AnotherMail(self, usr, pwd, mailbox):
        wait = WebDriverWait(self.browser, 10)
        self.browser.find_element(*self.BTN_PROFILE).click()
        wait.until(EC.visibility_of_element_located((By.XPATH,'//div[text()="NSW Rural Fire Service"]')))
        self.browser.find_element(*self.LINK_MAILBOX).click()
        wait.until(EC.visibility_of_element_located((By.XPATH,'//div[text()="Open another mailbox"]')))
        self.browser.find_element(*self.TXT_COMBOBOX).send_keys(mailbox)
        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[contains(text(),"results")]')))
        self.browser.find_element(By.XPATH,'//*[@id="sug-0"]').click()
        self.browser.find_element(By.XPATH, '//span[text()="Open"]').click()
        window_before = self.browser.window_handles[0]
        window_after = self.browser.window_handles[1]
        self.browser.switch_to.window(window_after)
        wait.until(EC.visibility_of_element_located((By.XPATH,'//a[contains(@href,"https://webmail.rfs.nsw.gov.au/")]')))
        self.browser.find_element(By.XPATH, '//a[contains(@href,"https://webmail.rfs.nsw.gov.au/")]').click()
        wait.until(EC.title_is('Outlook'))
        self.browser.find_element(*self.TXT_USERNAME).clear()
        self.browser.find_element(*self.TXT_USERNAME).send_keys(usr)
        self.browser.find_element(*self.TXT_PASSWORD).send_keys(pwd) 
        self.browser.find_element(*self.BTN_SIGNIN).click()
        try:
            wait.until (EC.visibility_of_element_located((By.XPATH,'//div[@class="_fce_Z ms-bgc-w"]')))
            print("alert Exists in page")
            # create alert object
            self.browser.find_element(By.XPATH,"//body[1]/div[12]/div[1]/div[2]/div[4]/div[1]/div[1]/span[1]/button[1]").click()
           
        except TimeoutException as ex:
            print("alert does not Exist in page" + str(ex))
        wait.until(EC.title_is('Email - Service_Now_Dev@rfs.nsw.gov.au'))

    
        
    
    def open_MailFolder(self, folder):
        self.browser.find_element(By.XPATH,'//span[@title="'+folder+'"]').click()

    def search_Email_Subject(self, sub, email):
        self.browser.find_element(By.XPATH,'//button[@aria-label="Activate Search Textbox"]').click()
        a = self.search_email(sub, email)
        print(a)
        assert a == True
        self.browser.find_element(By.XPATH,'//a[contains(text(),"click here")]').click()
        window_before = self.browser.window_handles[1]
        window_after = self.browser.window_handles[2]
        self.browser.switch_to.window(window_after)
        wait = WebDriverWait(self.browser, 10)
        wait.until(EC.title_is("eMBR RFS CSM Login - eMBR RFS Customer Service"))

    def search_email(self,sub, email):
        #self.browser.find_element(By.XPATH,'//button[@aria-label="Activate Search Textbox"]').click()
        self.browser.find_element(*self.TXT_EMAIL_SEARCH).clear()
        self.browser.find_element(*self.TXT_EMAIL_SEARCH).send_keys(sub + Keys.RETURN )
        wait = WebDriverWait(self.browser, 10)
        wait.until(EC.visibility_of_element_located((By.XPATH,"//span[contains(text(),'Choose a message to read it.')]")))
        wait.until(EC.visibility_of_element_located((By.XPATH,'//div[@role="option" and @aria-expanded="false"]')))        
        self.browser.find_element(By.XPATH,'//div[@role="option" and @aria-expanded="false"]').click()
        self.browser.implicitly_wait(10)
        em = self.browser.find_element(By.XPATH,'//tbody/tr[1]/td[2]/p[5]/span[1]')
        if em.text == email:            
            return True
        elif self.count == 10:
            return False
        else:
            self.count +=1
            print(self.count)            
            return self.search_email(sub,email)














