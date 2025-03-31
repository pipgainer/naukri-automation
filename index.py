import time
import os
import pyautogui 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv  # Import dotenv

# Load environment variables from .env
load_dotenv()

# Get credentials from .env
NAUKRI_EMAIL = os.getenv("NAUKRI_EMAIL")
NAUKRI_PASSWORD = os.getenv("NAUKRI_PASSWORD")

# Set up WebDriver
chrome_driver_path = "D:\\naukri-automation\\chromedriver.exe"
service = Service(chrome_driver_path)
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(service=service, options=options)

# Open Naukri website
driver.get("https://www.naukri.com/")

# Click on Login button
login_button = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.XPATH, "//a[text()='Login']"))
)
login_button.click()

# Wait for sidebar to fully open and username field to be visible
username = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//*[@id='root']/div[4]/div[2]/div/div/div[2]/div/form/div[2]/input"))
)
password = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//*[@id='root']/div[4]/div[2]/div/div/div[2]/div/form/div[3]/input"))
)
login_submit = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//*[@id='root']/div[4]/div[2]/div/div/div[2]/div/form/div[6]/button"))
)

# Enter login credentials
username.send_keys(NAUKRI_EMAIL)
password.send_keys(NAUKRI_PASSWORD)
login_submit.click()

print("Login successful!")
# Click on profile or resume update section
update_resume_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "/html/body/main/div/div/div[3]/div/div[3]/div[2]/a"))
)
update_resume_button.click()

def upload_resume(resume_path):
    # Wait for the resume upload section to load
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='lazyAttachCV']/div/div[2]/div[2]/div/div[2]/div[1]/div/section"))
    )

    # Find the file input element
    resume_upload = driver.find_element(By.XPATH, "//*[@id='lazyAttachCV']/div/div[2]/div[2]/div/div[2]/div[1]/div/section/div/div[2]/input")

    # Make input field visible (if hidden)
    driver.execute_script("arguments[0].style.display = 'block';", resume_upload)

    # Click on the input field before sending the file
    resume_upload.click()

    # Wait for file dialog to open
    time.sleep(2)

    # Use PyAutoGUI to type resume path and press Enter
    pyautogui.write(resume_path)  # Type the file path
    pyautogui.press("enter")  # Press Enter to select file

    print(f'Resume {resume_path} uploaded successfully!')

# 🔄 **Loop to Upload Resumes Indefinitely**
while True:
    # Upload resume1
    upload_resume("D:\\naukri-automation\\AbhishekPowadeMobileDeveloper.pdf")

    # Wait for 5 minutes
    print("Waiting for 5 minutes before uploading the second resume...")
    time.sleep(300)

    # Upload resume2
    upload_resume("D:\\naukri-automation\\AbhishekPowadeReactNativeDeveloper.pdf")

    # Wait for 5 minutes
    print("Waiting for 5 minutes before repeating the process...")
    time.sleep(300)

# Close browser after task is done
driver.quit()
