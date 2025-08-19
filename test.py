import tkinter as tk
from tkinter import simpledialog, messagebox
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# --- GUI 輸入報修問題 ---
root = tk.Tk()
root.withdraw()  # 隱藏主視窗
issue_text = simpledialog.askstring("報修問題", "請輸入報修問題：")

if not issue_text:
    messagebox.showinfo("提示", "你沒有輸入問題，程式將結束。")
    exit()

# --- Selenium Chrome headless ---
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # 隱藏 Chrome
options.add_argument('--disable-gpu')
options.add_argument('--window-size=1920,1080')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(options=options)
driver.get("http://www.stc.com.tw/client_handle/nkp.jsp?en=J1QSWuwdyZtjxwn0Y4gNMK0LTJpQf69ei8aUdV58xNY=")

wait = WebDriverWait(driver, 10)

# 等待姓名欄位出現
wait.until(EC.presence_of_element_located((By.NAME, "name")))

# 自動填寫欄位
driver.find_element(By.NAME, "name").send_keys("JY")
driver.find_element(By.NAME, "mail").send_keys("test@stc.com.tw")
driver.find_element(By.NAME, "phone").send_keys("1234")
driver.find_element(By.NAME, "engineer").send_keys("JY")

# 選擇單位
select_unit = Select(driver.find_element(By.NAME, "unit"))
select_unit.select_by_visible_text("動保處")

# 填入 GUI 輸入的問題
driver.find_element(By.NAME, "question").send_keys(issue_text)

time.sleep(2)
driver.find_element(By.XPATH, "//input[@type='button' and @value='送出']").click()
time.sleep(3)
driver.quit()

messagebox.showinfo("完成", "報修表單已送出！")
