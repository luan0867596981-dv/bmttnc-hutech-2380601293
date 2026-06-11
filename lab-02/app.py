from flask import Flask, render_template, request, json
from ex01.cipher.caesar import CaesarCipher
from ex01.cipher.playfair import PlayfairCipher
from ex01.cipher.railfence import RailFenceCipher
from ex01.cipher.vigenere import VigenereCipher

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

# ============== CAESAR ==============
@app.route("/caesar")
def caesar():
    return render_template('caesar.html')

@app.route("/encrypt", methods=['POST'])

def caesar_encrypt():
    text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])
    Caesar = CaesarCipher()
    encrypted_text = Caesar.encrypt_text(text, key)
    return f"text: {text}<br>key: {key}<br>encrypt text: {encrypted_text}"


@app.route("/decrypt", methods=['POST']) 
def caesar_decrypt():
    text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])
    Caesar = CaesarCipher()
    decrypted_text = Caesar.decrypt_text(text, key)
    return f"text: {text}<br>key: {key}<br>decrypt text: {decrypted_text}"

# ==========================================
# ============== RAIL FENCE ================
# ==========================================
@app.route("/railfence")
def railfence():
    return render_template('railfence.html')

@app.route("/railfence_encrypt", methods=['POST'])
def railfence_encrypt():
    try:
        text = request.form['inputPlainText']
        key = int(request.form['inputKeyPlain']) 
        
        # 1. Ràng buộc Key tối thiểu
        if key < 2:
            return render_template('railfence.html', error="Lỗi: Số đường ray (Key) phải lớn hơn hoặc bằng 2.")
            
        # 2. RÀNG BUỘC MỚI: Key không được lớn hơn chiều dài chuỗi
        if key > len(text):
            return render_template('railfence.html', error=f"Lỗi: Số đường ray ({key}) không được lớn hơn chiều dài của văn bản ({len(text)} ký tự).")
            
        cipher = RailFenceCipher()
        encrypted_text = cipher.rail_fence_encrypt(text, key) 
        
        return render_template('railfence.html', result=encrypted_text)
    except ValueError:
        return render_template('railfence.html', error="Lỗi: Key của Rail Fence bắt buộc phải là một con số!")
    except Exception as e:
        return render_template('railfence.html', error=f"Đã xảy ra lỗi: {str(e)}")


@app.route("/railfence_decrypt", methods=['POST'])
def railfence_decrypt():
    try:
        text = request.form['inputCipherText']
        key = int(request.form['inputKeyCipher']) 
        
        # 1. Ràng buộc Key tối thiểu
        if key < 2:
            return render_template('railfence.html', error="Lỗi: Số đường ray (Key) phải lớn hơn hoặc bằng 2.")
            
        # 2. RÀNG BUỘC MỚI: Key không được lớn hơn chiều dài chuỗi
        if key > len(text):
            return render_template('railfence.html', error=f"Lỗi: Số đường ray ({key}) không được lớn hơn chiều dài của bản mã ({len(text)} ký tự).")
            
        cipher = RailFenceCipher()
        decrypted_text = cipher.rail_fence_decrypt(text, key) 
        
        return render_template('railfence.html', result=decrypted_text)
    except ValueError:
        return render_template('railfence.html', error="Lỗi: Key của Rail Fence bắt buộc phải là một con số!")
    except Exception as e:
        return render_template('railfence.html', error=f"Đã xảy ra lỗi: {str(e)}")

# ==========================================
# ============== VIGENERE ==================
# ==========================================
@app.route("/vigenere")
def vigenere():
    return render_template('vigenere.html')

@app.route("/vigenere_encrypt", methods=['POST'])
def vigenere_encrypt():
    try:
        text = request.form['inputPlainText']
        key = request.form['inputKeyPlain']
        
        cipher = VigenereCipher()
        
        # KIỂM TRA TÊN HÀM MÃ HÓA CỦA BẠN
        encrypted_text = cipher.vigenere_encrypt(text, key) 
        
        return render_template('vigenere.html', result=encrypted_text)
    except Exception as e:
        return render_template('vigenere.html', error=f"Đã xảy ra lỗi: {str(e)}")


@app.route("/vigenere_decrypt", methods=['POST'])
def vigenere_decrypt():
    try:
        text = request.form['inputCipherText']
        key = request.form['inputKeyCipher']
        
        cipher = VigenereCipher()
        
        # KIỂM TRA TÊN HÀM GIẢI MÃ CỦA BẠN
        decrypted_text = cipher.vigenere_decrypt(text, key) 
        
        return render_template('vigenere.html', result=decrypted_text)
    except Exception as e:
        return render_template('vigenere.html', error=f"Đã xảy ra lỗi: {str(e)}")


# ==========================================
# ============== PLAYFAIR ==================
# ==========================================
@app.route("/playfair")
def playfair():
    return render_template('playfair.html')

@app.route("/playfair_encrypt", methods=['POST'])
def playfair_encrypt():
    try:
        text = request.form['inputPlainText']
        key = request.form['inputKeyPlain']
        
        cipher = PlayfairCipher()
        
        # KIỂM TRA TÊN HÀM MÃ HÓA CỦA BẠN
        matrix = cipher.create_playfair_matrix(key)
        encrypted_text = cipher.playfair_encrypt(text, matrix) 
        
        return render_template('playfair.html', result=encrypted_text)
    except Exception as e:
        return render_template('playfair.html', error=f"Đã xảy ra lỗi: {str(e)}")


@app.route("/playfair_decrypt", methods=['POST'])
def playfair_decrypt():
    try:
        text = request.form['inputCipherText']
        key = request.form['inputKeyCipher']
        
        cipher = PlayfairCipher()
        
        # KIỂM TRA TÊN HÀM GIẢI MÃ CỦA BẠN
        matrix = cipher.create_playfair_matrix(key)
        decrypted_text = cipher.playfair_decrypt(text, matrix) 
        
        return render_template('playfair.html', result=decrypted_text)
    except Exception as e:
        return render_template('playfair.html', error=f"Đã xảy ra lỗi: {str(e)}")
    
# Đặt đoạn này ở TẬN CÙNG của file app.py
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5050, debug=True)