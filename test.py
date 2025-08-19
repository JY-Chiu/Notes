import tkinter as tk
from tkinter import messagebox
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def submit_issue():
    issue_text = text_box.get("1.0", tk.END).strip()
    if not issue_text:
        messagebox.showinfo("提示", "你沒有輸入問題，程式將結束。")
        root.destroy()
        return

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
    wait.until(EC.presence_of_element_located((By.NAME, "name")))

    driver.find_element(By.NAME, "name").send_keys("JY")
    driver.find_element(By.NAME, "mail").send_keys("test@stc.com.tw")
    driver.find_element(By.NAME, "phone").send_keys("1234")
    driver.find_element(By.NAME, "engineer").send_keys("JY")

    select_unit = Select(driver.find_element(By.NAME, "unit"))
    select_unit.select_by_visible_text("動保處")

    driver.find_element(By.NAME, "question").send_keys(issue_text)

    time.sleep(2)
    driver.find_element(By.XPATH, "//input[@type='button' and @value='送出']").click()
    time.sleep(3)
    driver.quit()

    messagebox.showinfo("完成", "報修表單已送出！")
    root.destroy()

# --- 自訂 GUI 視窗 ---
root = tk.Tk()
root.title("報修問題輸入")
root.geometry("600x400")  # 視窗大小
root.resizable(True, True)  # 可調整大小

label = tk.Label(root, text="請輸入報修問題：", font=("Arial", 14))
label.pack(pady=10)

# 多行文字輸入框
text_box = tk.Text(root, font=("Arial", 12), height=10, width=60)
text_box.pack(padx=20, pady=10, fill=tk.BOTH, expand=True)

submit_btn = tk.Button(root, text="送出", font=("Arial", 14), command=submit_issue, bg="#4CAF50", fg="white")
submit_btn.pack(pady=20)

root.mainloop()
