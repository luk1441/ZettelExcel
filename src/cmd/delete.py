import os
import logging

def delete_excel_file(zettelnummer: str, excel_dir: str = "excel_output") -> None:
    """
    Löscht die Excel-Datei zur angegebenen Zettelnummer, wenn sie existiert.

    :param zettelnummer: Die 16-stellige Zettelnummer
    :param excel_dir: Ordner, in dem die Excel-Dateien gespeichert werden
    """
    filename = f"{zettelnummer}.xlsx"
    filepath = os.path.join(excel_dir, filename)

    if os.path.exists(filepath):
        try:
            os.remove(filepath)
            logging.info(f"Excel-Datei '{filename}' erfolgreich gelöscht.")
        except Exception as e:
            logging.error(f"Fehler beim Löschen der Datei '{filename}': {e}")
    else:
        logging.info(f"Excel-Datei '{filename}' nicht vorhanden, kein Löschvorgang notwendig.")


# Beispiel wie du die Funktion nutzen kannst:

def process_zettel(zettelnummer, daten):
    try:
        # (1) Zettel wird gespeichert (Dummy-Funktion)
        save_result = save_to_zettelstore(zettelnummer, daten)  # <-- Deine Speichermethode

        if save_result.success:
            delete_excel_file(zettelnummer)  # Erfolgreiches Speichern → Excel löschen
        else:
            raise Exception("Zettelstore-Speicherung fehlgeschlagen")

    except Exception as e:
        logging.error(f"Fehler im Prozess: {e}")
        delete_excel_file(zettelnummer)  # Fehler → Excel trotzdem löschen


# Dummy-Funktion zur Veranschaulichung:
class SaveResult:
    def __init__(self, success):
        self.success = success

def save_to_zettelstore(zettelnummer, daten):
    # Simuliere immer Erfolg
    return SaveResult(success=True)


# Beispielaufruf:
if __name__ == "__main__":
    zettelnummer = "1234567890123455"
    daten = {}
    process_zettel(zettelnummer, daten)