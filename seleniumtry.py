import os
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

firefox_capabilities = DesiredCapabilities.FIREFOX
firefox_capabilities['marionette'] = True
gecko = os.path.normpath(os.path.join(os.path.dirname(__file__), 'geckodriver'))
browser = webdriver.Firefox(capabilities=firefox_capabilities, executable_path=gecko+'.exe')

browser.get('http:///www.google.com')
browser.close()