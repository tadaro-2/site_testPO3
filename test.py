import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.webdriver import Options

CHROME_DRIVER_PATH = "C:/Program Files/Google/Chrome/Application/chromedriver-win64/chromedriver.exe"  # Замените на свой путь

options = Options()
options.add_argument('--headless')  # Запуск браузера в фоновом режиме
driver = webdriver.Chrome(service=Service(CHROME_DRIVER_PATH), options=options)

WAIT = WebDriverWait(driver, 10)

def test_booking_success():
    try:
        driver.get("http://localhost/hotel.loc/bb.html")  # Замените на свой URL

        driver.find_element(By.NAME, "name").send_keys("John Doe")
        driver.find_element(By.NAME, "email").send_keys("john.doe@example.com")
        driver.find_element(By.ID, "rooms").send_keys("Luxury Suite")

        room_plus_btn = driver.find_element(By.CSS_SELECTOR, "#handleCounter1 .counter-plus")
        ActionChains(driver).click(room_plus_btn).perform()

        guest_plus_btn = driver.find_element(By.CSS_SELECTOR, "#handleCounter2 .counter-plus")
        ActionChains(driver).click(guest_plus_btn).perform()
        
        date_input = driver.find_element(By.NAME, "dates")
        date_input.click()
        date_input.send_keys("2024-07-01 to 2024-07-07")
        date_input.send_keys(Keys.TAB)

        driver.find_element(By.ID, "sub").click()

        success_message = WAIT.until(EC.visibility_of_element_located((By.ID, "server-response"))).text
        assert "Your booking has been saved." in success_message
        print("Test 'test_booking_success' passed successfully!")

    except Exception as e:
        print(f"Test 'test_booking_success' failed: {e}")
    finally:
        driver.quit()




if __name__ == "__main__":
    print("Running E2E tests...")
    test_booking_success()
    
