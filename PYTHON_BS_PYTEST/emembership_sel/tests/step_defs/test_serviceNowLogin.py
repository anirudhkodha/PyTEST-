import pytest
from pytest_bdd import scenarios, parsers, given, when, then
from pages.serviceNow_LoginPage import serviceNow_LoginPage
from pages.serviceNowPage import serviceNowPage
from pages.db_OverviewPage import db_OverviewPage


@when(parsers.cfparse('User enters valid credentials "{user}" "{password}"'))
def user_Enters_Login_Det(browser, user, password):
    serviceNowLogin_page = serviceNow_LoginPage(browser)
    serviceNowLogin_page.enter_Credentials(user,password)

@then('User can see staff admin portal dashboard')
def user_View_Admin_PortalDB(browser):
    serviceNow_page = serviceNowPage(browser)
    serviceNow_page.navigate_AdminPortalDashboard()

@then('User clicks on user profile and select impersonate user')
def user_impersonate(browser):
    serviceNow_page = serviceNowPage(browser)
    serviceNow_page.click_impersonate_User()

@then(parsers.cfparse('User search for "{email}"'))
def user_Enters_Login_Det(browser, email):
    serviceNow_page = serviceNowPage(browser)
    serviceNow_page.impersonate_user(email)

@then('User clicks on Dashboard Overview')
def user_Clicks_OverviewDB(browser):    
    serviceNow_page = serviceNowPage(browser)
    serviceNow_page.click_overviewDB()

@then(parsers.cfparse('User verifies the dashboard as "{dashboard}"'))
def user_Enters_Login_Det(browser, dashboard):
    dbOverview_page = db_OverviewPage(browser)
    dbOverview_page.verify_DB(dashboard)

@then('User End Imperosnation')
def user_Clicks_Unimpersonate(browser):
    serviceNow_page = serviceNowPage(browser)
    serviceNow_page.click_Unimpersonate_User()