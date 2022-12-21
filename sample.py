import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get("https://www.facebook.com/")
cu_url = driver.current_url
if cu_url == "https://www.facebook.com/":
    print("Valid")
driver.find_element(By.XPATH, '//a[@class="_42ft _4jy0 _6lti _4jy6 _4jy2 selected _51sy"]').click()
time.sleep(5)
driver.find_element(By.XPATH, '//input[@class="inputtext _58mg _5dba _2ph-"]').send_keys("Naveen")
driver.find_element(By.XPATH, '//input[@name="lastname"]').send_keys("Kumar")
driver.find_element(By.XPATH, '//input[@name="reg_email__"]').send_keys("8790907540")
driver.find_element(By.XPATH, '//input[@autocomplete="new-password"]').send_keys("8790907540")

drop_day = Select(driver.find_element(By.XPATH, '//select[@name="birthday_day"]'))
drop_day.select_by_visible_text("21")
drop_month = Select(driver.find_element(By.XPATH, '//select[@name="birthday_month"]'))
drop_month.select_by_visible_text("Feb")
drop_year = Select(driver.find_element(By.XPATH, '//select[@name="birthday_year"]'))
drop_year.select_by_visible_text("1997")
driver.find_element(By.XPATH, '//input[@value="2"]').click()
driver.find_element(By.XPATH, '//button[@name="websubmit"]').click()
time.sleep(5)
driver.close()
