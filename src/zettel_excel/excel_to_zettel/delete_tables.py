import os

def delete_tables(zettelnummer, daten):
    dateiname = f"temp_excel/zettel_{zettelnummer}.xlsx"
    try:
        zettelstore.speichern(zettelnummer, daten)  # Beispielhafte Funktion
        if os.path.exists(dateiname):
            os.remove(dateiname)
    except Exception as e:
        print(f"Fehler beim Speichern: {e}")
        if os.path.exists(dateiname):
            os.remove(dateiname)





