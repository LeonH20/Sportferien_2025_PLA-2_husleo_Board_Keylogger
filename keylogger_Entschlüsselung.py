from cryptography.fernet import Fernet

#Gleicher Schlüssel wie von 'keylogger.py'
ENCRYPTION_KEY = b'kNryyxr5cPQqaIJ__DCIzzZ0Rrp7KRj4lT1-zML5KRw='  # Verwende den gleichen Schlüssel
cipher = Fernet(ENCRYPTION_KEY)

#Entschlüsselung der Nachricht
def decrypt_message(encrypted_message: str) -> str:
    decrypted_bytes = cipher.decrypt(encrypted_message.encode())
    return decrypted_bytes.decode()

# Beispiel für eine entschlüsselte Nachricht
encrypted_data = "Hier kommt die Verschlüsselte Nachricht rein"
print(decrypt_message(encrypted_data))
