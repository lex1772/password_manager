import base64

from cryptography.fernet import Fernet


def encrypt(password):
    # Функция для шифрования пароля
    entered_pw = 'secretpw'
    key = base64.b64encode(f'{entered_pw:<32}'.encode('utf-8'))
    encryptor = Fernet(key=key)
    encrypted = encryptor.encrypt(
        password.encode('utf-8')
    )
    return encrypted


def decrypt(encrypted_password):
    # Функция для дешифровки пароля
    entered_pw = 'secretpw'
    key = base64.b64encode(f'{entered_pw:<32}'.encode('utf-8'))
    encryptor = Fernet(key=key)
    bytes_password = str.encode(encrypted_password[2:-1])
    password = encryptor.decrypt(bytes(bytes_password)).decode('utf-8')
    return password
