import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Define constants for clarity and maintainability
LOGIN_URL = 'https://fieldservice-techs.com/login/'
USERNAME_FIELD = '#username'
PASSWORD_FIELD = '#password'
LOGIN_BUTTON = '#submit-check'
TECHNICIAN_LINK = "nav[id='navigation'] li:nth-child(3) a:nth-child(1)"
SEARCH_INPUT = "input[placeholder='Search for Technicians...']"
SEARCH_BUTTON = "/html/body/div[2]/div[3]/section[2]/div/div/aside[1]/div[2]/div[2]/form/div/div[1]/button"
PROFILE_LINK = "//body/div[@id='wrapper']/div[@id='page-content']/section[@class='section pt-lg-0']/div[@class='container-fluid']/div[@class='row']/aside[@class='col-lg-9 col-12']/div[@id='talent']/div[1]/div[1]/a[1]/span[1]"

# Store credentials securely (e.g., in environment variables or a separate secrets file)
username = 'kalash.agnihotri@fieldservice-techs.com'  # Replace with your credentials
password = '12345678'  # Replace with your credentials
technician_name ='Dennis Diepolder'

# try:
    # Create a WebDriver instance
browser = webdriver.Firefox()

    # Navigate to the login page
browser.get(LOGIN_URL)

    # Perform login actions
WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, USERNAME_FIELD))).send_keys(username)
browser.find_element(By.CSS_SELECTOR, PASSWORD_FIELD).send_keys(password)
browser.find_element(By.CSS_SELECTOR, LOGIN_BUTTON).click()

    # Navigate to the technicians page and search for the technician
time.sleep(3)  

technician_link=browser.find_element(By.CSS_SELECTOR, TECHNICIAN_LINK)
# for technician_names in technician_names:
technician_link.click()
search_input=WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, SEARCH_INPUT)))
search_input.send_keys(technician_name)
        # Click the search button
time.sleep(15)
search_button = browser.find_element(By.XPATH, SEARCH_BUTTON)
search_button.click()
time.sleep(20) 
        
        # Click the profile link
profile_link = browser.find_element(By.XPATH, PROFILE_LINK)
profile_link.click()

browser.back()

# finally:
# Ensure the browser is closed even if an error occurs
browser.quit()
