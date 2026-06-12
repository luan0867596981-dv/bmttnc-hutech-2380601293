import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui.caesar import Ui_MainWindow
import requests

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # CHÈN THÊM DÒNG NÀY VÀO ĐÂY ĐỂ ĐIỀN TÊN VÀO GIAO DIỆN
        if hasattr(self.ui, 'label_3'):
            self.ui.label_3.setText("Nguyễn Minh Luân_2380601293")
        
        self.ui.btn_encrypt.clicked.connect(self.call_api_encrypt)
        self.ui.btn_decrypt.clicked.connect(self.call_api_decrypt)
        
    def call_api_encrypt(self):
        url = "http://127.0.0.1:5000/api/caesar/encrypt"
        key_text = self.ui.txt_key.toPlainText()
        try:
            key = int(key_text)
        except ValueError:
            QMessageBox.warning(self, "Lỗi khoá", "Key phải là một số nguyên hợp lệ.")
            return

        payload = {
            "plain_text": self.ui.txt_plain_text.toPlainText(),
            "key": key
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.txt_cipher_text.setPlainText(data["encrypted_message"])
                
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Encrypted Successfully")
                msg.exec_()
            else:
                print("Error while calling API")
        except requests.exceptions.RequestException as e:
            print("Error: %s" % str(e))
    
    def call_api_decrypt(self):
        url = "http://127.0.0.1:5000/api/caesar/decrypt"
        key_text = self.ui.txt_key.toPlainText()
        try:
            key = int(key_text)
        except ValueError:
            QMessageBox.warning(self, "Lỗi khoá", "Key phải là một số nguyên hợp lệ.")
            return

        payload = {
            "cipher_text": self.ui.txt_cipher_text.toPlainText(),
            "key": key
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.txt_plain_text.setPlainText(data["decrypted_message"])
                
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Decrypted Successfully")
                msg.exec_()
            else:
                print("Error while calling API")
        except requests.exceptions.RequestException as e:
            print("Error: %s" % str(e))
            
if __name__ == "__main__":
        app = QApplication(sys.argv)
        window = MyApp()
        window.show()
        sys.exit(app.exec_())