readme_v0.2.1.md
***************************************
Vor dem Ausführen des Programms sollten einige Punkte beachtet werden:

    a. Überprüfen Sie, dass das Verzeichnis "project_directory" nur die Projekt-Nummer "xx" enthält und keine Excel-Datei.

    b. Stellen Sie sicher, dass Ihre neuen Projektverzeichnisse dem bereits unter dem Verzeichnis "projects_directory" gespeicherten Format entsprechen. Dieses Format lautet: "projects_directory/xx/[Excel-Datei mit der dreistelligen Niederlassungsnummer.xlsx]".

    c. Um die Daten aus den Excel-Tabellen mit dem Programm abrufen zu können, ist es wichtig, dass das Tabellenformat berücksichtigt wird. 
       Dabei müssen die benötigten AP-Typen identifiziert werden.  Diese sollen gefunden werden:
            - entweder in Spalte 'C' der Excel-Sheets, die den String 'Final' enthalten, wie Projekt 14, 
            - oder in Spalte 'H' der Excel-Sheets, die den Text 'AP-Liste' enthalten, wieProjekte 1-12.


***************************************
Öffnen Sie ein Windows-Terminal.
Kopieren Sie '!' nicht mit!

1. python and pip installieren!

    Überprüfen, welche Python-Version installiert ist.
    ! python --version

        Dieser schritt kann übersprungen werden, falls bereits eine Python-Version >= 3.10.5 installiert ist.
        ! powershell -ExecutionPolicy Bypass -File installer.ps1
    
        Im Falle einer vorhandenen x86/32 Bit System-Architektur
        ! powershell -ExecutionPolicy Bypass -File installer_x86.ps1

2. Navigieren Sie zum Projektverzeichnis
    ! cd [Zugeordneter Laufwerksbuchstabe für data Nas Server]\Kunden\BAUHAUS\Inbetriebnahme\_00 Bauhaus_ap_count v0.2.1

3. Installieren Sie die App-Anforderungen!
    ! pip install -r requirements.txt

4. Das Python-Programm ausführen, um die vollständige AP-Liste zu generieren.
    ! python main.py


***************************************
"Voraussichtliche Funktionen für die nächsten Releases"

- Zuordnung der Niederlassungsnummern zur entsprechenden Stadt.
- APs basierend auf Indoor/Outdoor-Kategorisierung .
- Die Terminalkommunikation interaktiver gestalten und sicherstellen, dass neue Projekte schnell zu den verfügbaren Ergebnissen hinzugefügt werden können.
- Arbeit an den visuellen Darstellungen des Ausgabe-Excel.

- Bitte teilen Sie mit, wenn Sie weitere Funktionen wünschen. Wir werden dies dann besprechen.



