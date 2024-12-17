from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.add_argument('--headless')  
options.add_argument('--disable-gpu') 
driver = webdriver.Chrome(options=options)

WAIT = WebDriverWait(driver, 15)  

def test_empty_form_submission():
    try:
        driver.get("http://localhost/hotel.loc/bb.html")  # Замените на свой URL
        print("Opened page successfully")

        submit_button = WAIT.until(EC.presence_of_element_located((By.ID, "sub")))
        print("Submit button found")

        submit_button.click()
        print("Clicked submit button on empty form")

        time.sleep(2)

        try:
            error_message = WAIT.until(EC.presence_of_element_located((By.ID, "error-message"))).text
            print(f"Error message: {error_message}")
            assert "Please fill out this field" in error_message or "This field is required" in error_message
            print("Step 1: Empty form submission resulted in error. Test passed so far!")
        except Exception as e:
            print(f"No error message found or error occurred: {e}")

        name_field = WAIT.until(EC.presence_of_element_located((By.NAME, "name")))
        email_field = WAIT.until(EC.presence_of_element_located((By.NAME, "email")))
        room_field = WAIT.until(EC.presence_of_element_located((By.ID, "rooms")))
        dates_field = WAIT.until(EC.presence_of_element_located((By.NAME, "dates")))

        name_field.send_keys("John Doe")  # Имя
        email_field.send_keys("john.doe@example.com")  # Email
        room_field.send_keys("Luxury Suite")  # Комната
        dates_field.send_keys("2024-07-01 to 2024-07-07")  # Даты
        print("Form filled with valid data")

        form = driver.find_element(By.TAG_NAME, 'form')
        form.submit()  

        time.sleep(2)

        success_message = WAIT.until(EC.presence_of_element_located((By.ID, "server-response"))).text
        print(f"Success message: {success_message}")
        
        assert "Your booking has been saved." in success_message
        print("Step 2: Form successfully submitted with valid data. Test passed!")

    except Exception as e:
        print(f"Test 'test_empty_form_submission' failed: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    print("Running E2E test...")
    test_empty_form_submission()
