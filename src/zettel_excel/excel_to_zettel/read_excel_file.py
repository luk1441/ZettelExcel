import os
import pandas as pd


def read_excel_file(zettel_id: str) -> list[pd.DataFrame]:
    filename = os.path.join("excel", f"{zettel_id}.xlsx")

    if not os.path.isfile(filename):
        raise ValueError(f"Datei '{filename}' nicht gefunden.")

    try:
        excel_data = pd.read_excel(filename, sheet_name=None, header=None)
        return [df for df in excel_data.values() if not df.empty]

    except Exception as e:
        print(f"Fehlerdetails: {e}")
        raise ValueError(f"Fehler beim Einlesen der Datei '{filename}': {e}")

