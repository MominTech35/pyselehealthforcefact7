from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()

try:

    driver.get('localhost:6464')
    driver.maximize_window()


    hyperlinks = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.TAG_NAME, 'a')))

    expected_hyperlinks = [
        {"text": "Terms and Conditions", "href": "/privacy"},
        {"text": "Privacy", "href": "/terms"},
        {"text": "Healthforce"},

    ]

    for expected_link in expected_hyperlinks:

        link = next((a for a in hyperlinks if a.text == expected_link['text']), None)


        assert link is not None, f"Hyperlink with text '{expected_link['text']}' not found"

        if 'href' in expected_link:
            href = link.get_attribute('href')

            assert href.endswith(expected_link['href']), (
                f"Hyperlink '{expected_link['text']}' href mismatch. "
                f"Expected: {expected_link['href']}, Found: {href}"
            )
        else:

            href = None

        print(f"Hyperlink '{expected_link['text']}' is present and active with href: {href}")


    driver.save_screenshot('hyperlinks_verification.png')
    print("Screenshot taken for hyperlinks verification.")

except Exception as e:

    driver.save_screenshot('error.png')
    print(f"An error occurred: {e}")

finally:

    driver.quit()

