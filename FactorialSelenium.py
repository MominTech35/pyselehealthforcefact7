from selenium import webdriver
import time
import logging
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


logging.basicConfig(
    filename='selenium_test.log',
    level=logging.INFO,
    format='%(asctime)s:%(levelname)s:%(message)s'
)

driver = webdriver.Chrome()

driver.get('localhost:6464')
driver.maximize_window()
logging.info("Opened the web application.")
time.sleep(10)

header = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[1]/div/h1')))


assert header is not None, "Header element is not present"

expected_title = "The greatest factorial calculator!"
assert header.text == expected_title, f"Header title does not match. Expected: {expected_title}, Found: {header.text}"


print("Header title is present and matches the expected value.")

driver.save_screenshot('header_verification.png')
print("Screenshot taken for header verification.")

input_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'number')))

input_field.send_keys('7')
logging.info("Entered the number 7 in the input field.")

submit_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'getFactorial')))
submit_button.click()
logging.info("Clicked the submit button.")

# Take a screenshot after clicking the submit button
driver.save_screenshot('after_submit.png')
logging.info("Screenshot taken after submitting the form.")
# Wait for the result to be displayed
time.sleep(5)

try:
    result_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'result')))
    result = result_element.text
    print(f"Result: {result}")
except:
    print("Calculation did not occur, button Calculate is not working.")

driver.quit()