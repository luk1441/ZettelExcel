import os
import pandas as pd
import requests

def update_all_modified_zettel_from_folder(folder_path):
    for filename in os.listdir(folder_path):
        if filename.startswith("zettel_") and filename.endswith(".xlsx"):
            # Zettelnummer aus Dateinamen extrahieren
            zettelnummer = filename.replace("zettel_", "").replace(".xlsx", "")
            filepath = os.path.join(folder_path, filename)

            # Excel-Datei lesen
            df = pd.read_excel(filepath)

            # Erwartete Spalten: Title, Content
            title = df.loc[0, "Title"]
            content = df.loc[0, "Content"]

            # PUT-Request vorbereiten
            url = f"http://localhost:23123/store/{zettelnummer}"
            updated_zettel = {
                "title": title,
                "content": content
            }

            response = requests.put(url, json=updated_zettel)

            if response.status_code == 200:
                print(f"Zettel {zettelnummer} erfolgreich aktualisiert.")
            else:
                print(f"Fehler bei Zettel {zettelnummer}: {response.status_code}")
                print(response.text)

