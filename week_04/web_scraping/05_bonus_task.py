'''
* BONUS TASK *
* DISCLAIMER: THIS IS PROBABLY HARD AND REQUIRES SOME TWEAKING *

Explore whether you can use the JavaScript support with requests_html,
to scrape the youtube comments from a video page you are interested in.
( you can use: https://www.youtube.com/watch?v=M54UFvJqQ5I )

Parse the content, locate the usernames of the people who commented,
and save all comments to file in the following form:

username:
    comment text

username:
    comment text

etc.

If requests_html doesn't quite make it and you want to learn more
about scraping dynamic page content, check out 'selenium'.

'''

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
profile = webdriver.FirefoxProfile()
profile.accept_untrusted_certs = True

driver=webdriver.Firefox(executable_path="C:/Utility/geckodriver.exe", firefox_profile=profile)
driver.get('https://www.youtube.com/watch?v=QOzZDdXetUA')
driver.execute_script('window.scrollTo(1, 500);')

time.sleep(5)
driver.execute_script('window.scrollTo(1, 3000);')

comments=driver.find_elements_by_xpath('//*[@id="content-text"]')
name=driver.find_elements_by_xpath('//*[@id="author-text"]')

while True:
    try:
        loadMoreButton = driver.find_element_by_xpath('//*[@id="more"]')
        time.sleep(2)
        loadMoreButton.click()
        time.sleep(5)
    except Exception as e:
        print(e)
        break

time.sleep(10)

number_of_items=len(name)
for i in range (number_of_items):
    print(name[i].text + " : ")
    print(comments[i].text)
driver.quit()