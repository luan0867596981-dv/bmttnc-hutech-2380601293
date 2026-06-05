from .alphabet import ALPHABET

class CaesarCipher:
    def __init__(self):
        self.alphabet = ALPHABET
        
    def encrypt_text(self, text, key):
        encrypted_text = ""
        text = text.upper() # Chuyển tất cả thành chữ in hoa để dễ xử lý
        for letter in text:
            # Chỉ mã hóa nếu ký tự đó nằm trong bảng chữ cái (A-Z)
            if letter in self.alphabet:
                letter_index = self.alphabet.index(letter)
                new_index = (letter_index + key) % len(self.alphabet)
                encrypted_text += self.alphabet[new_index]
            else:
                # Nếu là khoảng trắng, số, hay dấu (!, ?, .) -> GIỮ NGUYÊN
                encrypted_text += letter 
                
        return encrypted_text

    def decrypt_text(self, text, key):
        decrypted_text = ""
        for letter in text:
            # Nếu ký tự nằm trong bảng chữ cái thì tiến hành dịch vòng
            if letter in self.alphabet:
                letter_index = self.alphabet.index(letter)
                # Logic giải mã của bạn ở đây. Ví dụ:
                new_index = (letter_index - key) % len(self.alphabet)
                decrypted_text += self.alphabet[new_index]
            else:
                # Nếu là khoảng trắng, số, hay ký tự đặc biệt -> giữ nguyên không mã hóa
                decrypted_text += letter 
                
        return decrypted_text