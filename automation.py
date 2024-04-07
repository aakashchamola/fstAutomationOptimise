import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import variables
import creds
# Define constants for clarity and maintainability


# Store credentials securely (e.g., in environment variables or a separate secrets file)
userId =  creds.username # Replace with your credentials
userPassword = creds.password  # Replace with your credentials
technicianFieldInput = creds.technician_name

# try:
    # Create a WebDriver instance
browserInstance = webdriver.Firefox()

    # Navigate to the login page
browserInstance.get(variables.websiteLoginUrl)

    # Perform login actions
WebDriverWait(browserInstance, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, variables.usernameFieldElementId))).send_keys(userId)
browserInstance.find_element(By.CSS_SELECTOR, variables.passwordFieldElementId).send_keys(userPassword)
browserInstance.find_element(By.CSS_SELECTOR, variables.loginButtonElementId).click()

    # Navigate to the technicians page and search for the technician
time.sleep(3)  

technician_link=browserInstance.find_element(By.CSS_SELECTOR, variables.findTechnicianElementId)
    # for technician_names in technician_names:
technician_link.click()
search_input=WebDriverWait(browserInstance, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, variables.searchInputFieldElementId)))
search_input.send_keys(technicianFieldInput)
    # Click the search button
time.sleep(15)
search_button = browserInstance.find_element(By.XPATH, variables.searchButtonElementId)
search_button.click()
time.sleep(20) 
        
    # Click the profile link
profile_link = browserInstance.find_element(By.XPATH, variables.viewProfileButtonElementId)
profile_link.click()

browserInstance.back()

    # finally:
    # Ensure the browser is closed even if an error occurs
browserInstance.quit()
