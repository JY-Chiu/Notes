from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()


wait = WebDriverWait(driver, 10)

# 等待姓名欄位出現
wait.until(EC.presence_of_element_located((By.NAME, "name")))
driver.find_element(By.NAME, "name").send_keys("JY")
driver.find_element(By.NAME, "mail").send_keys("test@stc.com.tw")
driver.find_element(By.NAME, "phone").send_keys("1234")
driver.find_element(By.NAME, "engineer").send_keys("JY")

# 選擇單位
select_unit = Select(driver.find_element(By.NAME, "unit"))
select_unit.select_by_visible_text("動保處")

# 輸入問題
issue_text = input("請輸入報修問題：")
driver.find_element(By.NAME, "question").send_keys(issue_text)

time.sleep(2)
driver.find_element(By.XPATH, "//input[@type='button' and @value='送出']").click()
time.sleep(3)
driver.quit()
