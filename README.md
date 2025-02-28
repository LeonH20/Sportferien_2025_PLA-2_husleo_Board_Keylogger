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

## Wie starte/beendet sich das Script?
Das Script startet nicht Automatisch das es ein Virus ist, jedoch  
kann man die Leute tricken indem man es als irgndein System welches  
gestartet werden muss oder so etwaws tarnen, wozu man auch meistens  
das Logo ändert. Das Script kann man in zwei Wegen beenden:  
1. Den Laptop Herunterfahren
2. Taskmanager --> Kelogger deaktivieren und dann löschen

## Wie kann man sich davor schützen?
1. Antivirenschutz an haben
2. Nie Dateien Zugriff auf Laptop geben (Unerkannte Herausgeber)
3. Spam E-Mails meistens ignorieren
