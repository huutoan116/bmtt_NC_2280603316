class PlayFairCipher:
    def __init__(self):
        pass

    def create_playfair_matrix(self, key):
        key = key.replace("J", "I").upper()
        key_set = set(key)
        alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
        remaining_letters = [letter for letter in alphabet if letter not in key_set]

        matrix = list(key) + remaining_letters
        playfair_matrix = [matrix[i:i+5] for i in range(0, 25, 5)]
        return playfair_matrix

    def find_letter_coords(self, matrix, letter):
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                if matrix[row][col] == letter:
                    return row, col
        return None

    def playfair_encrypt(self, plain_text, matrix):
        plain_text = plain_text.replace("J", "I").upper()
        encrypted_text = ""

        # Đảm bảo văn bản có số ký tự chẵn
        if len(plain_text) % 2 != 0:
            plain_text += "X"

        for i in range(0, len(plain_text), 2):
            pair = plain_text[i:i+2]
            row1, col1 = self.find_letter_coords(matrix, pair[0])
            row2, col2 = self.find_letter_coords(matrix, pair[1])

            if row1 == row2:  # Cùng hàng
                encrypted_text += matrix[row1][(col1 + 1) % 5] + matrix[row2][(col2 + 1) % 5]
            elif col1 == col2:  # Cùng cột
                encrypted_text += matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2]
            else:  # Hình chữ nhật
                encrypted_text += matrix[row1][col2] + matrix[row2][col1]

        return encrypted_text

    def playfair_decrypt(self, cipher_text, matrix):
        cipher_text = cipher_text.upper()
        decrypted_text = ""

        for i in range(0, len(cipher_text), 2):
            pair = cipher_text[i:i+2]
            row1, col1 = self.find_letter_coords(matrix, pair[0])
            row2, col2 = self.find_letter_coords(matrix, pair[1])

            if row1 == row2:  # Cùng hàng
                decrypted_text += matrix[row1][(col1 - 1) % 5] + matrix[row2][(col2 - 1) % 5]
            elif col1 == col2:  # Cùng cột
                decrypted_text += matrix[(row1 - 1) % 5][col1] + matrix[(row2 - 1) % 5][col2]
            else:  # Hình chữ nhật
                decrypted_text += matrix[row1][col2] + matrix[row2][col1]

        # Xử lý trường hợp có 'X' chèn vào
        cleaned_text = ""
        for i in range(len(decrypted_text) - 1):
            if decrypted_text[i] == "X" and (i == 0 or decrypted_text[i - 1] == decrypted_text[i + 1]):
                continue  # Bỏ qua 'X' nếu nó nằm giữa hai chữ cái giống nhau
            cleaned_text += decrypted_text[i]
        
        cleaned_text += decrypted_text[-1]  # Thêm ký tự cuối

        return cleaned_text


# 📌 **Kiểm tra chương trình**
cipher = PlayFairCipher()
key = "KEYWORD"
matrix = cipher.create_playfair_matrix(key)

plaintext = "HELLO"
encrypted = cipher.playfair_encrypt(plaintext, matrix)
decrypted = cipher.playfair_decrypt(encrypted, matrix)

print("Encrypted:", encrypted)  # In ra văn bản đã mã hóa
print("Decrypted:", decrypted)  # In ra văn bản đã giải mã
