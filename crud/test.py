from selenium import webdriver

from selenium.webdriver.common.by import By

import time

driver = webdriver.Chrome(executable_path="E:\\Varsity Study\\3-2\\Software Engineering Lab (CSE 322)\\Drivers\\chromedriver.exe")

driver.get("http://127.0.0.1:8000/admin/login/?next=/admin/")
print(driver.current_url)

time.sleep(2)

driver.find_element(By.NAME, "username").send_keys("Ayman")
print("Name\n")
time.sleep(2)
driver.find_element(By.NAME, "password").send_keys("ayman123")
print("password\n")
time.sleep(2)
driver.find_element_by_css_selector(".submit-row").click()
print("login\n")
time.sleep(2)
driver.find_element(By.XPATH,"//a[contains(text(),'Log out')]").click()
print("Logout\n")
time.sleep(2)

driver.close()