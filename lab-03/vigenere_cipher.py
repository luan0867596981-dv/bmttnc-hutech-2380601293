import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
# Nếu file dịch ui/vigenere.py dùng class Ui_VigenereMainWindow thay vì Ui_MainWindow, 
# bạn chỉ cần sửa lại tên class ở dòng import bên dưới cho khớp.
from ui.vigenere import Ui_MainWindow
import requests

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # Tự động điền tên vào giao diện Vigenere (Chấp nhận mọi cách đặt tên biến nhãn)
        from PyQt5.QtCore import Qt
        if hasattr(self.ui, 'label_student_info'):
            self.ui.label_student_info.setText("Nguyễn Minh Luân_2380601293")
            self.ui.label_student_info.setAlignment(Qt.AlignCenter)
        elif hasattr(self.ui, 'label_3'):
            self.ui.label_3.setText("Nguyễn Minh Luân_2380601293")
            self.ui.label_3.setAlignment(Qt.AlignCenter)
            
        self.ui.btn_encrypt.clicked.connect(self.call_api_encrypt)
        self.ui.btn_decrypt.clicked.connect(self.call_api_decrypt)
        
    def call_api_encrypt(self):
        url = "http://127.0.0.1:5000/api/vigenere/encrypt"
        plain_text = self.ui.txt_plain_text.toPlainText()
        key = self.ui.txt_key.toPlainText()
        
        payload = {
            "plain_text": plain_text,
            "key": key
        }
        
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.txt_cipher_text.setPlainText(data.get("encrypted_message"))
                
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Mã hóa thành công!")
                msg.exec_()
            else:
                print("Error while calling API")
        except requests.exceptions.RequestException as e:
            print("Error: %s" % str(e))
    
    def call_api_decrypt(self):
        url = "http://127.0.0.1:5000/api/vigenere/decrypt"
        cipher_text = self.ui.txt_cipher_text.toPlainText()
        key = self.ui.txt_key.toPlainText()
        
        payload = {
            "cipher_text": cipher_text,
            "key": key
        }
        
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.txt_plain_text.setPlainText(data.get("decrypted_message"))
                
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Giải mã thành công!")
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