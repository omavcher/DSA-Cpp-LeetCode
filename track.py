from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import pyautogui
import os
from datetime import datetime

# Save folder for screenshots
save_folder = "C:/WhatsApp_Screenshots"
os.makedirs(save_folder, exist_ok=True)

# Setup Brave browser with Selenium
brave_path = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"  # Modify if your path is different

options = Options()
options.binary_location = brave_path
options.add_argument("--user-data-dir=C:/Users/YOUR_USERNAME/AppData/Local/BraveSoftware/Brave-Browser/User Data")  # Replace with your actual path
options.add_argument("--profile-directory=Default")  # Use the profile with WhatsApp logged in

# Launch browser
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
driver.get("https://web.whatsapp.com/")
print("🔓 Please scan QR code if not already logged in...")

time.sleep(15)  # Wait for WhatsApp Web to load

# Monitor loop
try:
    print("🟢 Monitoring WhatsApp for new messages...")
    while True:
        try:
            # Check for the green dot indicating new messages
            unread = driver.find_elements(By.CLASS_NAME, "_38M1B")  # Class may change, update if needed

            if unread:
                # Screenshot
                timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
                filepath = os.path.join(save_folder, f"whatsapp_{timestamp}.png")
                screenshot = pyautogui.screenshot()
                screenshot.save(filepath)
                print(f"[📸] Screenshot saved: {filepath}")

                time.sleep(5)  # Prevent duplicate screenshots

        except Exception as e:
            print("⚠️ Error while checking:", e)

        time.sleep(3)  # Check every 3 seconds

except KeyboardInterrupt:
    print("🛑 Monitoring stopped.")
    driver.quit()
