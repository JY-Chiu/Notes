import sys
import os
import time
from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QTextEdit, QPushButton, QVBoxLayout, QMessageBox, QLineEdit
)
from PyQt6.QtGui import QFont
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class RepairForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("STC報修")

        layout = QVBoxLayout()

        # --- Name ---
        label_name = QLabel("姓名：")
        label_name.setFont(QFont("Arial", 18))
        layout.addWidget(label_name)

        self.input_name = QLineEdit()
        self.input_name.setFont(QFont("Arial", 18))
        self.input_name.setText("江紫瑄")
        layout.addWidget(self.input_name)

        # --- Mail ---
        label_mail = QLabel("電子郵件：")
        label_mail.setFont(QFont("Arial", 18))
        layout.addWidget(label_mail)

        self.input_mail = QLineEdit()
        self.input_mail.setFont(QFont("Arial", 18))
        self.input_mail.setText("10027167@mail.tycg.gov.tw")
        layout.addWidget(self.input_mail)

        # --- Phone ---
        label_phone = QLabel("分機：")
        label_phone.setFont(QFont("Arial", 18))
        layout.addWidget(label_phone)

        self.input_phone = QLineEdit()
        self.input_phone.setFont(QFont("Arial", 18))
        self.input_phone.setText("204")
        layout.addWidget(self.input_phone)

        # --- 問題 ---
        label = QLabel("報修問題：")
        label.setFont(QFont("Arial", 18))
        layout.addWidget(label)

        self.text_box = QTextEdit()
        self.text_box.setFont(QFont("Arial", 18))
        self.text_box.setPlaceholderText("請輸入您的問題...")
        layout.addWidget(self.text_box)

        # --- Submit Button ---
        submit_btn = QPushButton("送出")
        submit_btn.setFont(QFont("Arial", 20))
        submit_btn.setStyleSheet("background-color: #4CAF50; color: white;")
        submit_btn.clicked.connect(self.submit_issue)
        layout.addWidget(submit_btn)

        self.setLayout(layout)

    def submit_issue(self):
        name = self.input_name.text().strip()
        mail = self.input_mail.text().strip()
        phone = self.input_phone.text().strip()
        issue_text = self.text_box.toPlainText().strip()

        if not issue_text:
            QMessageBox.information(self, "提示", "你沒有輸入問題，程式將結束。")
            self.close()
            return

        # --- Selenium Chrome ---
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        options.add_argument('--window-size=1920,1080')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')

        # 使用相對路徑載入 chromedriver
        chromedriver_path = os.path.join(os.path.dirname(__file__), "chromedriver.exe")
        driver = webdriver.Chrome(executable_path=chromedriver_path, options=options)

        driver.get("http://www.stc.com.tw/client_handle/nkp.jsp?en=J1QSWuwdyZtjxwn0Y4gNMK0LTJpQf69ei8aUdV58xNY=")
        wait = WebDriverWait(driver, 10)
        wait.until(EC.presence_of_element_located((By.NAME, "name")))

        driver.find_element(By.NAME, "name").send_keys(name)
        driver.find_element(By.NAME, "mail").send_keys(mail)
        driver.find_element(By.NAME, "phone").send_keys(phone)
        driver.find_element(By.NAME, "engineer").send_keys("OAP001")

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
