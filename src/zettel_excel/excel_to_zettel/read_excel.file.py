import sys
import os
import pandas as pd

def read_excel_tables(zettel_id: str) -> dict[str, list[list]]:
    # Erstelle den Pfad zur Excel-Datei im "excel"-Ordner
    filename = os.path.join("excel", f"{zettel_id}.xlsx")

    # Prüfe, ob die Datei existiert
    if not os.path.isfile(filename):
        print(f"Datei '{filename}' nicht gefunden.")
        return None

    try:
        # Lese alle Tabellenblätter der Excel-Datei ein
        excel_data = pd.read_excel(filename, sheet_name=None, header=0)
        tables = {}
        for sheet_name, df in excel_data.items():
            # Ignoriere leere Tabellenblätter
            if df.empty:
                continue
            # Ersetze fehlende Werte durch leere Strings und wandle in Liste um
            table = df.fillna("").values.tolist()
            tables[sheet_name] = table

        # Falls keine Tabellen eingelesen wurden, melde dies
        if not tables:
            print("Keine Tabellen zum Einlesen gefunden.")
            return None

        # Gib das Dictionary mit Tabellenblättern zurück
        return tables

    except Exception as e:
        # Gib eine Fehlermeldung aus, falls das Einlesen schiefgeht
        print(f"Fehler beim Einlesen der Datei '{filename}': {e}")
        return None

def main():
    # Prüfe, ob eine Zettel-ID als Argument übergeben wurde
    if len(sys.argv) != 2:
        print("Bitte Zettel-ID angeben.")
        return

    zettel_id = sys.argv[1]
    tables = read_excel_tables(zettel_id)

    if tables is None:
        print("Tabellen konnten nicht eingelesen werden.")
    else:
        # Hier können die eingelesenen Tabellen weiterverarbeitet werden
        pass

if __name__ == "__main__":
    main()
