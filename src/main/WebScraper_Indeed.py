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
    
    for word in search_terms:
        driver.get('https://www.indeed.com/?from=gnav-homepage')
        search_input = driver.find_element_by_id('text-input-what')
        search_input.send_keys(word)
        search_input.send_keys(Keys.RETURN)    
        time.sleep(3)
        scraper(driver, word)
    
    
    driver.quit()
    

def scraper(driver, search_term):
    total_word_count = [0,0,0,0,0]
    words_to_count = ['sql', 'python', 'excel', 'tableau']
    
    base_cards = driver.find_elements_by_class_name('job_seen_beacon')
    
    for card in base_cards:
        card.click()
        time.sleep(2) # Wait for the job details to load
        
        description_text = driver.find_element_by_id('jobDescriptionText').get_attribute('innerHTML')
        time.sleep(3)
        
        soup = BeautifulSoup(description_text, 'lxml')
        soup_lower = soup.text.lower() #makes all the text lowercase to make it easier to count
        
        for i, word in enumerate(words_to_count):
            word_count = soup_lower.count(word)
            total_word_count[i] += word_count
            
            
        #Because the programming langauge R is a standalone character r, we have to count it differently.
        #We use the re package
        standalone_r = len(re.findall(r'\br\b', soup_lower))
        total_word_count[4] += standalone_r
    
    #Final Output
    print(f"For {search_term}s:",end = '\n')
        
    total_words = ['SQL', 'Python', 'Excel', 'Tableau', 'R']
        
    for i, word in enumerate(total_words):
        print(f"{word} appears {total_word_count[i]} times.")
            
    print('\n')
    
    time.sleep(2)
    

if __name__ == "__main__":
    autobot()