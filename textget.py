import sys
from contextlib import closing

import lxml.html as html # pip install 'lxml>=2.3.1'
from lxml.html.clean        import Cleaner
from selenium.webdriver     import Firefox         # pip install selenium
from werkzeug.contrib.cache import FileSystemCache # pip install werkzeug
import os
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

firefox_capabilities = DesiredCapabilities.FIREFOX
firefox_capabilities['marionette'] = True
gecko = os.path.normpath(os.path.join(os.path.dirname(__file__), 'geckodriver'))
#browser = webdriver.Firefox(capabilities=firefox_capabilities, executable_path=gecko+'.exe')

cache = FileSystemCache('.cachedir', threshold=100000)

url = sys.argv[1] if len(sys.argv) > 1 else "http://reddit.com"


# get page
page_source = cache.get(url)
if page_source is None:
    # use firefox to get page with javascript generated content
    with closing(Firefox(capabilities=firefox_capabilities, executable_path=gecko+'.exe')) as browser:
        browser.get(url)
        page_source = browser.page_source
    cache.set(url, page_source, timeout=60*60*24*7) # week in seconds


# extract text
root = html.document_fromstring(page_source)
# remove flash, images, <script>,<style>, etc
Cleaner(kill_tags=['noscript'], style=True)(root) # lxml >= 2.3.1
str = "this is string example....wow!!!";

print "Encoded String: " + str.encode('base64','strict')
# print "Encoded String: " + root.text_content().encode('base64','strict')