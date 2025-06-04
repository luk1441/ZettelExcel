# ZettelExcel

# Installationsanleitung
1. Schritt: Klonen des Projekts
git clone https://github.com/luk1441/ZettelExcel.git
cd zettelexcel

2. Installation von Microsoft Office 365
https://www.microsoft.com/de-de/microsoft-365/download-office

3. Installation von Python (falls nicht vorhanden):
Lade Python herunter von https://www.python.org/downloads/.
Aktiviere "Add Python to PATH" während der Installation.
Überprüfe die Installation mit: python --version

4. Schritt: Erstellung einer virtuellen Umgebung
python -m venv gruppe08

5. Schritt: Aktivieren der virtuellen Umgebung#
source gruppe08/bin/activate # Linux/macOS
.\gruppe08\Scripts\activate # Windows

6. Schritt: Installieren der Abhängigkeiten
pip install -r requirements.txt 
7. Schritt: Zettelstore.exe auf dem Rechner starten 
8. Schritt: Anwendung starten (Tabellen aus Zettel in Excel übertragen)
python -m src.cmd.zettel_to_excel (Zettelnummer eintragen)
9. Schritt: Excel-Datei öffnen und in Excel bearbeiten
10. Schritt: Anwendung starten (Excel-Datei in einen Zettel übertragen)
python -m src.cmd.excel_to_zettel (Zettelnummer eintragen)

## License
This project is licensed under the European Union Public Licence 1.2 (EUPL-1.2). See the [LICENSE](LICENSE) file for details.

### Benamung

- Programmierung - Englisch
- Kommentare - Deutsch
- Website Sprache - Deutsch

### Start der CMD App 

In Root (ZettelExcel): python -m src.cmd.zettel_to_excel **Zettel Nummer**

### Programmierung Benamung

- HTML, CSS, HTML Dateien, CSS Dateien, Javascript Dateien - kebab-case: 
  my-variable-name
- Python, Python Dateien, Folder - snake_case: my_variable_name
- Konstanten - Screaming Snake Case: SCREAMING_SNAKE_CASE
- Javascript - camelCase: myVariableName

## Projektauftrag
Projektname: ZettelExcel  

Kurzbeschreibung: 
Ziel dieses Projekts ist die Entwicklung einer Software, die es ermöglicht, erstellte Tabellen aus dem Zettelstore in eine Microsoft Excel Datei zu exportieren. Danach soll die in Excel vorgenommenen Änderungen zurück in den Zettelstore übertragen werden können. 

Zielsetzung: 
Entwicklung einer Software zur Erstellung und Verwaltung von Tabellen im Zettelstore. 
Möglichkeit zur Übertragung der Tabellendaten in Microsoft Excel. 
Durchführung von Berechnungen in Excel mit den übertragenen Daten. 
Synchronisation von Änderungen zwischen Excel und dem Zettelstore in beide Richtungen. 
Sicherstellung der Datenkonsistenz bei der Synchronisation. 

Auftraggeber: 
Zettelstore-Team (Herr Stern) 

Projektteam:  
Max Timme (mtimme, 217105) 
Lukas Mayer (imayer, 217387) 
Confinance Fonkou Guy (gconfian, 205198) 
Petrit Vishi (pvishi, 219309) 
Furkan Mentese (fmentese, 219330) 
Philip Celar (pcelar, 214919) 
Berna Altundag (batici, 204907) 

Projektleiter: Max Timme 
Entwicklung: alle 
Testing & Qualitätssicherung: alle 
Dokumentation: alle 
Startdatum: 26.03.2025 
Enddatum: 28.06.2025 
 
Meilensteine: 
Anforderungsanalyse und Konzeptentwicklung 
Software-Design und Prototyping 
Implementierung der Kernfunktionen 
Testing und Optimierung 
Finalisierung und Dokumentation 
 
Erwartete Ergebnisse: 
Ein funktionierendes Software-Tool zur Synchronisation von Tabellen zwischen dem Zettelstore und Microsoft Excel. 
Eine stabile und zuverlässige Datenübertragungsmechanik. 
Dokumentation der Software mit Anwendungsanleitung. 
 
Abschluss und Bewertung: 
Das Projekt wird als erfolgreich bewertet, wenn die Software eine reibungslose Synchronisation zwischen dem Zettelstore und Excel ermöglicht und dabei eine konsistente Datenverarbeitung gewährleistet. Die Ergebnisse werden anhand von Testfällen überprüft und mit den initialen Anforderungen abgeglichen. 

Kosten: 
Keine Kosten 

Risiken: 
Zugang und Datenqualität: Eingeschränkter Zugriff oder unvollständige Daten können die Analyse verzögern oder beeinträchtigen. 
Netzwerkanalyse-Komplexität: Ein komplexes Zettelnetzwerk könnte die Identifikation 
Zeitliche Engpässe: Verzögerungen bei einzelnen Schritten, insbesondere in der Implementierung, könnten den Zeitplan gefährden. 
