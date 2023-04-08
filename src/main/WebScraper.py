from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
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
    
    
    #click the Jobs button on the side panel
    driver.get('https://app.joinhandshake.com/stu/postings')
    
    time.sleep(5)
    
    search_input = driver.find_element_by_xpath('//input[@value]')
    

    
    time.sleep(5)
    driver.quit()

if __name__ == "__main__":
    scraper()