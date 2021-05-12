from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
import time 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

path_to_chromedriver = 'C:\chromedriver'
browser = webdriver.Chrome(executable_path = path_to_chromedriver)
url = 'https://www.linkedin.ca'
browser.get(url)
browser.find_element_by_css_selector('#session_key').send_keys('samsauhard1@gmail.com')
browser.find_element_by_css_selector('#session_password').send_keys('**********')
browser.find_element_by_css_selector('#main-content > section.section.section--hero > div.sign-in-form-container > form > button').click()
browser.find_element_by_css_selector('#remember-me-prompt__form-primary > button').click()
time.sleep(2)
actions = ActionChains(browser)
N = 8 
for _ in range(N):
    actions = actions.send_keys(Keys.TAB)
actions = actions.send_keys(Keys.RETURN)
actions.perform()

actions = ActionChains(browser)
N = 9 
time.sleep(2)
for _ in range(N):
    actions = actions.send_keys(Keys.TAB)
actions = actions.send_keys('Canada')
actions = actions.send_keys(Keys.RETURN)
actions.perform()

#Select Easy Apply
actions = ActionChains(browser)
N = 7 
time.sleep(2)
for _ in range(N):
    actions = actions.send_keys(Keys.TAB)

actions = actions.send_keys(Keys.RETURN)
actions.perform()

#Go to Job
actions = ActionChains(browser)
N = 4 
time.sleep(2)
for _ in range(N):
    actions = actions.send_keys(Keys.TAB)

actions = actions.send_keys(Keys.RETURN)
actions.perform()

browser.find_element_by_css_selector('body').click()

#Easy Apply Job
actions = ActionChains(browser)
N = 6
time.sleep(2)
for _ in range(N):
    actions = actions.send_keys(Keys.TAB)

actions = actions.send_keys(Keys.RETURN)
actions.perform()

#Page 1 
actions = ActionChains(browser)
N = 6
time.sleep(2)
for _ in range(N):
    actions = actions.send_keys(Keys.TAB)

actions = actions.send_keys(Keys.RETURN)
actions.perform()


#Page 2 
actions = ActionChains(browser)
N = 6
time.sleep(2)
for _ in range(N):
    actions = actions.send_keys(Keys.TAB)

actions = actions.send_keys(Keys.RETURN)
actions.perform()
