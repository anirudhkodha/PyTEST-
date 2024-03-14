from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import *
from pyshadow.main import Shadow
from datetime import datetime


class Common_Functions:
	
	def __int__(self, browser):
		self.browser = browser
		self.commonsteps = Common_Functions(self.browser)
		shadow = Shadow(self.browser)
		shadow1 = Shadow0(self.browser)
	
	def wait_for_page_load(self, timeout: int):
		wait = WebDriverWait(self.browser, timeout)
		try:
			wait.until(lambda browser: self.browser.execute_script("return document.readyState === 'complete'"))
			return True
		except Exception as e:
			print(f"Timed out waiting for page to load: {e}")
			return False
	
	def get_Iframe(self):
		self.browser.implicitly_wait(10)
		shadow0 = Shadow(self.browser)
		shadow0.set_implicit_wait(1)
		shadow0.find_element('sn-polaris-layout')
		self.browser.switch_to.frame(shadow0.find_element('iframe'))
	
	def scroll_element_into_(self, *element):
		"""
		Scroll the given element into view using JavaScript.

		:param element: WebElement to scroll into view.
		"""
		scroll_to = self.browser.find_element(*element)
		self.browser.execute_script("arguments[0].scrollIntoView(true);", scroll_to)
	
	def wait_for_element_click(self, *element):
		
		wait = WebDriverWait(self.browser, timeout=20)
		wait.until(EC.element_to_be_clickable(element))
	
	def wait_for_element_visible(self, *element):
		
		wait = WebDriverWait(self.browser, timeout=20)
		wait.until(EC.visibility_of_element_located(element))
	
	def wait_for_element_present(self, *element):
		
		wait = WebDriverWait(self.browser, timeout=20)
		wait.until(EC.presence_of_element_located(element))
	
	def wait_for_element_invisible(self, *element):
		
		wait = WebDriverWait(self.browser, timeout=20)
		wait.until(EC.invisibility_of_element_located(element))
	
	def wait_for_title_contains(self, _predicate: str) -> bool:
		
		wait = WebDriverWait(self.browser, timeout=20)
		wait.until(EC.title_contains(_predicate))
	
	def wait_for_title(self, title: str):
		
		wait = WebDriverWait(self.browser, timeout=20)
		wait.until(EC.title_is(title))
	
	def wait_for_shadow_element_present(self, element):
		
		wait = WebDriverWait(self.browser, timeout=20)
		
		Shadow.is_present(element)
		wait.until(EC.presence_of_element_located(shadow))
	
	def action_to_scroll(self, *element):
		actions = ActionChains(self.browser)
		actions.scroll_to_element(element)
	
	def is_element_in_viewport(self, *element):
		"""Check if an element is in the viewport."""
		js_script = "arguments[0].getBoundingClientRect().top >= 0;"
		return self.browser.execute_script(js_script, element)
	
	def handle_modal(self, *element, locators):
		if self.browser.find_element(*element).is_displayed():
			Agree = self.browser.find_element(*locators)
			self.browser.execute_script("arguments[0].click();", Agree)
			if self.browser.find_element(*element).is_displayed():
				Agree = self.browser.find_element(*locators)
				self.browser.execute_script("arguments[0].click();", Agree)
	
	def read_JSON(*args):
		
		"""Loads data from JSON file"""
		
		def _loader(filename):
			with open(fillename, 'r') as f:
				print(filename)
				data = json.load(f)
			return _loader
