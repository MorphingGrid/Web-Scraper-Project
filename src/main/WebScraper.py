from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import requests
import time

def scraper():
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
    
    
    #Go to the student postings
    driver.get('https://app.joinhandshake.com/stu/postings')
    #Search for Data Analyst positions
    driver.get('https://app.joinhandshake.com/stu/postings?page=1&per_page=25&sort_direction=desc&sort_column=default&query=Data%20Analyst')
    
    # Get the page source after dynamic content is loaded
    time.sleep(5)  # Wait for dynamic content to load
    page_source = driver.page_source
    
    # Parse the page source with BeautifulSoup
    soup = BeautifulSoup(page_source, 'lxml')
    
    titles = soup.find_all('div', class_ = 'style__job-title___+ohfl')
    
    job_titles = []
    
    # Extract job titles from span elements within each div
    for title in titles[:2]:
        job_title = title.find_all('span')[1].get_text(strip=True)
        job_titles.append(job_title)
    
    print(job_titles)
        

if __name__ == "__main__":
    scraper()