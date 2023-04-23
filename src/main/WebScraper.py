from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import re
import time


def autobot():
    service = Service('/Users/vinny/Downloads/chromedriver_mac_arm64/chromedriver')
    service.start()
    driver = webdriver.Remote(service.service_url)

    driver.implicitly_wait(10)
    driver.get('https://www.linkedin.com/jobs/search?trk=guest_homepage-basic_guest_nav_menu_jobs&position=1&pageNum=0')
    
    #Searches for the role "Data Analyst" in Orlando, Florida using LinkedIn's built in search function
    search_input = driver.find_element_by_id('job-search-bar-keywords')
    search_input.send_keys('Data Analyst')
    location = driver.find_element_by_id('job-search-bar-location')
    location.clear()
    location.send_keys('Orlando,Florida')
    location.send_keys(Keys.RETURN)
    
    base_cards = driver.find_elements_by_css_selector('.base-card__full-link') # Corrected CSS selector
    
    for card in base_cards:
        card.click()
        time.sleep(2) # Wait for the job details to load
    
    time.sleep(5)
    driver.quit()
    
        

if __name__ == "__main__":
    autobot()