from pytest_bdd import scenarios, parsers, given, when, then
from pages.serviceNowPage import serviceNowPage

scenarios('../features/Adult_E2E_FF_Transfer.feature')


@then('User logs in service now portal for transfer application')
def serviceNow_Brigade(browser,read_JSON):
    # ref = read_JSON('data/appRef.json')
    serviceNow_page = serviceNowPage(browser)
    # serviceNow_page.navigate_AdminPortalDashboard("Yes")
    serviceNow_page.open_newTab()

