import sys
import time
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QTextEdit, QPushButton, QVBoxLayout, QMessageBox
from PyQt6.QtGui import QFont
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class RepairForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("報修問題輸入")
        self.resize(800, 500)

        layout = QVBoxLayout()

        label = QLabel("請輸入報修問題：")
        label.setFont(QFont("Arial", 22))
        layout.addWidget(label)

        # QTextEdit 支援 IME 預輸入文字，字體大小設定即可
        self.text_box = QTextEdit()
        self.text_box.setFont(QFont("Arial", 22))
        self.text_box.setPlaceholderText("這邊輸入你想問的問題...")
        layout.addWidget(self.text_box)

        submit_btn = QPushButton("送出")
        submit_btn.setFont(QFont("Arial", 22))
        submit_btn.setStyleSheet("background-color: #4CAF50; color: white;")
        submit_btn.clicked.connect(self.submit_issue)
        layout.addWidget(submit_btn)

        self.setLayout(layout)

    def submit_issue(self):
        issue_text = self.text_box.toPlainText().strip()
        if not issue_text:
            QMessageBox.information(self, "提示", "你沒有輸入問題，程式將結束。")
            self.close()
            return

        # --- Selenium Chrome headless ---
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
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

        QMessageBox.information(self, "完成", "報修表單已送出！")
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = RepairForm()
    window.show()
    sys.exit(app.exec())
