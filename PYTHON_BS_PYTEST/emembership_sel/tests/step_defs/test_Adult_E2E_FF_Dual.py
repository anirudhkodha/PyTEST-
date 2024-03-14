from pages.serviceNow_BrigadeReview_Page import serviceNow_BrigadeReview_Page
import time
from pytest_bdd import scenarios, parsers, given, when, then
from pages.serviceNowPage import serviceNowPage


# scenarios('../features/createCandidateProfile.feature')
scenarios('../features/Adult_E2E_FF_Dual.feature')


@then('User logs in service now portal for transfer application')
def serviceNow_Brigade(browser,read_JSON):
    # ref = read_JSON('data/appRef.json')
    serviceNow_page = serviceNowPage(browser)
    # serviceNow_page.navigate_AdminPortalDashboard("Yes")
    serviceNow_page.open_newTab()

@then('User logs in service now portal for closing serviceCheck task for dual')
def serviceNow_Brigade(browser, read_JSON):
        ref = read_JSON('data/appRef.json')
        serviceNow_page = serviceNowPage(browser)
        serviceNow_page.navigate_AdminPortalDashboard("No")
        serviceNow_page.search_AppRef(ref["ref"])
        sn_Brigade_page = serviceNow_BrigadeReview_Page(browser)
        sn_Brigade_page.set_FormerID("55144541")
        sn_Brigade_page.click_Task("service check")
        sn_Brigade_page.close_ServiceCheckTask()
        time.sleep(5)
