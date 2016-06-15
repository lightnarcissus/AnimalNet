import os
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

firefox_capabilities = DesiredCapabilities.FIREFOX
firefox_capabilities['marionette'] = True
gecko = os.path.normpath(os.path.join(os.path.dirname(__file__), 'geckodriver'))
driver = webdriver.Firefox(capabilities=firefox_capabilities, executable_path=gecko+'.exe')

driver.get('http://nytimes.com')
interval = 10  #or whatever interval you want
while True:
    element = driver.find_element_by_id("suggestions")
    print element.text.split()[0]
    sleep(interval)