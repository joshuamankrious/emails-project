from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep  # Import sleep for minor pauses
from selenium.webdriver.common.keys import Keys
import random
# Function to set up ChromeDriver
def setup_driver():
    service = Service(r"C:\Users\Jhin\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    return driver

# Main function to execute the automation steps
def main():
    # User input for first name, last name, password, and phone number
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    password = input("Enter your desired password: ")
    phone_number = input("Enter your phone number: ")
    random_integer = random.randint(10000, 999999)
    # Set up the WebDriver
    driver = setup_driver()

    try:
        # Open the target URL
        driver.get("https://support.google.com/mail/answer/56256?hl=en")

        # Wait for the button to be clickable
        create_account_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="page-width-container"]/div[1]/article/section/div/div[1]/div/p[1]/a'))
        )

        # Wait for 5 seconds before clicking
        
        # Force the button to be clicked using JavaScript
        driver.execute_script("arguments[0].click();", create_account_button)

        # Wait for the new tab to open and switch to it
          # Optional wait for the tab to open
        driver.switch_to.window(driver.window_handles[-1])  # Switch to the new tab

        # Wait for the new page to load properly
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="firstName"]'))
        )

        # Optional sleep to ensure the new page is fully loaded
        

        # Step 1: Fill in the first name and last name using send_keys
        first_name_input = driver.find_element(By.XPATH, '//*[@id="firstName"]')
        last_name_input = driver.find_element(By.XPATH, '//*[@id="lastName"]')

        # Clear the input fields before sending keys
        first_name_input.clear()
        last_name_input.clear()

        # Use send_keys to input the values
        first_name_input.send_keys(first_name)
        last_name_input.send_keys(last_name)

        # Wait for the "Next" button to be clickable
        next_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="collectNameNext"]/div/button/span'))
        )
        
        # Wait for 5 seconds before clicking
        
        next_button.click()
          # Waits up to 10 seconds for elements to be available
        
        sleep(4)
        # Wait for the month input dropdown to appear
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="month"]'))
        )

        # Step 2: Select Month, Day, Year, and Gender
        month_dropdown = driver.find_element(By.XPATH, '//*[@id="month"]')
        month_dropdown.send_keys("November")  # Select November

        # Use send_keys to fill the day and year fields
        day_input = driver.find_element(By.XPATH, '//*[@id="day"]')
        year_input = driver.find_element(By.XPATH, '//*[@id="year"]')
        day_input.send_keys('11')  # Set day
        year_input.send_keys('1987')  # Set year

        # Select gender (Male) using send_keys
        gender_dropdown = driver.find_element(By.XPATH, '//*[@id="gender"]')
        gender_dropdown.send_keys('Male')  # Select Male
        
        year_input = driver.find_element(By.XPATH, '//*[@id="year"]')
        year_input.send_keys(Keys.RETURN)  # Set year
        
        
        # Wait for the "Next" button to be clickable
        
        # Generate a random 4-digit integer
        
        sleep(1)
        user_input = driver.find_element(By.CSS_SELECTOR, '.whsOnd.zHQkBf')
        
        user_input.clear()
        user_input.send_keys(first_name)  # Set year
        user_input.send_keys(last_name)  # Set year
        user_input.send_keys(random_integer)  # Set year
        user_input.send_keys(Keys.RETURN)  # Set year
        
        
        
        sleep(2)
        pasword_input = driver.find_element(By.XPATH, '//*[@id="passwd"]/div[1]/div/div[1]/input')
        
        repassword_input = driver.find_element(By.XPATH, '//*[@id="confirm-passwd"]/div[1]/div/div[1]/input')
        
        pasword_input.send_keys(password)  # Set year
        repassword_input.send_keys(password)  # Set year
        
        
        # Wait for 5 seconds before clicking
        
        repassword_input.send_keys(Keys.RETURN)
        
    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        
        sleep(10)  # Wait for a while before closing
        driver.quit()  # Close the browser

# Run the main function
if __name__ == "__main__":
    main()
