from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# Setup Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Ensure GUI is off
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Set path to chromedriver as per your configuration
webdriver_service = ChromeService(ChromeDriverManager().install())

# Choose Chrome Browser
driver = webdriver.Chrome(service=webdriver_service, options=chrome_options)

try:
    driver.get("https://www.timeanddate.com/")
    # Assuming there's a stable element to fetch the date from
    date_element = driver.find_element(By.CSS_SELECTOR, "some stable selector")
    print("Today's date is:", date_element.text)
finally:
    driver.quit()

