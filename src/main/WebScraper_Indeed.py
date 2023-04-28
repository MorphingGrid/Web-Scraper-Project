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
    
    search_terms = ['Data Analyst', 'Data Scientist', 'Data Engineer']
    
    driver.get('https://www.indeed.com/?from=gnav-homepage')
    search_input = driver.find_element_by_id('text-input-what')
    search_input.send_keys('Data Analyst')
    search_input.send_keys(Keys.RETURN)    
    time.sleep(3)
    scraper(driver)
    
    
    #driver.quit()
    

def scraper(driver):
    total_word_count = [0,0,0,0,0]
    words_to_count = ['sql', 'python', 'excel', 'tableau']
    
    base_cards = driver.find_elements_by_class_name('job_seen_beacon')
    
    for card in base_cards:
        card.click()
        time.sleep(2) # Wait for the job details to load

if __name__ == "__main__":
    autobot()