import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_product_page_has_add_to_busket_button(browser):
	link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
	browser.get(link)
	# time.sleep(30)
	button = len(browser.find_elements(By.CSS_SELECTOR, "button.btn-add-to-basket"))
	assert button > 0, "No add to basket button on product page"
