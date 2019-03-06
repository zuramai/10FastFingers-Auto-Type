# ================================================================
# =							 									 =
# =		MADE BY AHMAD SAUGI			 							 =
# =		https://www.facebook.com/ahmadsaugi.gis					 =
# =							 									 =
# ================================================================

from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time


delay = 0.1 # CHANGE SPEED OF TYPING


driver = webdriver.Firefox()
driver.get('https://10fastfingers.com/typing-test/english')
time.sleep(5)

span = driver.find_elements_by_css_selector('#row1 > span')
driver.execute_script("$('#words').css('height','auto')")
inputField = driver.find_element_by_css_selector("#inputfield")

for texts in span:
	text = texts.text
	
	for character in text:
		inputField.send_keys(character)
		time.sleep(delay)

	inputField.send_keys(Keys.SPACE)
	
	print(text)