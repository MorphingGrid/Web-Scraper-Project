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
    driver.get('https://federation.net.ucf.edu/adfs/ls/?SAMLRequest=hZHBTsMwEER%2FJTefHIfEJMFqKhV6oFIRFQ0cuFSu7RJDYhuvjfh8mhZEuZTjrt6MdmYnwIfesVkMnXlQ71FBSGYAygdtzY01EAfl18p%2FaKEeH5YN6kJwwAjhzqWvVpuOGwkdf1OpsAMZ3TbiKEPJfO%2BmDR%2BtfoU7JZU%2F7FKjQhrFLlUyEi53QHogKFnMG7TZlqWktJD4sqIlphmtMadVjata1FWRy0KW%2BR4FiGphIHATGpRneYEzirO6vbhiNGdF9YySlbfBCttfayO1eWlQ9IZZDhqY4YMCFgRbz%2B6WLE8ztj1CwG7bdoVX9%2BsWJU%2FKwyHBHkDJ59AbYGPO8078p8RTiTuvcd%2BnoulkpNkhnp%2F%2BU7mbkFP6OP196fQL')
    # Find the username and password input fields on the login form, and enter your credentials
    username_input = driver.find_element_by_id('userNameInput')
    username_input.send_keys('NET\\vi927701')
    password_input = driver.find_element_by_id('passwordInput')
    password_input.send_keys('YoruSimp99!')
    password_input.send_keys(Keys.RETURN)
    
    #Go to the student job postings
    driver.get('https://app.joinhandshake.com/stu/postings')
    
    search_engine = ['Data Analyst', 'Data Scientist', 'Data Engineer']
    
    for word in search_engine:
        link = 'https://app.joinhandshake.com/stu/postings?page=1&per_page=25&sort_direction=desc&sort_column=default&query=' + word
        driver.get(link)
        time.sleep(5)
        
        #Get the page source after the page has loaded
        page = driver.page_source
        scraper(driver, page, word)
        time.sleep(5)
        
    driver.quit()
        
        

def scraper(driver, page_source, search_term):
    # Parse the page source with BeautifulSoup
    soup = BeautifulSoup(page_source, 'lxml')
    
    #Finds the element that contains all the job postings
    job_postings = soup.find_all('div', class_ = 'style__cards___1xGnw')
    
    job_links = []
    
    #For each job, append the reference link to the job into a list
    for element in job_postings:
        for link in element.find_all('a', href = True):
            job_links.append('https://app.joinhandshake.com' + link['href'])
            
    total_word_count = [0,0,0,0,0]
    words_to_count = ['sql', 'python', 'excel', 'tableau']
            
    for job in job_links:
        #Visit each web page and wait 5 seconds for the page to load 
        driver.get(job)
        source = driver.page_source
        soup = BeautifulSoup(source, 'lxml')
        job_description = soup.find('div', class_ = 'style__text___2ilXR style__large___3qwwG style__tight___RF4uH').text
        
        #Converts the job description to lower for counting purposes
        job_description_lower = job_description.lower()
        
        
        for i, word in enumerate(words_to_count):
            word_count = job_description_lower.count(word)
            total_word_count[i] += word_count
            #print(f"The word {word} appears {word_count} times.")
        
        #Because the programming langauge R is a standalone character r, we have to count it differently.
        #We use the re package
        standalone_r = len(re.findall(r'\br\b', job_description_lower))
        total_word_count[4] += standalone_r
        #print(f"The word 'r' appears {standalone_r} times.")
        
    print(f"For {search_term}s:",end = '\n')
    
    total_words = ['SQL', 'Python', 'Excel', 'Tableau', 'R']
    
    for i, word in enumerate(total_words):
        print(f"{word} appears {total_word_count[i]} times.")
        
    print('\n')
        
    
        

if __name__ == "__main__":
    autobot()