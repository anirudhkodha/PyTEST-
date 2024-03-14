from pytest_bdd import scenarios, parsers, given, when, then
from pages.sapQasPage import sapQasPage

scenarios('../features/Sap_Login.feature')


@when(parsers.cfparse('User enters valid  SAP credentials "{usr}" "{pwd}" to login'))
def login_sap(browser, usr, pwd):
	sapQas_Page = sapQasPage(browser)
	sapQas_Page.login_sap(usr, pwd)


@then(parsers.cfparse('User is displayed with the title on the homepage'))
def sap_title(browser):
	sapQas_Page = sapQasPage(browser)
	sapQas_Page.sap_homepage()
