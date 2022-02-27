import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException        

from selenium.webdriver.support import expected_conditions as EC



def test_exist_cart_button(browser):
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
        browser.get(link)
        time.sleep(30)
        try:
            browser.find_element(By.CLASS_NAME, 'btn-add-to-basket').click()
        except NoSuchElementException:
            return False
        return True

    
        
        
        